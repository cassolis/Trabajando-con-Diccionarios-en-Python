# Crear un diccionario llamado 'informacion_personal'
informacion_personal = {"nombre": "Juan Pérez", "edad": 30, "ciudad": "Barcelona",
                        "profesion": "Desarrollador de Software"}

# Acceder al valor asociado con la clave 'ciudad' y modificarlo

# Agregar una nueva clave-valor para la profesión

# Verificar si la clave 'telefono' existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave 'edad'
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
