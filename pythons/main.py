# print('да')
# print("Hello")

# class Human:
#     amount_of_human = 0
#     def __str__(self):
#         return print(f"Im {self.__name} and my height is {self.__height}")
#     def __init__(self, name = None,height = 160):
#         self.__height = height
#         self.__name = name
#         print("Hi","I am alive")
#         Human.amount_of_human+=1
#     def __int__(self):
#         return self.__height
#     def printer(self):
#         print(f"Im {self.__name} and my height is {self.__height}")
#     def grow(self, height=1):
#         self.__height += height
#     def __del__(self):
#         print("oh no")
        


# nick = Human("Nick",170)
# nick2 = Human("Nuke")
# alice = Human("Alice",180)
# nick.__height = 'hello world'
# # nick.height = 170
# # print(nick.height)
# # print(nick2.height)
# # print(alice.height)
# nick.printer()
# nick2.printer()
# alice.printer()
# print("humans: ",Human.amount_of_human)
# nick.grow()
# print(nick)
# print(int(nick))
# del nick


import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3
    
    def to_chill(self):
        print("Time to chill")
        self.gladness +=5
        self.progress -= 0.1


    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive=False
        elif self.gladness <=0:
            print("Depresion")
            self.alive=False
        elif self.progress > 5:
            print("Pass ")
            self.alive=False


    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Gladness - {self.progress}")


    def live(self, day):
        day = "Day " + day + "of " + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube ==1:
            self.to_study
        elif live_cube ==2:
            self.to_sleep
        elif live_cube ==3:
            self.to_chill
        self.end_of_day()
        self.is_alive()

nick = Student("Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)

        












