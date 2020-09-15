# grpc_test
  ### simple_grpc_transmit_image

file structure:
  * grpc_test
    * image
      * 01.jpg
      * 02.jpg
      * 03.jpg
      * 04.jpg        
    * result
    * client.py
    * data.proto
    * data_pb2.py
    * data_pb2_grpc.py
    * server.py
    
------


```
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. data.proto
```

Terminal:Local(1)

```
python server.py
```

Terminal:Local(2)

```
python client
```

