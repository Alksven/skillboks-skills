from classes import *

my_karam = Karma(my_karma=0)
count_day = 1
while True:
    try:
        my_karam.my_karma += my_karam.one_day()
    except TypeError:
        count_day += 1

