# REST API CLI Tool

This project is a simple Python-based Command Line Interface (CLI) tool designed to interact with the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/). JSONPlaceholder is a free to use fake REST API that can be used for testing and prototyping.

The tool is capable of executing GET, POST, PUT, and DELETE requests against the JSONPlaceholder API.

## Features

- Fetch all posts or a single post by ID
- Create a new post
- Update an existing post
- Delete a post

## How to Install

1. Clone this repository.
2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

## How to Use

Here are some example commands you can run:

Fetch all posts:

    ```
    python main.py list
    ```

Fetch a single post by ID:

    ```
    python main.py list --id 1
    ```

Create a new post:

    ```
    python main.py create --title "test" --body "this is a test" --user_id 1
    ```

Update an existing post:

    ```
    python main.py update --id 1 --title "updated title" --body "updated body" --user_id 1
    ```

Delete a post:

    ```
    python main.py delete --id 1
    ```

## Tests

To run tests, use the following command:
`python -m unittest tests/test_api_handler.py`

## Future Improvements

- Add more comprehensive error handling and messages
- Add more testing
- Support more endpoints of the JSONPlaceholder API
