# -*- coding: utf-8 -*-
"""Lab2_Programacion_Cientifica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ll4Qyf2W9jEVHoh2GUJZzkckodBBkvf

<h1><center>Laboratorio 2: Primeros pasos 👣</center></h1>

<center><strong>MDS7202: Laboratorio de Programación Científica para Ciencia de Datos - Otoño 2023</strong></center>

### Cuerpo Docente:

- Profesor: Pablo Badilla y Ignacio Meza 
- Auxiliar: Sebastián Tinoco
- Ayudante: Felipe Arias y Diego Cortez

### Equipo: SUPER IMPORTANTE - notebooks sin nombre no serán revisados

- Nombre de alumno 1: Javier Santidrián Salas
- Nombre de alumno 2: Patricio Yáñez Alarcón

### **Link de repositorio de GitHub:** https://github.com/jsantidrian/labs-Santidrian-Yanez

## Reglas:

- Fecha de entrega: 6 días desde la publicación, 3 días de atraso con 1 punto de descuento c/u. Pueden utilizar días bonus sin descuento.
- **Grupos de 2 personas**.
- Asistencia obligatoria a instrucciones del lab (viernes 16.15). Luego, pueden quedarse trabajando en las salas o irse.
- **Ausentes** deberán realizar la actividad solos. 
- Cualquier duda fuera del horario de clases al foro. Mensajes al equipo docente serán respondidos por este medio.
- Prohibidas las copias. 
- Pueden usar cualquer material del curso que estimen conveniente.

## Objetivos del lab:

Poner en práctica los tópicos básicos del lenguaje de programación Python vistos en clases.

- Variables, Operadores y Expresiones.
- Estructuras de Control (if/else).
- Iteraciones.
- Listas y Diccionarios.
- Funciones
- Programación Orientada a Objetos (Encapsulamiento, Polimorfismo y Herencia)

## Parte 1: 🍋 Frutas 🍓


<div align='center'>
<img src='https://upload.wikimedia.org/wikipedia/commons/a/a2/Berries_in_Berlin.jpg' width=600/>
</div>

Defina las siguientes frutas como diccionarios a partir de sus características (nombre, color, tipo y si posee o no pepas):

| Nombre    | Tipo     | Color    | Pepas |
|-----------|----------|----------|-------|
| limon     | cítrica  | amarillo | True  |
| naranja   | cítrica  | naranjo  | True  |
| plátano   | tropical | amarillo | False |
| piña      | tropical | amarillo | False |
| frutilla  | bosque   | rojo     | True |
| frambuesa | bosque   | rojo     | True |

### [0.5] Estructurar Datos 

Agregue Piña, Frutilla y Frambuesa como diccionarios (siga los ejemplos de las frutas dadas) y luego cree una lista que contenga estas frutas.
"""

limon = {
    "nombre": "limón", 
    "tipo": "cítrica", 
    "color": "amarillo", 
    "pepas": True
    }

naranja = {
    "nombre": "naranja", 
    "tipo": "cítrica", 
    "color": "naranjo", 
    "pepas": True
    }

platano = {
    "nombre": "plátano", 
    "tipo": "tropical", 
    "color": "amarillo", 
    "pepas": False
    }

# agregar las frutas que faltan aquí
piña = {
    "nombre": "piña", 
    "tipo": "tropical", 
    "color": "amarillo", 
    "pepas": False
    }

frutilla = {
    "nombre": "frutilla", 
    "tipo": "bosque", 
    "color": "rojo", 
    "pepas": True
    }

frambuesa = {
    "nombre": "frambuesa", 
    "tipo": "bosque", 
    "color": "rojo", 
    "pepas": True
    }

"""Ahora, agregue todas las frutas a una lista."""

# Ojo: agregue los datos en el mismo orden que aparecen en la tabla
datos = [limon, naranja, platano, piña, frutilla, frambuesa]

