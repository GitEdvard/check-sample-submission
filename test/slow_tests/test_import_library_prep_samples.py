import unittest
import os
from check_sample_submission.import_excel import ImportSampleSubmission


class TestImportLibraryPrepSamples(unittest.TestCase):
    def setUp(self):
        here = os.path.dirname(__file__)
        file_name = r'BLA-32605-v.4.0_Samples_for_library_preparation_SampleForm_test till validering.xlsx'
        file_path = os.path.join(here, file_name)
        sample_column_index = 4
        volume_column_index = 6
        sample_column_name = 'SAMPLE ID'
        here = os.path.dirname(__file__)
        export_file_path =os.path.join(here, 'newfile.xlsx')
        self.excel_reader = ImportSampleSubmission(
            file_path, sample_column_index, volume_column_index,
            sample_column_name, export_file_path)

    def test_get_caption_row(self):
        row_index = self.excel_reader._determine_caption_row_index()
        self.assertEqual(3, row_index)

    def test_list_all_samples_under_library_id_columns__entries_found(self):
        samples = self.excel_reader._samples
        self.assertEqual(11, len(samples))
        self.assertEqual('SE-402', samples[0])

    def test_validate(self):
        error_messages = self.excel_reader.check_faulty_contents()
        self.assertEqual(9, len(error_messages))
