# try, except, else e finally

try: #try não pode vir sozinho
    a = 18
    #b = 0
    print('linha 1')
    c = a / b # silenciar um erro
    print('linha 2')
except:
    print('dividiu por zero') #simulando que está tratando um erro, percisa informar qual erro está tratando

print('continuar')
# pode silenciar outros erros 



try: 
    a = 18
    b = 0
    print('linha 1')
    print(b[9])
    c = a / b 
    print('linha 2')
except ZeroDivisionError:
    print('dividiu por zero') 
except NameError:
    print('variável não está definida') 
except (TypeError, IndexError) as error: #o ideal pe dividir em 2
    print('TypeError, IndexError') 
    print('MSG',error) 
    print('name error',error.__class__.__name__) 
except Exception: #trata qualquer erro
    print('ERRO DESCONHECIDO') 

print('continuar')
# pode silenciar outros erros 

