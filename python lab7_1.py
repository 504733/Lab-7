import requests
import json
# 你的配置（南京+API Key）
city_name = 'Nanjing'
key = ''


try:

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric'
    response = requests.get(url)
    response.raise_for_status()  # 捕获HTTP错误


    result = json.loads(response.text)


    print(f"Город: {result['name']}")
    print(f"Погода: {result['weather'][0]['description']}")
    print(f"Температура: {result['main']['temp']} °C")
    print(f"Давление: {result['main']['pressure']} hPa")
    print(f"Скорость ветра: {result['wind']['speed']} м/с")

except Exception as e:
    print(f"Ошибка: {e}")