class Producto:
    __slots__ = ['nombre', 'precio', 'cantidad']  # Ahorra espacio

    def __init__(self, nombre: str, precio: float, cantidad: int):
        """
        Constructor de la clase. Valida que los argumentos sean válidos y, de ser así, genera un producto.

        :param nombre: String con el nombre del producto a añadir.
        :param precio: Precio del producto a añadir.
        :param cantidad: Cantidad del producto a añadir.
        """
        # Validar datos de entrada
        self.validar_nombre(nombre)
        self.validar_precio(precio)
        self.validar_cantidad(cantidad)

        # Declarar e inicializar atributos de objeto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizar_precio(self, nuevo_precio: float) -> None:
        """Valida y actualiza el precio del producto."""
        self.validar_precio(nuevo_precio)
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        """Valida y actualiza la cantidad del producto."""
        self.validar_cantidad(nueva_cantidad)
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        """Calcula el valor total de las unidades existentes del producto."""
        return self.precio * self.cantidad
    
    def __str__(self) -> str:
        """Convierte el objeto en un string que describe su contenido/estado."""
        return f'{self.nombre}: cuesta {self.precio:.2f} y hay {self.cantidad}'
    
    # Métodos estáticos para validar los atributos
    @staticmethod
    def validar_nombre(nombre: str) -> None:
        """Valida que el nombre sea un string no vacío. De no ser así, lanza un TypeError."""
        if not isinstance(nombre, str) or nombre == '':
            raise TypeError('Los nombres de los productos deben ser strings no vacías.')
        
    @staticmethod
    def validar_precio(precio: float) -> None:
        """Valida que el precio sea un número mayor o igual a 0. De no ser así, lanza un TypeError."""
        valid_type = isinstance(precio, int) or isinstance(precio, float)
        if not valid_type or precio < 0:
            raise TypeError('Los precios de los productos deben ser números mayores o iguales a 0.')
        
    @staticmethod
    def validar_cantidad(cantidad: int) -> None:
        """Valida que la cantidad sea un entero mayor o igual a 0. De no ser así, lanza un TypeError."""
        if not isinstance(cantidad, int) or cantidad < 0:
            raise TypeError('Las cantidades de los productos deben ser enteros mayores o iguales a 0.')
        
class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, nombre: str, precio: float, cantidad: int) -> None:
        """
        Crea un producto con los argumentos proporcionados y lo añade a la lista de productos.

        :param nombre: String con el nombre del producto a añadir.
        :param precio: Precio del producto a añadir.
        :param cantidad: Cantidad del producto a añadir.
        """
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)

    def actualizar_producto(self, nombre: str, precio: float, cantidad: int) -> None:
        """
        Actualiza un producto de la lista con los argumentos proporcionados.

        :param nombre: String con el nombre del producto a actualizar.
        :param precio: Precio del producto a actualizar.
        :param cantidad: Cantidad del producto a actualizar.
        """

        idx, _ = self.buscar_producto(nombre)
        self.productos[idx].actualizar_precio(precio)
        self.productos[idx].actualizar_cantidad(cantidad)

    def buscar_producto(self, nombre: str) -> tuple:
        """
        Busca en la lista de productos el primer producto que tenga el mismo nombre. Si se encuentra, se devuelve junto a su índice.
        Si no, se muestran los productos disponibles y se genera un TypeError.

        :param nombre: String con el nombre del producto a buscar.
        :return: El índice del producto encontrado en la lista y el producto en formato string.
        """
        resultado = None
        for idx, producto in enumerate(self.productos):
            if nombre == producto.nombre:
                resultado = str(producto)
                break
        
        # Si no se encontró el producto, se muestra la lista de productos y se genera una excepción
        if resultado is None:
            self.listar_productos()
            raise TypeError(f'No se pudo encontrar el producto {nombre}.')

        return idx, resultado
            
    def calcular_valor_inventario(self) -> float:
        """
        Suma el valor total de todos los productos del inventario y devuelve el resultado.
        """
        valor = 0
        for producto in self.productos:
            valor += producto.calcular_valor_total()

        return valor
    
    def listar_productos(self) -> None:
        """
        Imprime una lista de todos los productos en el inventario.
        """
        print('El inventario contiene los siguientes productos:')
        for producto in self.productos:
            print(f'\t- {str(producto)}')

def mostrar_menu() -> tuple:
    """
    Define la lista de opciones, las muestra y deuvelve el mínimo y el máximo del rango de valores válidos según el número de opciones existente.
    
    :return: El mínimo y el máximo del rango de valores válidos según el número de opciones existente.
    """
    opciones = ['Agregar producto', 'Buscar producto', 'Calcular valor total', 'Listar todos los productos', 'Actualizar producto', 'Finalizar programa']

    print('\nElija una de las siguientes opciones:')
    for op_idx, opcion in enumerate(opciones):
        print(f'\t{op_idx+1}. {opcion}')

    return 1, len(opciones)

def solicitar_accion() -> int:
    """
    Muestra el menu con todas las opciones disponibles. Después, captura y valida la opción del usuario.

    :return: Opción de la tarea a realizar escogida por el usuario.
    """
    min_op, max_op = mostrar_menu()

    # Capturar y validar entrada
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input('Su elección: '))  # Lanzará ValueError si la entrada NO es un número entero
            if isinstance(opcion, int) and opcion >= min_op and opcion <= max_op:
                opcion_valida = True
            else:
                raise ValueError
        except ValueError:
                print('Por favor, elija uno de los números enteros mostrados en el menu.')
    
    return opcion

def menu_principal() -> None:
    """
    Crea un inventario, propone opciones al usuario y actúa en consecuencia.
    """
    inventario = Inventario()
    finalizar = False

    while not finalizar:
        opcion = solicitar_accion()
        try:
            match opcion:
                case 1:  # Agregar producto
                    nombre = input('Introduzca el nombre del producto (string no vacía): ')
                    precio = float(input('Introduzca el precio del producto (número igual o superior a 0): '))
                    cantidad = int(input('Introduzca la cantidad del producto (entero igual o superior a 0): '))
                    inventario.agregar_producto(nombre, precio, cantidad)
                case 2:  # Buscar producto
                    nombre = input('Introduzca el nombre del producto (string no vacía): ')
                    _, producto = inventario.buscar_producto(nombre)
                    print(f'Resultado de la búsqueda: {producto}')
                case 3:  # Calcular valor total
                    valor = inventario.calcular_valor_inventario()
                    print(f'Valor total del inventario: {valor}')
                case 4:  # Listar todos los productos
                    inventario.listar_productos()
                case 5:  # Actualizar producto
                    nombre = input('Introduzca el nombre del producto (string no vacía): ')
                    precio = float(input('Introduzca el precio del producto (número igual o superior a 0): '))
                    cantidad = int(input('Introduzca la cantidad del producto (entero igual o superior a 0): '))
                    inventario.actualizar_producto(nombre, precio, cantidad)
                case 6:  # Finalizar programa
                    finalizar = True
        except TypeError as err:
            # Imprimir errores (e.g., mal input de algún argumento para añadir productos)
            print(err.args)


if __name__ == '__main__':
    menu_principal()
