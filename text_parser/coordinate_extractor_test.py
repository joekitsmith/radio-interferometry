## COORDINATE EXTRACTOR TESTS ##

import unittest
import coordinate_extractor

class ExtractCoordinateText(unittest.TestCase):

    def test_extractCoordinateText_UnitsTitleWithUnits_ReturnsStringOfUnits(self):
        title = 'Units ='
        text = "Units = [m, m, m]\nCoordinates = [1,2,3] [4,5,6] [10,11,12]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_str = coord_extractor.extractCoordinateText(title, text)
        self.assertEqual(output_coord_str, "[m, m, m]")

    def test_extractCoordinateText_CoordTitleWithCoordinates_ReturnsStringOfCoordinates(self):
        title = 'Coordinates ='
        text = "Units = [m, m, m]\nCoordinates = [1,2,3] [4,5,6] [10,11,12]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_str = coord_extractor.extractCoordinateText(title, text)
        self.assertEqual(output_coord_str, "[1,2,3] [4,5,6] [10,11,12]")

    def test_extractCoordinateText_TitleWithMissingCoordinates_ReturnsEmptyString(self):
        title = 'Coordinates ='
        text = "Units = [m, m, m]\nCoordinates ="
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_str = coord_extractor.extractCoordinateText(title, text)
        self.assertEqual(output_coord_str, "")

    def test_extractCoordinateText_InvalidTitle_ReturnsEmptyString(self):
        title = 'Invalid title'
        text = "Units = [m, m, m]\nCoordinates = [1,2,3] [4,5,6] [10,11,12]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_str = coord_extractor.extractCoordinateText(title, text)
        self.assertEqual(output_coord_str, "")

class ConvertCoordinateStringToList(unittest.TestCase):

    def test_convertCoordinateStringToList_StringOfUnitsList_ReturnsListOfListOfStrings(self):
        coord_str = "[m,m,m]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.convertCoordinateStringToList(coord_str)
        self.assertEqual(output_coord_list, [['m','m','m']])

    def test_convertCoordinateStringToList_StringOfCoordinatesLists_ReturnsListOfListOfStrings(self):
        coord_str = "[1,2,3] [4,5,6] [7,8,9]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.convertCoordinateStringToList(coord_str)
        self.assertEqual(output_coord_list, [['1','2','3'], ['4','5','6'], ['7','8','9']])

    def test_convertCoordinateStringToList_EmptyString_ReturnsListWithEmptyString(self):
        coord_str = ""
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.convertCoordinateStringToList(coord_str)
        self.assertEqual(output_coord_list, [['']])

    def test_convertCoordinateStringToList_SingleCommaString_ReturnsListWith2Elements(self):
        coord_str = "m,m"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.convertCoordinateStringToList(coord_str)
        self.assertEqual(output_coord_list, [['m', 'm']])

class ConvertCoordinateStringToList(unittest.TestCase):

    def test_correctCoordinateListDataType_ListOfListOfUnitStrings_ReturnsListOfListOfStrings(self):
        coord_list = [['m','m','m']]
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.correctCoordinateListDataType(coord_list)
        self.assertEqual(output_coord_list, [['m','m','m']])

    def test_correctCoordinateListDataType_ListOfListOfCoordinateIntsAsStrings_ReturnsListOfListOfInts(self):
        coord_list = [['1','2','3'],['2','4','6'],['7','8','9']]
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.correctCoordinateListDataType(coord_list)
        self.assertEqual(output_coord_list, [[1,2,3],[2,4,6],[7,8,9]])

    def test_correctCoordinateListDataType_ListOfListOfCoordinateFloatsAsStrings_ReturnsListOfListOfFloats(self):
        coord_list = [['1.5','3.3','9.5'], ['4.7','10.5','8.5'], ['8.9', '15.6', '100.9']]
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.correctCoordinateListDataType(coord_list)
        self.assertEqual(output_coord_list, [[1.5,3.3,9.5], [4.7,10.5,8.5], [8.9,15.6,100.9]])

    def test_correctCoordinateListDataType_ListOfListOfCoordinateFloatsAsStrings_ReturnsListOfListOfFloats(self):
        coord_list = [['1.5','3.3','9.5'], ['4.7','10.5','8.5'], ['8.9', '15.6', '100.9']]
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.correctCoordinateListDataType(coord_list)
        self.assertEqual(output_coord_list, [[1.5,3.3,9.5], [4.7,10.5,8.5], [8.9,15.6,100.9]])

    def test_correctCoordinateListDataType_ListOfListWithEmptyString_ListOfListWithEmptyString(self):
        coord_list = [['']]
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.correctCoordinateListDataType(coord_list)
        self.assertEqual(output_coord_list, [['']])

class ExtractCoordinateListFromText(unittest.TestCase):

    def test_extractCoordinateListFromText_UnitsTitleWithUnits_ReturnsListOfListOfStrings(self):
        title = 'Units ='
        text = "Units = [m,m,m]\nCoordinates = [1,2,3] [4,5,6] [10,11,12]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.extractCoordinateListFromText(title, text)
        self.assertEqual(output_coord_list, [['m','m','m']])

    def test_extractCoordinateListFromText_CoordinateTitleWithCoordinateInts_ReturnsListOfListOfInts(self):
        title = 'Coordinates ='
        text = "Units = [m,m,m]\nCoordinates = [1,2,3] [4,5,6] [10,11,12]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.extractCoordinateListFromText(title, text)
        self.assertEqual(output_coord_list, [[1,2,3], [4,5,6], [10,11,12]])

    def test_extractCoordinateListFromText_CoordinateTitleWithCoordinateFloats_ReturnsListOfListOfFloats(self):
        title = 'Coordinates ='
        text = "Units = [m,m,m]\nCoordinates = [[1.5,3.3,9.5] [4.7,10.5,8.5] [8.9,15.6,100.9]]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.extractCoordinateListFromText(title, text)
        self.assertEqual(output_coord_list, [[1.5,3.3,9.5], [4.7,10.5,8.5], [8.9,15.6,100.9]])

    def test_extractCoordinateListFromText_MissingTitle_ReturnsListOfListOfEmptyString(self):
        title = 'Invalid title'
        text = "Units = [m,m,m]\nCoordinates = [1,2,3] [4,5,6] [10,11,12]"
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.extractCoordinateListFromText(title, text)
        self.assertEqual(output_coord_list, [[""]])

    def test_extractCoordinateListFromText_EmptyText_ReturnsListOfListOfEmptyString(self):
        title = 'Coordinates ='
        text = ""
        coord_extractor = coordinate_extractor.CoordinateExtractor()
        output_coord_list = coord_extractor.extractCoordinateListFromText(title, text)
        self.assertEqual(output_coord_list, [[""]])

if __name__ == '__main__':
    unittest.main()