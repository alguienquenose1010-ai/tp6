import json
Datos = {"Alumnos": []}
 

def leer_json(file_name: str) -> dict:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {"Alumnos": []}
    return datos


def escribir_json(file_name: str, data: list[dict]) -> None:

    with open(file_name,"w") as file:
        json.dump(data, file)


# Funciones
def agregar_alumno(datos):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AA): ")
    tutor = input("Nombre del tutor: ")
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    datos["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado correctamente.")

def modificar_alumno(datos):
    dni = input("Ingrese el DNI del alumno a modificar: ")
    campo = input("Campo a modificar (Nombre, Apellido, Tutor, Faltas, Amonestaciones): ")
    nuevo_valor = input("Nuevo valor: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            alumno[campo] = nuevo_valor
            print("Dato actualizado.")
            return
    print("Alumno no encontrado.")

def registrar_nota(datos):
    dni = input("Ingrese el DNI del alumno: ")
    nota = float(input("Ingrese la nota: "))
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            alumno["Notas"].append(nota)
            print("Nota registrada.")
            return
    print("Alumno no encontrado.")

def expulsar_alumno(datos):
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            datos["Alumnos"].remove(alumno)
            print("Alumno expulsado.")
            return
    print("Alumno no encontrado.")

# Menú

def menu():
    while True:
        print("\n--- MENÚ DE GESTIÓN ESCOLAR ---")
        print("1. Mostrar alumnos")
        print("2. Agregar alumno")
        print("3. Modificar alumno")
        print("4. Registrar nota")
        print("5. Expulsar alumno")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Datos = leer_json("alumnos.json")
            if not Datos["Alumnos"]:
                print("No hay alumnos registrados todavía.")
            else:
                for i, alumno in enumerate(Datos["Alumnos"], start=1):
                    print(f"\nAlumno {i}:")
                    for clave, valor in alumno.items():
                        print(f"{clave}: {valor}")
                print()
        elif opcion == "2":
            agregar_alumno(Datos)
            escribir_json("alumnos.json", Datos["Alumnos"])
        elif opcion == "3":
            modificar_alumno(Datos)
            escribir_json("alumnos.json", Datos["Alumnos"])
        elif opcion == "4":
            registrar_nota(Datos)
            escribir_json("alumnos.json", Datos["Alumnos"])
        elif opcion == "5":
            expulsar_alumno(Datos)
            escribir_json("alumnos.json", Datos["Alumnos"])
        elif opcion == "6":
            escribir_json("alumnos.json", Datos["Alumnos"])
            print("Datos guardados. Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

menu()