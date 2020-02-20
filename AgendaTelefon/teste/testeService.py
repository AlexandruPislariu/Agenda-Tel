import unittest
from business.service import ServiceContact
from infrastructure.repository import RepositoryFile
from validari.validation import ValidContact
from domain.entitati import Contact


class TestService(unittest.TestCase):
#In acesta clasa testez service-ul aplicatiei

    def setUp(self):
    #Adaug entitati in repository pentru fiecare test
    
        self.repo = RepositoryFile('./fisier_test.txt',Contact)
        self.valid = ValidContact()
        self.service = ServiceContact(self.repo,self.valid)
        
        self.contact1 = Contact(1,'alex','072233','Familie')
        self.contact2 = Contact(2,'ana','072345','Familie')
        self.contact3 = Contact(4,'ion','072222','Familie')
        self.contact4 = Contact(5,'artimon','072258','Familie')
        self.contact5 = Contact(6,'andrei','072233','Altele')
        self.contact6 = Contact(7,'catalin','072233','Familie')

        self.repo.adauga_entitate(self.contact1)
        self.repo.adauga_entitate(self.contact2)
        self.repo.adauga_entitate(self.contact3) 
        self.repo.adauga_entitate(self.contact4)
        self.repo.adauga_entitate(self.contact5)
        self.repo.adauga_entitate(self.contact6)
       
        
    def tearDown(self):
    #Golesc continutul fisierului dupa fiecare test
        fisier = open('./fisier_test.txt','w')
        fisier.seek(0)
        fisier.truncate()
        fisier.close()
        
    def test_filtreaza_contacte_grup(self):
        
        rezultat = self.service.filtreaza_contacte_grup('Familie')
        self.assertEqual(rezultat[0].get_id(), self.contact1.get_id())
        self.assertEqual(rezultat[1].get_id(), self.contact2.get_id())
        self.assertEqual(rezultat[2].get_id(), self.contact4.get_id())
        self.assertEqual(rezultat[3].get_id(), self.contact6.get_id())
        
        rezultat = self.service.filtreaza_contacte_grup('Job')
        self.assertEqual(rezultat, [])
        
if __name__=='__main__':
    unittest.main()
        
