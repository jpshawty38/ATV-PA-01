import requests
from pprint import pprint

API_Key = 'cb771e45ac79a4e8e2205c0ce66ff633'

cidade = input ("Digite uma cidade ")

link = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + cidade + "&lang=pt_br"


requisisao = requests.get(link)
requisisao_dic = requisisao.json()
descricao = requisisao_dic['weather'][0]['description']
temperatura = requisisao_dic['main']['temp'] - 273.15
print (descricao, {temperatura})
