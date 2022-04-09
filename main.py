import os
from boto3 import client
import PyPDF2

import pdfplumber

with pdfplumber.open('example.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())
print("AAAAAAAAAA")
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
with open('example.pdf', 'rb') as pdfObj:
    pdfReader = PyPDF2.PdfFileReader(pdfObj)
    pages = pdfReader.numPages

    for i in range(pages):
        print(pdfReader.getPage(i).extractText())
        text = text + pdfReader.getPage(i).extractText()

record_sound(text)
