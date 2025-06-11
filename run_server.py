#!/usr/bin/env python3

"""
FastWhisperAPI Server Startup Script
This script starts the FastWhisperAPI server with proper configuration.
"""

import uvicorn
import os

if __name__ == "__main__":
    # Set environment variable to allow duplicate libraries
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    
    print("🚀 Starting FastWhisperAPI Server...")
    print("📋 Server will be available at: http://localhost:8000")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("ℹ️  Server Info: http://localhost:8000/info")
    print("🔑 API Key for testing: dummy_api_key")
    print("=" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 