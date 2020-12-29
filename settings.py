import os
from os.path import join, dirname
from dotenv import load_dotenv

# import os
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PREFIX = os.environ.get("PREFIX")

# # settings.py
# from dotenv import load_dotenv
# load_dotenv()

# # OR, the same with increased verbosity
# load_dotenv(verbose=True)

# # OR, explicitly providing path to '.env'
# from pathlib import Path  # Python 3.6+ only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# import os
# BOT_TOKEN = os.getenv("BOT_TOKEN")
# PREFIX = os.getenv("PREFIX")
# # SECRET_KEY = os.getenv("EMAIL")
# # DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

