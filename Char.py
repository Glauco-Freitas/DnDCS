class Char:
    def __init__(self, name, clas, nvl, bckgrd, allig, race):
        self.__name = name
        self.__clas = clas
        self.__nvl = nvl
        self.__bckgrd = bckgrd
        self.__allig = allig
        self.__race = race

        self.__prof = 2

        if 4 < self.__clas < 9:
            self.__prof = 3
        elif 8 < self.__clas < 13:
            self.__prof = 4
        elif 12 < self.__clas < 17:
            self.__prof = 5
        elif 16 < self.__clas < 21:
            self.__prof = 6
        else:
            self.__prof = 7

    @property
    def prof(self):
        return self.__prof
