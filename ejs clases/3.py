class Numero:
    def __init__(self, numeroPrincipal=[], numeroSecundario=[]):
        self.numeroPrincipal = numeroPrincipal
        self.numeroSecundario = numeroSecundario

    def __str__(self):
        return "Su numero es {}".format(self.numeroPrincipal)

    def suma(self):
        resSuma = []
        for i in range(len(self.numeroPrincipal)):
            resSuma.append([])
            for j in range(len(self.numeroPrincipal[0])):
                resSuma[i].append(self.numeroPrincipal[i][j] + self.numeroSecundario[i][j])
        print("Resultado Suma: ")
        print(resSuma[0])
        print(resSuma[1])
        print(resSuma[2])
        print('____________')

    def resta(self):
        resResta = []
        for i in range(len(self.numeroPrincipal)):
            resResta.append([])
            for j in range(len(self.numeroPrincipal[0])):
                resResta[i].append(self.numeroPrincipal[i][j] - self.numeroSecundario[i][j])
        print("Resultado Resta: ")
        print(resResta[0])
        print(resResta[1])
        print(resResta[2])
        print('____________')
    
    def producto(self):
        resProducto = []
        for i in range(len(self.numeroPrincipal)):
            resProducto.append([])
            for j in range(len(self.numeroPrincipal[0])):
                resProducto[i].append(self.numeroPrincipal[i][j] * self.numeroSecundario[i][j])
        print("Resultado Producto: ")
        print(resProducto[0])
        print(resProducto[1])
        print(resProducto[2])
        print('____________')


miMatriz = [[int(input("Dígito 1:1 : ")),int(input("Dígito 1:2 : ")),int(input("Dígito 1:3 : "))],
            [int(input("Dígito 2:1 : ")),int(input("Dígito 2:2 : ")),int(input("Dígito 2:3 : "))],
            [int(input("Dígito 3:1 : ")),int(input("Dígito 3:2 : ")),int(input("Dígito 3:3 : "))]]

print(miMatriz[0])
print(miMatriz[1])
print(miMatriz[2])

miMatrizDos = [[int(input("Dígito 1:1 : ")),int(input("Dígito 1:2 : ")),int(input("Dígito 1:3 : "))],
            [int(input("Dígito 2:1 : ")),int(input("Dígito 2:2 : ")),int(input("Dígito 2:3 : "))],
            [int(input("Dígito 3:1 : ")),int(input("Dígito 3:2 : ")),int(input("Dígito 3:3 : "))]]

print(miMatrizDos[0])
print(miMatrizDos[1])
print(miMatrizDos[2])

miNumeroUno = Numero(miMatriz, miMatrizDos)
miNumeroUno.suma()
miNumeroUno.resta()
miNumeroUno.producto()