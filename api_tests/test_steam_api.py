import requests
import logging
import json

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler for logging
file_handler = logging.FileHandler("steam_api.log", mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Add the file handler to the logger
logger.addHandler(file_handler)

def test_get_steam_app_list():
    """Test retrieving the list of Steam apps."""
    
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
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

    # Check if the response contains the expected structure
    if "applist" in data and "apps" in data["applist"]:
        game_list = [app["name"] for app in data["applist"]["apps"]]
        logger.info(f"Total games in list: {len(game_list)}")
        print(f"Total games in list: {len(game_list)}")
    else:
        logger.error("Invalid response format")
        print("Invalid response format")
