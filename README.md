# Game Test Automation
![Python](https://img.shields.io/badge/python-3.10-blue)

Automated testing for gaming services like Steam API, Epic Games Store, and game launchers. The goal is to verify game features such as login, inventory, and interactions within a web-based gaming environment using Selenium and Pytest.

## Tech Stack
- Python 3
- Pytest
- Selenium WebDriver (for UI tests)
- Requests (for API testing)
- Allure Report (for test reporting)

## Installation & Setup
 ```sh
 git clone https://github.com/dim-dimy4/Game-Test-Automation.git
 cd Game-Test-Automation
 pip install -r requirements.txt
 ```
## Running Tests
   1. Running all tests:
```sh
pytest tests/
```
   2. Running with detailed output:
```sh
pytest -v
```
   3. Running with report:
 ```sh     
 pytest --alluredir=allure-results
 allure serve allure-results
```
## Test Scenarios
### API Tests
| Test Name                    | Description |
|------------------------------|------------|
| `test_get_steam_free_games.py` | Retrieves a list of free games from Steam API and verifies the response. |
| `test_steam_api.py`            | General API validation for Steam services. |
| `test_steam_featured.py`       | Fetches featured game categories from Steam and validates data structure. |
Example API request:
```python
import requests

url = "https://store.steampowered.com/api/featuredcategories/"
response = requests.get(url)

assert response.status_code == 200, "API request failed!"
print(response.json())
```
### UI tests
| Test Name                    | Description |
|------------------------------|------------|
| `check_steam_free_games.py` | Opens the Steam store, checks if free games are correctly listed. |
Examples UI test structure:
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/")
assert "Steam" in driver.title
driver.quit()
```
## Project Structure
```bash
Game-Test-Automation/
│── api_tests/        # API tests
│   ├── test_get_steam_free_games.py
│   ├── test_steam_api.py
│   ├── test_steam_featured.py
│
│── ui_tests/         # UI tests
│   ├── check_steam_free_games.py
│
│── .gitignore        # Git exclusions
│── pytest.ini        # Pytest configuration
│── requirements.txt  # Project dependencies
│── README.md         # Project description
```
## Supported Browsers for UI Testing
• Chrome (default)
• Firefox (can be configured)
• Edge (optional)
To run UI tests with a specific browser:
```sh
pytest --browser=firefox
```
## Adding New Tests
• API tests should be placed in api_tests/
• UI tests should be placed in ui_tests/
• Fixtures and configurations should be in conftest.py
## Contacts
E-mail: kachuk.mail@gmail.com
LinkedIn: [Dmytro Kachuk](https://www.linkedin.com/in/dmytro-kachuk-289628206/)  
## Next Steps
• Implement more UI tests for login and checkout.
• Add performance testing for API responses.
• Extend support for mobile testing.






