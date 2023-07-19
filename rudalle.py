import requests
import base64
from time import sleep
import asyncio
from PIL import Image
from io import BytesIO
import asyncio
import aiohttp

class rudalleClient:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryrlQE4GkVXTOCFaq3',
            'Origin': 'https://editor.fusionbrain.ai',
            'Pragma': 'no-cache',
            'Referer': 'https://editor.fusionbrain.ai/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
    def ask(self,prompt='cat', style='', width='512', height='512'):
        data = "------WebKitFormBoundaryrlQE4GkVXTOCFaq3\r\nContent-Disposition: form-data; name=\"params\"; filename=\"blob\"\r\nContent-Type: application/json\r\n\r\n{{\"type\":\"GENERATE\",\"style\":\"{style}\",\"width\":{width},\"height\":{height},\"generateParams\":{{\"query\":\"{prompt}\"}}}}\r\n------WebKitFormBoundaryrlQE4GkVXTOCFaq3--\r\n".format(style=style, prompt=prompt, width=width, height=height)
        resp = requests.post('https://api.fusionbrain.ai/web/api/v1/text2image/run?model_id=1', headers=self.headers, data=data.encode('utf-8'))
        json = resp.json()
        if json['status'] == "INITIAL":
            return True, json['uuid']
        return False, ''

    async def async_ask(self,prompt='cat', style='', width='512', height='512'):
        data = "------WebKitFormBoundaryrlQE4GkVXTOCFaq3\r\nContent-Disposition: form-data; name=\"params\"; filename=\"blob\"\r\nContent-Type: application/json\r\n\r\n{{\"type\":\"GENERATE\",\"style\":\"{style}\",\"width\":{width},\"height\":{height},\"generateParams\":{{\"query\":\"{prompt}\"}}}}\r\n------WebKitFormBoundaryrlQE4GkVXTOCFaq3--\r\n".format(style=style, prompt=prompt, width=width, height=height)
        async with aiohttp.ClientSession() as session:
            async with session.post('https://api.fusionbrain.ai/web/api/v1/text2image/run?model_id=1',
                                    headers=self.headers, data=data.encode('utf-8')) as resp:
                json = await resp.json()
                if json['status'] == "INITIAL":
                    return True, json['uuid']
                return False, ''

    def check(self,id):
        response = requests.get(
            f'https://api.fusionbrain.ai/web/api/v1/text2image/status/{id}',
            headers=self.headers,
        )
        resp = response.json()
        if resp['status'] in ['INITIAL','PROCESSING']: return "generating"
        if resp['status'] == 'DONE': return resp['images'][0]
        else:
            print(response.content)
            return response.content

    async def async_check(self, id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.fusionbrain.ai/web/api/v1/text2image/status/{id}',
                                   headers=self.headers) as response:
                resp = await response.json()
                if resp['status'] in ['INITIAL', 'PROCESSING']:
                    return 'generating'
                elif resp['status'] == 'DONE':
                    return [resp['images'][0], resp['censored']]
                else:
                    print(await response.content.read())
                    return await response.content.read()
    def load(self, image_data ,path):
        img_bytes = base64.b64decode(image_data)
        img = Image.open(BytesIO(img_bytes))
        img.save(path)
        return True

def generate(prompt, path='./out.png', style='DEFAULT', ratio='1:1'):
    ratios = {
        "1:1" : ["512", "512"],
        "16:9": ["1024", "576"],
        "9:16": ["576", "1024"],
        "3:2": ["960", "640"],
        "2:3": ["640", "960"]
    }
    width = ratios[ratio][0] if ratio in ratios else "512"
    height = ratios[ratio][1] if ratio in ratios else "512"
    client = rudalleClient()
    status, id = client.ask(prompt,style, width, height)
    if status != True:return False
    x = client.check(id)
    while x == 'generating':
        sleep(0.5)
        x = client.check(id)
    client.load(x[0], path)
    return x[1]

async def async_generate(prompt, path='./out.png', style='DEFAULT', ratio='1:1'):
    ratios = {
        "1:1" : ["512", "512"],
        "16:9": ["1024", "576"],
        "9:16": ["576", "1024"],
        "3:2": ["960", "640"],
        "2:3": ["640", "960"]
    }
    width = ratios[ratio][0] if ratio in ratios else "512"
    height = ratios[ratio][1] if ratio in ratios else "512"
    client = rudalleClient()
    status, id = await client.async_ask(prompt,style, width, height)
    if not status:return False
    x = await client.async_check(id)
    while x == 'generating':
        sleep(0.5)
        x = await client.async_check(id)
    client.load(x[0], path)
    return x[1]
