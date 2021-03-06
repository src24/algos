import unittest
from typing import List
from sorting import merge_sort

arr: List[int] = [10, 2, 1, 7, 5, 3, 4, 6, 8, 9]


class TestMergeSort(unittest.TestCase):
    def test_merge_sort_asc(self):
        expected: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        merge_sort.merge_sort(arr)
        self.assertEqual(expected, arr)

    def test_merge_sort_desc(self):
        expected: List[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        merge_sort.merge_sort(arr, True)
        self.assertEqual(expected, arr)

    def test_merge_sort_one(self):
        arr_one: List[int] = [10]
        merge_sort.merge_sort(arr_one)
        self.assertEqual([10], arr_one)

    def test_merge_sort_empty(self):
        arr_one: List[int] = []
        merge_sort.merge_sort(arr_one)
        self.assertEqual([], arr_one)


if __name__ == '__main__':
    unittest.main()
