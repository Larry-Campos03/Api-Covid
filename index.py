import requests
import json
import os
from datetime import datetime


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
        Bienvenido a la API coronavirus, por favor elija el año, mes y año para obtener los resultados de dicha fecha.
        Tenga en cuenta que el rango de las fechas es de 2020-01-03 hasta 2021-03-07.
        """
    
    ingresar = True
    while ingresar:
        
        año = input("Ingrese el año: ")
        mes = input("Ingrese el mes: ")
        dia = input("Ingrese el dia: ")
        fecha = año + mes + dia
        print(int(fecha))
        datos = obtenerDatos()
        
        for dato in datos:
            if dato.get("date") == int(fecha):
                fechaObtenida = str(dato.get("date"))
                fecha = datetime.strptime(fechaObtenida, "%Y%m%d")
                positivos = float(dato.get("positive"))
                negativos = float(dato.get("negative"))
                muertos = float(dato.get("death"))
                imprimirDatos(fecha, positivos, negativos, muertos)             
                break
            
        print(" ")
        ingresar = input("¿Quiere buscar otros resultados? (Si/No) ").title() == 'Si'
        os.system("clear")
        
if __name__ == '__main__':
    main()