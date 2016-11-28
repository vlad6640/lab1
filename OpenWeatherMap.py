import pyowm
from datetime import datetime
print('OpenWeatherMap')
owm = pyowm.OWM('b72e8ad9d5363b07ad1df7206c0887a1')
observation = owm.weather_at_place('Rostov-on-Don,ru')
wether = observation.get_weather()
location = observation.get_location()


translate = {'Rostov-na-Donu': 'Ростов-на-Дону','RU': 'Россия'}


def cloudiness():
    if 0 <= wether.get_clouds() <= 10:
        return 'ясная'
    if 10 < wether.get_clouds() <=30:
        return 'немного облачная'
    if 30 < wether.get_clouds() <= 70:
        return 'пасмурная'
    if 70 < wether.get_clouds() <= 100:
        return 'мрачная'

def temperature(string): #функция выводит результат string - погода днём и ночью
    f_observation = owm.daily_forecast('Rostov-on-Don, RU')
    f_weather = f_observation.get_weather_at(datetime.now())
    return str(round(f_weather.get_temperature('celsius')[string]))

def direction_wind():
    if 337.5 < wether.get_wind()['deg'] <= 22.5:
        return 'северный'
    if 157.5 < wether.get_wind()['deg'] <= 202.5:
        return 'южный'
    if 67.5 < wether.get_wind()['deg'] <= 112.5:
        return 'восточный'
    if 247.5 < wether.get_wind()['deg'] <= 292.5:
        return 'западный'
    if 22.5 < wether.get_wind()['deg'] <= 67.5:
        return 'северо-восточный'
    if 112.5 < wether.get_wind()['deg'] <= 157.5:
        return 'юго-восточный'
    if 202.5 < wether.get_wind()['deg'] <= 247.5:
        return 'юго-западный'
    if 292.5 < wether.get_wind()['deg'] <= 337.5:
        return 'северо-западный'

def status(x): #интерпретация значений переменных
    return {
        '10d' or '10n': ', дождь',
        '09d' or '09n': ', ливень',
        '11d' or '11n': ', гроза',
        '13d' or '13n': ', снег',
        '50d' or '50n': ', туман'
    }.get(x, '')


print('Погода в городе ' + translate[location.get_name()] + '('
      +translate[location.get_country()] + ')' +'на сегодня '
      + str(datetime.now().strftime("%H:%M")) +' ' + cloudiness()
      + ', \nоблачность составляет ' + str(wether.get_clouds()) + '%, давление '
      + str(round(wether.get_pressure()['press']*0.750062)) + ' мм рт. ст.,\nтемпература '
      + str(round(wether.get_temperature('celsius')['temp'])) + ' градусов Цельция' + ', днём '
      + temperature('day') + ', ночью ' + temperature('night') + ' ветер ' + direction_wind() +  ', '
      + str(round(wether.get_wind()['speed'])) + ' м/c ' + status(wether.get_status()) + '.')
