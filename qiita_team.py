import requests
import settings

# Setting for Qiita Team
ACCESS_TOKEN = settings.ACCESS_TOKEN
TEAM_DOMAIN = settings.TEAM_DOMAIN
GROUP_NAME = settings.GROUP_NAME
COEDITING = settings.COEDITING

def post_qiita_team(filepath, body):
  url = 'https://' + TEAM_DOMAIN + '.qiita.com/api/v2/items/'
  body = body
  params = {
    'body': body,
    'coediting': COEDITING,
    'tags': [
      {'name': '音声認識'},
      {'name': 'QiitaAPI'}
    ],
    'group_url_name': GROUP_NAME,
    'title': filepath.split('/')[-1].split('.')[0],
  }
  headers = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}
  requests.post(url, headers=headers, json=params)
