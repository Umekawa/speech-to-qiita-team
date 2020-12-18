import azure.cognitiveservices.speech as speechsdk
import time
import re
import settings

# Setting for speech to text
SUBSCRIPTION = settings.SUBSCRIPTION
REGION = settings.REGION


def get_text(filepath):
  speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION, region=REGION)
  speech_config.speech_recognition_language = 'ja-JP'
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