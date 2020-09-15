# -*- coding: utf-8 -*-

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc
import cv2
import base64
import numpy as np

_HOST = 'localhost'
_PORT = '8008'
_PATH = 'image/04.jpg'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    print(conn)
    client = pb2_grpc.TransmitDataStub(channel=conn)
    print(client)
    img = cv2.imread(_PATH)
    cv2.waitKey(0)
    img_encode = cv2.imencode('.jpg', img)[1]
    data_encode = base64.b64encode(img_encode)

    response = client.DoTransmit(pb2.DataRequest(data=data_encode))
    print("received: " + response.result)


if __name__ == '__main__':
    run()
