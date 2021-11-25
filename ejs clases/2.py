class Vector3D:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def __str__(self):
         return "(" f"{self.n1} {self.n2} {self.n3}" ")"

    def sumar(self,vector):
        self.n1 = (self.n1 + vector.n1) 
        self.n2 = (self.n2 + vector.n2) 
        self.n3 = (self.n3 + vector.n3)
        print(self)

    def restar(self, vector):
        self.n1 = (self.n1 - vector.n1) 
        self.n2 = (self.n2 - vector.n2) 
        self.n3 = (self.n3 - vector.n3)
        print(self)

    def multiplicar(self, escalar):
        self.n1 = (self.n1 * escalar) 
        self.n2 = (self.n2 * escalar) 
        self.n3 = (self.n3 * escalar)
        print(self)

    def dividir(self, escalar):
        self.n1 = (self.n1 / escalar) 
        self.n2 = (self.n2 / escalar) 
        self.n3 = (self.n3 / escalar)
        print(self)
          

vector = Vector3D(1,3,1)
vector2 = Vector3D(4,7,2)

print(vector)
print(vector2)


vector.sumar(vector2)

vector.restar(vector2)

vector.multiplicar(2)

vector.dividir(2)



