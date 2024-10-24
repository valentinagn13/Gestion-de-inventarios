# main.py
import tkinter as tk
from panel_izquierdo import PanelIzquierdo
from Arbol import ArbolAVL
from panel_derecho import PanelDerecho
from seccion4 import Seccion4  # Asegúrate de importar tu clase Seccion4

class Aplicacion:
    def __init__(self, root):
        root.title("Gestión de inventarios")
        root.geometry("800x400")  # Cambié el tamaño inicial a 800x400

        # Establecer el tamaño mínimo de la ventana
        root.minsize(800, 400)  # Esto previene que la ventana se reduzca a menos de 800x400 píxeles

        # Crear un frame izquierdo con borde y color
        frame_izquierdo = tk.Frame(root, width=200, height=200, bg="lightblue", relief="sunken", borderwidth=2)
        frame_izquierdo.pack(side="left", fill="both", expand=True)

        # Crear un frame derecho con borde y color
        frame_derecho = tk.Frame(root, width=200, height=200, bg="#f0f0f0", relief="sunken", borderwidth=2)
        frame_derecho.pack(side="right", fill="both", expand=True)

        # Crear el árbol AVL
        self.arbol = ArbolAVL()  # Asegúrate de que esta línea carga correctamente desde inventario.json

        # Instanciar Seccion4
        self.seccion4 = Seccion4(frame_izquierdo, self.arbol, None)  # Cambia None después

        # Instanciar el panel derecho y pasar la referencia a Seccion4
        self.panel_derecho = PanelDerecho(frame_derecho, self.arbol, self.seccion4)

        # Instanciar el panel izquierdo
        self.panel_izquierdo = PanelIzquierdo(frame_izquierdo, self.arbol, self.panel_derecho)



if __name__ == "__main__":
    # Ejecutar la aplicación Tkinter
    root = tk.Tk()
    app = Aplicacion(root)

    root.mainloop()  # Bucle principal de Tkinter