"""Esta lista será la información con la que se trabajará durante el lab.

### Funciones Aplicadas a los Datos [2.5 puntos]

En esta sección se les pide generar una serie de funciones que cumplan diferentes propósitos. Un aspecto clave de la programación funcional es la apropiada **documentación** de lo que ustedes generen. Si bien existen diferentes formas de documentar código, una de las mas usadas es el formato docstring de `numpy`:

```python
# manual para describir:
# https://numpydoc.readthedocs.io/en/latest/format.html

# plantilla (agregar todos los argumentos que sean necesarios)
# pensar _type_ como los tipos básicos que hemos visto hasta ahora: int, float, string, list, dict, tuple, set, etc...

def funcion_generica(arg1, arg2):
    '''_summary_

    Parameters
    ----------
    arg1 : _type_
        _description_
    arg2 : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    '''
    return ...
```

Considerando esto y **sin olvidar la documentación**, se les pide generar las siguientes funciones:

**1. La función `generar_descripcion(fruta)` que reciba una fruta genere una descripción de la fruta de la siguiente manera:**

```{El/La} {...} es una fruta de tipo {...} de color {...}. {Presenta/No presenta} pepas en su interior.```
    
Por ejemplo, `generar_descripcion(plátano)` debe generar el siguiente string:
    
```
'El plátano es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior.'
```
    
Indicaciones: 
- Usen formateo o suma de strings, if, else y for.
- Para saber si ocupar 'El' o 'La', pueden acceder al nombre de la fruta y ver cual es el último carácter a través de indexadores `string[indice]`.
- Utilice los siguientes test para corroborar el funcionamiento de su código:

```python
assert generar_descripcion(limon) == "El limón es una fruta de tipo cítrica de color amarillo. Presenta pepas en su interior."
assert generar_descripcion(naranja) == "La naranja es una fruta de tipo cítrica de color naranjo. Presenta pepas en su interior."
assert generar_descripcion(platano) == "El plátano es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior."
assert generar_descripcion(piña) == "La piña es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior."
assert generar_descripcion(frutilla) == "La frutilla es una fruta de tipo bosque de color rojo. Presenta pepas en su interior."
assert generar_descripcion(frambuesa) == "La frambuesa es una fruta de tipo bosque de color rojo. Presenta pepas en su interior."
```
"""

def generar_descripcion(fruta):
    # Documentación Aquí
    """función que genera una descripción de una fruta

    Parameters
    ----------
    fruta : dict
        contiene la información asociada a la fruta

    Returns 
    -------
    str
        {El/La} {...} es una fruta de tipo {...} de color {...}.
        {Presenta/No presenta} pepas en su interior.
    """
    # Código Aquí
    #creamos la variable (str) a retornar como string vacío
    descripcion = ''

    #accedemos a la información que necesitamos
    nombre = fruta['nombre']
    tipo = fruta['tipo']
    color = fruta['color']
    pepas = fruta['pepas']

    #si el nombre de la fruta tiene genero femenino (termina con a)
    if nombre[-1] == 'a':
      #si tiene pepas
      if pepas == True:
        descripcion = ('La ' + nombre
                       + ' es una fruta de tipo ' + tipo 
                       +' de color ' + color
                       + '. Presenta pepas en su interior.')
      
      #si no tiene pepas
      else:
        descripcion = ('La ' + nombre
                       + ' es una fruta de tipo ' + tipo
                       +' de color ' + color
                       + '. No presenta pepas en su interior.')  

    #si el nombre de la fruta tiene genero masculino
    else:
      #si tiene pepas
      if pepas == True:
        descripcion = ('El ' + nombre
                       + ' es una fruta de tipo ' + tipo
                       +' de color ' + color
                       + '. Presenta pepas en su interior.')
      #si no tiene pepas  
      else:
        descripcion = ('El ' + nombre
                       + ' es una fruta de tipo ' + tipo
                       +' de color ' + color
                       + '. No presenta pepas en su interior.')

    return descripcion

#comprobamos el ejemplo
generar_descripcion(platano)

