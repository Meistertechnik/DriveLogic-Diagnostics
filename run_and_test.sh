#!/bin/bash

# Start the Flask app in the background
echo "Starting Flask application..."
python main.py &
SERVER_PID=$!

# Wait a bit for the server to start
echo "Waiting for server to start..."
sleep 5

# Run the test script
echo "Running tests..."
python test_app.py
TEST_STATUS=$?

# Kill the server
echo "Stopping server..."
kill $SERVER_PID

# Exit with the test status
exit $TEST_STATUS