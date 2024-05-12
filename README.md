
# Wordle Wizard

This Python script automates playing the Wordle game from The New York Times using Selenium WebDriver.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Web Browser
- Chromedriver
- pyperclip
- CSV (built-in Python module)

Install the required dependencies using pip:


pip install selenium pyperclip


Download the Chromedriver executable and place it in your system's PATH or specify its path in the script.

## Usage

1. Clone the repository.
2. Ensure you have the necessary dependencies installed (see Requirements section).
3. Run the script using the command:


python main.py


The script will automatically start playing Wordle and record the answers along with the current date in a CSV file named `answers.csv`. You can adjust the number of games played or timeframes by modifying the `timeframe` variable in the script.

## Notes

- Ensure you have a stable internet connection while running the script to access the Wordle game webpage.
- Make sure to use the latest version of Chromedriver compatible with your Chrome browser version.

