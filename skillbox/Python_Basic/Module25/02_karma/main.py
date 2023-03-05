from classes import Karma

my_karma = Karma(my_karma=0)
count_day = 1
while True:
    try:
        my_karma.my_karma_count += my_karma.one_day()
        print('Day: {}. Total karma {}'.format(count_day, my_karma.my_karma_count))
    except TypeError:
        print("Day: {}. You don't get karma today.".format(count_day))
    count_day += 1