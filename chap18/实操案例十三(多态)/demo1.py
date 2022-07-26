#编写程序实现乐手弹奏乐器，乐手可以弹奏不同乐器从而发出不同的声音可以弹奏的乐器包括二胡，钢琴，琵琶
class Instrument():#父类
    def make_sound(self):
        pass

class Erhu(Instrument):#子类
    def make_sound(self):#重写
        print('二胡在演奏')
class Pinao(Instrument):#子类
    def make_sound(self):
        print('钢琴在演奏')
class Violin(Instrument):#子类
    def make_sound(self):
        print('小提琴在演奏')

#演奏的函数
def play(instrument):
    instrument.make_sound()
class Bird():
    def make_sound(self):#不管声明类只要有make_sound方法就可以使用play函数
        print('小鸟在唱歌')
if __name__ == '__main__':
    play(Erhu())
    play(Pinao())
    play(Violin())
    play(Bird())