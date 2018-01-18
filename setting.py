import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

Github_User = os.environ.get("Github_User")
Github_Pass = os.environ.get("Github_Password")
