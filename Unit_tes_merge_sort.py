"""
Unit testing para Merge Sort
"""

import pytest
# Asegúrate de que el archivo se llame merge_sort.py y la función merge_sort
from merge_sort import merge

# Casos de prueba: (entrada, salida_esperada)
MERGE_SORT_TEST_CASES = [
    ([3, 1, 4, 1, 5, 9, 2], [1, 1, 2, 3, 4, 5, 9]),  # Desordenado con duplicados
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),              # Ya ordenado
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),              # Orden inverso
    ([], []),                                       # Lista vacía (Caso límite)
    ([42], [42]),                                   # Un solo elemento (Caso límite)
    ([-5, 0, -3, 8], [-5, -3, 0, 8]),               # Números negativos
    ([10, 30, 20, 10, 20], [10, 10, 20, 20, 30]),   # Duplicados adicionales
]

@pytest.mark.parametrize("input_list, expected", MERGE_SORT_TEST_CASES)
def test_merge_sort(input_list, expected):
    """
    Prueba que la función merge_sort ordene correctamente las listas.
    """
    # Usamos .copy() para no mutar la lista original de los casos de prueba
    assert merge(input_list.copy()) == expected