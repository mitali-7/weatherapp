# import requests
# from flask import Flask, request, render_template

# app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html', weather=None)

# @app.route('/weather', methods=['POST'])
# def weather():
#     data = request.get_json()
#     city_name = data['cityname']
#     api_key = '21f264c87538384d01870f19ec2e087b'
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
#     response = requests.get(url)

#     data = response.json()

#     if response.status_code == 200:
#         weather_desc = data['weather'][0]['description']
#         temperature = data['main']['temp']
#         humidity = data['main']['humidity']
#         weather_info = {
#             'city': city_name,
#             'weather': weather_desc,
#             'temp': temperature,
#             'humidity': humidity,
#         }
#         return weather_info

# if __name__ == '__main__':
#     app.run(debug=True)

################################################
    
# api_key = '21f264c87538384d01870f19ec2e087b'

# city = input('Enter city name: ')

# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     temp = data['main']['temp']
#     desc = data['weather'][0]['description']
#     rounded = round((temp-273.15), 2)
#     print(f'Temperature: {rounded} C')
#     # print(f'Temperature: {round(temp-273)} K')
#     print(f'Description: {desc}')
# else:
#     print('Error fetching weather data')

#############################################

import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['POST'])
def weather():
    data = request.get_json()
    city_name = data['cityname']
    api_key = '21f264c87538384d01870f19ec2e087b'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        weather_desc = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_info = {
            'city': city_name,
            'weather': weather_desc,
            'temp': temperature,
            'humidity': humidity,
        }
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
