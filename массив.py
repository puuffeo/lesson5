l  =[] #пустой список 
l = list() #пустой список 

l.append(5) #добавление в конец списка 
#print(l)
l.append(55)
l.append(5)
l.append(35)

#добавить эл по индексу 
l.insert(5,67)
#print(l)

d = [6,7]
l.extend(d) #добавления множества в конец 
#print(l)


#получить эл по индексу 
c = l[5]
#print(c)

#количество эл с заданными значением
i = l.count(5)
#print(i)

#показать индекс эл с заданным значением 
#g = l.index(67)
#print(g)


#del l[4]
#print(l)

#l.pop() #удаяем полслед эл не сохраняя
#r = l.pop()
#print(r) 
#print(l)
m=max(l)
#print(m)
minm=min(l)
#print(minm)

s= sum(l) #сумма 
#print(s)

le=len(l)
#print(le)

h= sorted(l)
#print(h)

h.reverse() 
#print(h)

h.remove(5)
#print(h)

#кортежи 
t = (20,30)
cars = ["kia","bmw","VV"]
for car in cars:
		if car== "bmw":
			print("ты крут")
		else:
			print("ты не курут")





