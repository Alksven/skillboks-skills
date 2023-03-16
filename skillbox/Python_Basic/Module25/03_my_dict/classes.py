class Dict:

    def __init__(self):
        self.dict = dict()

    def set_element(self, key, value):
        self.dict[key] = value

    def get_key(self, key):
        return self.dict.get(key)


class MyDict(Dict):

    def __init__(self):
        super().__init__()

    def get_key(self, key):
        if key in self.dict:
            return f'Key value {key} = {self.dict[key]}.'
        return self.dict.get(key, 0)
