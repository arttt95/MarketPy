from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import (formata_float_str_moeda,
                          formata_str_float_moeda)

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('===========================================')
    print('===========================================')
    print('=============== Bem-vindo(a) ==============')
    print('============ Mercadinho do Jair ===========')
    print('==========================================')
    print('=========== SELECIONE UMA OPÇÃO ===========')
    print('===========================================')
    print('===========================================')
    print('==       [1] - Cadastrar Produto         ==')
    print('==        [2] - Listar Produtos          ==')
    print('==        [3] - Comprar Produto          ==')
    print('==      [4] - Visualizar Carrinho        ==')
    print('==         [5] - Fechar Pedido           ==')
    print('==        [6] - Sair do Sistema          ==')
    print('===========================================')
    print('===========================================')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        compra_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_carrinho()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Você inserir uma opção inválida.')
        print('Por favor, insira um número de [1] a [7].')
        sleep(1)
        menu()


def cadastrar_produto() -> None:

    print('=======================')
    print('= Cadastro de Produto =')
    print('=======================')

    nome: str = input('Informe o nome do Produto:\n')
    preco: float = float(input('Informe o Preço do Produto:\n'))

    produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi inserido com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('========================')
        print('= Listagem de Produtos =')
        print('========================')
        for produto in produtos:
            print(produto)
            print('========================')
            sleep(1)

    else:
        print('Ainda não existem produtos cadastrados.')
        print('Para cadastrar um produto acesse o menu e\n'
              'selecione a opção [1].')
        sleep(2)
    menu()


def compra_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adcionar ao carrinho:')
        print('============================================================')
        print('==================  Produtos disponíveis  ==================')
        print('============================================================')
        for produto in produtos:
            print(produto)
            print('==========================')
            sleep(1)

        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:

            print('Informe a quantidade que deseja deste produto:\n')
            qtd_adc: int = int(input())

            if len(carrinho) > 0:
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + qtd_adc
                        print(f'O produto {produto} agora possui {quant + qtd_adc} '
                              f'unidades no carrinho.')
                        tem_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:

                    prod = {produto: qtd_adc}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            else:
                item = {produto: qtd_adc}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f"O código '[{codigo}]' informado não corresponde a nenhum produto.")
            print('Para cadastrar um produto acesse o menu e\n'
                  'selecione a opção [1].')
            print('Você será redirecionado ao menu principal.')
            sleep(3)
            menu()
    else:
        print('Ainda não existem produtos cadastrados no sistema.')
        print('Para cadastrar um produto acesse o menu e\n'
              'selecione a opção [1].')
        print('Você será redirecionado ao menu principal.')
        sleep(3)
        menu()


def visualizar_carrinho() -> None:
    if len(produtos) > 0:
        print('============================================================')
        print('==================  Produtos do Carrinho  ==================')
        print('============================================================')
        for item in carrinho:
            for dados in item.items():
                print(f'Produto: {dados[0]}')
                print(f'Quantidade: {dados[1]}')
                print('===============================')
                sleep(1)
    else:
        print('Ainda não existem produtos cadastrados no sistema.')
        print('Para cadastrar um produto acesse o menu e\n'
              'selecione a opção [1].')
        print('Você será redirecionado ao menu principal.')
        sleep(3)
        menu()
    sleep(2)
    menu()


def fechar_carrinho() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('===================================')
        print('==     Produtos no carrinho      ==')
        print('===================================')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('===================================')
        print(f'A sua fatura é {formata_float_str_moeda(valor_total)}.')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho')
        print('Você será redirecionado ao menu novamente.')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
