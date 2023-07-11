import requests

API_URL = "https://jsonplaceholder.typicode.com"

def get_posts(post_id=None):
    url = f"{API_URL}/posts"
    if post_id:
        url += f"/{post_id}"
    response = requests.get(url)
    return response.json()

def create_post(title, body, user_id):
    url = f"{API_URL}/posts"
    post = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, data=post)
    return response.json()

def update_post(post_id, title=None, body=None, user_id=None):
    url = f"{API_URL}/posts/{post_id}"
    updated_fields = {}
    if title:
        updated_fields['title'] = title
    if body:
        updated_fields['body'] = body
    if user_id:
        updated_fields['userId'] = user_id
    response = requests.put(url, data=updated_fields)
    return response.json()

def delete_post(post_id):
    url = f"{API_URL}/posts/{post_id}"
    response = requests.delete(url)
    return response.status_code
