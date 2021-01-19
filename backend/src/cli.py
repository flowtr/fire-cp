import argparse
from .api.models.user import User, UserDAO
from getpass import getpass
from .config import logger

parser = argparse.ArgumentParser(description="Process some integers.")

subparsers = parser.add_subparsers()
db_init_parser = subparsers.add_parser("init")

db_init_parser.add_argument("-u", "--username")

args = parser.parse_args()
DAO = UserDAO()
if args and args.username:
    password = getpass()
    try:
        if DAO.create(
            {"username": args.username, "password": password.encode("utf-8")}
        ):
            logger.info(f"Created user {args.username}")
        else:
            logger.error(
                f"Unable to create user {args.username}. This user may already exist."
            )
    except Exception as ex:
        logger.error(
            f"Unable to create user {args.username}: {ex}",
        )
