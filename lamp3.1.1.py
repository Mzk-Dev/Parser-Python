# class lamp():
#     def __init__(self, light1=['Green', 'Red', 'Blue', 'Yellow']):
#         self.light1 = iter(['Green', 'Red', 'Blue', 'Yellow'])
#
#     def light(self):
#         try:
#             return next(self.light1)
#         except StopIteration:
#             self.light1 == iter(['Green', 'Red', 'Blue', 'Yellow'])
#             return next(self.light1)
#
#
# light_1 = lamp()
# print(light_1.light())
# print(light_1.light())
# print(light_1.light())
# print(light_1.light())
# print(light_1.light())
# light_2 = lamp()
# print(light_2.light())
# print(light_2.light())
import itertools
class lamp:
    def __init__(self):
        self.color=itertools.cycle(['Green','Red','Blue','Yellow'])
    def light(self):
        return next(self.color)
light_1 = lamp()
print(light_1.light())
print(light_1.light())
print(light_1.light())
print(light_1.light())
print(light_1.light())
