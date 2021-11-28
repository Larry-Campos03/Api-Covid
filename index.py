import requests
import json


def obtenerDatos():
    try:    
        url = 'https://api.covidtracking.com/v1/us/daily.json'
        contenido = requests.get(url)
        
        if contenido.status_code == 200:
            convertir = contenido.json() # la variable converir se convierte en un diccionario con la funion .json
                 
    except Exception as e:
        print(f"Este es el error encontrado: {e}")
    
    finally:
        return convertir

def imprimirDatos(dato1, dato2, dato3, dato4):
    total = f"""
    fecha: {dato1}
    casos positivos: {dato2}
    casos negativos: {dato3}
    muertos: {dato4}
    """
    print(total)


def main():
    
    menu = """
        Bienvenido a la API coronavirus, porfavor elija la fecha para obtener los resultados de dicha fecha.
        ingrese la fecha en el formato '20210411' año, mes y dia: """
    fecha = int(input(menu))
    
    datos = obtenerDatos()
    
    for dato in datos:
        if dato.get("date") == fecha:
            fecha = dato.get("date")
            positivos = dato.get("positive")
            negativos = dato.get("negative")
            muertos = dato.get("death")
            imprimirDatos(fecha, positivos, negativos, muertos)
            break
    


if __name__ == '__main__':
    main()