# -*- coding: utf-8 -*-

import grpc
import time
import datetime
from concurrent import futures
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc
import cv2
import base64
import numpy as np

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8008'


class TransmitData(pb2_grpc.TransmitDataServicer):
    def DoTransmit(self, request, context):
        data = request.data
        print(pb2.DataResponse(result=data.upper()))
        decode_img = base64.b64decode(data)
        img = np.frombuffer(decode_img, dtype=np.int8)
        datetime_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f'result/{datetime_now}.jpg', 'wb') as f:
            f.write(img)
            f.flush
        return pb2.DataResponse(result=f'ok! saved to result/{datetime_now}.jpg')


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    pb2_grpc.add_TransmitDataServicer_to_server(TransmitData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            print(f'start===============>{_HOST}:{_PORT}')
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
