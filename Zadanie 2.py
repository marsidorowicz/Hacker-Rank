# LAB1

a=b=c=10
print(a,b,c)
print(id(a), id(b), id(c))
a=20
print(a,b,c)
print(id(a), id(b), id(c))

a=b=c=[1,2,3]
print(a,b,c)
print(id(a), id(b), id(c))
a.append(4)
print(a,b,c)
print(id(a), id(b), id(c)) # Nie zgadza się (identyfikator zmiennej a powinien być teraz taki sam jak b i c, dodatkowo zmieni się jednocześnie lista w zmiennych b i c)
print()
x=10
y=10
print((x,y))
print(id(x), id(y))
print()
x=10
y=10+1-1
print((x,y))
print(id(x), id(y))
print()
x=10
y=10+1234567890-1234567890
print((x,y))
print(id(x), id(y))