from src import app
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
#import os


#from flask import request
from flask import make_response
# from flask import jsonify


@app.route("/")
def home():
    return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = process_req(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def process_req(req):
    if req.get("result").get("action") == "query":
        qry = req.get("result").get("parameters").get("text")
        res = wa_search(qry)
        return res


def wa_search(query):
    url = 'http://api.wolframalpha.com/v1/result?appid=UJKYEW-YKL88PHUER'
    srch = query.replace(' ', '+')
    final_url = url + "&i=" + srch + "%3f"

    obj = requests.get(final_url)
    data = obj.text

    print(data)

    return {
        "speech" : data,
        "displayText" : data,
        "source" : "wolfram_alpha_bot"
    }


if __name__ == '__main__':
    app.run()