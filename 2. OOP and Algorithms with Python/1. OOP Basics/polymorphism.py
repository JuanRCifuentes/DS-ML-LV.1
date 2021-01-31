class Person:

    def __init__(self, name):
        self.name = name
    
    def forward(self):
        print("I'm walking")

class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)
    
    def forward(self):
        print("I'm biking")

def main():
    persona = Person('David')
    persona.forward()

    ciclista = Cyclist('Daniel')
    ciclista.forward()

if __name__ == "__main__":
    main()