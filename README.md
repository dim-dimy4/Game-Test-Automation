![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)

Automated testing for gaming services like Steam API, Epic Games Store, and game launchers.
Automated tests for game UI and mechanics using Selenium and Pytest. The goal is to test game features such as login, inventory, and actions within a web-based game environment.

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
## Project Structure
```bash
Game-Test-Automation/
├── pages/                # Page Object Model
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── ...
├── tests/                # Tests
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
├── conftest.py           # Pytest Fixtures
├── requirements.txt      # Project Dependencies
├── README.md             # Project Description
└── .gitignore            # Exceptions for Git
```
## Contacts
E-mail: kachuk.mail@gmail.com
LinkedIn: [Dmytro Kachuk](https://www.linkedin.com/in/dmytro-kachuk-289628206/)  






