#!/usr/bin/env python3

"""
FastWhisperAPI Test Script
This script tests the API endpoints to ensure everything is working correctly.
"""

import requests
import time

def test_api():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing FastWhisperAPI...")
    print("=" * 50)
    
    # Wait a moment for server to start
    time.sleep(2)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/info", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running!")
            print(f"   Status: {response.status_code}")
        else:
            print(f"❌ Server responded with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Server is not responding: {e}")
        print("\n💡 Make sure to start the server first:")
        print("   python run_server.py")
        return False
    
    # Test 2: Check docs endpoint
    try:
        response = requests.get(f"{base_url}/docs", timeout=5)
        if response.status_code == 200:
            print("✅ API documentation is accessible!")
        else:
            print(f"⚠️  Docs endpoint returned: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Could not access docs: {e}")
    
    # Test 3: Check root endpoint (should redirect to docs)
    try:
        response = requests.get(f"{base_url}/", timeout=5, allow_redirects=False)
        if response.status_code in [302, 307]:
            print("✅ Root endpoint redirects to docs!")
        else:
            print(f"⚠️  Root endpoint returned: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Could not access root endpoint: {e}")
    
    print("\n🎉 Basic tests completed!")
    print("\n📋 Next steps:")
    print("1. Open http://localhost:8000/docs in your browser")
    print("2. Use the API key: dummy_api_key")
    print("3. Upload an audio file to test transcription")
    print("\n📖 See SETUP_GUIDE.md for detailed usage instructions")
    
    return True

if __name__ == "__main__":
    test_api() 