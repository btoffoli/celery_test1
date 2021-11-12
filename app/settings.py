from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

config = {
    "broker": getenv("BROKER"),
    "name": getenv("WORKER_NAME")
}
