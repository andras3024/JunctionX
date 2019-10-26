from statistics_app.models import Result
from JunctionX.settings import BASE_DIR, MEDIA_DIR, MEDIA_ROOT
import requests
import json
import asyncio, io, glob, os, sys, time, uuid, requests
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import azure.cognitiveservices.speech as speechsdk


def emotion_detction(result_id):
    KEY = "0aa7184d59da46daa3c503a2ca802b4c"
    ENDPOINT = "https://facetestfirsttry.cognitiveservices.azure.com/face/v1.0/detect"
    result = Result.objects.get(pk=result_id)
    image_path = BASE_DIR + os.path.normpath(str(result.image.url))
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': KEY,
               'Content-Type': 'application/octet-stream'}
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    }
    response = requests.post(
        ENDPOINT, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    data = response.json()
    print(response)
    print(data)
    emotion = data[0]['faceAttributes']['emotion']
    result.emotion_0 = emotion['anger']
    result.emotion_1 = emotion['contempt']
    result.emotion_2 = emotion['disgust']
    result.emotion_3 = emotion['fear']
    result.emotion_4 = emotion['happiness']
    result.emotion_5 = emotion['neutral']
    result.emotion_6 = emotion['sadness']
    result.emotion_7 = emotion['surprise']
    result.save()

    '''response = requests.get(image_url)
    img = Image.open(BytesIO(image_data))
    draw = ImageDraw.Draw(img)
    for face in data:
        draw.rectangle(getRectangle(face), outline='red', width=5)'''


def text_to_speech(text):
    speech_key = "8c908ab70ab54a8f8d11657875e5a1be"
    service_region = "https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    # Synthesizes the received text to speech.
    # The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")