#tests
assert generar_descripcion(limon) == "El limón es una fruta de tipo cítrica de color amarillo. Presenta pepas en su interior."
assert generar_descripcion(naranja) == "La naranja es una fruta de tipo cítrica de color naranjo. Presenta pepas en su interior."
assert generar_descripcion(platano) == "El plátano es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior."
assert generar_descripcion(piña) == "La piña es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior."
assert generar_descripcion(frutilla) == "La frutilla es una fruta de tipo bosque de color rojo. Presenta pepas en su interior."
assert generar_descripcion(frambuesa) == "La frambuesa es una fruta de tipo bosque de color rojo. Presenta pepas en su interior."

"""**2. La función `describir(datos)` que generalice la función `generar_descripcion` para recibir una lista de frutas y devolver una lista con las descripciones de cada una:**

Por ejemplo, `describir([limon, naranja]])` deberá devolver una lista de la forma `[descripcion_limon, descripcion_naranja]`
"""

def describir(datos):
    # Documentación Aquí
    """función que recibe una lista de frutas y 
    devuelve una lista con las descripciones de cada una

    Parameters
    ----------
    datos: list
        recibe una lista de frutas (donde cada una es un diccionario)

    Returns 
    -------
    list
        descripciones de cada fruta
    """
    # Código Aquí
    #creamos la variable (list) a retornar como lista vacía
    descripciones = []

    #iteramos sobre datos
    for fruta in datos:
      #agregamos a la lista la descripción de la fruta
      descripciones.append(generar_descripcion(fruta))

    return descripciones

#comprobamos el ejemplo
describir([limon, naranja])

"""**3. La función `filtrar_por_pepa(datos, tiene_pepas)` que dado un tipo de fruta y un booleano, retorne las frutas que tienen o no tienen pepas (según el valor de `tiene_pepas`).**
    

Por ejemplo, `filtrar_por_pepa(datos, True)` deberá retornar una lista con los diccionarios de: naranja, limon, frutilla y frambuesa.
"""

def filtrar_por_pepa(datos, tiene_pepas):
    # Documentación Aquí
    """función que recibe una lista de frutas y un booleano y
    retorna una lista de las frutas que tienen o no tienen pepas

    Parameters
    ----------
    datos: list
        recibe una lista de frutas (donde cada una es un diccionario)
    tiene_pepas: bool
        True si queremos filtrar frutas con pepas y False para las sin pepas

    Returns 
    -------
    list
        lista con los diccionarios de las frutas filtradas según pepas
    """
    # Código Aquí

    #creamos la variable (list) a retornar como lista vacía
    filtrados = []

    #iteramos sobre datos
    for fruta in datos:
      #filtramos frutas segun el valor de verdad de tiene_pepas
      if fruta['pepas'] == tiene_pepas:
        filtrados.append(fruta)

    return filtrados

#comprobamos el ejemplo
filtrar_por_pepa(datos, True)

"""**4. La función `conteo_colores(datos)` que cree un diccionario que haga un conteo los colores de las frutas.**

Para estos datos, la función debería retornar el siguiente diccionario: 
    
```python
{"amarillo": 3, "naranjo": 1, "rojo": 2}
```
"""

def conteo_colores(datos):
      # Documentación Aquí
      """función que crea un diccionario
      que hace un conteo de los colores de las frutas.

      Parameters
      ----------
      datos: list
          recibe una lista de frutas donde cada una es un diccionario

      Returns 
      -------
      dict
          entrega la cantidad de frutas que hay por color
      """
      # Código Aquí
      #creamos una lista vacía para agregar todos los colores de las frutas
      colores = []

      #iteramos sobre datos
      for fruta in datos:
        #guardamos color de la fruta
        color = fruta['color']
        #agregamos a lista de colores
        colores.append(color)
      
      #guardamos los colores únicos mediante set() y los guardamos en una lista
      colores_unicos = list(set(colores))

      #lista vacía que contendrá tuplas (color, cantidad)
      lista_conteo = []

      #iteramos sobre cada color unico
      for color in colores_unicos:
        #obtenemos cantidad de veces que se repite en colores
        cantidad = colores.count(color)
        #generamos la tupla (color, cantidad) y la agregamos a la lista
        tupla = (color, cantidad)
        lista_conteo.append(tupla)

      #transformamos lista_conteo a diccionario
      conteo = dict(lista_conteo)

      return conteo

