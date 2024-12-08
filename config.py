# config.py
import os
from dotenv import load_dotenv
from pathlib import Path

# Définir le chemin vers le fichier .env
env_path = Path(__file__).parent / 'credentials' / '.env'

# Charger les variables d'environnement depuis .env
load_dotenv(dotenv_path=env_path)

# Notion
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

# Google Docs
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE').replace('\\ ', ' ')
TEMPLATE_DOC_ID = os.getenv('TEMPLATE_DOC_ID')

# Gmail API
GMAIL_CREDENTIALS_FILE = os.getenv('GMAIL_CREDENTIALS_FILE').replace('\\ ', ' ')
GMAIL_TOKEN_FILE = os.getenv('GMAIL_TOKEN_FILE').replace('\\ ', ' ')

# Email (si nécessaire pour d'autres usages)
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# SMTP (optionnel)
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

# Ajouter des print pour vérifier (à supprimer après tests)
print("NOTION_API_KEY:", NOTION_API_KEY)
print("NOTION_DATABASE_ID:", NOTION_DATABASE_ID)
print("GOOGLE_SERVICE_ACCOUNT_FILE:", GOOGLE_SERVICE_ACCOUNT_FILE)
print("TEMPLATE_DOC_ID:", TEMPLATE_DOC_ID)
print("GMAIL_CREDENTIALS_FILE:", GMAIL_CREDENTIALS_FILE)
print("GMAIL_TOKEN_FILE:", GMAIL_TOKEN_FILE)
print("EMAIL_ADDRESS:", EMAIL_ADDRESS)
print("EMAIL_PASSWORD:", EMAIL_PASSWORD)
print("SMTP_SERVER:", SMTP_SERVER)
print("SMTP_PORT:", SMTP_PORT)
