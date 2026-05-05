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