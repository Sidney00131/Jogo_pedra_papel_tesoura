import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from jogo import determinar_vencedor
import pytest



@pytest.mark.parametrize("jogador, computador, esperado", [
    ("pedra", "tesoura", "Jogador"),
    ("tesoura", "papel", "Jogador"),
    ("papel", "pedra", "Jogador"),
    ("pedra", "papel", "Computador"),
    ("tesoura", "pedra", "Computador"),
    ("papel", "tesoura", "Computador"),
    ("pedra", "pedra", "Empate"),
    ("papel", "papel", "Empate"),
    ("tesoura", "tesoura", "Empate"),
])
def test_determinar_vencedor(jogador, computador, esperado):
    resultado = determinar_vencedor(jogador, computador)
    assert resultado == esperado
