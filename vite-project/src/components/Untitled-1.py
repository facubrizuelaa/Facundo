class Estudiante:
    def __init__(self, nombre, inteligencia, atencion, horas):
        self.nombre = nombre
        self.inteligencia = inteligencia
        self.atencion = atencion
        self.horas = horas
    
    def estudiar(self):
        self.inteligencia += self.horas * 4
        self.atencion -= self.horas * 2
    
    def objetos(self, lapiz, goma, corrector):#esto debería ser por ejemplo el método saludar, muestra un print (f"Hola{self.nombre}")
        self.lapiz = lapiz
        self.goma = goma
        self.corrector = corrector


p1 = Estudiante("mijo", 19, 170, 4)

p1.estudiar()

print(p1.inteligencia)
print(p1.atencion)