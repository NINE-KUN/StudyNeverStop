'''对象=属性+方法'''

class Turtle:
    color='green'
    weight=10
    legs=4

    def func4(self,x):
        if x>0:
            self.func4(x-1)
            print(x)
t=Turtle()
print(t.func4(4))