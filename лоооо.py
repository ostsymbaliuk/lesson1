class a:
    def __init__(self):
        self.x = 10
    def met1(self):
        return self.x

class b:
    def __init__(self):
        self.y = 20
    def met2(self):
        return self.y

class c(a, b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
        self.z = 30
    def met3(self):
        return self.z

ob = c()
print(ob.met1())
print(ob.met2())
print(ob.met3())