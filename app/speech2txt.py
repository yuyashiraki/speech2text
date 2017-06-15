import os, json, base64, time
import urllib2

class GoogleSpeechAPI:
    """A class for requesting Google Speech API"""
    def __init__(self, token):
        self.token = token
    def shortRecognize(self, audio, lang_code):
        endpoint = 'https://speech.googleapis.com/v1/speech:recognize'
        enc_f    = base64.b64encode(audio)
        req      = urllib2.Request(endpoint)
        ret      = []
        req.add_header('Authorization', 'Bearer ' + self.token)
        req.add_header('Content-Type', 'application/json')
        body     = {
            "config": {
                "languageCode" : lang_code,
            },
            "audio": {
                "content" : enc_f,
            },
        }
        response = urllib2.urlopen(req, json.dumps(body))
        res      = json.loads(response.read())
        transcripts = "Transcript:"
        for result in res['results']:
            for alternative in result['alternatives']:
                transcripts += " " + alternative['transcript']
        ret.append(transcripts)
        return ret 
    def longRecognize(self, audio, lang_code):
        endpoint = 'https://speech.googleapis.com/v1/speech:longrunningrecognize'
        enc_f    = base64.b64encode(audio)
        req      = urllib2.Request(endpoint)
        ret      = []
        req.add_header('Authorization', 'Bearer ' + self.token)
        req.add_header('Content-Type', 'application/json')
        body     = {
            "config": {
                "languageCode": lang_code,
            },
            "audio": {
                "content": enc_f,
            },
        }
        response = urllib2.urlopen(req, json.dumps(body))
        res      = json.loads(response.read())
        if "name" in res:
            ret.append("Name: " + res['name'])
        return ret
        
    def getResult(self, name):
        endpoint = 'https://speech.googleapis.com/v1/operations/' + name
        req      = urllib2.Request(endpoint)
        ret      = []
        req.add_header('Authorization', 'Bearer ' + self.token)
        req.add_header('Content-Type', 'application/json')
        http_response = urllib2.urlopen(req)
        res      = json.loads(http_response.read())
        if "name" in res:
            ret.append("Name:" + res['name'])
        if "metadata" in res:
            metadata = res['metadata']
            if 'progressPercent' in metadata:
                ret.append("Progress Percent: {:d}% done".format(metadata['progressPercent']))
        if 'done' in res and res['done']:
            response = res['response']
            transcripts = "Transcript:"
            for result in response['results']:
                for alternative in result['alternatives']:
                    transcripts += ' ' + alternative['transcript']
            ret.append(transcripts)
        return ret
