'''
Created on 05 мая 2014 г.


'''
from random import Random

r = Random()
r.seed()

maxChoises = 100000
numChoises = 0

golds = 0
silvers = 0

boxes = [["gold","gold"], ["gold","silver"], ["silver", "silver"]]

while numChoises != maxChoises:
    box = r.choice(boxes)
    if r.choice(box) == "gold":
        # наш случай, вытащили из случайного ящика наугад золото
        if box[0] == box [1] == "gold":
            golds = golds + 1 # в ящике оба золота
        else:
            silvers = silvers + 1 # вторым в ящике оказалось серебро
        numChoises = numChoises + 1
        #если наугад вытащили не то, не наш случай, всё по новой вытаскиваем
print ("Золота вытащили раз: " + str(golds))
print ("Серебра вытащили раз: " + str(silvers))
print ("Вероятность золота практическая:" + str((golds/maxChoises)))