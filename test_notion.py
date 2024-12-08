# test_notion.py
from notion_module import get_data_from_notion

def test():
    data = get_data_from_notion()
    results = data.get('results', [])
    
    for item in results:
        properties = item.get('properties', {})
        
        # Extraction des informations
        nom = properties.get('Nom', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Nom inconnu')
        prenom = properties.get('Prénom', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Prénom inconnu')
        email = properties.get('E-mail', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Email non spécifié')
        telephone = properties.get('Tp', {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Téléphone non spécifié')
        entreprise = properties.get("Nom de l'entreprise", {}).get('rich_text', [{}])[0].get('text', {}).get('content', 'Entreprise non spécifiée')
        
        # Affichage structuré
        print(f"Nom : {nom}")
        print(f"Prénom : {prenom}")
        print(f"E-mail : {email}")
        print(f"Téléphone : {telephone}")
        print(f"Entreprise : {entreprise}")
        print("-" * 40)  # Ligne de séparation pour plus de lisibilité

if __name__ == "__main__":
    test()