#comprobamos el ejemplo
conteo_colores(datos)

"""**5. La función `obtener_tipos` que devuelva una lista con los tipos únicos de fruta usando `set()`**.

Por ejemplo, `obtener_tipos([limon, naranja, platano])` debería devolver `["citrica", "tropical"]`
"""

def obtener_tipos(datos):
    # Documentación Aquí
    """función que recibe una lista de frutas y 
    devuelve una lista con los tipos únicos de fruta presentes usando set()

    Parameters
    ----------
    datos: list
        recibe una lista de frutas (donde cada una es un diccionario)

    Returns 
    -------
    list
        lista con los tipos únicos de fruta presentes
    """

    # Código Aquí
    #creamos la variable (set) a retornar como conjunto vacío (evita duplicados)
    tipos_conjunto = set()
    
    #iteramos sobre datos
    for fruta in datos:
      #agregamos al conjunto el tipo de fruta del dato
      tipos_conjunto.add(fruta['tipo'])
    
    #convertimos tipos_conjunto a lista
    tipos = list(tipos_conjunto)

    return tipos

#comprobamos el ejemplo
obtener_tipos([limon, naranja, platano])

"""**6. Genere tres test para cada una de las funciones de la pregunta 5 y así comprobar que funcionan correctamente.**

Se <u>sugiere</u> que se apoyen en las siguientes directrices: 
- Test para tratar resultados nulos
- Test para un subconjunto interesante cuyo resultado no sea nulo
- Test para todos los datos

**Ejecuten esta celda para comprobar su código:**
"""

# ---------------------------------------------------------------------
# test descripciones

assert describir([platano]) == ['El plátano es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior.'] # test 1
assert describir([limon, naranja]) == ['El limón es una fruta de tipo cítrica de color amarillo. Presenta pepas en su interior.',
 'La naranja es una fruta de tipo cítrica de color naranjo. Presenta pepas en su interior.',] #test 2
assert describir([frambuesa, frutilla, platano]) == ['La frambuesa es una fruta de tipo bosque de color rojo. Presenta pepas en su interior.',
 'La frutilla es una fruta de tipo bosque de color rojo. Presenta pepas en su interior.',
 'El plátano es una fruta de tipo tropical de color amarillo. No presenta pepas en su interior.'] # test 3

# ---------------------------------------------------------------------
# test filtro

assert filtrar_por_pepa([limon, naranja], True) == [{'nombre': 'limón', 'tipo': 'cítrica', 'color': 'amarillo', 'pepas': True},
 {'nombre': 'naranja', 'tipo': 'cítrica', 'color': 'naranjo', 'pepas': True}]  # test 1
assert filtrar_por_pepa([platano], True) == [] # test 2 
assert filtrar_por_pepa(datos, False) == [{'nombre': 'plátano',
  'tipo': 'tropical',
  'color': 'amarillo',
  'pepas': False},
 {'nombre': 'piña', 'tipo': 'tropical', 'color': 'amarillo', 'pepas': False}] # test 3

# ---------------------------------------------------------------------
# test conteo

assert conteo_colores([limon]) == {'amarillo': 1} # test 1
assert conteo_colores([limon,frambuesa,platano]) == {'rojo': 1, 'amarillo': 2} # test 2
assert conteo_colores(datos) == {'rojo': 2, 'amarillo': 3, 'naranjo': 1} # test 3

# ---------------------------------------------------------------------
# test tipos

assert obtener_tipos([frambuesa]) == ['bosque'] # test 1
assert obtener_tipos([limon, naranja, platano]) == ['cítrica', 'tropical'] # test 2
assert obtener_tipos(datos) == ['cítrica', 'tropical', 'bosque'] # test 3

