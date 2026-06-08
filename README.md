# 🤖 My Genia Agent

> **A Production-Ready AI Assistant Powered by Google Gemini with Voice and Text Capabilities**

A sophisticated, multi-modal AI agent that combines Google's Gemini-2.5-Flash model with advanced file processing, web scraping, and voice interaction capabilities. Built for developers and power users who need intelligent automation with rich terminal UI and real-time token tracking.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Components](#core-components)
- [API Reference](#api-reference)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Architecture](#architecture)
- [Best Practices](#best-practices)
- [Performance Considerations](#performance-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**My Genia Agent** is an interactive AI assistant that leverages Google's Gemini API to provide intelligent responses with access to multiple tools for data processing, web access, and multimedia handling. The agent supports both text and voice interaction modes with a beautiful, intuitive terminal interface powered by the Rich library.

### Key Use Cases
- Real-time information retrieval via internet search
- PDF document analysis and extraction
- Image recognition and analysis
- Web content scraping and data extraction
- YouTube video downloading (audio/video)
- File management and data export to Excel
- Voice-controlled assistant functionality
- Document generation (Word files)

---

## ✨ Features

### 🎯 Core Capabilities

| Feature | Description |
|---------|-------------|
| **Dual Input Modes** | Seamlessly switch between text and voice interaction during runtime |
| **Voice I/O** | Speech-to-text (powered by Faster-Whisper) and text-to-speech (Piper TTS) |
| **Rich Terminal UI** | Beautiful formatted output with panels, spinners, and color-coded sections |
| **Real-Time Token Tracking** | Monitor API usage (prompt tokens, response tokens) per request and session-wide |
| **Intelligent Routing** | System-configured to prioritize real-time information via internet search |

### 🛠️ Integrated Tools

#### **1. File Manager** (`file_manager`)
- **Read** text files (with error handling for missing files)
- **Create** new files with content
- **Write/Overwrite** existing files
- **Supported formats**: `.txt`, `.md`, `.py`, `.json`, and any text-based format

```python
# Example: file_manager("notes.txt", "read")
# Returns: File content or error message
```

#### **2. Internet Search** (`internet_search`)
- Real-time search using DuckDuckGo API
- Returns top 3 results with titles, snippets, and URLs
- Perfect for current news, prices, weather, and trending topics

```python
# Example: internet_search("Bitcoin price today")
```

#### **3. PDF Reader** (`read_pdf`)
- Extract text from PDF documents
- Read all pages or specific pages
- Handles scanned PDFs (with limitations)
- Page-by-page metadata extraction

```python
# Example: read_pdf("report.pdf", "all")
# Example: read_pdf("report.pdf", "3")  # Page 3 only
```

#### **4. Image Analyzer** (`read_image`)
- Analyze images using Gemini's vision capabilities
- Custom question support ("What text is in this image?")
- **Supported formats**: JPG, JPEG, PNG, WebP, GIF, BMP
- Base64 encoding for secure API transmission

```python
# Example: read_image("chart.png", "Summarize the data shown")
```

#### **5. Web Scraper** (`scrape_webpage`)
- Extract **text** content (default)
- Extract **tables** as structured data
- Extract all **links** with text
- Extract **images** with alt text
- Automatic junk tag removal (scripts, styles, ads)

```python
# Examples:
# scrape_webpage("https://example.com", "text")
# scrape_webpage("https://example.com", "tables")
# scrape_webpage("https://example.com", "links")
# scrape_webpage("https://example.com", "images")
```

#### **6. YouTube Downloader** (`download_youtube`)
- Download videos or audio from YouTube
- Multiple resolution options: 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 4K
- Automatic fallback to highest available resolution
- Custom output directory support
- Duration and title extraction

```python
# Examples:
# download_youtube("https://youtube.com/watch?v=...", "video", "720p", "downloads/")
# download_youtube("https://youtube.com/watch?v=...", "audio")
```

#### **7. DOCX Manager** (`manage_docx`)
- **Read** Word documents with paragraph and table extraction
- **Create** new `.docx` files with formatted content
- **Write** (append) content to existing documents
- **Replace** entire document content
- Support for headings, bullet points, formatting options

Formatting syntax:
```
# Title           # Renders as title (level 0)
## Heading 1      # Renders as heading 1
### Heading 2     # Renders as heading 2
- Bullet point    # Renders as bullet list
\n                # New paragraph
---               # Page break
```

```python
# Example: manage_docx("report.docx", "create", "# Title\n## Section\n- Point 1")
```

#### **8. Excel Export** (`save_to_xlsm`)
- Save structured data as Macro-Enabled Workbook (.xlsm)
- Accepts list of dictionaries (each dict = row)
- Automatic extension handling
- Preserves data types

```python
# Example: save_to_xlsm("data.xlsm", [{"name": "John", "age": 30}])
```

#### **9. Voice Input** (`listen`)
- Record audio via microphone (configurable duration)
- Transcribe using Faster-Whisper (base model, CPU-optimized)
- Automatic temporary file cleanup
- Default 6-second recording window

```python
# Example: listen(duration=10)  # Records 10 seconds
```

#### **10. Text-to-Speech** (`speak`)
- Use local Piper TTS engine (no API calls)
- High-quality voice output
- Multiple voice models available
- Supports custom `.onnx` voice models

```python
# Example: speak("Hello, this is a test")
```

---

## System Requirements

### Minimum Requirements
- **Python**: 3.14 or higher
- **RAM**: 4GB minimum (8GB+ recommended for optimal performance)
- **Storage**: 2GB for Whisper model + additional space for downloads
- **Internet**: Required for API calls and web scraping
- **Audio Equipment**: Microphone and speaker for voice features

### Optional Requirements for Voice
- **Microphone**: For speech-to-text functionality
- **Speaker**: For text-to-speech output
- **ffmpeg**: (Usually pre-installed; only needed for advanced audio processing)

### Tested On
- Ubuntu 20.04 LTS+
- macOS 12.0+
- Windows 10/11 (WSL2 recommended)

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/Lordkilla12/My_Genia_Agent.git
cd My_Genia_Agent
```

### Step 2: Obtain Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. **Important**: Keep this key secure and never commit it to version control

### Step 3: Create Environment File

```bash
# Create .env file
cp .env.example .env
```

Edit `.env` and add your API key:
```env
Gemini_API_Key=your_actual_api_key_here
```

### Step 4: Install Dependencies

#### Option A: Using `uv` (Recommended - faster)
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

#### Option B: Using pip
```bash
pip install -r requirements.txt
```

#### Option C: Manual Installation
```bash
pip install google-genai>=2.0.1 \
            rich>=15.0.0 \
            faster-whisper>=1.2.1 \
            beautifulsoup4>=4.14.3 \
            pymupdf>=1.27.2.3 \
            python-docx>=1.2.0 \
            yt-dlp>=2026.3.17 \
            ddgs>=9.14.4 \
            requests>=2.33.1 \
            sounddevice>=0.5.5 \
            soundfile>=0.13.1 \
            openpyxl>=3.1.5 \
            pandas>=3.0.3 \
            lxml>=6.1.0
```

### Step 5: Verify Installation

```bash
python main.py
```

Expected output:
```
[Voice] Loading Whisper model...
[Voice] Whisper ready.

╭────────────────────────────────────────────╮
│          🤖 AI Agent Ready!                │
│                                            │
│  Enter → type your message                 │
│  v      → switch to voice mode             │
│  t      → switch to text mode              │
│  exit   → quit                             │
╰────────────────────────────────────────────╯
```

---

## Quick Start

### Text Mode (Default)
```bash
# Start the agent
python main.py

# Type your message
Me: What is the capital of France?

# Receive response in formatted panel
🤖 Gemini
Paris is the capital of France...

📊 Prompt: 42 tokens  |  Response: 18 tokens
```

### Voice Mode
```bash
# Start the agent
python main.py

# Switch to voice mode
Me: v

# Speak your question
🎙 VOICE MODE
🔊 Speaking…

# Listen to response
🎙 Listening for 6 seconds… speak now!
```

### Quick Command Reference
| Command | Action |
|---------|--------|
| `v` | Switch to Voice Mode |
| `t` | Switch to Text Mode |
| `exit` | Exit application |
| (any text) | Send message to Gemini |

---

## Core Components

### `main.py` - Main Application
- Initializes Gemini client
- Manages conversation loop
- Handles mode switching (text/voice)
- Displays formatted output with Rich library
- Tracks token usage

### `read_files.py` - Tool Implementations
Contains all 10 integrated tools:
- File management functions
- API integrations (DuckDuckGo, YouTube)
- Document processing (PDF, DOCX)
- Voice processing (transcription, TTS)
- Web scraping utilities

### `pyproject.toml` - Project Configuration
- Dependency declarations
- Python version specification
- Project metadata

### `piper/` & `piper-voices/`
- Local text-to-speech engine
- Pre-installed voice models
- Runs offline (no API calls needed)

---

## API Reference

### Complete Tool List

```python
# From read_files.py (all available as Gemini tools)
from read_files import (
    file_manager,        # File I/O
    save_to_xlsm,       # Excel export
    internet_search,    # Web search
    read_pdf,           # PDF extraction
    read_image,         # Image analysis
    scrape_webpage,     # Web scraping
    download_youtube,   # Video/audio download
    manage_docx,        # Word doc management
    speak,              # Text-to-speech
    listen              # Voice recording
)
```

### Configuration in main.py
```python
tools_list = [
    file_manager, 
    save_to_xlsm, 
    internet_search, 
    read_pdf,
    read_image, 
    scrape_webpage, 
    download_youtube, 
    manage_docx
]

chat = client.chats.create(
    model="gemini-2.5-flash-lite",  # Current model
    config={
        "tools": tools_list,
        "system_instruction": "You are a helpful assistant..."
    }
)
```

---

## Usage Examples

### Example 1: Search for Current Information
```bash
Me: What is the current Bitcoin price?

# Agent automatically uses internet_search tool
🤖 Gemini
The current Bitcoin price is...
```

### Example 2: PDF Analysis
```bash
Me: Analyze the contents of report.pdf and summarize the key findings

# Agent uses read_pdf tool
🤖 Gemini
Based on the report, the key findings are...
```

### Example 3: Image Recognition
```bash
Me: What products are shown in this screenshot.png?

# Agent uses read_image tool
🤖 Gemini
I can see the following products in the image...
```

### Example 4: Web Scraping
```bash
Me: Extract all the news headlines from bbc.com

# Agent uses scrape_webpage with "text" extraction
🤖 Gemini
Here are the current headlines:
- ...
- ...
```

### Example 5: File Management
```bash
Me: Create a file called notes.txt with today's meeting agenda

# Agent uses file_manager
🤖 Gemini
I've created notes.txt with the following agenda:
...
```

### Example 6: YouTube Download
```bash
Me: Download the audio from https://youtube.com/watch?v=... to the downloads folder

# Agent uses download_youtube
🤖 Gemini
✅ Download complete!
Title: [Video Title]
Duration: 12m 34s
```

---

## Configuration

### Environment Variables
Create `.env` file in project root:
```env
# Required
Gemini_API_Key=your_api_key_here

# Optional (defaults shown below)
# VOICE_DURATION=6  # Seconds to record in voice mode
# LOG_LEVEL=info    # Logging level
```

### Customize System Instruction
Edit `main.py`, line ~40:
```python
"system_instruction": (
    "You are a helpful assistant with access to local files and the internet. "
    "ALWAYS use internet_search for current prices, news, or real-time info. "
    "Keep responses concise and natural."
)
```

### Choose Voice Model
Edit `read_files.py`, line ~502:
```python
# Default: en_US-ryan-high.onnx
# Available models in piper-voices/ folder
model = os.path.join(base_dir, "piper-voices", "your_voice_model.onnx")
```

---

## Troubleshooting

### Issue: "Error: Gemini_API_Key not found"
**Solution**: 
1. Create `.env` file in project root
2. Add: `Gemini_API_Key=your_key_here`
3. Restart the application

### Issue: "Could not hear anything" (Voice mode)
**Solutions**:
1. Check microphone connection
2. Test microphone: `arecord -d 2 test.wav` (Linux) or `ffmpeg -f dshow -i audio="Microphone" -t 2 test.wav` (Windows)
3. Increase recording duration: Edit line 112 in main.py from `duration=6` to `duration=10`
4. Check volume levels

### Issue: Piper TTS not working
**Solution**:
1. Verify Piper installation: `ls -la piper/` and `ls -la piper-voices/`
2. Make executable: `chmod +x piper/piper`
3. Test directly: `echo "Hello" | ./piper/piper --model piper-voices/en_US-ryan-high.onnx --output_file test.wav`

### Issue: PDF reading returns "No readable text found"
**Reason**: Scanned PDFs (images) cannot be extracted as text
**Solution**: Use `read_image` tool on extracted PDF pages or convert PDF to images first

### Issue: Web scraping returns empty content
**Reasons**: 
1. Website blocked scraping (User-Agent headers should help)
2. Content loaded by JavaScript (BeautifulSoup can't execute JS)
**Solution**: 
1. Verify URL is correct
2. Try different extraction mode (`text`, `links`, `images`)
3. For JS-heavy sites, consider using Playwright or Selenium

### Issue: "Connection timeout" on YouTube download
**Reasons**: Network speed, video region restrictions, very large files
**Solutions**:
1. Check internet connection
2. Try lower resolution: `"720p"` instead of `"1080p"`
3. Try audio mode: `"audio"` instead of `"video"`
4. Ensure yt-dlp is up-to-date: `pip install --upgrade yt-dlp`

### Issue: High token usage / Slow responses
**Optimization tips**:
1. Ask more specific questions (reduces context needed)
2. Use internet_search strategically (adds tokens)
3. Provide context upfront rather than follow-ups
4. Monitor token counts and adjust usage

---

## Architecture

### System Flow Diagram
```
┌─────────────────────┐
│  User Input (Text   │
│  or Voice)          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  Input Processing                       │
│  - Text: Direct input                   │
│  - Voice: Whisper transcription         │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  Gemini API Chat                        │
│  - Model: gemini-2.5-flash-lite        │
│  - Tools available: 8 tools             │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  Tool Execution (if needed)             │
│  - File Manager, Internet Search        │
│  - PDF Reader, Image Analyzer           │
│  - Web Scraper, YouTube Download        │
│  - DOCX Manager, Excel Export           │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  Response Generation                    │
│  - Gemini generates final response      │
│  - Token count extraction               │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  Output Rendering                       │
│  - Rich formatted panels                │
│  - Voice output (TTS) if enabled        │
│  - Token display                        │
└─────────────────────────────────────────┘
```

### Model Specification
- **Model**: `gemini-2.5-flash-lite`
- **Type**: Multi-modal (text, image, video understanding)
- **Context Window**: 1M tokens
- **Cost**: Efficient (flash model pricing)
- **Latency**: Sub-second response times

---

## Best Practices

### 1. **API Key Management**
```bash
# ✅ DO
export Gemini_API_Key="your_key"
# Add .env to .gitignore
echo ".env" >> .gitignore

# ❌ DON'T
# Hardcode API key in source
# Commit .env file
# Share API key publicly
```

### 2. **Token Optimization**
```python
# ✅ DO: Be specific
"What are the current prices of NVIDIA stock and Apple stock?"

# ❌ DON'T: Vague queries require more processing
"Tell me about stocks"
```

### 3. **Voice Mode Usage**
```bash
# ✅ DO: Speak clearly and complete your thought
# "What's the current Bitcoin price in USD?"

# ❌ DON'T: Mumble or pause
# "Um... what's... Bitcoin... price?"
```

### 4. **File Naming**
```python
# ✅ DO: Use clear, descriptive names
file_manager("monthly_report_jan_2024.txt", "create", content)

# ❌ DON'T: Ambiguous names
file_manager("file1.txt", "create", content)
```

### 5. **Error Handling**
Always check responses for errors:
```bash
# Check if Gemini returned an error message
🤖 Gemini
Error: Could not connect to the website...

# Retry with different parameters or approach
```

---

## Performance Considerations

### Token Usage
- **Typical query**: 50-200 prompt tokens, 50-500 response tokens
- **Internet search**: Adds ~100 tokens
- **Image analysis**: Adds ~50-200 tokens per image
- **PDF reading**: Depends on page count; ~10-20 tokens per page

### Speed Benchmarks
| Operation | Duration |
|-----------|----------|
| Text query response | 1-3 seconds |
| Voice recording + transcription | 8-12 seconds (6s audio) |
| PDF extraction | 1-5 seconds (depends on size) |
| Web scraping | 2-5 seconds |
| YouTube download | Varies with file size |

### Memory Usage
- Idle: ~150-200 MB
- With Whisper loaded: ~500-800 MB
- During processing: Up to 1.5 GB (brief spikes)

### Optimization Tips
1. **Reuse conversation context** when possible
2. **Batch multiple questions** into one if related
3. **Use voice mode judiciously** (adds processing time)
4. **Monitor token usage** and adjust query specificity

---

## Contributing

### Report Issues
1. Check existing issues on GitHub
2. Provide detailed reproduction steps
3. Include error messages and logs
4. Specify Python version and OS

### Contribute Code
1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit pull request with description

### Guidelines
- Follow Python PEP 8 style guide
- Add docstrings to functions
- Test your changes before submitting
- Update README if adding new features

---

## License

This project is open source and available under the **MIT License**.

```
MIT License

Copyright (c) 2024 Lordkilla12

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## Additional Resources

- [Google Gemini API Documentation](https://ai.google.dev/)
- [Rich Library Documentation](https://rich.readthedocs.io/)
- [Faster-Whisper GitHub](https://github.com/guillaumekln/faster-whisper)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

---

## Changelog

### v0.1.0 (Current)
- Initial release
- Core Gemini integration
- 10 integrated tools
- Voice/text mode switching
- Rich terminal UI
- Token tracking

### Planned for Future
- [ ] Conversation history persistence
- [ ] Multi-language support
- [ ] Custom tool creation interface
- [ ] Integration with additional APIs (OpenAI, Anthropic)
- [ ] Web UI dashboard
- [ ] Performance monitoring/analytics
- [ ] Advanced caching mechanisms

---

## Support & Community

- **Issues**: [GitHub Issues](https://github.com/Lordkilla12/My_Genia_Agent/issues)
- **Email**: Contact maintainer via GitHub profile
- **Discussions**: [GitHub Discussions](https://github.com/Lordkilla12/My_Genia_Agent/discussions)

---

**Made with ❤️ by Lordkilla12 | Powered by Google Gemini API**

*Last Updated: June 2024 | Version 0.1.0*
