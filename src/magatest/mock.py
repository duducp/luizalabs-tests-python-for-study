from contextlib import contextmanager
from functools import wraps
import importlib
import inspect


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


"""

@parametrize('parametro,parametro2', 
    [(param1, param2)]
)
def test_caso_de_teste(parametro1, parametro2):
    ...
"""


def parametrize(parameters, values):

    def callable(func):
        @wraps(func)

        def wrapper(*args, **kwargs):
            parameters_list = [
                parameter.strip()
                for parameter in parameters.split(',')
            ]
            metadata = inspect.signature(func)
            metadata_parameters = [*metadata.parameters.keys()]
            if not set(parameters_list).issubset(set(metadata_parameters)):  # a, b, c => b, c é um subconjunto de a, b, c
                raise AttributeError(
                    'The attributes list is not equal to the function parameters, '
                    f'{metadata_parameters} != {parameters_list}'
                )

            for value in values:
                if len(parameters_list) != len(value):
                    raise AttributeError(
                        'The parameters entered did not match the values '
                        f'{parameters_list} != {value}'
                    )

                parameters_dict = {
                    k: v for k, v in zip(parameters_list, value)
                }

                try:
                    func(*args, **{**kwargs, **parameters_dict})
                except:
                    print('\033[93m')
                    print(f'Broke with {value} values :(')
                    print('\033[91m')
                    raise
    
        return wrapper

    return callable
