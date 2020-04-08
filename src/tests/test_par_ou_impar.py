from par_ou_impar import jogar
from typing import Callable
from time import sleep
from magatest.mock import MagicMock, patch
import par_ou_impar
from unittest import mock as unittest_mock


def test_par_ou_impar_should_win_when_result_is_even():
    
    with patch('par_ou_impar.randint', return_value=2):
        assert jogar('par', 2)

def test_par_ou_impar_should_lose_when_result_is_even():

    with patch('par_ou_impar.randint') as mock:
        mock.return_value = 3
        assert not jogar('par', 2)

def test_magic_mock_instance():
    mock = MagicMock()

    soma_mock = mock.soma
    assert isinstance(soma_mock, MagicMock)
    assert soma_mock is mock.soma


def test_jogador():
    with unittest_mock.patch(
        'par_ou_impar.Jogador.jogou', 
        return_value=False
    ):
        assert not par_ou_impar.jogador_jogou()