class Item:
    
    def __init__(self, name, owned):
        self._name = name
        self._owned = owned
        self._properties = {}

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

    @property
    def properties(self):
        return self._properties

    def new_property(self, key, value):
        self._properties[key] = value

    def __str__(self):
        return "Name: %s Owned: %s" % (self.name, self.owned)

