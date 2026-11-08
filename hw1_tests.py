"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1
from hw1 import vowel_count
from hw1 import short_lists
from hw1 import ascending_pairs
from hw1 import add_prices
from hw1 import rectangle_area
from hw1 import books_by_author
from hw1 import circle_bound
from hw1 import below_pay_average
class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(3, vowel_count("AdeFga"))
    def test_vowel_count_empty_string(self):
        self.assertEqual(0, vowel_count(""))
    def test_vowel_count_test1(self):
        self.assertEqual(3, vowel_count("OOoh"))
    def test_vowel_count_test2(self):
        self.assertEqual(3, vowel_count("#8eApo"))

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual([[2,8]], short_lists([[1,2,3], [2,8], []]))
    def test_short_lists_no_matching_lengths(self):
        self.assertEqual([], short_lists([[1,2,3], [2], []]))
    def test_short_lists_test1(self):
        self.assertEqual([], short_lists([[], [], []]))
    def test_short_lists_test2(self):
        self.assertEqual([[1,2], [2,1], [2,5], [8,16]], short_lists([[1,2], [2,1], [2,5], [8,16]]))

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual([[1,2,3], [2,8], [3,9]], ascending_pairs([[1,2,3], [8,2], [9,3]]))
    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual([[1,2], [2,8], [3,9]], ascending_pairs([[1,2], [2,8], [3,9]]))
    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        result = add_prices(data.Price(10,22), data.Price(2,55))
        self.assertEqual(12, result.dollars)
        self.assertEqual(77, result.cents)
    def test_add_prices_with_cents_carry(self):
        result = add_prices(data.Price(8,54), data.Price(1,55))
        self.assertEqual(10, result.dollars)
        self.assertEqual(9, result.cents)

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        self.assertEqual(50, rectangle_area(data.Rectangle((0,10),(5,0))))
    def test_rectangle_area_negative_coordinates(self):
        self.assertEqual(100, rectangle_area(data.Rectangle((-5,5),(5,-5))))

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        list = (data.Book("Jim", "Book1"), data.Book("Max", "Book2"), data.Book("Carl", "Book3"), data.Book("Jim", "Book4"))
        result = books_by_author("Jim", list)
        self.assertEqual(2, len(result))
    def test_books_by_author_no_matches(self):
        list = (data.Book("Jim", "Book1"), data.Book("Max", "Book2"), data.Book("Carl", "Book3"), data.Book("Jim", "Book4"))
        result = books_by_author("Hank", list)
        self.assertEqual(0, len(result))

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        self.assertEqual(data.Circle((1,1), 2**.5), circle_bound(data.Rectangle((0,2),(2,0))))
    def test_circle_bound_non_square_rectangle(self):
        self.assertEqual(data.Circle((2,1), 5**.5), circle_bound(data.Rectangle((0,2),(4,0))))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        list = [data.Employee("Jim", 10), data.Employee("Max", 20), data.Employee("Dave", 10), data.Employee("Carl", 20)]
        self.assertEqual(["Jim", "Dave"], below_pay_average(list))

    def test_below_pay_average_empty_list(self):
        list = []
        self.assertEqual([], below_pay_average(list))


if __name__ == '__main__':
    unittest.main()
