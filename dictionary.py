d1={'AP':'Amravati',"Ap":'Guntur','MH':'Mumbai',2:4,8:64,2:16}
print(d1)
print(type(d1))
print(d1.keys())
print(d1.values())

#Dicitionary Methods
#1.get()
print(d1.get('Ap'))

#2.popitem()
print(d1.popitem())
print(d1)

#setdefault
#d2="Name","Pujitha"
#d1.setdefault(d2)
print(d1)
print(d1.setdefault(9,"hello"))
print(d1)

#pop()
d5={"India":"New Delhi","USA":"Newyork",'KA':'Bangalore',2:8}
print(d5)
print(d5.pop(2))
print(d5)

#copy()
d6=d5.copy()
print(d6)

#len()
print(len(d5))

for(i=0;i<5;i++){
      logic