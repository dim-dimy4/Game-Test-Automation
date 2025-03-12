import requests
import logging
import json

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler for logging
file_handler = logging.FileHandler("steam_featured.log", mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Add the handler to the logger
logger.addHandler(file_handler)

def test_get_steam_featured():
    """Test retrieving featured games (discounts and promotions)."""
    
    url = "https://store.steampowered.com/api/featured/"
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

    # Verify that the response contains required sections
    required_sections = ["featured_win", "featured_mac", "featured_linux"]
    for section in required_sections:
        assert section in data, f"Missing section '{section}' in response"
        assert isinstance(data[section], list), f"Section '{section}' is not a list"
        print(f"Section '{section}' found with {len(data[section])} games")
        logger.info(f"Section '{section}' found with {len(data[section])} games")

    # Verify that at least one game has a discount
    has_discount = any(game.get("discount_percent", 0) > 0 for game in data["featured_win"])
    assert has_discount, "No games with discounts found"
    print("Found games with discounts")
    logger.info("Found games with discounts")
