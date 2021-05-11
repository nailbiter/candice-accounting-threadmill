"""===============================================================================

        FILE: _common.py

       USAGE: (not intended to be directly executed)

 DESCRIPTION: 

     OPTIONS: ---
REQUIREMENTS: ---
        BUGS: ---
       NOTES: ---
      AUTHOR: Alex Leontiev (alozz1991@gmail.com)
ORGANIZATION: 
     VERSION: ---
     CREATED: 2021-05-09T14:28:51.296432
    REVISION: ---

==============================================================================="""
import os
from os import path


class Input:
    def __init__(self,):
        self._id = 0
        self._dropdowns = {}
        for fn in os.listdir("data/dropdowns"):
            if fn.endswith(".txt"):
                with open(path.join("data/dropdowns", fn)) as f:
                    content = f.read().strip()
                self._dropdowns[fn[:-4]] = [line.strip()
                                            for line in content.split("\n") if len(line.strip()) > 0]

    def input(self):
        id_ = self._id
        self._id += 1
        return f"""<input type="text" id="{id_}" name="{id_}"></input>"""

    def dropdown_names(self):
        res = list(self._dropdowns)
#        print(f"dropdown_names: {res}")
        return res

    def dropdown(self, dropdown_name):
        choices = self._dropdowns[str(dropdown_name)]
        choices = ["",*choices]
#        print(f"{dropdown_name} => {choices}")

        id_ = self._id
        self._id += 1

        res = f"<select name=\"{id_}\">"
        for choice in choices:
            res += f"""<option value="{choice}">{choice}</option>"""
        res += "</select>"
        return res
