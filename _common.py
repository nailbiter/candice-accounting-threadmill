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

class Input:
    def __init__(self,):
        self._id = 0
    def input(self):
        id_ = self._id
        self._id += 1
        return f"""<input type="text" id="{id_}" name="{id_}"></input>"""
    def dropdown_1(self):
        choices = """
        普通預金
        支払利息
        前払利息
        未払利息
        次期繰越
        前期繰越
        損益
        繰越利益剰余金
        """
        choices = choices.split("\n")
        choices = [line.strip() for line in choices]
        choices = [choice for choice in choices if len(choice)>0]

        id_ = self._id
        self._id += 1

        res = f"<select name=\"{id_}\">"
        for choice in choices:
            res += f"""<option value="{choice}">{choice}</option>"""
        res += "</select>"
        return res
    def dropdown_2(self):
        choices = """
        受取
        未収
        前愛
        示払
        前払
        """
        choices = choices.split("\n")
        choices = [line.strip() for line in choices]
        choices = [choice for choice in choices if len(choice)>0]

        id_ = self._id
        self._id += 1

        res = f"<select name=\"{id_}\">"
        for choice in choices:
            res += f"""<option value="{choice}">{choice}</option>"""
        res += "</select>"
        return res
