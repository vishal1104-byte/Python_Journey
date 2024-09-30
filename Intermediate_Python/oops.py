# class car:
#     def start(self):
#         print(f"The {self.color} {self.model} is start")

# car1 = car()
# car1.model = "Toyota"
# car1.color = "Red"

# car2 = car()
# car2.model = "Thar"
# car2.color = "Black"

# car1.start()
# car2.start()

                                    #      POLYMORPHISM   --> This is the functional method of oops 

# class Bird:
#     def fly(self):
#         print('Birs is flying')

# class Airplane:
#     def fly(self):
#         print('Airplane is flying')

# bird = Bird()
# airplane = Airplane()

# bird.fly()
# airplane.fly()



# class cricket:
#     def batsmen(self):
#         print("Score as much as you can ")
#     def bowler(self):
#         print("Take Wicket as much as you can")

# check = cricket()
# check.batsmen()
# check.bowler()


#This is Run time Polymorphism we can also say this as an  method overriding ----> here child class redefines the methods of parent class 

# Class Creation 

# Parent Class
# class Animal:
#     def make_sound(self):
#         print("Animals Makes Sounds")

# # Child class 
# class Dog(Animal):
#     def make_sound(self):
#         print("Dogs Barks !")

# # Another child class 
# class cat(Animal):
#     def make_sound(self):
#         print("Cats Meow !")

# # creating the objects 
# animal = Animal()
# dog = Dog()
# cat = cat()

# animal.make_sound()
# dog.make_sound()
# cat.make_sound()    # Here we use the same methods or functions but it give other output just because it override the comment   

# class calculator:
#     def add(self,a,b,c):
#         print("The addition of the Number is",a+b+c)


# calc = calculator()
# calc.add(8,9,7)


# class Mediaplayer:
#     def play(self):
#         print("Play Music")

# class audio(Mediaplayer):
#     def play(self):
#         print("Play audio ")

# class video(Mediaplayer):
#     def play(self):
#         print("Play Video ")

# media = Mediaplayer()
# aud = audio()
# vid = video()

# media.play()
# aud.play()
# vid.play()



                                        # INHERITANCE ---> ek class ki properties aur methods ko doosre class me reuse karne ki facility deti hai 

# This is single level inheritance where child use the properties of single parent
# class parent:
#     def show(self):
#         print('This is Parent class ')
# class child(parent):
#     def display(self):
#         print('This is child class ')

# p = parent()
# c = child()
# p.show()
# c.display()
# c.show()

# This is Multiple inheritance here child can use the properties of both parents .

# class father:
#     def show_father(self):
#         print("This is Father class ")

# class mother:
#     def show_mother(self):
#         print("This is Mother class")

# class child(mother,father):
#     def show_child(self):
#         print('I am the child class ')

# child = child()
# child.show_child()
# child.show_father()
# child.show_mother() 


# This is Multilevel inheritance where child get the properties of parent and parent the get the properties of there parents 

# class grandparents:
#     def show_grandparents(self):
#         print("This is grandparents")
# class parents(grandparents):
#     def show_parents(self):
#         print("This is parents")

# class child(parents):
#     def show_child(self):
#         print("This is child ")

# child1 = child()                   # Child can take the properties of all
# child1.show_child()
# child1.show_grandparents()
# child1.show_parents()

# parent1 = parents()                # see parent class can take the properties of grandparents only not child 
# parent1.show_grandparents()
# parent1.show_parents()

# This is Hierarichal inheritance which is the opposite of multiple inheritance here the parents is one but child can be 2 or more 

# class parents:
#     def show_parent(self):
#         print('I am parents ')
# class son(parents):
#     def show_son(self):
#         print('I am Son ')
# class daughter (parents):
#     def show_daughter(self):
#         print("I am Daughter")

# son1 = son()
# son1.show_parent()                    # see here children can get the method of parents only not other children 
# daughter1 = daughter()
# daughter1.show_parent()


