"""
Unit testing para Merge Sort
"""

import pytest
# CORRECCIÓN: Importamos merge_sort, no merge
from merge_sort import merge_sort 

# Casos de prueba: (entrada, salida_esperada)
MERGE_SORT_TEST_CASES = [
    ([3, 1, 4, 1, 5, 9, 2], [1, 1, 2, 3, 4, 5, 9]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([], []),
    ([42], [42]),
    ([-5, 0, -3, 8], [-5, -3, 0, 8]),
    ([10, 30, 20, 10, 20], [10, 10, 20, 20, 30]),
]

@pytest.mark.parametrize("input_list, expected", MERGE_SORT_TEST_CASES)
def test_merge_sort(input_list, expected):
    """
    Prueba que la función merge_sort ordene correctamente las listas.
    """
    # CORRECCIÓN: Llamamos a merge_sort
    assert merge_sort(input_list.copy()) == expected