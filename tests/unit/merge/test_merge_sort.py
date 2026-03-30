# 3 Prestandatest: merge sort
# Betrakta följande funktioner. Merge sort är en algoritm som
# först delar upp en lista i halvor, tills det bara är ett element i
# varje del; sedan kombinerar alla delar så att listan blir sorterad.
# Vill du lära dig mera kan du läsa här: Python Sorting Algorithms:
# merge_sort() | by Abel Garrido
# Länk: https://python.plainenglish.io/python-sorting-algorithms-merge-sort-7eda999ca5cf
#
# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst
#
#     mid = len(lst) // 2
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#
#     return merge(left, right)
#
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
#==============================================================================

#------------------------------------------------------------------------------
# 1 Vad har funktionen för tidskomplexitet?
#   Den har O(nlog n) - Linjär-logaritmisk tid
#
#   (Linjerna är nästan linjära men har en svag, svag böjning uppåt, vilket är
#   exakt vad man förväntar sig av Merge Sort.)
#------------------------------------------------------------------------------

import pytest

from src.merge.merge_sort import merge_sort

pytestmark = pytest.mark.unit

#------------------------------------------------------------------------------
# 2 Skriv enhetstest som kontrollerar att funktionen kan sortera en lista med tal,
#   på samma sätt som i föregående uppgift.
#   (Använd till exempel följande testdata: [], [10], [10, 8, 6, 4, 2, 0])
#------------------------------------------------------------------------------

# Testar att skicka tom lista för sortering
def test_merge_sort__empty_list():
    test_list = []
    result = merge_sort(test_list)
    assert result == []


# Testar att skicka lista med bara ett värde i
def test_merge_sort__one_value():
    test_list = [10]
    result = merge_sort(test_list)
    assert result == [10]


# Testar att skicka en lista med flera värden
def test_merge_sort__more_values():
    test_list = [10, 8, 6, 4, 2, 0]
    result = merge_sort(test_list)
    assert result == [0, 2, 4, 6, 8, 10]


