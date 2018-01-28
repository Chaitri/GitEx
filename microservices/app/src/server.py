from src import app
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import json
#import os
from flask import request
from flask import make_response, jsonify
# from flask import jsonify

@app.route("/")
def home():
    return "Hello World!"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return "webhook page"
    else:
        req = request.get_json(silent=True, force=True)

        print("Request:")
        print(json.dumps(req, indent=4))
        return req

        #res = process_req(req)

        #resq = json.dumps(res)
        # print(res)
        #r = make_response(jsonify(resq))
        #r.add_header("Content-type", "application/json")
        #return r


if __name__ == '__main__':
    app.run()