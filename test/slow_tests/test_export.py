import unittest
import os
from unittest import skip
from check_sample_submission.import_excel import ImportSampleSubmission


class TestImportReadyMadeLibraries(unittest.TestCase):
    def setUp(self):
        here = os.path.dirname(__file__)
        file_name = r'BLA-32606-v.5.0_Ready-made-libraries_SampleForm.xlsx'
        file_path = os.path.join(here, file_name)
        export_path = os.path.join(here, 'newfile.xlsx')
        self.export_path = export_path
        sample_column_index = 3
        volume_column_index = 7
        sample_column_name = 'LIBRARY ID'
        self.excel_reader = ImportSampleSubmission(
            file_path, sample_column_index, volume_column_index, sample_column_name,
            export_to_file_path=export_path)

    def test_export(self):
        self.excel_reader.check_faulty_contents()
        print('NewFile.xlsx is updated to: \n{}'.format(self.export_path))
        self.assertEqual(1, 2)

    @skip('')
    def test_row_cols(self):
        number_rows = self.excel_reader.number_rows()
        number_cols = self.excel_reader.number_cols()
        print('rows: {}, cols: {}'.format(number_rows, number_cols))
        self.assertEqual(1, 2)

    @skip('')
    def test_print_sample_col(self):
        self.excel_reader.print_sample_column()
        self.assertEqual(1, 2)
