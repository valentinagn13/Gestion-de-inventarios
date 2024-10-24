# guardarInventario.py
import json

def guardar_en_json(id_producto, nombre, cantidad, precio, categoria):
    # Cargar el inventario existente desde el archivo JSON
    try:
        with open('inventario.json', 'r') as f:
            inventario = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        inventario = []

    for producto in inventario:
        if producto['id'] == id_producto:
            return  # Si ya existe, no lo volvemos a agregar

    # Crear un nuevo producto
    nuevo_producto = {
        "id": id_producto,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria
    }

    # Agregar el nuevo producto a la lista de inventario
    inventario.append(nuevo_producto)

    # Guardar la lista actualizada en el archivo JSON
    with open('inventario.json', 'w') as f:
        json.dump(inventario, f, indent=4)
    print(f"Producto con ID {id_producto} agregado al inventario.")
    
    #PARA ELIMINAR EL PRODUCTO
def eliminar_de_json(id_producto):
    try:
        with open('inventario.json', 'r') as f:
            inventario = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        inventario = []

    # Eliminar el producto con el ID especificado
    inventario = [producto for producto in inventario if producto['id'] != id_producto]

    # Guardar el inventario actualizado en el archivo JSON
    with open('inventario.json', 'w') as f:
        json.dump(inventario, f, indent=4)

   