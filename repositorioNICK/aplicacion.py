# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:09:04 2024

@author: Alumno
"""


def cargar_datos():
    """Carga los logins y claves desde archivos."""
    with open("login.txt", "r") as f:
        logins = f.read().splitlines()  

    with open("clave.txt", "r") as f:
        claves = f.read().splitlines()  

    return logins, claves

def validar_login(logins, claves):
    """Valida el login y la clave ingresados por el usuario."""
    intentos = 0
    while intentos < 2:  
        login_ingresado = input("Ingresa tu login: ")
        clave_ingresada = input("Ingresa tu clave: ")

       
        if login_ingresado in logins and clave_ingresada in claves:
            indice = logins.index(login_ingresado)
            if claves[indice] == clave_ingresada:
                return True

        print("Login o clave incorrectos. Intenta de nuevo.")
        intentos += 1

    print("Demasiados intentos fallidos. El programa se cerrará.")
    return False

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nDatos Persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

def listar_personas():
    """Lista las personas registradas en los archivos."""
    print("\nListado de Personas:")
    print("DNI\t\tNombre\t\tApellido")  
   
    try:
        with open("dni.txt", "r") as dni_file, open("nombre.txt", "r") as nombre_file, open("apellido.txt", "r") as apellido_file:
            dni_list = dni_file.read().splitlines()
            nombre_list = nombre_file.read().splitlines()
            apellido_list = apellido_file.read().splitlines()

            for dni, nombre, apellido in zip(dni_list, nombre_list, apellido_list):
                
                print(f"{dni}\t{nombre.ljust(20)}\t{apellido.ljust(20)}")  
    except FileNotFoundError:
        print("Error: Uno o más archivos no se encontraron.")

def agregar_personas():
    """Agrega una nueva persona a los archivos."""
    dni = input("Ingrese el DNI de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")

    # Validación simple para evitar datos vacíos
    if not dni or not nombre or not apellido:
        print("Error: Todos los campos deben ser llenados.")
        return

    # Agregar los datos a los archivos
    with open("dni.txt", "a") as dni_file, open("nombre.txt", "a") as nombre_file, open("apellido.txt", "a") as apellido_file:
        dni_file.write(dni + "\n")
        nombre_file.write(nombre + "\n")
        apellido_file.write(apellido + "\n")

    print("Persona agregada exitosamente.")

def main():
    """Función principal del programa."""
    logins, claves = cargar_datos()  # Cargar logins y claves desde archivos

    if validar_login(logins, claves):  # Validar las credenciales
        while True:
            mostrar_menu()  # Mostrar el menú
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                listar_personas()  # Listar personas
            elif opcion == "2":
                agregar_personas()  # Agregar personas
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
