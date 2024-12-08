# gmail_module.py

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(to, subject, body, attachment_path=None):
    """
    Envoie un email via l'API Gmail avec un texte et une pièce jointe optionnelle.
    
    Arguments :
        to (str) : Adresse email du destinataire.
        subject (str) : Sujet de l'email.
        body (str) : Corps de texte de l'email.
        attachment_path (str, optionnel) : Chemin de la pièce jointe (fichier PDF).
    
    Retourne :
        dict ou None : Les informations du message envoyé, ou None en cas d'erreur.
    """
    
    # Charger les informations d'identification depuis le fichier token.json
    creds = Credentials.from_authorized_user_file(
        '/Users/patrick_guillaume/Library/Mobile Documents/com~apple~CloudDocs/Python/propositions/credentials/token.json', 
        ["https://www.googleapis.com/auth/gmail.send"]
    )
    
    # Construire le service Gmail
    service = build('gmail', 'v1', credentials=creds)
    
    # Créer le message
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Ajouter une pièce jointe, si elle existe
    if attachment_path:
        with open(attachment_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype="pdf")
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            message.attach(attachment)

    # Encoder le message en base64 pour l'envoi via l'API Gmail
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Envoyer l'email
    try:
        send_message = service.users().messages().send(userId="me", body={"raw": raw_message}).execute()
        print(f"Message envoyé avec succès, ID : {send_message['id']}")
        return send_message
    except Exception as error:
        print(f"Erreur lors de l'envoi de l'email : {error}")
        return None
