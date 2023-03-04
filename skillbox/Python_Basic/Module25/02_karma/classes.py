import random


class Karma:
    KARMA = 500

    def __init__(self, my_karma):
        self.my_karma = my_karma
        self.kara = [killError(), DrunkenMistake(), CarCrashError(), GluttonyError(), DepressionMistake()]

    def one_day(self):
        if self.my_karma >= Karma.KARMA:
            print('You have reached nirvana')
            exit()
        bad_day = random.randint(1, 100)
        print(bad_day)
        if bad_day <= 10:
            random_kara = random.choice(self.kara)
            try:
                raise random_kara
            except Exception as e:
                print('Caught an exception:', e)
        else:
            karma_today = random.randint(1, 7)
            print('You get {} karma today. Total {} karma'.format(karma_today, self.my_karma))
            return karma_today


class killError(Exception):

    def __str__(self):
        return 'kill'


class DrunkenMistake(Exception):
    def __str__(self):
        return 'рьяный'


class CarCrashError(Exception):
    def __str__(self):
        return 'автокатастрофы'


class GluttonyError(Exception):
    def __str__(self):
        return 'ОбжорствоОшибка'


class DepressionMistake(Exception):
    def __str__(self):
        return 'депрессии'
