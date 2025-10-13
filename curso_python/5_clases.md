# Clases y Objetos

## 1. Introducción a la POO
La POO (programación orientada a objetos) se sustenta en cuatro pilares conceptuales que definen su esencia:
- **Abstracción**: Identificar las características esenciales de un objeto e ignorar lo demás. Para un cierto programa, un automóvil puede estar definido por su marca, modelo y velocidad pero su peso, color, o cantidad de tornillos utilizados pueden ser irrelevantes.
- **Encapsulamiento**: Ocultar detalles internos para simplificar el uso de las clases y proteger la integridad de los datos. Es mejor utilizar métodos para modificar y consultar las variables de las clases desde el exterior.
- **Herencia**: Permite a una clase (*subclase*) adquirir propiedades y comportamientos de otra (*superclase*). Esto permite reutilizar código y crear jerarquías conceptuales.
- **Polimorfismo**: Cuando dos objetos de clases distintas responden con el mismo comportamiento a un mismo método. Si tenemos clases para varios animales, todas las clases pueden tener un método que se llame y se use de la misma manera para obtener el ruido que hacen, su peso, su color, etc.

## 2. Variables y Métodos de Clase vs de Instancia
En una clase, las variables pueden ser de instancia, si pertenecen a las instancias de los objetos, o de clase, si son propios a la clase y se comparten entre todas las instancias de la misma. Normalmente, las **variables de clase** se usan sólo para datos constantes o, a veces, para contadores o temporizadores. Es recomendable modificarlos utilizando métodos de clase especificos, los cuales se implementan utilizando el decorador `@classmethod`. Estos métodos reciben como parámetro a la clase (por convención, llamado `cls`), en lugar de la referencia a la instancia `self`.

Para acceder y modificar las variables de clase, se debe utilizar `[IdentificadorClase].[IdentificadorVariable]` o `self.__class__.[IdentificadorVariable]`.

## 3. Particularidades de la POO en Python
Al igual que para las funciones, las clases también se documentan usando *docstrings*, a las que se accede usando `help(clase)`.

En Python existe un concepto conocido como ***duck typing***, que consiste en que si un objeto puede ejecutar sus métodos en más que en su tipo específico, siguiendo el principio "si camina como un pato y grazna como un pato, entonces es un pato". Por ejemplo, una función `def procesar_secuencia(secuencia): return secuencia[0]` puede funcionar con listas, tuplas y strings.

Otra particularidad es que Python soporta la **herencia múltiple**. Una clase puede heredar de varias a la vez. Si varias de las *superclases* tienen un método llamado igual, se utilizará el método de la primera *superclase* mencionada.

Python usa **métodos especiales** (también llamados métodos *dunder* o *mágicos*) cuyos nombres están rodeados por dos guiones bajos para definir comportamientos específicos de las clases. Los más comunes son:
- `__init__()`: Inicializa un nuevo objeto (se verá en detalle en la siguiente sección).
- `__str__()`: Devuelve una representación legible (i.e., en `string`) del objeto.
- `__dict__()`: Devuelve una representación en diccionario del objeto. Normalmente sólo suelen incorporar los atributos del objeto, no los de la clase. En ocasiones, esto se implementa en una función `to_dict()`. Muchas veces también se implementa un método `from_dict()`, que permite generar un objeto a partir de un diccionario existente. A esto se le llama **serialización y deserialización**.
- `__repr__()`: Devuelve una representación que idealmente podría usarse para recrear el objeto.
- `__len__()`: Define el comportamiento cuando se usa `len(objeto)`.
- `__eq__()`: Define cómo se comparan dos objetos con el operador `==`.
- `__sum__()`: Define cómo se suman dos objetos con el operador `+`.
- `__sub__()`: Define cómo se restan dos objetos con el operador `-`.
- `__mul__()`: Define cómo se multiplican dos objetos con el operador `*`.
- `__hash__()`: Permite usar la clase como objeto *hashable*. Por ejemplo, como clave en un diccionario. Suele devolver algún tipo de ID del objeto o clase.

