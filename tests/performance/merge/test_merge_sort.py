import pytest
import random

from src.merge import merge_sort


@pytest.mark.merge
def test_merge_sort_benchmark__random(benchmark):
    """Testar en lång lista sorterad slumpmässigt"""
    test_list = generate_list_random(50000)
    benchmark(merge_sort.merge_sort, test_list)

# Skapar en lista med (size) item i, sorterad i random ordning
def generate_list_random(size):
    return [random.randint(0, 50000) for _ in range(size)]

#------------------------------------------------------------------------------

@pytest.mark.merge
def test_merge_sort_benchmark__ascending(benchmark):
    """Testar en lång lista sorterad stigande"""
    test_list = generate_list_ascending(50000)
    benchmark(merge_sort.merge_sort, test_list)


# Skapar en lista med (size) item i, sorterad i stigande ordning
def generate_list_ascending(size):
    return list(range(size))

#------------------------------------------------------------------------------

@pytest.mark.merge
def test_merge_sort_benchmark__descending(benchmark):
    """Testar en lång lista sorterad fallande"""
    test_list = generate_list_descending(50000)
    benchmark(merge_sort.merge_sort, test_list)


# Skapar en lista med (size) item i, sorterad i fallande ordning
def generate_list_descending(size):
    return list(range(size -1, -1, -1))

#------------------------------------------------------------------------------
