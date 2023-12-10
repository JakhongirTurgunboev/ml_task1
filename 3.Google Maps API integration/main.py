import os
from dotenv import load_dotenv
import requests


def google_maps_places_text_search(api_key, query):
    """Perform a Places Text Search using the Google Maps API."""
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Set up the parameters for the text search
    params = {
        "query": query,
        "key": api_key,
    }

    # Make the request to the Places Text Search API
    response = requests.get(base_url, params=params)
    results = response.json()

    # Process and print the results
    if "results" in results:
        print("Places found:")
        for place in results["results"]:
            print(f"- {place['name']}, {place['formatted_address']}")
    else:
        print("No places found.")


if __name__ == "__main__":
    # Load environment variables from the .env file
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    if api_key is None:
        raise "Error: Google Maps API key not found in the environment variables."
    else:
        search_query = input("Search a place you want get information about: ")

    google_maps_places_text_search(api_key, search_query)
