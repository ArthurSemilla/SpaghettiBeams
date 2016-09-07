class Item:
    
    def __init__(self, name, owned):
        self._name = name
        self._owned = owned

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def owned(self):
        return self._owned

    @owned.setter
    def owned(self, owned):
        self._owned = owned