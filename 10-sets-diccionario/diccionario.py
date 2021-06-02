"""

Diccionario es un tipo de dato que almacena un conjundto de datos que almacena una valor

"""

persona ={
    "nombre": "Jesus",
    "apellidos": "anglas",
    "web": "jesus@gmail.com"
}

# print(persona["web"])

# Lista con diccionarios

contactos =[
    {
        "nombre": "Jesus",
        "email": "jesus@gmail.com",
    },
    {
        "nombre": "Marcos",
        "email": "marcos@gmail.com",
    },
    {
        "nombre": "Juan",
        "email": "juan@gmail.com",
    }
]

print(contactos[0]["nombre"])


print("\nListado de contactos")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("----------------------------------------")