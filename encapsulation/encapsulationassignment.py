class Patient:

    def setId(self, Id):
        self.Id = Id

    def getId(self):
        return self.Id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setssn(self, ssn):
        self.ssn = ssn

    def getssn(self):
        return self.ssn
        
x = Patient()
x.setId("123")
x.setname("John")
x.setssn("56789")
print(x.getId())
print(x.getname())
print(x.getssn())

