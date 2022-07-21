# Operadores aritméticos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2 #potência
di = n1 // n2 #divisão inteira
r = n1 % n2 # resto

print(a)
print(s)
print(m)
print(d)
print(p)
print(di)
print(r)

print('=' * 20)
print('A soma vale {}' .format(n1 + n2))

nome = 'Gustavo'
print('Prazer em te conhecer {:20}!' .format(nome))
print('Prazer em te conhecer {:>20}!' .format(nome))
print('Prazer em te conhecer {:<20}!' .format(nome))
print('Prazer em te conhecer {:^20}!' .format(nome))
print('Prazer em te conhecer {:= ^20}!' .format(nome))

print('Olá, meu nome é' .format(nome), end = ' ') # end evita a quebra de linha
print('Ok?') 

print('Olá,\n turobom?')