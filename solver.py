import kociemba 



#u = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

#print(u)

z = kociemba.solve('ULBUUUULDBBRDRDLDRRULRFBDLFLFURDFBDFBFFULFLBFDBRLBRDRU')
print(z)

for i in z:
    if i == 'D':
        clockwise()
    