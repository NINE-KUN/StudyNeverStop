'''不同的类 有相同的方法'''
class Cat(object):
    def say(self):
        print('i am cat')

class Dog(object):
    def say(self):
        print('i am a dog')

class Duck(object):
    def say(self):
        print('i am a duck')

animal = Cat
animal().say()