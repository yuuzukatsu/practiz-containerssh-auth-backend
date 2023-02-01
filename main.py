import flask
from flask import request, jsonify, Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

password = [
    {
        "username": "yzk",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "passwordBase64": "Y29iYQ=="
    }
]

pubkey = [
    {
        "username": "yzk",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "publicKey": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO+JyAQHdjnMLd6Hg5Pblet6L83Eetfu/ZeDoNlgPrr9 eddsa-key-20221230"
    }
]

 

@app.route('/', methods=['GET'])
def home():
    return "<h1>API TEST</h1><p>API for ContainerSSH</p>"

@app.route('/password', methods=['POST'])
def api_password():
    
    if 'username' in request.json:
        if 'passwordBase64' in request.json:
            username = request.json['username']
            passwordBase64 = request.json['passwordBase64']
            print("DB Username = " + username)
            print("Request Username = " + request.json['username'])
            print("DB Password = " + passwordBase64)
            print("Request Password = " + request.json['passwordBase64'])
            for i in password:
                if i['username'] == username:
                    if i['passwordBase64'] == passwordBase64:
                        print("Login Success")
                        return jsonify({
                            "success": True
                        })
            else:
                print("Wrong Password")
                return Response("Wrong Password", 401)
        else:
            print("No Password")
            return Response("No Password", 401)
    else:
        print("No Username")
        return Response("No Username", 401)

@app.route('/config', methods=['POST'])
def api_config():
    
    if 'username' in request.json:
        return jsonify({
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:node",
                            "shell": "/bin/bash"
                        }
                    }
                }
            }
        })
    else:
        return Response("No Username", 401)

app.run(host="0.0.0.0")