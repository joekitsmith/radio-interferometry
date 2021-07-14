## FILE READER ##

import sys, os

class FileReader():

    def extractText(self, text_file_path : str) -> str:
        """
        Opens text file from same directory as script

        Parameters
        -------
        text_file_name : str 
            path to text file relative to parent repo folder
        
        Returns
        -------
        text : str
            all text extracted from text file
        """
        try:
            source_dir = sys.path[0]+"\..\.."
            with open(os.path.join(source_dir, text_file_path)) as file:
                text = file.read()
            return(text)
        except:
            return("")

f = FileReader()
f.extractText("source\input_coordinates.txt")