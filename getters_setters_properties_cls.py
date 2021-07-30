class WebDeveloper:
    ''' This is the Developer class, along with its docstrings '''

    def __init__(self, name):
        # declaramos atributos o propiedades como privad@s
        self.__name = name

    # método getter para obtener las propiedades usando un objeto
    def get_name(self):
        return self.__name

    # método getter para cambiar el valor 'name' usando un objeto
    def set_name(self, name):
        self.__name = name


# creando un objeto basado en la clase WebDeveloper
objWebDev = WebDeveloper("Alvison Hunter")

# obteniendo el valor de 'name' usando el método get_name()
print(f"Name: {objWebDev.get_name()}")

# establecer un nuevo valor para el atributo 'name' con el método set_name()
objWebDev.set_name("Alvison Lucas Hunter Arnuero")

# Veamos los resultados ahora
print(f"Name: {objWebDev.get_name()}")


# --------------- Developer Class -------------------

class Developer:
    ''' This is the Developer class, along with its docstrings '''

    def __init__(self, name, age):
        # declaramos atributos o propiedades como privad@s
        self.__name = name
        self.__age = age

    # método getter para obtener las propiedades usando un objeto
    def get_name(self):
        return self.__name

    # método getter para cambiar el valor 'name' usando un objeto
    def set_name(self, name):
        self.__name = name

   # método getter para obtener la propiedad age del objeto
    def get_age(self):
        return self.__age

    # Agregemos la opcion de establecer la edad solamente
    # si el parametro enviado es numero positivo y no cadena
    def set_age(self, age):
        # condicion esperada para ver si el parametro es un entero valido
        if not isinstance(age, int):
            print("You entered an invalid age. We will set the default value to 18.")
            self.__age = 18
        else:
            self.__age = age


# --------------- Implementacion -------------------
# creando un objeto basado en la clase Developer
obj = Developer("Alvison Hunter", 40)

# obteniendo el valor de 'name' usando el método get_name()
print(f"Name: {obj.get_name()}")

# obteniendo el valor de 'age' usando el método get_age()
print(f"Age: {obj.get_age()}")

# establecer un nuevo valor para el atributo 'name' con el método set_name()
obj.set_name("Alvison Lucas Hunter Arnuero")
# establecer un nuevo valor para el atributo 'age' con el método set_age()
obj.set_age("35")

# Veamos los resultados ahora para ambos casos
print(f"Name: {obj.get_name()} | Age: {obj.get_age()}")

# ------------ Implementacion Pythonica -------------------


class PythonicWay:
    def __init__(self, url):
        self.url = url


# Creando un objeto para la clase PythonicWay
obj2 = PythonicWay("https://alvisonhunter.com/")

# Veamos ahora el resultado en pantalla
print(f"Developer Website: {obj2.url}")

# ------------ Property Decorator -------------------


class Property:

    def __init__(self, language):
        # inicializando el atributo
        self.language = language

    @property
    def language(self):
        return self.__language

    # el nombre del atributo y el nombre del método deben ser iguales
    # que el se usa para establecer el valor del atributo
    @language.setter
    def language(self, language):
        if language.title() == "Python":
            self.__language = language.title()
        else:
            self.__language = "Cambiate a Python"


obj3 = Property("JavaScript")
print(obj3.language)

# ----------- Property Alternative -----------


class PropertyAlternative:

    def __init__(self, new_lang):
        # llamando al método set_lang() para establecer el valor 'lang'
        # comprobando determinadas condiciones primero
        self.__set_lang(new_lang)

    # método getter para obtener las propiedades usando un objeto
    def __get_lang(self):
        return self.__lang

    # método setter para cambiar el valor 'lang' usando un objeto
    def __set_lang(self, new_lang):

        # condicion para verificar si new_lang es apropiada o no
        if new_lang.title() == "Python":
            self.__lang = new_lang
        else:
            self.__lang = "Get Pythonized, Chavalo!"

    # Primero pasemos todos los métodos getter y setter al metodo property()
    # Asígnemos el resultado a una variable que usaremos como atributo de clase.
    language = property(__get_lang, __set_lang)


# creamos un objeto nuevo de la clase PropertyAlternative
obj4 = PropertyAlternative("Java")

print(f"Lenguaje: {obj4.language}")


# ----------- Class Dog Example -----------


class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


# Instanciemos aca creando dos objects de esta clase
chele = Dog("Chele", 4, "Belgian Tervuren")
kiki = Dog("Kiki", 2, "Doberman Pinscher")

# Veamos entonces que contienen estos objs instancias de Dog

# Chele is a 4 years old Belgian Tervuren.
print(f"{chele.name} is a {chele.age} years old {chele.breed}.")

# Kiki is a 2 years old Doberman Pinscher.
print(f"{kiki.name} is a {kiki.age} years old {kiki.breed}.")


# ----------- Class PythonDev Example -----------

class PythonDev:
    ''' This is the PythonDev class, along with its docstrings '''

    def __init__(self, age=18, nationality="Nicaraguense"):
        self.age = age
        self.nationality = nationality

    def greet(self):
        print(f"Nationality: {self.nationality}.")
        print(f"Current age: {self.age} years old.")


# Creamos primero la instancia de esta clase
pythonDev01 = PythonDev(39)

# Usemos los metodos de este object ahora
pythonDev01.greet()

# ahora crearemos otra instancia pasando ambos parametros
pythonDev02 = PythonDev(20, "Costarricense")
pythonDev02.greet()

# Tambien podemos acceder a sus metodos individualmente
print(f"Nationality: {pythonDev01.nationality}")
print(f"Current Age: {pythonDev01.age}")


# ----------- Class NicaraguanTypicalMeals Example -----------

class NicaraguanTypicalMeals:
    ''' This is the NicaraguanTypicalMeals class, along with its docstrings '''

    # Declaremos los atributos de la clase desde aca con sus valores
    breakfast = "Nacatamal o Tamuga de Masatepe"
    lunch = "Sopa de Mondongo Masatepina"
    dinner = "GalloPinto con Queso Frito y Tajadas Maduras"


# Creamos ahora la instancia de esta clase
dish = NicaraguanTypicalMeals()

# Veamos que posee el object creado como herencia primaria de la clase
print(f"Breakfast: {dish.breakfast}.")
print(f"Lunch: {dish.lunch}.")
print(f"Dinner: {dish.dinner}.")

# ----------- Class PythonZealot Example -----------


class PythonZealot:
    ''' This is the PythonZealot class, along with its docstrings '''
    # Declaremos los atributos de la clase desde aca con sus valores
    job_title = "Python Developer"

    def sayHello(self):
        print(f"Hi guys: I am a {self.job_title}.")


# Creamos primero la instancia de esta clase
PythonZealot01 = PythonZealot()

# Usemos los metodos de este object ahora
PythonZealot01.sayHello()
