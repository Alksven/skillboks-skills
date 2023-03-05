import random
import datetime


class Karma:
    NEED_KARMA = 500

    def __init__(self, my_karma):
        self.my_karma_count = my_karma
        self.kara = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]

    def one_day(self):
        if self.my_karma_count >= Karma.NEED_KARMA:
            print('You have reached nirvana')
            exit()
        bad_day = random.randint(1, 100)
        if bad_day <= 10:
            random_kara = random.choice(self.kara)
            try:
                raise random_kara
            except Exception as error:
                with open('karma.log', 'a') as karma_log:
                    date_now = datetime.datetime.now()
                    karma_log.write(str(date_now) + ' ' + str(error) + '\n')
        else:
            karma_today = random.randint(1, 7)
            print('You get {} karma today.'.format(karma_today))
            return karma_today


class KillError(Exception):

    def __str__(self):
        return self.__class__.__name__


class DrunkError(Exception):
    def __str__(self):
        return self.__class__.__name__


class CarCrashError(Exception):
    def __str__(self):
        return self.__class__.__name__


class GluttonyError(Exception):
    def __str__(self):
        return self.__class__.__name__


class DepressionError(Exception):
    def __str__(self):
        return self.__class__.__name__
