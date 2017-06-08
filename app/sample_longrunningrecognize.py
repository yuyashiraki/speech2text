import os, json, base64, time
import urllib2
abspath = os.path.dirname(os.path.abspath(__file__))

def longrunningrecognize_request(token, file_name):
    endpoint = 'https://speech.googleapis.com/v1/speech:longrunningrecognize'
    
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
    return res['name']


def longrunningrecognize_poll(token, name):
    endpoint = 'https://speech.googleapis.com/v1/operations/' + name
    
    req = urllib2.Request(endpoint)
    req.add_header('Authorization', 'Bearer ' + token)
    req.add_header('Content-Type', 'application/json')
    
    http_response = urllib2.urlopen(req)
    res = json.loads(http_response.read())
    if "metadata" in res:
        metadata = res['metadata']
        if 'progressPercent' in metadata:
            print "{:d}% done".format(metadata['progressPercent'])
    if 'done' in res and res['done']:
        response = res['response']
        transcript = "Transcript:"
        for result in response['results']:
            for alternative in result['alternatives']:
                transcript = transcript + ' ' + alternative['transcript']
        print transcript
        return 0
    else:
        return 1
 

with open(abspath + '/../.token', 'r') as token_file:
    token = token_file.readline().replace('\n', '')

# The name of the audio file to transcribe
file_name = os.path.join(
    abspath + '/..',
    'resources',
    'hello.wav')

name = longrunningrecognize_request(token, file_name)
while (longrunningrecognize_poll(token, name)):
    time.sleep(5)
