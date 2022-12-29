#formatação de strings com método format
a = 'A'
b = 'B'
c = 1.1
formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
string = 'a={0} a={0} a={0} b={1} c={nome3:.2f}'
formato2 = string.format(a, b, nome3=c)

print(formato,'\n',formato2)