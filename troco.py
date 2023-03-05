import os


compra = []
produtos = []



def menu():
    list = ['cadastrar produto', 'troco']
    print('================')
    for index, v in enumerate(list):
        print(f'{index + 1}ª: {v}')
    print('================')

def cadastrar():
    try:
        print('Nome do produto')
        nome = str(input('>> ')).upper()

        print('Valor do produto')
        valor_produto = float(input('>> '))
        produto = {}

        produto[nome] = valor_produto

        produtos.append(produto)
    except:
        print('Erro no cadastro')


def troco():
    
    valor = 0
    try:
        while True:
            print('Nome do produto: ')
            prod = str(input('>> ')).upper()

            print('Quantidade: ')
            quant = int(input('>> '))
            
            
            
            for v in range(len(produtos)):
                if prod in produtos[v]:
                    valor = valor + produtos[v][prod] * quant
                    cp = []
                    cp.append(prod)
                    cp.append(produtos[v][prod])
                    cp.append(quant)
                    compra.append(cp)
            


            print('Digite N para somar mais produtos ou X para fechar troco')
            res = str(input('>> ')).upper()

            if res == 'X':
                break
    except:
        print('Erro no troco')

    print('Valor recebido: ')       
    valor_recebido = float(input('>> '))

    troco = valor_recebido - valor

    for id, v in enumerate(compra):
        print(f'{v[0]} -- R${v[1]} -- {v[2]}X')
    

    print(f' seu troco {troco}')
    
    

while True:
    menu()
    print('Qual sua opção? ')
    op = int(input('>> '))
    os.system('cls')

    if op == 1:
        cadastrar()
        input('>> ')
        os.system('cls')

    elif op == 2:
        troco()
        input('>> ')
        os.system('cls')