## 4. Herencia
Para **heredar de una superclase**, se menciona la *superclase* en la declaración de la *subclase*. También se debe llamar al constructor de la *superclase* de la siguiente manera:
```python
class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        self.encendido = False
    
    def encender(self):
        self.encendido = True

class Automovil(Vehiculo):
    def __init__(self, marca, año, puertas):
        # Llamamos al constructor de la clase base
        super().__init__(marca, año)
        # Añadimos atributos específicos
        self.puertas = puertas

# Uso de la clase derivada
mi_auto = Automovil("Toyota", 2022, 4)
print(f"{mi_auto.marca} {mi_auto.modelo}")  # Toyota Corolla
mi_auto.encender()  # Método heredado
```

Aunque técnicamente en Python todos los atributos son públicos, por convención, si queremos marcar que un atributo debe ser utilizado como **atributo protegido** (solo debe usarse en la clase donde se declara y en las clases que hereden de ella) y no debería accederse desde fuera de la clase, se le añade un guión bajo al principio de su identificador. Si se le añaden dos guiones bajos, actúa como un **atributo privado** y no se heredaría. Sin embargo, es posible usarla desde clases heredadas accediendo así: `_[IdentificadorClaseBase]__[identificador_privado]`.

Cuando heredamos de una clase, es posible **sobreescribir métodos de la clase base** creando métodos con su mismo nombre en sus subclases. También es posible **extender la funcionalidad** de dichos métodos utilizando `super()`, que nos permite llamar al método de la superclase desde un método de una subclase. Por ejemplo, podemos ejecutar `super().__init__()` desde el constructor de la subclase para inicializar la superclase antes de completar la inicialización con los atributos de instancia de la subclase.

> ATENCIÓN: En ocasiones, tiene más sentido la **composición** que la herencia. Esto consiste en tener un objeto como atributo (ya sea de clase o de instancia) en lugar de heredar de heredar. Siempre es preferible utilizar jerarquías poco profundas, para simplificar el código y facilitar la implementación de tests unitarios.

## 5. Conceptos Avanzados
Uno de los conceptos avanzados más importantes de las clases de Python son los **slots**. Son una herramienta que permite ahorrar espacio cuando se usan muchos objetos pequeños. Las clases con *slots* definen todos los atributos a la vez que la clase, por lo que no se pueden definir más atributos del objeto después de crearlo (pero sí se pueden añadir atributos de clase). Cuantos más atributos de objeto hayan en una clase, más memoria se ahorra al utilizar esta herramienta. Para utilizarla, se hace de la siguiente manera:
```python
class PersonaOptimizada:
    __slots__ = ['nombre', 'edad']  # Puede ser una lista o una tupla, no afectará a la eficiencia
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Este es el link a la [documentación oficial](https://docs.python.org/3/reference/datamodel.html#object.__slots__) y en [este video](https://youtu.be/Iwf17zsDAnY?si=74zLiQZTa2JeACsg) se explican en más detalle.

Al igual que con las funciones, también se pueden usar **decoradores** con clases, ya sea para medir o *loggear* el tiempo de su creación, para añadir nuevos métodos, etc. Nativamente, Python ofrece el decorador `@property`, que permite acceder a métodos como si fuesen atributos (sin usar paréntesis). Esto es muy útil para implementar *getters*:
```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        """Getter para el radio"""
        return self._radio
    
    @property
    def diametro(self):
        """Propiedad calculada (solo lectura)"""
        return self._radio * 2

# Uso de properties
circulo = Circulo(5)
print(circulo.radio)     # 5
print(circulo.diametro)  # 10
```

> ADVERTENCIA: El uso de propiedades es menos eficiente que el uso de atributos públicos, por lo que debe priorizarse el uso de atributos públicos.

Otros decoradores útiles son:
- `@staticmethod`: Permite crear **métodos estáticos** dentro de una clase que no reciban ni la instancia del objeto ni la clase, por lo que no usan ni el atributo `self` ni el atributo `cls`. Sirven para estructurar el código y/o añadir funcionalidades a una clase que no depende ni de las variables de clase ni de las de instancia.
- `@abstractmethod`: Permite definir **métodos abstractos**, que son métodos vacíos (suelen contener únicamente una instrucción `pass`) que sirven como una plantilla de qué métodos deben ser implementados por las clases que hereden de esa clase.
