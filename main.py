import os
from boto3 import client
import pdfplumber

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

poly = client('polly', region_name='us-west-2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)


def record_sound(text):
    response = poly.synthesize_speech(Engine='neural',
                                      LanguageCode='en-US',
                                      OutputFormat='mp3',
                                      Text=text,
                                      VoiceId='Joanna',
                                      TextType='text')
    body = response['AudioStream'].read()

    with open('voice.mp3', 'wb') as file:
        file.write(body)

text = ''

with pdfplumber.open('example.pdf') as pdf:
    for i in pdf.pages:
        text = text + i.extract_text()
print(text)

record_sound(text)
