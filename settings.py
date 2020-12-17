import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Settings for Qiita Team
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
TEAM_DOMAIN = os.environ.get('TEAM_DOMAIN')
GROUP_NAME = os.environ.get('GROUP_NAME') if os.environ.get('GROUP_NAME') != '' and os.environ.get('GROUP_NAME') != None else None
COEDITING = True if os.environ.get('COEDITING') == 'True' else False

# Settings for speech to text api
SUBSCRIPTION = os.environ.get('SUBSCRIPTION')
REGION = os.environ.get('REGION')
