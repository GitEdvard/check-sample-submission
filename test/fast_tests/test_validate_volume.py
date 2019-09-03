import unittest
from unittest import skip
from sheet_validator import SheetValidator


class TestValidateVolume(unittest.TestCase):
    def test__one_correct_row__no_errors(self):
        rows = [
            ('sample1', '30')
        ]
        validator = SheetValidator()
        error_lst = validator.list_faulty(rows)
        self.assertEqual(0, len(error_lst))

    def test__one_row_with_lacking_volume__one_error(self):
        rows = [
            ('sample1', 'None')
        ]
        validator = SheetValidator()
        error_lst = validator.list_faulty(rows)
        self.assertEqual(1, len(error_lst))
        self.assertEqual('sample1\tDo not have volume', error_lst[0])

    def test__one_row_with_volume_not_numeric__error(self):
        rows = [
            ('sample1', '30 ul')
        ]
        validator = SheetValidator()
        error_lst = validator.list_faulty(rows)
        self.assertEqual(1, len(error_lst))

    def test__one_row_with_volume_contains_comma__error(self):
        rows = [
            ('sample1', '30,4')
        ]
        validator = SheetValidator()
        error_lst = validator.list_faulty(rows)
        self.assertEqual(1, len(error_lst))

    def test__one_row_with_volume_contains_dot__no_error(self):
        rows = [
            ('sample1', '30.4')
        ]
        validator = SheetValidator()
        error_lst = validator.list_faulty(rows)
        self.assertEqual(0, len(error_lst))

    def test__one_row_with_both_faulty_name_and_string_volume__two_errors(self):
        rows = [
            ('sample 1', '30 ul')
        ]
        validator = SheetValidator()
        error_lst = validator.list_faulty(rows)
        self.assertEqual(2, len(error_lst))
