import os
import threading
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.rule import Rule
from rich.prompt import Prompt
from rich.theme import Theme
from read_files import (file_manager, save_to_xlsm, internet_search,
                        read_pdf, read_image, scrape_webpage,
                        download_youtube, manage_docx, speak, listen)

# ── RICH THEME ────────────────────────────────────────────────────────────────
theme = Theme({
    "voice":   "bold magenta",
    "text":    "bold cyan",
    "gemini":  "bold green",
    "user":    "bold yellow",
    "info":    "dim white",
    "error":   "bold red",
    "success": "bold green",
    "tokens":  "dim cyan",
})
console = Console(theme=theme)

load_dotenv()
client = genai.Client(api_key=os.environ.get("Gemini_API_Key"))

tools_list = [file_manager, save_to_xlsm, internet_search, read_pdf,
              read_image, scrape_webpage, download_youtube, manage_docx]

chat = client.chats.create(
    model="gemini-2.5-flash-lite",
    config={
        "tools": tools_list,
        "system_instruction": (
            "You are a helpful assistant with access to local files and the internet. "
            "ALWAYS use internet_search for current prices, news, or real-time info. "
            "Keep responses concise and natural."
        )
    }
)

# ── STARTUP BANNER ────────────────────────────────────────────────────────────
console.print()
console.print(Panel.fit(
    Text.assemble(
        ("  AI Agent Ready!\n\n", "bold white"),
        ("  Enter", "bold cyan"),   ("  → type your message\n", "white"),
        ("  v",     "bold magenta"), ("      → switch to voice mode\n", "white"),
        ("  t",     "bold cyan"),   ("      → switch to text mode\n",  "white"),
        ("  exit",  "bold red"),    ("  → quit", "white"),
    ),
    title="[bold white]🤖 Gemini Agent[/]",
    border_style="bright_blue",
    padding=(1, 4),
))
console.print()

response     = None
voice_mode   = False
keyboard_command = None

def keyboard_listener():
    global keyboard_command
    keyboard_command = input()

def show_spinner(message: str, style: str = "dots"):
    """Return a Live spinner context you can use as a with-block."""
    return Live(Spinner(style, text=f"[info]{message}[/]"), console=console, transient=True)

def print_gemini(reply: str):
    console.print(Panel(
        f"[gemini]{reply}[/]",
        title="[bold green]🤖 Gemini[/]",
        border_style="green",
        padding=(0, 2),
    ))

def print_user(text: str):
    console.print(Panel(
        f"[user]{text}[/]",
        title="[bold yellow]🧑 You[/]",
        border_style="yellow",
        padding=(0, 2),
    ))

def print_mode_banner(mode: str):
    if mode == "voice":
        console.print(Rule("[voice]🎙  VOICE MODE  — type 't' + Enter to switch | 'exit' + Enter to quit[/]", style="magenta"))
    else:
        console.print(Rule("[text]⌨   TEXT MODE   — type 'v' to switch to voice | 'exit' to quit[/]", style="cyan"))

def print_tokens(prompt_tok: int, response_tok: int):
    console.print(f"  [tokens]📊 Prompt: {prompt_tok} tokens  |  Response: {response_tok} tokens[/]\n")

# ── MAIN LOOP ─────────────────────────────────────────────────────────────────
print_mode_banner("text")

while True:
    try:
        # ── VOICE MODE ────────────────────────────────
        if voice_mode:
            keyboard_command = None
            kb_thread = threading.Thread(target=keyboard_listener, daemon=True)
            kb_thread.start()

            with show_spinner("🎙  Listening for 6 seconds… speak now!", "arc"):
                user_input = listen(duration=6)

            kb_thread.join(timeout=0.1)

            # Check keyboard override first
            if keyboard_command is not None:
                cmd = keyboard_command.strip().lower()
                if cmd == "t":
                    voice_mode = False
                    console.print()
                    print_mode_banner("text")
                    continue
                elif cmd == "exit":
                    if response and response.usage_metadata:
                        total = (response.usage_metadata.prompt_token_count or 0) + \
                                (response.usage_metadata.candidates_token_count or 0)
                        console.print(f"\n[tokens]📊 Total tokens used: {total}[/]")
                    console.print("\n[success]👋 Goodbye![/]\n")
                    break

            if not user_input:
                console.print("[error]⚠  Could not hear anything — please try again.[/]\n")
                speak("Sorry, I didn't catch that. Please try again.")
                continue

            print_user(user_input)

        # ── TEXT MODE ─────────────────────────────────
        else:
            user_input = Prompt.ask("[cyan]Me[/]").strip()

            if user_input.lower() == "v":
                voice_mode = True
                console.print()
                print_mode_banner("voice")
                continue

            elif user_input.lower() == "t":
                console.print("[info]Already in text mode.[/]\n")
                continue

            elif user_input.lower() == "exit":
                if response and response.usage_metadata:
                    total = (response.usage_metadata.prompt_token_count or 0) + \
                            (response.usage_metadata.candidates_token_count or 0)
                    console.print(f"\n[tokens]📊 Total tokens used: {total}[/]")
                console.print("\n[success]👋 Goodbye![/]\n")
                break

            elif not user_input:
                continue

            print_user(user_input)

        # ── SEND TO GEMINI ────────────────────────────
        with show_spinner("🤖 Gemini is thinking…", "dots2"):
            response = chat.send_message(user_input)

        reply = response.text if response.text else "Sorry, something went wrong."

        print_gemini(reply)

        if voice_mode:
            with show_spinner("🔊 Speaking…", "dots"):
                speak(reply)

        prompt_tokens   = response.usage_metadata.prompt_token_count or 0
        response_tokens = response.usage_metadata.candidates_token_count or 0
        print_tokens(prompt_tokens, response_tokens)

    except KeyboardInterrupt:
        console.print("\n[error]⚠  Interrupted.[/]\n")
        break