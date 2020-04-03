class MagicMock():

    def __init__(self, return_value=None):
        self.return_value = return_value

    @property
    def return_value(self):
        return self._return_value

    @return_value.setter
    def return_value(self, value):
        self._return_value = value

    def __call__(self, *args, **kwargs):
        return self.return_value

    def __getattr__(self, nome_atributo):
        obj = MagicMock()
        self.__dict__[nome_atributo] = obj
        return obj
        