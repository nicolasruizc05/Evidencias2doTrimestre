  # ¿Cómo se crea una clase?
class Persona:
      pass
  # ¿Cómo se crea el constructor de una clase?
class Persona:
      def __init__(self):
          pass    
 # ¿Cómo se inicializa un atributo de una clase?
class Persona:
     def __init__(self,nombre,identificacion,edad):
         self.nombre = nombre
         self.identificacion = identificacion
         self.edad = edad   
 # ¿Cómo se crea un método o función en una clase?
class Persona:
     def saludar(self):
        print("hola, ¿como estas?")       
 # ¿Cómo se crea un objeto de una clase?
class Persona:
     def __init__(self,nombre):
         self.nombre=nombre
Persona1=Persona()
 # ¿Cómo modifica un atributo de un objeto?
class Persona:
     def __init__(self,nombre):
         self.nombre=nombre
persona1=Persona("Juan")
persona1.nombre=input("Escriba el nuevo nombre")
 # ¿Cómo accedo a un método de la clase?
class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def saludar(self,nombre):
        print("hola como estas")    
persona2=Persona("Juan")
persona2.saludar()

        