import requests

def get_web_page(url):
    """
    Retrieves a web page using the requests library.
    Args:
    url (str): URL of the web page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        print(response.text[:500]) # Print the first 500 characters of the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == '__main__':
    get_web_page('https://www.example.com')
