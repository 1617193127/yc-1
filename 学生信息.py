
#！/ usr / bin / python
# -  *  - 编码：UTF-8  -  *  -

class student:
   stuCount =  0
 
   def  __init__(self, name, stu_no, stu_class, male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1

    def canstudy(self):
       打印 “学生可以学习”
       
    def  getStuCount(self):
       打印 Student.stuCout
