class MatrizCalc:
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

    def imprimir(self):
        def imprimirFilaA(self):
            print("{}".format(self.a),"{}".format(self.b),"{}".format(self.c))
        def imprimirFilaB(self):
            print("{}".format(self.d),"{}".format(self.e),"{}".format(self.f))
        def imprimirFilaC(self):
            print("{}".format(self.g),"{}".format(self.h),"{}".format(self.i))   
        imprimirFilaA(self)
        imprimirFilaB(self)
        imprimirFilaC(self)
        
matriz1 = MatrizCalc(1,2,3,4,5,6,7,8,9)
matriz1.imprimir()