class NumeroComplejo():
    def __init__(self,real,imaginaria):
        self.real = real
        self.imaginaria = imaginaria
    
    def sumar(self,Rn2,In2):
        pReal = self.real+Rn2
        pImg = self.imaginaria + In2
        print(f"Resultado Suma: {pReal} + ({pImg})i")
        pass

    def restar(self,Rn2,In2):
        pReal = self.real-Rn2
        pImg = self.imaginaria - In2
        print(f"Resultado Resta: {pReal} + ({pImg})i")
        pass

    def dividir(self,Rn2,In2):
        numR = ((self.real*Rn2) + (self.imaginaria*In2)) # (ac + bd)
        numI = ((self.imaginaria*Rn2) - (self.real*In2)) #(bc - ad)i
        denom = (Rn2*Rn2) + (In2*In2)
        print(f"Resultado Divi: {numR} + ({numI})i")
        print(f"                ------------")
        print(f"                {denom}")

    def multiplicar(self,Rn2,In2):
        pReal = ((self.real*Rn2) - (self.imaginaria*In2)) # (ac - bd)
        pImg = (self.real*In2) + (self.imaginaria * Rn2) # (ad + bc)*i
        print(f"Resultado Multi: {pReal} + ({pImg})i")
    

num1 = NumeroComplejo(3,2)
num1.sumar(2,5)
num1.restar(2,5)
num1.dividir(4,-5)
num1.multiplicar(5,6)