"""**7. Programe nuevamente las funciones `describir`, `filtrar_por_pepa` y `obtener_tipos`, pero esta vez usando *comprehensions*.**

*Hint: Pueden reutilizar la documentación escrita en la pregunta 5*
"""

def obtener_descripciones_v2(datos):
    # Documentación Aquí
    """función que recibe una lista de frutas y 
    devuelve una lista con las descripciones de cada una

    Parameters
    ----------
    datos: list
        recibe una lista de frutas (donde cada una es un diccionario)

    Returns 
    -------
    list
        descripciones de cada fruta
    """
    # Código Aquí
    descripciones = [generar_descripcion(fruta) for fruta in datos]
    return descripciones

def filtrar_por_pepa_v2(datos, tiene_pepas):
    # Documentación Aquí
    """función que recibe una lista de frutas y un booleano y
    retorna una lista de las frutas que tienen o no tienen pepas

    Parameters
    ----------
    datos: list
        recibe una lista de frutas (donde cada una es un diccionario)
    tiene_pepas: bool
        True si queremos filtrar frutas con pepas y False para las sin pepas

    Returns 
    -------
    list
        lista con los diccionarios de las frutas filtradas según pepas
    """
    # Código Aquí
    filtrados = [fruta for fruta in datos if fruta['pepas'] == tiene_pepas]
    return filtrados

def obtener_tipos_v2(datos):
    # Documentación Aquí
    """función que recibe una lista de frutas y 
    devuelve una lista con los tipos únicos de fruta presentes usando set()

    Parameters
    ----------
    datos: list
        recibe una lista de frutas (donde cada una es un diccionario)

    Returns 
    -------
    list
        lista con los tipos únicos de fruta presentes
    """
    # Código Aquí
    tipos = list({fruta['tipo'] for fruta in datos})
    return tipos

"""## Parte 2: Electrodomésticos 

En esta parte se solicitarán un par de clases que permitirá jugar con la Programación Orientada a Objetos.

<div align='center'>
<img src='https://upload.wikimedia.org/wikipedia/commons/6/67/Breville.jpg' width=400/>
</div>


### [0.5] Clase Electrodoméstico

Defina la clase `Electrodomestico` que implemente:


- Un constructor que defina un atributo de instancia llamado `enchufado` que almacene valores booleanos. 
- Un método llamado `esta_enchufado(self)` que levante una excepción `Exception` y que termine con la ejecución del programa cuando el atributo enchufado sea `False`. La excepción debe levantar el mensaje `'Alerta ⚠️: El electrodoméstico no está enchufado'`
- Un método llamado `enchufar(self)` que cambia el estado de `enchufado` a True.


"""

class Electrodomestico:
    
    def __init__(self):
      self.enchufado = False

    def esta_enchufado(self):
      if self.enchufado == False:
        raise Exception('Alerta!: El electrodoméstico no está enchufado')
      
    def enchufar(self):
      self.enchufado = True

"""### Clase Jugera [1.5 puntos] 


<div align='center'>
<img src='https://upload.wikimedia.org/wikipedia/commons/b/bb/Liquadora_%28parts%29.JPG' width=400/>
</div>


Implemente la clase `Jugera` que extiende `Electrodomestico` y que implemente: 


- Un constructor que tenga una lista de ingredientes frutales (llamado `bandeja`).


- Un método llamado `agregar_ingrediente(self, nueva_fruta)` que dado una fruta, agregue esa fruta a la `bandeja`.

- Un método llamado `listar_ingredientes(self)` que imprima (con `print`) los ingredientes actuales de la `bandeja` de la siguiente forma: 

    `Ingredientes en la bandeja: frutilla, frambuesa, piña.`

De lo contrario si no tiene ingredientes imprima:

    `Bandeja vacía`


**Hint:** Investigar el método `join` de un string para generar el string con los nombres de las frutas.
    
    
    

- Un método llamado `preparar_jugo(self)` que: 
    - Primero verifique que el electrodoméstico esté enchufado usando `self.esta_enchufado()`.
    - Verifique que haya por lo menos un ingrediente en la `bandeja`. En el caso que no haya, levantar una excepción con contenido `'Error ❌: La bandeja no tiene ingredientes.'`
    - Verifique que ninguna fruta tenga pepas. En el caso que haya alguna, imprimir (con `print`) el mensaje de advertencia `'Alerta ⚠️: El jugo puede contener restos de pepas.'`. Puede usar la función definida en la sección anterior.
    - Genere un mensaje indicado `Jugo de {nombres de las frutas separadas por una ,} listo. 🏖️🥤 Que lo disfrutes!!! 🥤🏖️. ` (Hint: Usar nuevamente `join`).
    - Vacie la `bandeja` (es decir, eliminar todas las frutas de la bandeja).
    - Retorne el mensaje generado.

"""

