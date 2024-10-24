import tkinter as tk
import json

class PanelDerecho:
    def __init__(self, master, arbol, seccion4):
        self.master = master
        self.titulo = tk.Label(self.master, text="ÁRBOL AVL DEL INVENTARIO", font=("Arial", 13, "bold"), bg="#f0f0f0")
        self.titulo.pack(pady=(20, 10))

        self.arbol = arbol  # Referencia al árbol AVL
        self.seccion4 = seccion4  # Referencia a la sección de eliminación

        self.canvas = tk.Canvas(master, bg="lightgray", width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Cargar el inventario desde un archivo JSON al iniciar
        self.cargar_inventario_json("inventario.json")  
        # Dibuja el árbol inicialmente
        self.dibujar_arbol()

    def dibujar_arbol(self):
        # Limpiar el canvas
        self.canvas.delete("all")

        # Llamar a la función recursiva para dibujar el árbol
        if self.arbol.raiz:
            self._dibujar_nodo(self.arbol.raiz, 350, 30, 150)  # Posición inicial

    def _dibujar_nodo(self, nodo, x, y, offset):
        if not nodo:
            return
        
        # Verificar si la cantidad es cero y cambiar el color del nodo
        color_nodo = "red" if nodo.cantidad == 0 else "lightgreen"

        # Dibujar el nodo actual (un círculo con su ID)
        oval = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color_nodo, outline="green", width=2)
        self.canvas.create_text(x, y, text=str(nodo.id_producto))

        # Etiqueta para el nodo que contendrá su ID
        self.canvas.tag_bind(oval, "<Button-1>", lambda event, id_producto=nodo.id_producto: self.on_node_click(id_producto))
        self.canvas.tag_bind(oval, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(oval, "<Leave>", lambda event: self.canvas.config(cursor=""))

        vertical_offset = 70  # Distancia vertical entre los nodos

        # Dibujar los nodos hijos y las líneas que conectan los nodos
        if nodo.izquierda:
            # Dibujar línea hacia el hijo izquierdo
            self.canvas.create_line(x, y + 20, x - offset, y + vertical_offset)
            # Dibujar el hijo izquierdo
            self._dibujar_nodo(nodo.izquierda, x - offset, y + vertical_offset, offset // 2)

        if nodo.derecha:
            # Dibujar línea hacia el hijo derecho
            self.canvas.create_line(x, y + 20, x + offset, y + vertical_offset)
            # Dibujar el hijo derecho
            self._dibujar_nodo(nodo.derecha, x + offset, y + vertical_offset, offset // 2)

    def on_node_click(self, id_producto):
        # Manejar el clic en el nodo
        print(f"Hiciste clic en el nodo con ID: {id_producto}")
        # Establecer el ID del producto en el campo de entrada de la sección de eliminación
        self.seccion4.actualizar_id_producto(id_producto)  # Actualizar el campo de entrada en Seccion4

    def cargar_inventario_json(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos = json.load(f)
                productos_insertados = set()  # Para evitar duplicaciones

                # Recorrer la lista de productos y añadirlos al árbol AVL
                for producto in productos:
                    id_producto = producto['id']
                    nombre = producto['nombre']
                    cantidad = producto['cantidad']
                    precio = producto['precio']
                    categoria = producto['categoria']

                    # Verificar si el ID ya ha sido insertado
                    if id_producto not in productos_insertados and not self.arbol.buscar(id_producto):
                        # Insertar el producto en el árbol AVL
                        self.arbol.insertar(id_producto, nombre, cantidad, precio, categoria)
                        productos_insertados.add(id_producto)  # Marcar el ID como insertado
                        print(f"Agregando producto: {id_producto} - {nombre}")
                    else:
                        print(f"Producto con ID {id_producto} ya existe, no se volverá a insertar.")

        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario en panel derecho: {e}")
