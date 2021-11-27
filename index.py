import requests
import json

def main():
    try:    
        url = 'https://api.covidtracking.com/v1/us/20200501.json'
        contenido = requests.get(url)
        
        if contenido.status_code == 200:
            convertir = contenido.json() # la variable converir se convierte en un diccionario con la funion .json
                 
    except Exception as e:
        print(f"Este es el error encontrado: {e}")
        

if __name__ == '__main__':
    main()