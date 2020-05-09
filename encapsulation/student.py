# class Student:
#     def __init__(self):
#         self.__id = 123
#         self.__name = "John"

#     def display(self):
#         print(self.__id)
#         print(self.__name)

# s = Student()
# #s.display()
# print(s._Student__id)

#Encapsulation

class Student:

    def setId(self, Id):
        self.id = Id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

s = Student()
s.setId(123)
s.setName("John")
print(s.getId())
print(s.getName())