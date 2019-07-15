import datetime
import shutil

from sphinx.util import requests

import parameters

proxy_username =parameters.proxy_username
proxy_password = parameters.proxy_password
proxy_host = parameters.proxy_host
proxy_port = parameters.proxy_port
client_port = parameters.client_port

def send_response(text, chat_id, client_ip):
    url = "http://{client_ip}:{client_port}".format(client_ip=client_ip, client_port=client_port)
    if chat_id>0:
        p = (('text', text), ('chat_id', chat_id))
    else:
        p = ('text', text)
    r = requests.get(url, params=p)

def download_image(url):
    time = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
    proxies = {"https": "socks5://{username}:{password}@{host}:{ip}"
        .format(username=proxy_username,password=proxy_password,host=proxy_host,ip=proxy_port)}
    filename = str(time) + ".jpg"
    response = requests.get(url, stream=True, proxies=proxies)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return filename