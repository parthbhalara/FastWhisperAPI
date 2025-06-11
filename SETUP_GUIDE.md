# FastWhisperAPI Setup and Usage Guide

## Issues Fixed ✅

1. **Syntax Warning**: Fixed invalid escape sequences in the HTML string (line 104 in main.py)
2. **Missing Dependencies**: Updated requirements.txt with compatible versions
3. **Module Not Found**: Installed faster-whisper and all required dependencies
4. **Compatibility Issues**: Updated to faster-whisper 1.1.0 which includes compatible av package

## Quick Start

### 1. Virtual Environment Setup
```bash
# Navigate to project directory
cd /Users/bhalarapro/Documents/GitHub/3.\ Misc/FastWhisperAPI

# Activate virtual environment (already created)
source venv/bin/activate

# Dependencies are already installed
```

### 2. Start the Server

**Option A: Using the startup script (Recommended)**
```bash
source venv/bin/activate
python run_server.py
```

**Option B: Using uvicorn directly**
```bash
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Access the Application

- **Main Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Server Info**: http://localhost:8000/info

## API Usage

### Authentication
- **API Key**: `dummy_api_key`
- **Header**: `Authorization: Bearer dummy_api_key`

### Example Usage with curl

```bash
# Simple transcription
curl -X POST "http://localhost:8000/v1/transcriptions" \
  -H "Authorization: Bearer dummy_api_key" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_audio.wav" \
  -F "model=base"

# Advanced usage with all parameters
curl -X POST "http://localhost:8000/v1/transcriptions" \
  -H "Authorization: Bearer dummy_api_key" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@audio1.wav" \
  -F "file=@audio2.wav" \
  -F "model=base" \
  -F "language=en" \
  -F "response_format=verbose_json" \
  -F "timestamp_granularities=word"
```

### Supported Parameters

- **file**: Audio files (required) - Supports multiple files
- **model**: Model size (optional) - `tiny`, `base`, `small`, `medium`, `large` (default: `base`)
- **language**: ISO-639-1 language code (optional) - Auto-detect if not specified
- **initial_prompt**: Context to guide transcription (optional)
- **vad_filter**: Voice activity detection (optional) - Default: `false`
- **min_silence_duration_ms**: Minimum silence duration (optional) - Default: `1000`
- **response_format**: Response format (optional) - `text` or `verbose_json` (default: `text`)
- **timestamp_granularities**: Timestamp detail (optional) - `segment` or `word` (default: `segment`)

### Supported Audio Formats
- MP3, MP4, MPEG, MPGA, M4A, WAV, WEBM, OPUS, FLAC, OGG

## Features

✅ **OpenAI API Compatible**: Drop-in replacement for OpenAI Whisper API  
✅ **Multiple Files**: Process multiple audio files in one request  
✅ **Language Detection**: Automatic language detection  
✅ **Voice Activity Detection**: Filter out silence  
✅ **Multiple Formats**: Support for various audio formats  
✅ **Fast Processing**: Uses faster-whisper for 4x speed improvement  
✅ **GPU Support**: Automatic GPU detection and usage  

## Troubleshooting

### Force CPU Usage
If you want to run on CPU only (even with GPU available):
```bash
FORCE_CPU=true python run_server.py
```

### Check Server Status
```bash
curl http://localhost:8000/info
```

### View Logs
Server logs are displayed in the terminal and also saved to `app.log`.

## Development

To modify the application:
1. Make changes to the code
2. The server will auto-reload (if using --reload flag)
3. API documentation updates automatically at `/docs`

## Hardware Requirements

- **CPU**: Any modern CPU
- **RAM**: 4GB+ recommended
- **GPU**: Optional but recommended for faster processing
- **Storage**: 1GB+ for models

## Performance Notes

- First run downloads the base model (~145MB)
- GPU processing is ~4x faster than CPU
- Multiple file processing uses ThreadPoolExecutor for parallel processing
- Models are cached after first download 