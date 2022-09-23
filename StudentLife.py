import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.mood = 50
        self.respectByPeople = 0
        self.alive = True
    def to_eat(self):
        print("'Ok, time to eat my food... Am nam nam'")
        self.respectByPeople += 0.12
        self.mood += 2
    def to_sleep(self):
        print("'I will go to bed now' *yawns* ")
        self.mood += 3
        self.respectByPeople += 0.12
    def to_destroy(self):
        print("Hehe... Time to destroy the house while humans are not home! :D")
        self.mood += 6
        self.respectByPeople -= 0.5
    def is_alive(self):
        if self.respectByPeople < -0.5:
            print("Oh so they've kicked me out of their home. Huh?")
            self.alive = False
        elif self.mood <= 0:
            print("I'm depressed. Depressed cat = bad. I've escaped out of this bad house! Grrr")
            self.alive = False
        elif self.respectByPeople > 5:
            print("Wow! I'm an adult cat now!")
            self.alive = False
    def end_of_the_day(self):
        print(f"Mood = {self.mood}")
        print(f"Respect by people = {round(self.respectByPeople, 2)}")
    def life(self, day):
        day = "Day " +str(day) + " of " + self.name+"'s life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_destroy()
        self.end_of_the_day()
        self.is_alive()


Murchelo = Cat(name="Murrrrchelo")
for day in range (365):
    if Murchelo.alive == False:
        break
    Murchelo.life(day)


