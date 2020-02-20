from domain.entitati import Contact
import csv
class ServiceContact(object):
    
    
    def __init__(self, repoContact, validConctact):
        self.__repoContact = repoContact
        self.__validConctact = validConctact
        
    def adauga_contact(self,id,nume,numar,grup):
        
    #creez o entitate contact cu aceste atribute
        contact = Contact(id,nume,numar,grup)  
    #verific daca este valida
        if self.__validConctact.validare_contact(contact):
        #adaug in repository
            self.__repoContact.adauga_entitate(contact)
    
    
    def cauta_contact(self,nume):
    
    #creez o entitate contact cu acest nume
        contact = Contact(0,nume,'0722','Altele')
    #verifica daca este valida
        if self.__validConctact.validare_contact(contact):
            index = self.__repoContact.cauta_entitate(contact)
            
            if index == -1:
                return -1
            else:
                return self.__repoContact.get_entitate(index)

    def filtreaza_contacte_grup(self,grup):
        
    #Preiau contactele
        contacte = self.__repoContact.get_all()
    #Retin doar contactele care fac parte din acest grup
        contacte_grup = []
        for contact in contacte:
            if contact.get_grup() == grup:
                contacte_grup.append(contact)
                
    #Verific daca exista contacte in acest grup
        if contacte_grup == []:
            return contacte_grup
        else:
        #Ordonez crescator contactele dupa nume
            return sorted(contacte_grup,key = lambda x: x.get_nume())
        
    def exporta_contacte(self,nume_fisier,grup):
        
    #Preiau contactele
        contacte = self.__repoContact.get_all()
    #Retin doar contactele care fac parte din acest grup
        contacte_grup = []
        for contact in contacte:
            if contact.get_grup() == grup:
                contacte_grup.append(contact)
                
    #Le scriu intr-un fisier csv
        
        with open(nume_fisier, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for contact in contacte_grup:
                writer.writerow(contact.get_nume())
                writer.writerow(contact.get_numar())