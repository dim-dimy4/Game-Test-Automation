import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
def test_check_steam_free_games():
    """Test case for checking free games on Steam."""
    
    # Set up WebDriver (Chrome)
    driver = webdriver.Chrome()

    try:
        # Open Steam website
        driver.get("https://store.steampowered.com/")
        driver.maximize_window()

        # Wait for the search bar
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "store_nav_search_term"))
        )

        # Ensure we are on the correct page
        assert "Steam" in driver.title, "Steam page title is incorrect!"

        # Enter "Free Games" and search
        search_box.send_keys("Free Games")
        search_box.send_keys(Keys.RETURN)

        # Wait for results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search_name"))
        )

        # Get game titles
        game_titles = driver.find_elements(By.CLASS_NAME, "search_name")

        # Find game prices
        price_selectors = ["search_price", "discount_final_price", "col search_price_discount_combined"]
        game_prices = []
        
        for selector in price_selectors:
            prices = driver.find_elements(By.CLASS_NAME, selector)
            if prices:
                game_prices = prices
                break

        # Debugging: Show found elements
        print(f"Found {len(game_titles)} game titles.")
        print(f"Found {len(game_prices)} game prices.")

        # Ensure lists are not empty
        assert game_titles, "No game titles found!"
        assert game_prices, "No game prices found!"

        # Extract free games
        free_games = []
        for title, price in zip(game_titles, game_prices):
            game_name = title.text.strip()
            game_price = " ".join(price.text.strip().split("\n"))  # Merge multiline text

            print(f"Game: {game_name} | Price: {game_price}")

            if "Бесплатно" in game_price or "Free" in game_price:
                free_games.append(game_name)

        assert free_games, "No free games found!"
        print(f"✔ Found {len(free_games)} free games!")

    finally:
        driver.quit()
