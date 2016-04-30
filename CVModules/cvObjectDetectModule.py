import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvController
import argparse
import base64
import httplib2
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'

class ObjectModule(object):

    def __init__(self):
        self.toPrint = True
        self.currentFrame = None


    def run(self, image,condition):

        self.currentFrame = image
        picName = "../photos/objDetectTemp.jpg"
        cv2.imwrite(picName, image)
        return (self.testCondition(condition,image,picName), [])


    def objectDetect(self,photo_file):
        credentials = GoogleCredentials.get_application_default()

        service = discovery.build('vision', 'v1', credentials=credentials,
                                  discoveryServiceUrl=DISCOVERY_URL)

        with open(photo_file, 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = service.images().annotate(body={
                'requests': [{
                    'image': {
                        'content': image_content.decode('UTF-8')
                    },
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': 4
                    }]
                }]
            })
            response = service_request.execute()
            print response
            tags = []
            r = response['responses'][0]['labelAnnotations']
            for element in r:
                tags.append(element['description'])
            """tags.append(response['responses'][0]['labelAnnotations'][0]['description'])
            tags.append(response['responses'][0]['labelAnnotations'][1]['description'])
            tags.append(response['responses'][0]['labelAnnotations'][2]['description'])
            tags.append(response['responses'][0]['labelAnnotations'][3]['description'])"""
            return tags


    def testCondition(self,condition,image,pictureName):
        variable = condition["var"]
        comparison = condition["comp"]
        equality = condition["eq"]

        tags = self.objectDetect(pictureName)
        compTags = equality.split(',')

        
        for ct in compTags:
            for t in tags:
                if t == ct:
                    return True

        return False
