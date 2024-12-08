# google_docs_module.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# Charger les configurations et les identifiants
from config import GOOGLE_SERVICE_ACCOUNT_FILE, TEMPLATE_DOC_ID

# Initialisation de l'API Google Docs
credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/documents", "https://www.googleapis.com/auth/drive"]
)
docs_service = build("docs", "v1", credentials=credentials)
drive_service = build("drive", "v3", credentials=credentials)

def create_google_doc(template_id, data):
    try:
        # Copie le document template pour un nouveau document
        copy_title = f"{data['prenom']} {data['nom']} - Document personnalisé"
        document = drive_service.files().copy(
            fileId=template_id, body={"name": copy_title}
        ).execute()
        doc_id = document.get("id")

        # Remplacement des placeholders par les valeurs
        requests = [
            {"replaceAllText": {"containsText": {"text": "{{nom}}", "matchCase": True}, "replaceText": data['nom']}},
            {"replaceAllText": {"containsText": {"text": "{{prenom}}", "matchCase": True}, "replaceText": data['prenom']}},
            {"replaceAllText": {"containsText": {"text": "{{email}}", "matchCase": True}, "replaceText": data['email']}},
            {"replaceAllText": {"containsText": {"text": "{{telephone}}", "matchCase": True}, "replaceText": data['telephone']}},
            {"replaceAllText": {"containsText": {"text": "{{entreprise}}", "matchCase": True}, "replaceText": data['entreprise']}},
        ]
        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
        return doc_id

    except HttpError as error:
        print(f"Une erreur s'est produite : {error}")
        return None

def export_doc_to_pdf(doc_id):
    try:
        # Exporter le document Google Docs en PDF
        file_path = f"{doc_id}.pdf"
        request = drive_service.files().export_media(fileId=doc_id, mimeType="application/pdf")
        with open(file_path, "wb") as pdf_file:
            pdf_file.write(request.execute())
        return file_path

    except HttpError as error:
        print(f"Une erreur s'est produite lors de l'exportation en PDF : {error}")
        return None
