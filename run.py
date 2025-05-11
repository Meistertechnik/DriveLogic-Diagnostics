#!/usr/bin/env python3
import os
import sys
import logging
import traceback

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def run_app():
    try:
        logger.info("Starting Flask application...")
        
        # Import the Flask app
        from app import app
        
        # Verify important routes are registered
        routes = [str(rule) for rule in app.url_map.iter_rules()]
        logger.info(f"Registered routes: {routes}")
        
        # Ensure session is properly configured
        logger.info(f"Session secret key is set: {bool(app.secret_key)}")
        
        # Run the application
        if __name__ == "__main__":
            port = int(os.environ.get("PORT", 5000))
            logger.info(f"Starting server on port {port}")
            
            # Use development server in debug mode
            app.run(host="0.0.0.0", port=port, debug=True)
            
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    run_app()