class Jugera(Electrodomestico):

    def __init__(self):
        super().__init__()
        self.bandeja = []

    def agregar_ingrediente(self, nueva_fruta):
        self.bandeja.append(nueva_fruta)

    def listar_ingredientes(self):
        #si no hay ingredientes
        if len(self.bandeja) == 0:
          print('Bandeja vacía')
        else:
          #guardamos los nombres de los ingredientes
          string_lista = []
          for fruta in self.bandeja:
            nombre = fruta['nombre']
            string_lista.append(nombre)
          print('Ingredientes en la bandeja: ' + ', '.join(string_lista))

    def preparar_jugo(self):
        #verificamos si está enchufado
        self.esta_enchufado()
        #si no hay ingredientes
        if len(self.bandeja) == 0:
          raise Exception('Error!: La bandeja no tiene ingredientes.')

        #avisamos si es que hay pepas
        if len(filtrar_por_pepa(self.bandeja,True))>0:
          print('Alerta !: El jugo puede contener restos de pepas.')
        
        #guardamos los nombres de los ingredientes y preparamos el jugo
        string_lista = []
        for fruta in self.bandeja:
          nombre = fruta['nombre']
          string_lista.append(nombre)
        string_final = 'Jugo de ' + ', '.join(string_lista) + ' listo. Que lo disfrutes!!!'
        
        #vaciamos los ingredientes
        self.bandeja = []

        #retornamos el mensaje final
        return string_final

"""### Interacciones

Las siguientes celdas les permitirán probar las interacciones de esta clase.
La ejecución es solo referencial y no lleva puntaje. La idea es que la utilice como guía para desarrollar la clase.
"""

jugera = Jugera()

# Como no tenemos ingredientes, listar_ingredientes deberá imprimir 'Bandeja vacía'
jugera.listar_ingredientes()

# Esta celda debería levantar una excepcion indicando que no está enchufada la jugera.
jugera.preparar_jugo()

# Enchufamos el electrodoméstico
jugera.enchufar()

# Esta celda debería levantar ina excepción informandoles que la bandeja no tiene ingredientes.
jugera.preparar_jugo()

# Agregamos algunos ingredientes
jugera.agregar_ingrediente(naranja)
jugera.agregar_ingrediente(platano)

# Y los listamos (debería imprimir: 'Ingredientes en la bandeja: naranja, plátano')
jugera.listar_ingredientes()

# Preparamos el jugo: 'Jugo de naranja, plátano listo. 🏖️🥤 Que lo disfrutes!!! 🥤🏖️.'
jugera.preparar_jugo()

# Una vez preparado el jugo, debería vaciarse la bandeja (imprimir Bandeja vacía)
jugera.listar_ingredientes()

"""### Clase Jugera + Properties  [1.0]

Implementar `bandeja` usando una `property` que permita setear una `nueva_bandeja` como `bandeja` según las siguientes condiciones:


- Compruebe que `nueva_bandeja` sea una lista. En caso contrario, levante una excepción.
- No permita agregar más de 3 ingredientes a la bandeja a la vez. Si se entregan más de 3 frutas, se levante una excepción.
- Se compruebe que todos los elementos de la lista sean frutas. Para esto, por cada fruta compruebe que:
    1. La fruta sea diccionario.
    2. El diccionario entregado tenga las llaves `nombre`, `tipo`, `color` y `pepas`.
"""

