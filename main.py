import warnings

# Suppress the specific FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

import logging
import logging.config
from dotenv import load_dotenv
import os
from app import App    

# Load environment variables from .env file
load_dotenv()

# Access environment variables
environment = os.getenv('ENVIRONMENT')
debug = os.getenv('DEBUG')

print(f"Environment: {environment}")
print(f"Debug: {debug}")

# Load logging configuration
logging.config.fileConfig('logging.conf')

# Initialize and run the application
app = App()
app.run()