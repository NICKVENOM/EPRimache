# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:09:04 2024

@author: Alumno
"""

def cargar_datos():
    # Carga los logins y claves desde archivos
    with open("login.txt", "r") as f:
        logins = f.read().splitlines()  # Cargar todos los logins en una lista

    with open("clave.txt", "r") as f:
        claves = f.read().splitlines()  # Cargar todas las claves en una lista

    return logins, claves

def validar_login(logins, claves):
    intentos = 0
    while intentos < 2:  # Limitar a 2 intentos
        login_ingresado = input("Ingresa tu login: ")
        clave_ingresada = input("Ingresa tu clave: ")

        # Validar si el login y clave coinciden
        if login_ingresado in logins and clave_ingresada in claves:
            indice = logins.index(login_ingresado)
            if claves[indice] == clave_ingresada:
                return True

        print("Login o clave incorrectos. Intenta de nuevo.")
        intentos += 1

    print("Demasiados intentos fallidos. El programa se cerrará.")
    return False

def mostrar_menu():
    print("\nDatos Persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

def main():
    logins, claves = cargar_datos()  # Cargar logins y claves desde archivos

    if validar_login(logins, claves):  # Validar las credenciales
        mostrar_menu()  # Mostrar el menú si las credenciales son correctas

if __name__ == "__main__":
    main()
