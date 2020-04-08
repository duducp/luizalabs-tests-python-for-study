from contextlib import contextmanager
import importlib



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


@contextmanager
def patch(
    object_to_mock: str,
    *args,
    **kwargs
):  # magatest.par_ou_impar.randint
    parts = object_to_mock.split('.')  # ['magatest', 'par_ou_impar', 'randint']

    module_path = '.'.join(parts[:-1]) # 'magatest.par_ou_impar'

    object_to_mock_path = parts[-1]  # randint
    
    module = importlib.import_module(module_path) # mocka o método
    
    old_obj = getattr(module, object_to_mock_path)

    mock = MagicMock(*args, **kwargs)

    setattr(module, object_to_mock_path, mock)

    yield mock # entrega o mock

    setattr(module, object_to_mock_path, old_obj)



"""
import mock

def test_par_ou_impar_should_lose_when_result_is_even():
    # randint_magic_mock = MagicMock()
    # randint_magic_mock.return_value = 3

    # with RandIntMock(randint_magic_mock):

    with mock.patch('par_ou_impar.randint') as randint_mock:
        randint_mock.return_value = 3
        assert not jogar('par', 2)
"""