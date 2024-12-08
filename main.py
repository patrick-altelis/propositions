# main.py

import os
import logging
from notion_module import get_data_from_notion
from google_docs_module import create_google_doc, export_doc_to_pdf
from gmail_module import send_email

print("Modules importés avec succès : create_google_doc et export_doc_to_pdf")  # Ajout pour vérifier l'import

from config import TEMPLATE_DOC_ID

# Configuration du logging pour enregistrer les actions
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def main():
    try:
        logging.info("Début de l'extraction des données depuis Notion.")
        data = get_data_from_notion()
        
        # Parcourir chaque résultat de Notion pour traiter les données
        for item in data.get('results', []):
            properties = item.get('properties', {})
            
            # Extraction des informations de chaque champ
            nom = properties.get('Nom', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Nom inconnu')
            prenom = properties.get('Prénom', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Prénom inconnu')
            email = properties.get('E-mail', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Email non spécifié')
            telephone = properties.get('Tp', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Téléphone non spécifié')
            entreprise = properties.get("Nom de l'entreprise", {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Entreprise non spécifiée')
            
            # Préparer les données pour le document Google Docs
            doc_data = {
                'nom': nom,
                'prenom': prenom,
                'email': email,
                'telephone': telephone,
                'entreprise': entreprise
            }
            
            logging.info(f"Création d'un document Google Docs pour {prenom} {nom} de {entreprise}.")
            # Création du document Google Docs à partir du template
            doc_id = create_google_doc(TEMPLATE_DOC_ID, doc_data)
            
            logging.info(f"Exportation du document {doc_id} en PDF.")
            # Exporter le document en PDF
            pdf_path = export_doc_to_pdf(doc_id)
            
            logging.info(f"Envoi de l'email avec le PDF à {email}.")
            # Envoi du PDF par email
            send_email(
                to=email,
                subject="Votre document personnalisé",
                body=f"Bonjour {prenom},\n\nVeuillez trouver ci-joint votre document.",
                attachment_path=pdf_path
            )
            
            # Suppression du fichier PDF local après envoi
            os.remove(pdf_path)
            logging.info(f"PDF {pdf_path} supprimé après envoi.")
        
        logging.info("Processus terminé avec succès.")

    except Exception as e:
        logging.error(f"Une erreur est survenue : {e}", exc_info=True)

if __name__ == '__main__':
    main()
