class Attrib:

    def __init__(self, str, dex, con, wis, int, cha):
        self.__str = str
        self.__dex = dex
        self.__con = con
        self.__wis = wis
        self.__int = int
        self.__cha = cha
        self.__modstr = 0
        self.__moddex = 0
        self.__modcon = 0
        self.__modwis = 0
        self.__modint = 0
        self.__modcha = 0

        mod = [self.__str, self.__dex, self.__con, self.__wis, self.__int, self.__cha]
        for i in range(6):
            if mod[i] == 8 or mod[i] == 9:
                mod[i] = -1
            elif mod[i] == 10 or mod[i] == 11:
                mod[i] = 0
            elif mod[i] == 12 or mod[i] == 13:
                mod[i] = 1
            elif mod[i] == 14 or mod[i] == 15:
                mod[i] = 2
            elif mod[i] == 16 or mod[i] == 17:
                mod[i] = 3
            elif mod[i] == 18 or mod[i] == 19:
                mod[i] = 4
            elif mod[i] == 20 or mod[i] == 21:
                mod[i] = 5
            elif mod[i] == 22 or mod[i] == 23:
                mod[i] = 6
            elif mod[i] == 24 or mod[i] == 25:
                mod[i] = 7

        self.__modstr = mod[0]
        self.__moddex = mod[1]
        self.__modcon = mod[2]
        self.__modwis = mod[3]
        self.__modint = mod[4]
        self.__modcha = mod[5]