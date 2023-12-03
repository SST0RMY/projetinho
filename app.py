import datetime
import hashlib


class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = hashlib.md5(senha.enconde())
        self.carros_interesse = []
        self.carros_carrinho = []
        self.notificacoes = []
        self.nif = None
        self.tipo_veiculo = None
        self.opcoes_pagamento = {
            'paypal': False,
            'visa': False,
            'prestacoes': False,
            'morada_faturacao': None,
            'detalhes_compra': None,
            'pedir_entrega': False
        }
        self.carros_recentes = []
        self.compras_realizadas = []
        self.dia_reserva = None

    def adicionar_carro_interesse(self, carro):
        self.carros_interesse.append(carro)
        print("Carro adicionado aos interesses!")

    def adicionar_ao_carrinho(self, carro):
        self.carros_carrinho.append(carro)
        print("Carro adicionado ao carrinho!")

    def alterar_senha(self, nova_senha):
        self.senha = hashlib.md5(nova_senha.encode())
        print("Senha alterada com sucesso!")

    def alterar_email(self, novo_email):
        self.email = novo_email
        print("Email alterado com sucesso!")

    def reservar_viatura(self, dia_reserva, carro):
        self.dia_reserva = dia_reserva
        self.carro_reserva = carro
        print(f"Carro {self.carro_reserva} reservado para o dia {self.dia_reserva} com sucesso!")

    def receber_oferta(self, oferta):
        self.notificacoes.append(oferta)
        print("Oferta recebida!")

    def marcar_test_drive(self, carro):
        print(f"Test-drive marcado para o carro {carro.marca} {carro.modelo}!")

    def reservar_veiculo(self, carro):
        print(f"Veículo {carro.marca} {carro.modelo} reservado!")

    def adicionar_nif(self, nif):
        self.nif = nif
        print("NIF adicionado com sucesso!")

    def escolher_tipo_veiculo(self, tipo):
        self.tipo_veiculo = tipo
        print(f"Tipo de veículo escolhido: {tipo}")

    def configurar_opcoes_pagamento(self, opcoes):
        for opcao, valor in opcoes.items():
            if opcao in self.opcoes_pagamento:
                self.opcoes_pagamento[opcao] = valor
        print("Opções de pagamento configuradas com sucesso!")

    def adicionar_detalhes_compra(self, detalhes):
        self.opcoes_pagamento['detalhes_compra'] = detalhes
        print("Detalhes para a compra adicionados com sucesso!")

    def escolher_entrega(self):
        self.opcoes_pagamento['pedir_entrega'] = True
        print("Opção de entrega selecionada!")

    def ver_carros_recentes(self):
        print("Carros/Motos Recém-Visualizados:")
        for carro in self.carros_recentes:
            print(f"{carro.marca} {carro.modelo}")

    def ver_compras_realizadas(self):
        print("Compras Realizadas:")
        for compra in self.compras_realizadas:
            print(f"{compra.marca} {compra.modelo}")


# Carro permanece igual ao código anterior
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


def main():
    # Carros de exemplo
    car1 = Carro("Toyota", "Corolla")
    car2 = Carro("Honda", "Civic")
    car3 = Carro("Tesla", "Model S")

    # exemplo de cliente enquanto não há base de dados
    cliente = Cliente("João", "joao@email.com", "senha123")

    # adicionar carros ao cliente de exemplo
    cliente.adicionar_carro_interesse(car1)
    cliente.adicionar_carro_interesse(car2)
    cliente.adicionar_carro_interesse(car3)

    # Adicionar a parte do carrinho
    cliente.adicionar_ao_carrinho(car1)
    cliente.adicionar_ao_carrinho(car3)

    # Mostrando os carros que interessam ao utilizador
    print("\n")
    print(f"Carros de interesse do cliente {cliente.nome}:")
    for carro in cliente.carros_interesse:
        print(f"{carro.marca} {carro.modelo}")

    # Carros no carrinho
    print("\n")
    print(f"\nCarros no carrinho do cliente {cliente.nome}:")
    for carro in cliente.carros_carrinho:
        print(f"{carro.marca} {carro.modelo}")

    # Reserva do veiculo
    print("Qual o dia para a reserva e o veiculo?")
    dia_reserva = datetime.date(2023, 3, 12)
    cliente.reservar_viatura(dia_reserva, car1)

    # Exemplo de uso dos novos métodos
    cliente.alterar_senha("novaSenha456")
    cliente.alterar_email("novo@email.com")

    oferta = "Oferta especial para você!"
    cliente.receber_oferta(oferta)

    car4 = Carro("BMW", "Série 3")
    cliente.marcar_test_drive(car4)

    cliente.reservar_veiculo(car2)

    # Adicionando mais funcionalidades conforme necessário


if __name__ == "__main__":
    main()
