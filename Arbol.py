from decimal import Decimal  # Importar Decimal para manejar precios con precisión
from guardarInventario import eliminar_de_json
from guardarInventario import guardar_en_json

class Nodo:
    def __init__(self, id_producto, nombre, cantidad, precio, categoria):
        self.id_producto = id_producto  # Clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = Decimal(precio)  # Usar Decimal para el precio
        self.categoria = categoria
        self.izquierda = None  # Nodo hijo izquierdo
        self.derecha = None  # Nodo hijo derecho
        self.altura = 1  # Altura del nodo

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        
    # Búsqueda de un producto en el árbol AVL
    def buscar(self, id_producto):
        # Método para buscar un producto por su ID en el árbol AVL
        nodo = self._buscar_nodo(self.raiz, id_producto)
        if nodo is not None:
            # Si la cantidad es 0, devolver 'fuera de stock' en lugar de 0
            cantidad = "fuera de stock" if nodo.cantidad == 0 else nodo.cantidad
            
            return {
                'nombre': nodo.nombre,
                'cantidad': cantidad,  # Aquí cambiamos el valor
                'precio': str(nodo.precio),  # Convertir Decimal a string para la salida
                'categoria': nodo.categoria
            }
        return None

    def _buscar_nodo(self, nodo, id_producto):
        # Búsqueda binaria en el árbol AVL
        if nodo is None:
            return None
        if id_producto == nodo.id_producto:  # Cambié de nodo.id a nodo.id_producto
            return nodo
        elif id_producto < nodo.id_producto:
            return self._buscar_nodo(nodo.izquierda, id_producto)
        else:
            return self._buscar_nodo(nodo.derecha, id_producto)

    def buscar_por_rango(self, precio_min, precio_max):
        resultados = []
        # Convertir a Decimal para la búsqueda
        precio_min = Decimal(precio_min)
        precio_max = Decimal(precio_max)
        self._buscar_por_rango(self.raiz, precio_min, precio_max, resultados)
        return resultados

    def _buscar_por_rango(self, nodo, precio_min, precio_max, resultados):
        if nodo is not None:
            if nodo.precio >= precio_min:
                self._buscar_por_rango(nodo.izquierda, precio_min, precio_max, resultados)
            if precio_min <= nodo.precio <= precio_max:
                cantidad = "fuera de stock" if nodo.cantidad == 0 else nodo.cantidad
                resultados.append({
                    'id': nodo.id_producto,
                    'nombre': nodo.nombre,
                    'cantidad': cantidad,
                    'precio':   (nodo.precio),  # Convertir Decimal a string para la salida
                    'categoria': nodo.categoria
                })
            if nodo.precio <= precio_max:
                self._buscar_por_rango(nodo.derecha, precio_min, precio_max, resultados)
                
    def buscar_por_categoria(self, categoria):
        resultados = []
        self._buscar_por_categoria(self.raiz, categoria, resultados)
        return resultados

    def _buscar_por_categoria(self, nodo, categoria, resultados):
        if nodo is not None:
            # Verificar si la categoría del nodo coincide
            if nodo.categoria == categoria:
                cantidad = "fuera de stock" if nodo.cantidad == 0 else nodo.cantidad
                resultados.append({
                    'id': nodo.id_producto,  # Cambié de nodo.id a nodo.id_producto
                    'nombre': nodo.nombre,
                    'cantidad': cantidad,
                    'precio': str(nodo.precio),  # Convertir Decimal a string para la salida
                    'categoria': nodo.categoria
                })
            # Búsqueda recursiva en el subárbol izquierdo y derecho
            self._buscar_por_categoria(nodo.izquierda, categoria, resultados)
            self._buscar_por_categoria(nodo.derecha, categoria, resultados)

    # Altura y balance del árbol
    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha) if nodo else 0

    # Rotaciones para balancear el árbol AVL
    def rotacion_derecha(self, y):
        print(f"Rotación a la derecha en el nodo con ID {y.id_producto}")
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        return x

    def rotacion_izquierda(self, x):
        print(f"Rotación a la izquierda en el nodo con ID {x.id_producto}")
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        return y
    # Insertar un nuevo nodo en el árbol AVL
    def insertar(self, id_producto, nombre, cantidad, precio, categoria):
        self.raiz = self._insertar_recursivo(self.raiz, id_producto, nombre, cantidad, precio, categoria)
        guardar_en_json(id_producto, nombre, cantidad, str(Decimal(precio)), categoria)  # Guardar en JSON

    def _insertar_recursivo(self, nodo, id_producto, nombre, cantidad, precio, categoria):
        if not nodo:
            return Nodo(id_producto, nombre, cantidad, precio, categoria)

        if id_producto < nodo.id_producto:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, id_producto, nombre, cantidad, precio, categoria)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, id_producto, nombre, cantidad, precio, categoria)

        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

        balance = self.balance(nodo)

        # Rotaciones para mantener el balance
        if balance > 1:
            if id_producto < nodo.izquierda.id_producto:
                return self.rotacion_derecha(nodo)
            else:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)

        if balance < -1:
            if id_producto > nodo.derecha.id_producto:
                return self.rotacion_izquierda(nodo)
            else:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

        return nodo

    # Eliminar un producto del árbol AVL
    def eliminar(self, id_producto):
        self.raiz, eliminado = self._eliminar_nodo(self.raiz, id_producto)
        if eliminado:
            eliminar_de_json(id_producto)  # Eliminar del JSON
        return eliminado

    def _eliminar_nodo(self, nodo, id_producto):
        if nodo is None:
            return nodo, False

        if id_producto < nodo.id_producto:
            nodo.izquierda, eliminado = self._eliminar_nodo(nodo.izquierda, id_producto)
        elif id_producto > nodo.id_producto:
            nodo.derecha, eliminado = self._eliminar_nodo(nodo.derecha, id_producto)
        else:
            eliminado = True
            # Caso 1: Nodo sin hijos o con un solo hijo
            if nodo.izquierda is None:
                return nodo.derecha, eliminado
            elif nodo.derecha is None:
                return nodo.izquierda, eliminado

            # Caso 2: Nodo con dos hijos, encontrar el sucesor
            sucesor = self._nodo_mas_pequeno(nodo.derecha)
            nodo.id_producto = sucesor.id_producto
            nodo.nombre = sucesor.nombre
            nodo.cantidad = sucesor.cantidad
            nodo.precio = sucesor.precio
            nodo.categoria = sucesor.categoria
            nodo.derecha, _ = self._eliminar_nodo(nodo.derecha, sucesor.id_producto)

        # Actualizar la altura del nodo
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

        # Balancear el árbol AVL
        balance = self.balance(nodo)

        # Rotaciones para mantener el balance
        if balance > 1:
            if self.balance(nodo.izquierda) >= 0:
                return self.rotacion_derecha(nodo), eliminado
            else:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo), eliminado

        if balance < -1:
            if self.balance(nodo.derecha) <= 0:
                return self.rotacion_izquierda(nodo), eliminado
            else:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo), eliminado

        return nodo, eliminado

    def _nodo_mas_pequeno(self, nodo):
        # Obtener el nodo más pequeño en el subárbol
        if nodo is None or nodo.izquierda is None:
            return nodo
        return self._nodo_mas_pequeno(nodo.izquierda)

