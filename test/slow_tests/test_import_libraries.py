import unittest
import os
from check_sample_submission.import_excel import ImportSampleSubmission


class TestImportReadyMadeLibraries(unittest.TestCase):
    def setUp(self):
        here = os.path.dirname(__file__)
        file_name = r'BLA-32606-v.5.0_Ready-made-libraries_SampleForm.xlsx'
        file_path = os.path.join(here, file_name)
        sample_column_index = 3
        volume_column_index = 7
        sample_column_name = 'LIBRARY ID'
        here = os.path.dirname(__file__)
        export_file_path =os.path.join(here, 'newfile.xlsx')
        self.excel_reader = ImportSampleSubmission(
            file_path, sample_column_index, volume_column_index,
            sample_column_name, export_file_path)

    def test_get_caption_row(self):
        row_index = self.excel_reader._determine_caption_row_index()
        self.assertEqual(5, row_index)

    def test_list_all_samples_under_library_id_columns__three_entries_found(self):
        samples = self.excel_reader._samples
        self.assertEqual(3, len(samples))
        self.assertEqual('edvardsample', samples[0])

    def test_read_empty_volume_value__parsed_value_is_magic_str(self):
        contents = self.excel_reader.contents
        empty_volume = contents[1][1]
        self.assertEqual('None', empty_volume)

    def test_read_numeric_volume__parsed_value_is_str(self):
        contents = self.excel_reader.contents
        numeric_volume = contents[0][1]
        self.assertEqual('29', numeric_volume)
