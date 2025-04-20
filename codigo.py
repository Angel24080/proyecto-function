def crear_mensajes(nombre, apellido, edad, anio_nacimiento):
    # Crear el primer mensaje con el nombre y apellido
    mensaje1 = f"Hola {nombre} {apellido}. ¿Cómo estás?"
    
    # Crear el segundo mensaje con los datos de la edad y año de nacimiento
    mensaje2 = f"Ya veo que tienes {edad} años porque naciste en {anio_nacimiento}."
    
    # Imprimir ambos mensajes
    print(mensaje1)
    print(mensaje2)

# Invocar la función con tus datos
crear_mensajes("Lautaro", "Wild", 16, 2001)
