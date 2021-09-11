lista = """5
1
2
3
4
5"""
lista = lista.split('\n')
soma = 0
for numero in lista:
	soma += int(numero)
media = soma/len(lista)
print(media)