class Jugera(Electrodomestico):
    def __init__(self):
        super().__init__()
        self._bandeja = []

    @property
    def bandeja(self):
        return self._bandeja
    
    @bandeja.setter
    def bandeja(self, nueva_bandeja):
      if not isinstance(nueva_bandeja, list):
        raise ValueError('La nueva_bandeja debe ser una lista.')

      if len(nueva_bandeja) > 3:
        raise ValueError('No se permiten más de 3 frutas por bandeja.')

      for fruta in nueva_bandeja:
        if not isinstance(fruta, dict):
          raise ValueError('La nueva_bandeja solo debe contener diccionarios de frutas.')
        if not all(key in fruta for key in ['nombre', 'tipo', 'color', 'pepas']):
          raise ValueError('Los diccionarios de frutas en la nueva_bandeja deben tener las llaves "nombre", "tipo", "color" y "pepas".')

      self._bandeja = nueva_bandeja

    def agregar_ingrediente(self, nueva_fruta):
      self.bandeja.append(nueva_fruta)

    def listar_ingredientes(self):
        #si no hay ingredientes
        if len(self.bandeja) == 0:
          print('Bandeja vacía')
        else:
          #guardamos los nombres de los ingredientes
          string_lista = []
          for fruta in self.bandeja:
            nombre = fruta['nombre']
            string_lista.append(nombre)
          print('Ingredientes en la bandeja: ' + ', '.join(string_lista))

    def preparar_jugo(self):
        #verificamos si está enchufado
        self.esta_enchufado()
        #si no hay ingredientes
        if len(self.bandeja) == 0:
          raise Exception('Error!: La bandeja no tiene ingredientes.')

        #avisamos si es que hay pepas
        if len(filtrar_por_pepa(self.bandeja,True))>0:
          print('Alerta !: El jugo puede contener restos de pepas.')
        
        #guardamos los nombres de los ingredientes y preparamos el jugo
        string_lista = []
        for fruta in self.bandeja:
          nombre = fruta['nombre']
          string_lista.append(nombre)
        string_final = 'Jugo de ' + ', '.join(string_lista) + ' listo. Que lo disfrutes!!!'
        
        #vaciamos los ingredientes
        self.bandeja = []
        return string_final

"""### Interacciones

Las siguientes celdas les permitirán probar las interacciones de esta clase.
La ejecución es solo referencial y no lleva puntaje. La idea es que la utilice como guía para desarrollar la clase.
"""

jugera_2 = Jugera()

jugera_2.listar_ingredientes()

jugera_2.preparar_jugo()

# Enchufamos el electrodoméstico
jugera_2.enchufar()

# Esta celda debería levantar ina excepción informandoles que la bandeja no tiene ingredientes.
jugera_2.preparar_jugo()

# Agregamos algunos ingredientes (en este caso, como son más de 3, fallará)
jugera_2.bandeja = [naranja, platano, frutilla, limon]

# Agregamos algunos ingredientes 
# (en este caso debería fallar, ya que estamos entregando un string en el primer lugar)
jugera_2.bandeja = ["naranja", platano, frutilla]

# Agregamos algunos ingredientes 
# (en este caso debería fallar, ya que arándando tiene solo la llave nombre)
jugera_2.bandeja = [{'nombre': 'arándano'}, platano, frutilla]

# Agregamos algunos ingredientes (en este caso, como son 3, debería funcionar)
jugera_2.bandeja = [naranja, platano, frutilla]

# Y los listamos (debería imprimir: 'Ingredientes en la bandeja: naranja, plátano, frutilla')
jugera_2.listar_ingredientes()

# Una vez preparado el jugo, imprima el contenido del jugo y si una alerta, 
# en el caso que el jugo tenga pepas.
jugera_2.preparar_jugo()

# Una vez preparado el jugo, debería vaciarse la bandeja (imprimir Bandeja vacía)
jugera_2.listar_ingredientes()

"""<a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=87110296-876e-426f-b91d-aaf681223468' target="_blank">
<img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
"""