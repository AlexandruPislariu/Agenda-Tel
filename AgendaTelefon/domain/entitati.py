class Contact():
#In aceasta clasa manageriez contactele

    def __init__(self,id,nume,numar,grup):
    #Atributele unui contact
        self.__id = id
        self.__nume = nume
        self.__numar = numar
        self.__grup = grup

    def get_id(self):
        return self.__id


    def get_nume(self):
        return self.__nume


    def get_numar(self):
        return self.__numar


    def get_grup(self):
        return self.__grup


    def set_numar(self, value):
        self.__numar = value


    def set_grup(self, value):
        self.__grup = value
        
    def __str__(self):
        
        str(str(self.get_id()) + ' ' + self.get_nume() + ' ' + self.get_numar() + ' ' + self.get_grup())

    @classmethod
    def read_entity(cls,line):
        """
    Functia transforma un string intr-o entitate contact
        """
        line = line.split(' ')
        id = int(line[0])
        nume = line[1]
        numar = line[2]
        grup = line[3]
        
        return Contact(id,nume,numar,grup)
    
    @classmethod
    def write_entity(cls,entitate):
        """
    Functia transforma o entitate contact intr-un string pentru a putea fi scrisa pe o linie a fisierului
        """
        
        return str(str(entitate.get_id()) + ' ' + entitate.get_nume() + ' ' + entitate.get_numar() + ' ' + entitate.get_grup())
        

