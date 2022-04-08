import os
import boto3

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

poly = boto3.client('polly', region_name='us-west-2',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
# print(client.describe_voices(LanguageCode='en-GB', Engine='neural', IncludeAdditionalLanguageCodes=False, NextToken='string'))

def play_sound(text):
    response = poly.synthesize_speech(Engine='neural',
                                      LanguageCode='en-US',
                                      OutputFormat='mp3',
                                      Text=text,
                                      VoiceId='Joanna',
                                      TextType='text')
    body = response['AudioStream'].read()

    with open('voice.mp3', 'wb') as file:
        file.write(body)
        file.close()

play_sound("Hello")