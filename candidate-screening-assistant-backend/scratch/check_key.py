from app.config import settings
import os

print(f"Environment variable GOOGLE_API_KEY: {os.environ.get('GOOGLE_API_KEY', 'Not set in os.environ')}")
key = settings.GOOGLE_API_KEY
if key:
    masked_key = key[:8] + "..." + key[-4:]
    print(f"Loaded Settings GOOGLE_API_KEY: {masked_key}")
else:
    print("GOOGLE_API_KEY is not set in settings!")
