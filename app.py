#Area do cliente
class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carros_interesse = []
        self.carros_carrinho = []

    def adicionar_carro_interesse(self, carro):
        self.carros_interesse.append(carro)
        print("Carro adicionado aos interesses!")

    def adicionar_ao_carrinho(self, carro):
        self.carros_carrinho.append(carro)
        print("Carro adicionado ao carrinho!")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

def main():
    # Carros de exemplo
    car1 = Carro("Toyota", "Corolla")
    car2 = Carro("Honda", "Civic")
    car3 = Carro("Tesla", "Model S")

    # exemplo de cliente enquanto n ha base de dados
    cliente = Cliente("João", "joao@email.com", "senha123")

    # adicionar carros ao cliente de exemplo
    cliente.adicionar_carro_interesse(car1)
    cliente.adicionar_carro_interesse(car2)
    cliente.adicionar_carro_interesse(car3)

    # Adicionar a parte do carrinho
    cliente.adicionar_ao_carrinho(car1)
    cliente.adicionar_ao_carrinho(car3)

    # Mostrando os carros q interessam ao utilizador
    print(f"Carros de interesse do cliente {cliente.nome}:")
    for carro in cliente.carros_interesse:
        print(f"{carro.marca} {carro.modelo}")

    # carros no carrinho
    print(f"Carros no carrinho do cliente {cliente.nome}:")
    for carro in cliente.carros_carrinho:
        print(f"{carro.marca} {carro.modelo}")

if __name__ == "__main__":
    main()
