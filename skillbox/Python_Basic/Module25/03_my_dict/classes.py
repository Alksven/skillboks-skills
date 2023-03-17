
class MyDict(dict):
    def __init__(self):
        super().__init__()

    def get(self, key):
        if key in self:
            return self[key]
        return 0