from flask import Flask, render_template, request, redirect, url_for
import speech2txt

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    results = []
    return render_template('index.html',
                           shortrecog = 1,
                           results=results)

@app.route('/shortrecog', methods=['POST'])
def shortrecog():
    token  = request.form['token']
    lang   = request.form['lang']
    f      = request.files['file']
    audio  = f.read()
    gsa    = speech2txt.GoogleSpeechAPI(token)
    results = gsa.shortRecognize(audio, lang)
    return render_template('index.html',
                           shortrecog = 1,
                           token      = token,
                           lang       = lang,
                           results    = results)

@app.route('/longrecog', methods=['POST'])
def longrecog():
    token  = request.form['token']
    lang   = request.form['lang']
    f      = request.files['file']
    audio  = f.read()
    gsa    = speech2txt.GoogleSpeechAPI(token)
    results= gsa.longRecognize(audio, lang)
    return render_template('index.html',
                           longrecog = 1,
                           token     = token,
                           lang      = lang,
                           results   = results)

@app.route('/getresult', methods=['POST'])
def getresult():
    token  = request.form['token']
    name   = request.form['name']
    gsa    = speech2txt.GoogleSpeechAPI(token)
    results= gsa.getResult(name)
    return render_template('index.html',
                           getresult = 1,
                           token     = token,
                           name      = name,
                           results   = results)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
