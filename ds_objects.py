color=["black","green","pink","yelloow","white"]     #enumerate it show index value
for j in enumerate(color):                            # class 
 print(j)

cities=["Chittoor","yadamari","BAngloree","kolar"]   #ds objest
for i in cities:
 print(i)

color=["black","green","pink","yelloow","white"]       #memory allocation
jyo=color[1:2] 
print(jyo)  

color=['black','green','pink','yelloow','white']
subcolor=color[1:2]
print(subcolor)

a="JYOTHISWAR"   #object
print(a[:6])    #starting and ending index
print(a[0:6])   #starting and ending index
print(a[::2])    #starting and ending index and step

col=["jyothi","Shiva","hari","Ramesh","nandu","Lalitha","nadhiya"]
print(col[:])
print(col[::2])
print(col[2:])
print(col[2:4])

color=['black','green','pink','yelloow','white']
print(color[:])
print(color[::2])
print(color[2:])
print(color[2:4])



#using methods perform methods

india=["ap","ts","ks","jk"]
j=india.count("ap")
print(j)
k=india.append("AP")
print(india)



india.append        #adding the delemrmntss end of the list
india.clear         #remove all the elements in the list
india.index         #use to find the index of the element
india.copy()        #it copy shalow copy   #deepcopy ?
india.count         #it counts no of elements present in a list
india.extend     
india.index
india.insert
india.pop
india.remove
india.reverse
india.sort