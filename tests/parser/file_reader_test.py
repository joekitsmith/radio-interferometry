## FILE READER TESTS ##

import unittest
from source.parser.file_reader import FileReader

class ExtractTextTest(unittest.TestCase):

    def test_extractText_PathToTextFile_FilledStringReturned(self):
        text_file_name = 'tests\input_coordinates_test.txt'
        text_parser = FileReader()
        self.assertGreater(len(text_parser.extractText(text_file_name)), 0)

    def test_extractText_PathToMissingTextFile_EmptyStringReturned(self):
        text_file_name = 'tests\input_coordinates_test_notpresent.txt'
        text_parser = FileReader()
        self.assertEqual(len(text_parser.extractText(text_file_name)), 0)

if __name__ == '__main__':
    unittest.main()