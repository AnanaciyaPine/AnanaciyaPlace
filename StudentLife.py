import random
class Student:
    def __init__(self, name):
        self.name = name
        self.mood = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("'Time to study... ':(")
        self.progress += 0.12
        self.mood -= 3
    def to_sleep(self):
        print("'I will go to sleep.' *secretly "
              "plays videogames on his"
              " phone* 's-sssh'")
        self.mood += 3
    def to_chill(self):
        print("I need to rest :D")
        self.mood += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Rip me, I think I will be homeless now")
            self.alive = False
        elif self.mood <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Wow! I've finished colledge!")
            self.alive = False
    def end_of_the_day(self):
        print(f"Mood = {self.mood}")
        print(f"Progress = {round(self.progress, 2)}")
    def life(self, day):
        day = "Day " +str(day) + " of " + self.name+"'s life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_the_day()
        self.is_alive()


Tolik = Student(name="Tolik")
for day in range (365):
    if Tolik.alive == False:
        break
    Tolik.life(day)


