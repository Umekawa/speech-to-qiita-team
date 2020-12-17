import requests

import azure.cognitiveservices.speech as speechsdk
import time
import re
import settings
import sys

ACCESS_TOKEN = settings.ACCESS_TOKEN
TEAM_DOMAIN = settings.TEAM_DOMAIN
GROUP_NAME = settings.GROUP_NAME
COEDITING = settings.COEDITING

SUBSCRIPTION = settings.SUBSCRIPTION
REGION = settings.REGION

def text_from_audiofile(filepath):
    speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION, region=REGION)
    speech_config.speech_recognition_language='ja-JP'
    audio_input = speechsdk.AudioConfig(filename=filepath)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    done = False
    text = ''
    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
    def split(evt):
        st = re.search(r'\".+?\"',str(evt))
        new_text = st.group(0).strip('"')
        nonlocal text
        text = text + '\n' + new_text
    speech_recognizer.recognized.connect(split)

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    speech_recognizer.stop_continuous_recognition()
    return text

def post_qiita_team(filepath):
    url = 'https://' + TEAM_DOMAIN + '.qiita.com/api/v2/items/'
    body = text_from_audiofile(filepath)
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
    response = requests.post(url, headers = headers, json=params)

if __name__ == '__main__':
    post_qiita_team(sys.argv[1])
