#!/usr/bin/python3
""" Task 02 - Requests """

import requests
import csv


def fetch_and_print_posts():
    """ Fetch and print posts """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        posts_data = []
        posts_data = []
        for post in posts:
            post_data = {key: post[key] for key in ['id', 'title', 'body']}
            posts_data.append(post_data)
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
