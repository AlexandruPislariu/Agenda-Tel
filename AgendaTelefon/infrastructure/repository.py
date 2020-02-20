from exceptii.erori import RepoError

class RepositoryFile():
    
    
    def __init__(self, filename, entity):
        self.__filename = filename
        self.__entity = entity
        self.__lista_entitati = []
        self.__read_all_from_file()
        
    def __read_all_from_file(self):
        """
    Functia citeste toate contactele din fisier si le adauga in lista din memorie
        """
        
        fisier = open(self.__filename,'r')
        
        content = fisier.read()   
    #despart in linii
        content = content.split('\n')
        
        for line in content:
            if line.strip() == '':
                continue
            
            entitate = self.__entity.read_entity(line)
            self.adauga_entitate(entitate)
            
        fisier.close()
        
    def __write_all_in_file(self):
        """
    Functia adauga contactele din lista din memori in fisier
        """
        
        fisier = open(self.__filename,'w')
        
    #Golesc continutul fisierului
        fisier.seek(0)
        fisier.truncate()
        
    #Preiau lista din memorie
        entitati = self.get_all()
        
    #Rescriu continutul fisierului
        for element in entitati:
                fisier.write(self.__entity.write_entity(element))
                fisier.write('\n')
                
        fisier.close()
        
    def get_all(self):
        """
    Functia returneaza lista entitatilor
        """
        return self.__lista_entitati
    
    def get_entitate(self,index):
        """
    Functia returneaza o entitate de pe un anumit index
        """
        return self.__lista_entitati[index]
    
    def cauta_entitate(self,entitate):
        """
    Functia cauta o entitate in functie de nume
    Daca exista se returneaza indicele din lista, altfel -1
        """
        
        entitati = self.get_all()
        
        for element in entitati:
            if element.get_nume() == entitate.get_nume():
                return entitati.index(element)
            
        return -1
    
    def adauga_entitate(self,entitate):
        """
    Functia adauga o entitate atat in fisier cat si in lista din memorie
    Daca exista deja o entitate cu acest nume se produce o eroare
        """
        index = self.cauta_entitate(entitate)
        
        if index!=-1: #se afla deja acest nume
            raise RepoError("Contact existent")
        
        self.__lista_entitati.append(entitate)#adaug in lista din memorie
        self.__write_all_in_file()#adaug si in fisier



