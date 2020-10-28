import itertools
class Lamp:
    def __init__(self,Colors):
          self.Colors = itertools.cycle['Green', 'Red', 'Blue', 'Yellow']

    def light(self):
        return next(self.Colors)

if __name__ == '__main__':
    p = Lamp()
print(p.light())
print(p.light())
print(p.light())
print(p.light())
print(p.light())
