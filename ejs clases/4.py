class Perfil:
    def __init__(self,username,tipo="user"):
        self.username = username
        self.carritoDCompras  = []
        self.tipo = tipo
    
    def AgregarACarrito(self, item):
        self.carritoDCompras.append(item)


class Administrador(Perfil):
    def __init__(self,username, tipo = "Admin"):
        super().__init__(username, tipo)
        self.tipo = "Admin"
    
    def printUserData(self,username):
        print(f'Data on {username.username}: Type= {username.tipo}')
        print("En carrito de compras:",username.carritoDCompras)

        


class Reporter(Perfil):
    def __init__(self,username,tipo="Reporter"):
        super().__init__(username, tipo)
        self.tipo = "Reporter"
    
    def CheckCarrito(self,userVar):
        print("En carrito de compras:",userVar.carritoDCompras)


user1 = Perfil("pepito")
user2 = Administrador("admin")
user3 = Reporter("reportero")

user1.AgregarACarrito("leche")
user1.AgregarACarrito("pan")
user1.AgregarACarrito("queso")

user2.printUserData(user1)
user3.CheckCarrito(user1)

# No me gusta como quedo.. no entendi muy bien el ejercicio...

