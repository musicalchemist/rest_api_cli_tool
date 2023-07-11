import argparse
import api_handler as api

def list_command(args):
    post = api.get_posts(args.id)
    print(post)

def create_command(args):
    post = api.create_post(args.title, args.body, args.user_id)
    print(post)

def update_command(args):
    post = api.update_post(args.id, args.title, args.body, args.user_id)
    print(post)

def delete_command(args):
    status_code = api.delete_post(args.id)
    print(f"Delete status code: {status_code}")

parser = argparse.ArgumentParser(prog="jsonplaceholder")
subparsers = parser.add_subparsers()

parser_list = subparsers.add_parser("list")
parser_list.set_defaults(func=list_command)
parser_list.add_argument("--id", type=int, help="ID of the post to retrieve")

parser_create = subparsers.add_parser("create")
parser_create.set_defaults(func=create_command)
parser_create.add_argument("--title", required=True, help="Title of the post")
parser_create.add_argument("--body", required=True, help="Body of the post")
parser_create.add_argument("--user_id", type=int, required=True, help="User ID of the post author")

parser_update = subparsers.add_parser("update")
parser_update.set_defaults(func=update_command)
parser_update.add_argument("--id", type=int, required=True, help="ID of the post to update")
parser_update.add_argument("--title", help="Updated title of the post")
parser_update.add_argument("--body", help="Updated body of the post")
parser_update.add_argument("--user_id", type=int, help="Updated User ID of the post author")

parser_delete = subparsers.add_parser("delete")
parser_delete.set_defaults(func=delete_command)
parser_delete.add_argument("--id", type=int, required=True, help="ID of the post to delete")

args = parser.parse_args()
args.func(args)
