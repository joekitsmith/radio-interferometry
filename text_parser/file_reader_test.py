## FILE READER TESTS ##

import unittest
import file_reader

class ExtractTextTest(unittest.TestCase):

    def test_extractText_PathToTextFile_FilledStringReturned(self):
        text_file_name = 'cartesian_coordinates_test.txt'
        parser = file_reader.FileReader()
        self.assertGreater(len(parser.extractText(text_file_name)), 0)

    def test_extractText_PathToMissingTextFile_EmptyStringReturned(self):
        text_file_name = 'cartesian_coordinates_test_notpresent.txt'
        parser = file_reader.FileReader()
        self.assertEqual(len(parser.extractText(text_file_name)), 0)

if __name__ == '__main__':
    unittest.main()