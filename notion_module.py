# notion_module.py
import requests
from config import NOTION_API_KEY, NOTION_DATABASE_ID

NOTION_API_URL = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def get_data_from_notion():
    response = requests.post(NOTION_API_URL, headers=NOTION_HEADERS)
    response.raise_for_status()  # Assure que toute erreur HTTP déclenche une exception
    return response.json()

