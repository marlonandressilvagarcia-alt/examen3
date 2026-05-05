import json
import os

ARCHIVO = "servicios.json"


def cargar_servicios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []


def guardar_servicios(servicios):
    with open(ARCHIVO, "w") as f:
        json.dump(servicios, f, indent=4)


# =========================
# REGISTRAR SERVICIO
# =========================
def registrar():
    print("=== Registro de Servicios ===")

    nombre = input("Nombre del paquete fotográfico: ")

    try:
        precio = float(input("Precio del servicio: "))
    except ValueError:
        print("Error: El precio debe ser un número.\n")
        return

    tipo_evento = input("Tipo de evento (boda, retrato, producto, etc.): ")

    try:
        duracion = float(input("Duración estimada (en horas): "))
    except ValueError:
        print("Error: La duración debe ser un número.\n")
        return

    servicios = cargar_servicios()

    nuevo_servicio = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo_evento,
        "duracion": duracion
    }

    servicios.append(nuevo_servicio)

    guardar_servicios(servicios)

    print("✔ Servicio registrado correctamente.\n")


# =========================
# EDITAR SERVICIO
# =========================
def editar_servicio():
    servicios = cargar_servicios()

    if not servicios:
        print("No hay servicios registrados.\n")
        return

    print("=== Lista de Servicios ===")
    for i, s in enumerate(servicios):
        print(f"{i + 1}. {s['nombre']} - {s['tipo_evento']} - ${s['precio']}")

    try:
        opcion = int(input("Seleccione el número del servicio a editar: ")) - 1
        if opcion < 0 or opcion >= len(servicios):
            print("Opción inválida.\n")
            return
    except ValueError:
        print("Debe ingresar un número.\n")
        return

    servicio = servicios[opcion]

    print("\n--- Editando servicio ---")

    nuevo_nombre = input(f"Nombre ({servicio['nombre']}): ") or servicio['nombre']
    
    try:
        nuevo_precio = input(f"Precio ({servicio['precio']}): ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else servicio['precio']
    except ValueError:
        print("Precio inválido.\n")
        return