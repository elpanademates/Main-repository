
class ClassA:
    def method1(self):
        print("Method from A")

class ClassB:
    def method2(self):
        print("Method from B")

class ClassC(ClassA, ClassB):
    def method3(self):
        print("Method from C")


instance_c = ClassC()
def llamar():
    instance_c.method1()
    instance_c.method2()
    instance_c.method3()

llamar()
