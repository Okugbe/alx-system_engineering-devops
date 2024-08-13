#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set the base URL and headers
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful and the subreddit is valid
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers')
        else:
            return 0
    except Exception:
        return 0

