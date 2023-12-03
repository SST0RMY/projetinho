
class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carros_interesse = []
        self.carros_carrinho = []
        self.notificacoes = []

    def adicionar_carro_interesse(self, carro):
        self.carros_interesse.append(carro)
        print("Carro adicionado aos interesses!")

    def adicionar_ao_carrinho(self, carro):
        self.carros_carrinho.append(carro)
        print("Carro adicionado ao carrinho!")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso!")

    def alterar_email(self, novo_email):
        self.email = novo_email
        print("Email alterado com sucesso!")

    def receber_oferta(self, oferta):
        self.notificacoes.append(oferta)
        print("Oferta recebida!")

    def marcar_test_drive(self, carro):
        print(f"Test-drive marcado para o carro {carro.marca} {carro.modelo}!")

    def reservar_veiculo(self, carro):
        print(f"Veículo {carro.marca} {carro.modelo} reservado!")

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
    print ("Interesses:")
    cliente.adicionar_carro_interesse(car1)
    cliente.adicionar_carro_interesse(car2)
    cliente.adicionar_carro_interesse(car3)
    print("\n")

    # Adicionar a parte do carrinho
    print ("Carrinho")
    cliente.adicionar_ao_carrinho(car1)
    cliente.adicionar_ao_carrinho(car3)
    print("\n")

    # Mostrando os carros q interessam ao utilizador
    print("\n")
    print(f"Carros de interesse do cliente {cliente.nome}:")
    for carro in cliente.carros_interesse:
        print(f"{carro.marca} {carro.modelo}")

    # carros no carrinho
    print("\n")
    print(f"\nCarros no carrinho do cliente {cliente.nome}:")
    for carro in cliente.carros_carrinho:
        print(f"{carro.marca} {carro.modelo}")

    # Exemplo de uso dos novos métodos
    cliente.alterar_senha("novaSenha456")
    cliente.alterar_email("novo@email.com")

    oferta = "Oferta especial para você!"
    cliente.receber_oferta(oferta)

    car4 = Carro("BMW", "Série 3")
    cliente.marcar_test_drive(car4)

    cliente.reservar_veiculo(car2)

if __name__ == "__main__":
    main()
