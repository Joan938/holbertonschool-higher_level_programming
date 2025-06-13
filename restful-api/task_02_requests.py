import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print the status code
    and each post title.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            title = post.get('title')
            if title:
                print(title)
    else:
        print(f'Failed to fetch posts: {response.status_code}')


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them to posts.csv
    with columns: id, title, body.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        # Structure data as list of dicts
        rows = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        # Write to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
    else:
        raise Exception(f'Failed to fetch posts: {response.status_code}')
