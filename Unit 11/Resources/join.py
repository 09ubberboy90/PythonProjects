from random import randint
def join(lsfirst,lssec):
    new = []
    for num, el in enumerate(lsfirst):
        new.append([el,lssec[num]])
    return new
def random(number):
    ls = []
    ls_2 = []
    for i in range(number):
        ls.append(randint(2,10))
        ls_2.append(randint(2,10))
    print(join(ls, ls_2))
    print(split(join(ls, ls_2)))
def split(listinput):
    ls = []
    ls_2 =[] 
    for el in listinput:
        ls.append(el[0])
        ls_2.append(el[1])
    return ls,ls_2
#random(5)
