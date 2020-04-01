from par_ou_impar import jogar
from typing import Callable
from time import sleep
import par_ou_impar


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


class RandIntMock:

    def __init__(self, func: Callable):
        self._func = func

    def __enter__(self):
        self._old_func = par_ou_impar.randint
        par_ou_impar.randint = self._func

    def __exit__(self, exc_type, exc, stacktrace):
        par_ou_impar.randint = self._old_func


def test_par_ou_impar_should_win_when_result_is_even():
    randint_magic_mock = MagicMock()
    # randint_magic_mock.return_value = 2
    
    with RandIntMock(randint_magic_mock):
        assert jogar('par', 2)

    print('Deu tudo certo: test_par_ou_impar_should_win_when_result_is_even!')

def test_par_ou_impar_should_lose_when_result_is_even():
    with RandIntMock(lambda x, y: 3):
        assert not jogar('par', 2)

    print('Deu tudo certo: test_par_ou_impar_should_lose_when_result_is_even!')


def test_magic_mock_instance():
    mock = MagicMock()

    soma_mock = mock.soma
    assert isinstance(soma_mock, MagicMock)
    assert soma_mock is mock.soma

    print('Deu tudo certo: test_magic_mock_instance')

def main():
    for key, value in globals().items():
        if key.startswith('test_'):
            value()

if __name__ == "__main__":
    main()