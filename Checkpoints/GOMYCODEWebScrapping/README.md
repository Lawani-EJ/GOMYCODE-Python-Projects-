# Web Scraping Checkpoint
This repository contains a Python script that performs web scraping using the `requests` and `BeautifulSoup` libraries. The script is designed to fetch information from Wikipedia based on user input, as assigned for the web scraping checkpoint at GOMYCODE.

## 📝 Script Overview

### 1. Purpose
The script allows users to search for a topic on Wikipedia, retrieves the corresponding page, and extracts key details from the infobox (if available) as well as the first few paragraphs of the content.

### 2. Features
- **Dynamic User Input:** The user inputs a search term, which the script formats to match Wikipedia's URL structure.
- **Data Extraction:** The script retrieves and displays information from the Wikipedia infobox (if available) and the first two paragraphs of the article.
- **Error Handling:** If the page does not contain an infobox or any other error occurs, the script provides an appropriate message.

## 🔧 Technologies Used
- **Python**: The core programming language used for the script.
- **Requests**: To send HTTP requests and fetch the webpage.
- **BeautifulSoup**: For parsing the HTML content and extracting the desired information.
- **String Manipulation**: To format the user input for URL construction.

## 📂 How It Works
1. **User Input**: The user enters a search term.
2. **URL Construction**: The script formats the input to create a valid Wikipedia URL.
3. **Web Scraping**:
   - Fetches the content from the Wikipedia page.
   - Extracts information from the infobox table (if present).
   - Prints the first two paragraphs of the article.
4. **Error Handling**: Provides error messages for missing content or failed requests.

## ⚠️ Important Note
The script performs web scraping, which may be against the terms of service of some websites. Use it responsibly, and respect the terms and conditions of the source website.