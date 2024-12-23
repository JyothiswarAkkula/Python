

class join_school1:
    def __init__(self,name,Fname,age,city):
        self.name=name
        self.age=age
        self.city=city
        self.Fname=Fname
    def __str__(self):
        return F"my name is {self.name} and my Father name is {self.Fname} i am {self.age} and i am from {self.city}"
j=join_school1("LAvanya","Ramesh",25,"chittoor")
print(j)