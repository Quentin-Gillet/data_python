from Models.NameSearchers.nameSearcher import NameSearcher


class FindWithName(NameSearcher):

    def __init__(self, name, window):
        super().__init__(name, window)

    def find(self):
