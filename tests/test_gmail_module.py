# test_gmail_module.py
from gmail_module import send_email

send_email(
    to="recipient@example.com",
    subject="Test Email",
    body="Ceci est un test d'envoi d'email.",
    attachment_path="chemin_vers_fichier_test.pdf"  # Optionnel, ou None si pas de pièce jointe
)
