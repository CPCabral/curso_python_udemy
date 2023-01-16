import os
lista = []

while True:
    acao = input(f'O que deseja fazer?\n[A]dicionar item à lista de compras \n[E]xcluir item da lista de compras \n[L]istar itens da lista de compras \n[S]air\n').lower()
    permissao = 'ales'

    if acao not in permissao:
        print(f'\nEntrada inválida!\n')
        continue
    elif len(acao) != 1:
        print(f'\nEntrada inválida!\n')
        continue

    #adicionar
    if acao == 'a':
        os.system('cls')
        while True:
            item = input(f'Item a ser adicionado ([C]ancelar): ').lower()
            if item == 'c':
                os.system('cls')
                break
            lista.append(item)
    
    elif acao == 'e':#excluir
        
        if len(lista) == 0:
            print(f'\nAinda não há itens na lista de compras!\n')
            continue
        else:
            item = input(f'\nNome ou índice do item a ser excluído: ')
            if item in lista:
                lista.remove(item)
            elif item.isdigit() and int(item) < (len(lista)):
                del lista[int(item)]
            else:
                print(f'\nItem não consta na lista!\n')
       
    elif acao == 'l':#listar
        os.system('cls')
        for indice,item_compra in enumerate(lista):
            print(indice,item_compra)
    
    elif acao == 's':
        break
