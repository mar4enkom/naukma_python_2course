from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    url = 'http://api.weatherstack.com/current'
    access_key = request.args.get('access_key')
    query = request.args.get('query')
    params = {'access_key': access_key, 'query': query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error fetching weather data', 500

if __name__ == '__main__':
    app.run(debug=True)
