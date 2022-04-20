class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):

        # 初始化super class(Animal)繼承Animal的所有屬型和方法
        super().__init__()

    def breathe(self):
        super().breathe() # print("Inhale, exhale.")
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()