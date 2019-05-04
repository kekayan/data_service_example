from flask import Flask,json,jsonify
import requests

app = Flask(__name__)

@app.route("/<options>")
def getdata(options):
    url="https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json"
    if options=="codes":
        url="https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json"
        response = requests.get(url)
        data = response.text
        return data
    if options =="states":
        url="https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json"
        response = requests.get(url)
        result = response.text
        data={}
        for record in json.loads(result):
            data[record['name'].lower()]=record['abbreviation']
            print(record)
        return jsonify(data)
    return "Error"
@app.route("/")
def welcome():
    return "welcome to dataservice"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=80)