import requests
import flask
import datetime
import os
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

app = flask.Flask(__name__)

authorized_addrs = [
    '127.0.0.1',
    '192.168.0.107',
    '192.168.0.106'
]

@app.route('/')
def home():
    if flask.request.remote_addr in authorized_addrs:
        req = requests.get('http://192.168.0.83/1/status')
        if req.text[:2] == 'on':
            s1 = 'OFF'
        else:
            s1 = 'ON'
        req = requests.get('http://192.168.0.83/2/status')
        if req.text[:2] == 'on':
            s2 = 'OFF'
        else:
            s2 = 'ON'
        req = requests.get('http://192.168.0.83/3/status')
        if req.text[:2] == 'on':
            s3 = 'OFF'
        else:
            s3 = 'ON'
        req = requests.get('http://192.168.0.83/4/status')
        if req.text[:2] == 'on':
            s4 = 'OFF'
        else:
            s4 = 'ON'
        dt = datetime.datetime.now()
        time = dt.time()
        return flask.render_template('home.html', sut=str(time)[:8], s1=s1, s2=s2, s3=s3, s4=s4)
    else:
        return 'UNAUTHORIZED ACCESS', 403

@app.route('/switches')
def switches():
    if flask.request.remote_addr in authorized_addrs:
        req = requests.get('http://192.168.0.83/1/status')
        if req.text[:2] == 'on':
            s1 = 'OFF'
        else:
            s1 = 'ON'
        req = requests.get('http://192.168.0.83/2/status')
        if req.text[:2] == 'on':
            s2 = 'OFF'
        else:
            s2 = 'ON'
        req = requests.get('http://192.168.0.83/3/status')
        if req.text[:2] == 'on':
            s3 = 'OFF'
        else:
            s3 = 'ON'
        req = requests.get('http://192.168.0.83/4/status')
        if req.text[:2] == 'on':
            s4 = 'OFF'
        else:
            s4 = 'ON'
        dt = datetime.datetime.now()
        time = dt.time()
        return flask.render_template('switches.html', s1=s1, s2=s2, s3=s3, s4=s4, sut=str(time)[:8])
    else:
        return 'UNAUTHORIZED ACCESS', 403

@app.route('/s/<switch>/<mode>')
def switchChange(switch, mode):
    if flask.request.remote_addr in authorized_addrs:
        req = requests.get('http://192.168.0.83/'+switch[1:]+'/'+mode)
        return flask.redirect('/switches')
    else:
        return 'UNAUTHORIZED ACCESS', 403

@app.route('/get-remote_addr')
def get_remote_addr():
    return 'Your address is '+flask.request.remote_addr

@app.route('/test')
def test():
    return str(flask.request.user_agent)

if __name__=='__main__':
    context = ('local.crt', 'local.key')#certificate and key files
    app.run(debug=True, port='80', host='0.0.0.0')
