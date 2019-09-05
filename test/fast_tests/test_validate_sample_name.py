import unittest
from check_sample_submission.sheet_validator import SheetValidator


class TestValidateSampleName(unittest.TestCase):
    def test__with_two_samples__one_has_underscore__error(self):
        rows = [
            ('sample1', '1'),
            ('sample 2', '1')
        ]
        validator = SheetValidator()
        faulty_samples = validator.list_faulty(rows)
        self.assertEqual(1, len(faulty_samples))
        self.assertEqual('sample 2\tHas faulty tokens, \'(space)\'', faulty_samples[0])

    def test__with_two_samples__one_has_dash__no_error(self):
        rows = [
            ('sample1', '1'),
            ('sample-2', '1')
        ]
        validator = SheetValidator()
        faulty_samples = validator.list_faulty(rows)
        self.assertEqual(0, len(faulty_samples))

    def test__with_two_samples__one_has_underscore(self):
        rows = [
            ('sample1', '1'),
            ('sample_2', '1')
        ]
        validator = SheetValidator()
        faulty_samples = validator.list_faulty(rows)
        self.assertEqual(1, len(faulty_samples))

    def test__with_one_sample_has_multiple_faulty_tokens(self):
        rows = [
            ('sample##2', '1')
        ]
        validator = SheetValidator()
        faulty_samples = validator.list_faulty(rows)
        self.assertEqual(1, len(faulty_samples))
        self.assertEqual('sample##2\tHas faulty tokens, \'##\'', faulty_samples[0])

    def test__with_one_sample_has_two_faulty_tokens_containing_space(self):
        rows = [
            ('sample #2', '1')
        ]
        validator = SheetValidator()
        faulty_samples = validator.list_faulty(rows)
        self.assertEqual(1, len(faulty_samples))
        self.assertEqual('sample #2\tHas faulty tokens, \'(space)#\'', faulty_samples[0])
