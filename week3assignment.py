from random import randrange
class Pet(object):
    Boredom_decrement = 4
    Hunger_decrement = 6
    Boredom_threshold = 5
    Hunger_threshold = 10
    Sounds = ['"Grrr..."','"moeww"]

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.Hunger = randrange(self.Hunger_threshold)
        self.Boredom = randrange(self.Boredom_threshold)
        self.Sounds = self.Sounds[:]

    def clock_tick(self):
        self.Boredom += 1
        self.Hunger += 1

    def mood(self):
        if self.Hunger <= self.Hunger_threshold and self.Boredom <= self.Boredom_threshold:
            return "happy"
        elif self.Hunger > self.Hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "\nI'm" + self.name + ". " + "\n feel" + self.mood() + "."

    def hi(self):
        print("\nI am a", self.animal_type, "named", self.name, ".", "I feel", self.mood(), " now.\n")
        self.clock_tick()
        print(self.Sounds[randrange(len(self.Sounds))])

    def teach(self, word):
        self.Sounds.append(word)
        self.clock_tick()

    def feed(self):
        print('thankyou!')
        meal = randrange(0, self.Hunger_threshold)
        self.Hunger += meal
        if self.Hunger < 0:
            self.Hunger = 0
            print('im still hungry')
        elif self.Hunger > self.Hunger_threshold:
            self.Hunger = self.Hunger_threshold
            print("im full")
        self.clock_tick()

    def play(self):
        print("im so so happy!")
        fun = randrange(0, self.Boredom_threshold)
        self.Boredom += fun
        if self.Boredom < 0:
            self.Boredom = 0
            print("im bored")
        elif self.Boredom >= self.Boredom_threshold:
            self.Boredom = self.Boredom_threshold
            print("im really happy")
        self.clock_tick()


def main():
    pet_name = input("what do you want to name your pet?")
    pet_type = input("what type of animal is your pet?")
    my_pet = Pet(pet_name, pet_type)
    input("\nHello!I am " +
          my_pet.name +
          "\nand I am new here!" +
          "\npress enter to start."
          )
    choice = None
    while choice != 0:
        print(
            """*** Interaction with pet  ***
         1-Feed your pet
         2-Greet your pet
         3-Teach your pet
         4-Play with your  pet
         0-Quit
         """
        )
        choice = input("choice:")
        if choice == '0':
            print("bye!")
        elif choice == '1':
            my_pet.feed()
        elif choice == '2':
            my_pet.hi()
        elif choice == '3':
            new_word = input("enter word you want to teach")
            my_pet.teach()
        elif choice == "4":
            my_pet.play()
        else:
            print('sorry,invalid choice')


main()
