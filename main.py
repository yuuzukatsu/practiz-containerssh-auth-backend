import flask
from flask import request, jsonify, Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

password = [
    {
        "username": "node",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "passwordBase64": "Y29iYQ=="
    },{
        "username": "nix",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "passwordBase64": "Y29iYQ=="
    },{
        "username": "ubuntu",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "passwordBase64": "Y29iYQ=="
    },{
        "username": "docker",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "passwordBase64": "Y29iYQ=="
    },{
        "username": "python",
        "remoteAddress": "0.0.0.0",
        # "connectionId": "123",
        "passwordBase64": "Y29iYQ=="
    },{
        "username": "pythonnix",
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

config = [
    {
        "username": "nix",
        "konfigurasi":{
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:nix"
                        },
                        "shellCommand":["/bin/sh"]
                    }
                }
            }
        }
    },
    {
        "username": "node",
        "konfigurasi":{
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:node"
                        },
                        "shellCommand":["/bin/sh"]
                    }
                }
            }
        }
    },{
        "username": "ubuntu",
        "konfigurasi":{
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:ubuntu",
                            "HostConfig":{
                                "Privileged": True
                            }
                        },
                        "shellCommand":["/bin/bash"]
                    }
                }
            }
        }
    },{
        "username": "docker",
        "konfigurasi":{
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:dind",
                            "HostConfig":{
                                "Privileged": True
                            }
                        },
                        "shellCommand":["/bin/sh"]
                    }
                }
            }
        }
    },{
        "username": "pythonnix",
        "konfigurasi":{
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:python_nix"
                        },
                        "shellCommand":["/nix/store/gl20v5wsmwr3gpg313v2ffr4nalzhb6a-user-environment/bin/nix-shell", "-p", "python3"]
                    }
                }
            }
        }
    },{
        "username": "python",
        "konfigurasi":{
            "config": {
                "docker": {
                    "execution": {
                        "container": {
                            "image": "yuuzukatsu/coba:python"
                        },
                        "shellCommand":["/bin/sh"]
                    }
                }
            }
        }
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
                print("User Not Found")
                return Response("User Not Found", 401)
                
        else:
            print("No Password")
            return Response("No Password", 401)
    else:
        print("No Username")
        return Response("No Username", 401)

@app.route('/config', methods=['POST'])
def api_config():
    
    if 'username' in request.json:
        username = request.json['username']
        for i in config:
            if i['username'] == username:
                print(i['konfigurasi'])
                return jsonify(i['konfigurasi'])
        else:
            return Response("Username Not Found", 401)
    else:
        return Response("No Username", 401)

app.run(host="0.0.0.0")
