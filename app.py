import requests
import sys

def get_joke():
    # L'URL interroge l'API pour une blague simple (type=single)
    api_url = "https://v2.jokeapi.dev/joke/Programming,Misc?type=single" 
    
    try:
        # Fait la requête HTTP
        response = requests.get(api_url, timeout=5)
        response.raise_for_status() # Vérifie que la requête a réussi
        
        joke_data = response.json()
        
        if joke_data.get('error'):
            print("Erreur de l'API: impossible de récupérer la blague.", file=sys.stderr)
            return
            
        joke = joke_data.get('joke', 'Aucune blague trouvée.')
        
        print("\n=== La blague du jour ===")
        print(joke)
        print("===========================\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à l'API: {e}", file=sys.stderr)

if __name__ == "__main__":
    get_joke()
