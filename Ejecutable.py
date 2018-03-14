from Compilador import *

with open("Ecuaciones.txt",'rU') as f:
    content = f.readlines()

cal = Compilador()

for i in content:
    content = i.strip('\n').split(' ')
    print(cal.posOrden(content))
