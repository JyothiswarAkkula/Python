class studentMarks:
    def __inti__(self,name,c,numpy,java,python):
        self.name=name
        self.c=c
        self.numpy=numpy
        self.java=java
        self.python=python

    def cal_Avg_marks(self):
        total_marks=self.c+self.numpy+self.java+self.python
        Avg_marks=total_marks%4
        return Avg_marks
    
student1=studentMarks("jyothi",30,40,45,33)   
student2=studentMarks("omkar",33,34,45,43)
student3=studentMarks("Gowri",45,44,34,42)
student4=studentMarks("Sandeep",33,32,24,45)
student5=studentMarks("Afreen",44,24,43,43)
student6=studentMarks("teju",32,23,43,44)

print(student1)
        