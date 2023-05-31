try: #naço pode ficar sozinho
    print(111)
    #8/0
except ZeroDivisionError:#pode ter qntos excepts quiser
    print('dividiu por zero') 
else:
    print('não deu erro')
    #executa se não houver erro
finally: #sempre será executado, mesmo que tenha erro antes
    print(222)