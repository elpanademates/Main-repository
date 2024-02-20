class Person:
    def speak(self):
        print("Hello i'm a person.")
    
class Boy(Person):
    def speak_boy(self):
        print("Hello i'm a boy.")

boy = Boy()

boy.speak()
boy.speak_boy()