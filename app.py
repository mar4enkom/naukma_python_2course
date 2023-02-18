from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    url = 'http://api.weatherstack.com/current'
    params = {
        'access_key': '2677f37ac9054af75d1f9589df30252b',
        'query': 'New York'
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()