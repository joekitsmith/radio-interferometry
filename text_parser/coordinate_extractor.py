## COORDINATE EXTRACTOR ##

from typing import List

class CoordinateExtractor():

    def extractCoordinateText(self, title : str, text : str) -> str:
        """
        Extracts coordinates from text following a defined title string

        Parameters
        -------
        title : str
            string preceding desired data on same line of text file

        text : str
            all text extracted from text file
        
        Returns
        -------
        coord_str : str
            string of list in form '[a,b,c]'
        """
        if title in text:
            split_text = text[text.index(title) + len(title):].strip()
            if '\n' not in split_text:
                coord_str = split_text
            else:
                coord_str = split_text[:split_text.index('\n')].strip()
        else:
            coord_str = ""
            print(f"{title} not found in text")
        return(coord_str)

    def convertCoordinateStringToList(self, coord_str : str) -> List[list]:
        """
        Converts string of list to list of list of strings that were comma-separated in text

        Parameters
        -------
        coord_str : str 
            string of list in form '[a,b,c]'
        
        Returns
        -------
        coord_list_of_str : list of list
            list of list of strings in form [['a','b','c']]
        """
        coord_list_of_str = []
        coord_list = coord_str.split(' ')
        for coord_str in coord_list:
            coord_str = coord_str.replace("[","").replace("]","").replace(' ','')
            coord_str = coord_str.split(",")
            coord_list_of_str.append(coord_str)
        return(coord_list_of_str)

    def correctCoordinateListDataType(self, coord_list: list) -> List[list]:
        """
        Converts elements in list of list from string to either string, float or digit as necessary

        Parameters
        -------
        coord_list : list 
            list of list of strings in form [['a','b','c'], ['1','2','3']]
        
        Returns
        -------
        corrected_coord_list : list of list
            list of list of strings, floats or ints in form [['a', 'b', 'c'], [1,2,3]]
        """
        corrected_coord_list = []
        for coord in coord_list:
            new_coord = []
            for elem in coord:
                if '.' in elem:
                    if elem.replace('.', '', 1).isdigit():
                        elem = float(elem)
                elif elem.isdigit():
                    elem = int(elem)
                new_coord.append(elem)
            corrected_coord_list.append(new_coord)
        return(corrected_coord_list)

    def extractCoordinateListFromText(self, title : str, text : str) -> List[list]:
        """
        Runs all extraction functions and extracts coordinates from text following defined title string

        Parameters
        -------
        title : str
            string preceding desired data on same line of text file

        title : str
            whole text containing all data
        
        Returns
        -------
        corrected_coord_list : list of list
            list of list of strings, floats or ints in form [['a', 'b', 'c'], [1,2,3]]
        """
        coord_str = self.extractCoordinateText(title, text)
        coord_list = self.convertCoordinateStringToList(coord_str)
        corrected_coord_list = self.correctCoordinateListDataType(coord_list)
        return(corrected_coord_list)