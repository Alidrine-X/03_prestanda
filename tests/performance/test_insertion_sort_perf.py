#------------------------------------------------------------------------------
# 3 Skriv prestandatest som testar att sortera en riktigt lång, slumpad lista.
#   Sikta på en körtid som är ca 100 ms. Du behöver en funktion som kan generera
#   en lång slumpad lista.
#   def generate_list(size):  → funktion som returnerar en lista med size antal
#   slumpade tal
#
# 4 Skriv fler prestandatest för längre listor. Anteckna körtiderna och plotta
#   dem i ett diagram med axlarna n (längden på listan) och t (körtiden som
#   benchmark rapporterar).
#
#------------------------------------------------------------------------------

import pytest
import random

from src.insertion import insertion_sort


@pytest.mark.performance
def test_insertion_sort_benchmark__random(benchmark):
    """Testar en lång lista sorterad slumpmässigt"""
    test_list = generate_list_random(2700)
    benchmark(insertion_sort.insertion_sort, test_list)

# Skapar en lista med (size) item i, sorterad i random ordning
def generate_list_random(size):
    return [random.randint(0, 10000) for _ in range(size)]

#------------------------------------------------------------------------------

@pytest.mark.performance
def test_insertion_sort_benchmark__ascending(benchmark):
    """Testar en lång lista sorterad stigande"""
    test_list = generate_list_ascending(2700)
    benchmark(insertion_sort.insertion_sort, test_list)


# Skapar en lista med (size) item i, sorterad i stigande ordning
def generate_list_ascending(size):
    return list(range(size))

#------------------------------------------------------------------------------

@pytest.mark.performance
def test_insertion_sort_benchmark__descending(benchmark):
    """Testar en lång lista sorterad fallande"""
    test_list = generate_list_descending(2700)
    benchmark(insertion_sort.insertion_sort, test_list)


# Skapar en lista med (size) item i, sorterad i fallande ordning
def generate_list_descending(size):
    return list(range(size -1, -1, -1))

#------------------------------------------------------------------------------

