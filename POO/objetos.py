class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
persona1 = Persona('Juan', 21, 'Masculino')
print(persona1.nombre, persona1.edad, persona1.genero)
print(persona1)

        
persona2 = Persona('Juana', 28, 'Femenina')
print(persona2.nombre, persona2.edad, persona2.genero)
print(persona2)    # cada objeto es distinto, pero viene de la clase Persona
        