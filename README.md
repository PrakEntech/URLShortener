# URL Shortener

This is a simple URL shortening service built using Flask. It allows you to enter a long URL and generates a short, easily shareable link. The application also handles redirection, allowing users to navigate to the original URL via the shortened link.

## Features

- **URL Validation**: The application validates URLs to ensure they are correctly formatted and contain the appropriate scheme (http, https, ftp).
- **Custom Short URLs**: Generates unique short URLs using a mix of alphanumeric characters and symbols.
- **Redirection**: Automatically redirects users from the short URL to the original long URL.

## How It Works

1. **User Input**: Enter a URL that you want to shorten.
2. **URL Validation**: The application checks if the URL is valid and correctly formatted.
3. **Short URL Generation**: If the URL is valid, the app generates a unique 5-character identifier for the URL.
4. **Redirection**: When a user visits the short URL, they are redirected to the original long URL.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PrakEntech/URLShortener.git
   cd URLShortener
   ```

2. **Install the Required Dependencies**:
   Ensure you have Python installed, then install flask:
   ```bash
   pip install flask
   ```

3. **Run the App**:
   ```bash
   python flask_app.py
   ```

## Usage

- **Accessing the App**: Open your browser and go to `http://127.0.0.1:5000/`.
- **Enter URL**: Input the URL you wish to shorten and submit the form.
- **Get Shortened URL**: The app will provide a shortened URL, which you can copy and share.
- **Redirection**: Accessing the shortened URL in the browser will redirect you to the original URL.

## Code Overview

- **Flask**: Used to handle the web server and routing.
- **Regex**: Employed to validate the format of URLs and ensure proper schema.
- **Randomized Link Generation**: Uses a combination of letters, numbers, and symbols to create unique short links.

## Files

- **flask_app.py**: The main application file that handles routing, URL validation, and redirection.
- **templates/index.html**: The front-end template where users input their long URLs.
- **templates/goto.html**: The template that displays the shortened URL.

## Future Enhancements

- **Database Integration**: Replace the text file storage with a database for better scalability.
- **Custom Short Links**: Allow users to create custom short links.
- **Analytics**: Track the number of clicks for each shortened URL.
