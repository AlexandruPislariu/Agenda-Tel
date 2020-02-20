from exceptii.erori import ValidError
class ValidContact():
    
    def validare_contact(self,contact):
        """
    Functia valideaza un contact
        """
    #validez ID
        id = contact.get_id()
        try:
            id = int(id)
            
            if id<0:
                raise ValidError("ID invalid")
        except ValueError:
            raise ValidError("ID invalid")
         
    #validez numele
        nume = contact.get_nume()
        if nume is None:
            raise ValidError("Nume invalid")
        
    #validez numar de telefon
        numar = contact.get_numar()
        for cifra in numar:
            try:
                cifra = int(cifra)
            except ValueError:
                raise ValidError("Numar telefon invalid")
            
    #validez grupul
        grup = contact.get_grup()
        if grup!='Prieteni' and grup!='Familie' and grup!='Job' and grup!='Altele':
            raise ValidError("Grup invalid")
        
        return True


