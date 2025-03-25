from problems.two_pointers import (
    is_palindrome,
    is_subsequence,
    two_sum_no_space,
    three_sum,
    three_sum_closest,
    max_area,
    move_zeros_in_place,
)


def test_is_palindrome():
    # Test with a string containing spaces and punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") == True


def test_two_sum_no_space():
    # Test with sorted array and target
    assert two_sum_no_space([2, 7, 11, 15], 9) == [0, 1]


def test_three_sum():
    # Test with array containing duplicates
    assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])


def test_three_sum_closest():
    # Test with array and target
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2


def test_max_area():
    # Test with array of heights
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_move_zeros_in_place():
    # Test with array containing zeros
    nums = [0, 1, 0, 3, 12]
    move_zeros_in_place(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_is_subsequence():
    assert is_subsequence("abc", "ahbgdc") == True
    assert is_subsequence("axt", "ahbgdc") == False
