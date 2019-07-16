# Image recognition service
This service receives image's URL and recognizes objects on photo by using pretrained CNN model [VGG16][vgg16].  Code written in python with KERAS API.

To start application create **parameters** file in root and define these fields:
```xml
proxy_username = ""
proxy_password = ""
proxy_host = ""
proxy_port = ""
client_port = ""
```
where client_port is requester application port. Be ready to get response in GET request-body by this IP.

# API
To get an answer, send GET-request to /predict

Parameters:
* url - image URL (requiered)
* chat_id - special info

Application send the result of processing back to caller IP with port you have set in parameters file in GET-request in parameter "text". 

[vgg16]: <https://keras.io/applications/>
