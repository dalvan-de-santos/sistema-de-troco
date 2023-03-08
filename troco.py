import os

import pymysql

#criando conexão com banco de dados
conexao = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='produtos')

cursor = conexao.cursor()

#selecionando tabela
cursor.execute("SELECT * FROM produto")


compra = []
produtos = []

#adicionando dados da tabela em uma lista
for v in cursor:
    produtos.append(v)



#função para calcular troco
def troco():
    
    valor = 0
    try:
        while True:
            print('Nome do produto: ')
            prod = str(input('>> ')).upper()

            print('Quantidade: ')
            quant = int(input('>> '))
            
            
            
            for v in range(len(produtos)):
                if prod == produtos[v][1]:
                    valor = valor + produtos[v][2] * quant
                    cp = []
                    cp.append(prod)
                    cp.append(produtos[v][2])
                    cp.append(quant)
                    compra.append(cp)
            


            print('Digite N para somar mais produtos ou X para fechar troco')
            res = str(input('>> ')).upper()

            if res == 'X':
                break
    except:
        print('Erro no troco')
    
    #gerando recibo da compra
    print(f'Valor da compra R${valor}')
    print('Valor recebido: ')       
    valor_recebido = float(input('>> '))

    troco = valor_recebido - valor

    print('********Recibo*********')
    for id, v in enumerate(compra):
        print(f'{v[0]} -- R${v[1]} -- {v[2]}X')
    
    print(f'Total da compra R${valor}')
    print(f'Total recebido R${valor_recebido}')
    print(f'Troco R${troco:.2f}')
    print('************************')
    

while True:
    troco()
    input('>> ')
    os.system('cls')