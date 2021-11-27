import requests
import json

def main():
    #url = 'https://api.covidtracking.com/v1/us/daily.json'
    url = 'https://api.covidtracking.com/v1/us/20200501.json'
    contenido = requests.get(url)
    
    if contenido.status_code == 200:
        #convertir = contenido.json() # la variable converir se convierte en un diccionario con la funion .json
        convertir = contenido.text
        print(convertir)
        #print(convertir[0].get('date', 'No se encontro ese dato'))
        
        

if __name__ == '__main__':
    main()