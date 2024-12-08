from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os

# Définir les portées
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# Chemin vers vos identifiants client OAuth 2.0
creds_file = "/Users/patrick_guillaume/Library/Mobile Documents/com~apple~CloudDocs/Python/propositions/credentials/credentials_gmail.json"

# Lancer le processus d'authentification
flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
creds = flow.run_local_server(port=0)

# Enregistrer les informations d'identification dans token.json
token_path = "/Users/patrick_guillaume/Library/Mobile Documents/com~apple~CloudDocs/Python/propositions/credentials/token.json"
with open(token_path, "w") as token:
    token.write(creds.to_json())

print("Token d'accès enregistré avec succès.")
