class MyDict:

    def __init__(self):
        self.__my_dict = dict()

    def set_element(self, key, value):
        self.__my_dict[key] = value

    def get_key(self, key):
        return self.__my_dict.get(key, 0)