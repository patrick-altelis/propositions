# test_config.py
import config

def test_config():
    assert config.NOTION_API_KEY is not None, "NOTION_API_KEY n'est pas défini"
    assert config.NOTION_DATABASE_ID is not None, "NOTION_DATABASE_ID n'est pas défini"
    assert config.GOOGLE_SERVICE_ACCOUNT_FILE is not None, "GOOGLE_SERVICE_ACCOUNT_FILE n'est pas défini"
    assert config.TEMPLATE_DOC_ID is not None, "TEMPLATE_DOC_ID n'est pas défini"
    assert config.GMAIL_CREDENTIALS_FILE is not None, "GMAIL_CREDENTIALS_FILE n'est pas défini"
    assert config.GMAIL_TOKEN_FILE is not None, "GMAIL_TOKEN_FILE n'est pas défini"
    print("Toutes les variables d'environnement sont correctement configurées.")

if __name__ == "__main__":
    test_config()
