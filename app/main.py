from flask import Flask
import requests

app = Flask(__name__)

@app.route("/<options>")
def getdata(options):
    if options=="codes":
        url="https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json"
    elif options =="states":
        url="https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json"
    response = requests.get(url)
    data = response.text
    return data

@app.route("/")
def welcome():
    return "welcome to dataservice"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=80)