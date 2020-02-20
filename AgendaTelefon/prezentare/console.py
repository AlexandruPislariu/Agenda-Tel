from exceptii.erori import ValidError,RepoError
class Console(object):
    
    
    def __init__(self, srvContact):
        self.__srvContact = srvContact
        self.__panou_comenzi()
        self.__comenzi = {
        'add':self.__ui_adauga_contact,
        'find':self.__ui_cauta_contact,
        'filter':self.__ui_filtreaza_contacte_grup,
        'export':self.__ui_exporta}
        
    def __panou_comenzi(self):
        pass
    
    def __ui_adauga_contact(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a adauga un nou contact
        """
        
        if len(parametrii)!=4: #id,nume,numar,grup
            raise ValueError("Numar incorect de date introduse")
        
        id = parametrii[0]
        nume = parametrii[1]
        numar = parametrii[2]
        grup = parametrii[3]
        
        self.__srvContact.adauga_contact(id,nume,numar,grup)
        
    def __ui_cauta_contact(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a cauta un contact
        """
        
        if len(parametrii)!=1: #nume
            raise ValidError("Numar incorect de date introduse")
        
        nume = parametrii[0]
        
        contact = self.__srvContact.cauta_contact(nume)
        
        if contact == -1:
            print("Contact inexistent")
        else:
            print(contact)
        
    def __ui_filtreaza_contacte_grup(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a filtra contactele dintr-un anumit grup
        """
        
        if len(parametrii)!=1 : #grup
            raise ValueError("Numar incorect de date introduse")
        
        grup = parametrii[0]
        contacte_filtrate = self.__srvContact.filtreaza_contacte_grup(grup)
        
        if contacte_filtrate == []:
            print("Nu exista contacte in acest grup")
        else:
            for contact in contacte_filtrate:
                print(contact)
                
    def __ui_exporta(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a exporta toate contactele unui grup intr-un fisier
        """
        if len(parametrii)!=1: #grup
            raise ValueError("Numar incorect de date introduse")
        
        grup = parametrii[0]
        
        self.__srvContact.exporta_contacte('./fisier_export.csv',grup)
        
    def run(self):
        """
    Functie principala de rulare a interfetei cu utilizatorul
        """
        
        while True:
            
            comanda = input("Introduceti comanda dorita! ")
            
            if comanda is None:
                print('Comanda invalida!')
                
            if comanda == 'exit':
                print('Aplicatia a fost inchisa cu succes!')
                break
            
            comanda = comanda.split(' ')
        #despart comanda
            nume_comanda = comanda[0]
            parametrii = comanda[1:]
            
        #verific daca exista comanda introdusa
            if nume_comanda in self.__comenzi.keys():
            #rulez comanda si tratez eventualele exceptii
                try:
                    self.__comenzi[nume_comanda](parametrii)
                except ValueError as ve:
                    print("UI error: \n" + str(ve))
                except ValidError as valide:
                    print("Valid error: \n" + str(valide))
                except RepoError as re:
                    print("Repo error: \n" + str(re))
            
            else:
            #Nu exista o asemenea comanda
                print("Comanda invalida!")
                    
    
    



