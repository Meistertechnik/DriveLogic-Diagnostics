#!/usr/bin/env python3
"""
Simple test script to verify the Flask app is working correctly.
"""
import requests
import sys
import time

def test_app():
    """Test if the flask app is accessible and responding correctly."""
    print("Testing connection to Flask app...")
    
    # Test main page
    try:
        response = requests.get("http://localhost:5000/")
        if response.status_code == 200:
            print(f"✓ Main page accessible (status code: {response.status_code})")
        else:
            print(f"✗ Main page returned unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Failed to connect to main page: {str(e)}")
        return False
    
    # Test chat API
    try:
        response = requests.post(
            "http://localhost:5000/api/message",
            json={"message": "Hello"}
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Chat API responding (status code: {response.status_code})")
            print(f"✓ Bot response: {data.get('response', 'No response')}")
        else:
            print(f"✗ Chat API returned unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Failed to connect to chat API: {str(e)}")
        return False
    
    # Test history API
    try:
        response = requests.get("http://localhost:5000/api/history")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ History API responding (status code: {response.status_code})")
            print(f"✓ History entries: {len(data.get('history', []))}")
        else:
            print(f"✗ History API returned unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Failed to connect to history API: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    # Allow the server some time to start up if we're running tests immediately after launch
    time.sleep(2)
    
    if test_app():
        print("\n✓✓✓ All tests passed! The Flask app is working correctly.")
        sys.exit(0)
    else:
        print("\n✗✗✗ Some tests failed. Check the Flask app configuration.")
        sys.exit(1)