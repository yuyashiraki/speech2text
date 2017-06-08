import os, json, base64
import urllib2
abspath = os.path.dirname(os.path.abspath(__file__))

endpoint = 'https://speech.googleapis.com/v1/speech:recognize'

with open(abspath + '/../.token', 'r') as token_file:
    token = token_file.readline().replace('\n', '')

# The name of the audio file to transcribe
file_name = os.path.join(
    abspath + '/..',
    'resources',
    'hello.wav')

# Loads the audio into memory
with open(file_name, 'rb') as audio_file:
    content = audio_file.read()

# Encode by base64
enc_file = base64.b64encode(content)

req = urllib2.Request(endpoint)
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')

body = {
    "config": {		
        "languageCode": "en-US"
    },
    "audio": {
        "content": enc_file 
    }
}

response = urllib2.urlopen(req, json.dumps(body))
res = json.loads(response.read())

for result in res['results']:
    for alternative in result['alternatives']:
        print alternative['transcript']
