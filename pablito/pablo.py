def lucas(position):
    luc=0
    if position>3:
        luc = lucas(position-1) + lucas(position-2)
        return luc
    else:
        if position==1:
            luc =2
            return luc
        elif position==2:
            luc= 1
            return luc
        elif position==3:
            luc= 3
            return luc

        
def limites(a,b):
    count = 0
    for i in range(1,b):
        lc = lucas(i)
        value = ((a<=lc)and(lc<=b))
        if value:
            count +=1
    print(count)

a= int(input("ingrese limite inferior: "))
b = int(input("ingrese limite superior: "))   
limites(a,b)
