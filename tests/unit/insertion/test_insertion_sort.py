# 2 Prestandatest: insertion sort
# Betrakta följande funktion.
#
# def insertion_sort(lst):
#     result = []
#     for item in lst:
#         inserted = False
#         index = 0
#         while not inserted and index < len(result):
#             if item < result[index]:
#                 result.insert(index, item)
#                 inserted = True
#             index += 1
#         if not inserted:
#             result.append(item)
#     return result
#
#==============================================================================

#------------------------------------------------------------------------------
# 1 Vad har funktionen för tidskomplexitet?
#   Den har O(n²) (kvadratisk tid).
#------------------------------------------------------------------------------

import pytest

from src.insertion.insertion_sort import insertion_sort

pytestmark = pytest.mark.unit

#------------------------------------------------------------------------------
# 2 Skriv enhetstest som kontrollerar att funktionen kan sortera en lista med tal.
#   Använd till exempel följande testdata: [], [10], [10, 8, 6, 4, 2, 0]
#------------------------------------------------------------------------------

# Testar att skicka tom lista för sortering
def test_insertion_sort__empty_list():
    test_list = []
    result = insertion_sort(test_list)
    assert result == []


# Testar att skicka lista med bara ett värde i
def test_insertion_sort__one_value():
    test_list = [10]
    result = insertion_sort(test_list)
    assert result == [10]


# Testar att skicka en lista med flera värden
def test_insertion_sort__more_values():
    test_list = [10, 8, 6, 4, 2, 0]
    result = insertion_sort(test_list)
    assert result == [0, 2, 4, 6, 8, 10]




