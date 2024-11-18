import requests
from pprint import pprint

# Chave da API do OpenWeatherMap
API_Key = 'cb771e45ac79a4e8e2205c0ce66ff633'

# Captura de entrada de dados
try:
    cidade = input("Digite uma cidade: ").strip()
    if not cidade:
        raise ValueError("O nome da cidade não pode estar vazio!")
except Exception as e:
    print(f"Erro na entrada: {e}")
    cidade = "São Paulo"  # Valor padrão para evitar erros

# link da API
link = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={cidade}&lang=pt_br"

# Requisição à API
try:
    requisicao = requests.get(link)
    requisicao.raise_for_status()  # Levanta um erro se o código HTTP não for 200
    requisicao_dic = requisicao.json()

    # informações relevantes
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15  # Conversão de Kelvin para Celsius

    # informações
    print(f"Descrição do tempo: {descricao.capitalize()}")
    print(f"Temperatura: {temperatura:.2f}°C")

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a API:", e)
except KeyError as e:
    print("Verifique o nome da cidade ou a chave da API.")
    print(f"Detalhes: {e}")
except Exception as e:
    print("Ocorreu um erro inesperado:", e)

input("Pressione Enter para sair...")