import requests
import logging
import json

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler for logging
file_handler = logging.FileHandler("steam_free_games.log", mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

def test_get_steam_free_games():
    """Test retrieving the list of free Steam games."""
    url = "https://store.steampowered.com/api/featuredcategories/"
    print(f"Sending request to {url}...")
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    logger.info(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        logger.error(f"Failed request. Status: {response.status_code}, Response: {response.text}")
        print(f"ERROR! Status: {response.status_code}, Response: {response.text}")
        return

    # Parse JSON response
    data = response.json()
    logger.info(f"JSON Response: {json.dumps(data, indent=4, ensure_ascii=False)}")
    print("JSON received, checking content...")

    # Collect all free games from all categories
    free_games = []
    for category, content in data.items():
        if isinstance(content, dict) and "items" in content:
            free_games.extend([game for game in content["items"] if game.get("final_price", 1) == 0])

    # Ensure the list of free games is not empty
    assert free_games, "No free games found in any category!"

    print(f"Found {len(free_games)} free games")
    logger.info(f"Found {len(free_games)} free games")

    print("Free games detected!")
    logger.info("Free games detected!")
