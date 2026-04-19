from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import json

restaurante_bk = Restaurante('bk', 'hamburgues')
refrigerante = Bebida('Coca Cola', 10.0,'grande')
refrigerante.aplicar_desconto()
australiano_hamburguer = Prato('Australiano',70.0,'Bom demaize')
australiano_hamburguer.aplicar_desconto()
restaurante_bk.adicionar_no_cardapio(refrigerante)
restaurante_bk.adicionar_no_cardapio(australiano_hamburguer)

def menu():
    while True:
        print("\n=== SISTEMA DE RESTAURANTE ===")
        print("1.Ver Cardapio")
        print('2.Avaliar Restaurante')
        print("3.Sair")

        opcao = input('Escolha: ')

        if opcao == '1':
            restaurante_bk.exibir_cardapio
        elif opcao == '2':
            nome = input('Nome do cliente: ')
            nota = float(input('Avalie o restaurante de 1 a 5: '))
            restaurante_bk.receber_avaliacao(nome, nota)
            print('Avaliação registrada')
            print('Media atual', restaurante_bk.media_avaliacoes)
        elif opcao == '3':
            print('Saindo...')
            break

def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            for dado in dados.get("restaurantes", []):
                restaurante = Restaurante(dado["nome", dado["categoria"]])
                for avaliacao in dado.get("avaliaçoes", []):
                    restaurante.receber_avaliacao(avaliacao["Cliente"], avaliacao["nota"])
    except FileNotFoundError:
        pass

def salvar_dados():
    dados = {"restaurante": []}
    for restaurante in restaurante.restaurantes:
        dados["restaurante"].append({
            "nome": restaurante._nome,
            "categoria": restaurante._categoria,
            "avaliacoes": [
                {"cliente": av._cliente, "nota": av_nota}
                for av in restaurante._avaliacao
            ]
        })

    with open(dados.json, "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def main():
    carregar_dados()
    menu()

if __name__ == '__main__':
    main()
