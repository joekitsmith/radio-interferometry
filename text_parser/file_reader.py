## FILE READER ##

import sys, os

class FileReader():

    def extractText(self, text_file_name : str) -> str:
        """
        Opens text file from same directory as script

        Parameters
        -------
        text_file_name : str 
            path to text file containing input data
        
        Returns
        -------
        text : str
            all text extracted from text file
        """
        try:
            with open(os.path.join(sys.path[0], text_file_name)) as file:
                text = file.read()
            return(text)
        except:
            return("")