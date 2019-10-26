from statistics_app.models import Result
from JunctionX.settings import BASE_DIR, STATIC_DIR
import time
from xml.etree import ElementTree
import requests
import json
import asyncio, io, glob, os, sys, time, uuid, requests
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType


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
    if data != []:
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
