class Char:
    def __init__(self, name, clas, nvl, bckgrd, allig, race):
        self.__name = name
        self.__clas = clas
        self.__nvl = nvl
        self.__bckgrd = bckgrd
        self.__allig = allig
        self.__race = race

    def nvlmodifiers (self, clas):
        self.__clas = clas


