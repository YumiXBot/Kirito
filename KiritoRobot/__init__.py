# By < @Awesome_Prince >
# // @BlackLoverNeterk //

import logging
import os
import sys
import time
from logging import INFO, basicConfig, getLogger
from os import environ as e

from telethon import TelegramClient
from telethon.sessions import StringSession

StartTime = time.time()
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

CMD_HELP = {}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
)

LOGGER = logging.getLogger(__name__)
TOKEN = e.get("TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID", 5362971543))
API_KEY = int(os.environ.get("API_KEY", ))
API_HASH = os.environ.get("API_HASH", "")
DB_URI = os.environ.get("DATABASE_URL", "")
BOT_ID = 5534493283

BlackLover = TelegramClient(None, API_KEY, API_HASH)
