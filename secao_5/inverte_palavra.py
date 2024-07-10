frase = "onde fica o café mais próximo".split(' ')
palavra_invertida = ''
for palavra in frase:
    palavra_invertida += palavra[::-1] + ' '

print(palavra_invertida)



palavra_invertida = palavra_invertida.split(' ')
palavra_invertida2 = ''
for palavra in palavra_invertida:
    palavra_invertida2 += palavra[::-1] + ' '

print(palavra_invertida2)
