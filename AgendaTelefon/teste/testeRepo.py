import unittest
from infrastructure.repository import RepositoryFile
from exceptii.erori import RepoError
from domain.entitati import Contact


class TestRepo(unittest.TestCase):
#In acesta clasa testez repository pentru contacte

    def setUp(self):
    #Se executa inainte de fiecare test
    #creez cateva contacte 
    
        self.repo = RepositoryFile('./fisier_test.txt',Contact)
        
        self.contact1 = Contact(1,'alex','072233','Familie')
        self.contact2 = Contact(2,'ana','072345','Prieteni')
        self.contact3 = Contact(4,'ion','072222','Job')
        self.contact4 = Contact(5,'alex','072258','Job')
        self.contact5 = Contact(6,'andrei','072233','Altele')
        self.contact6 = Contact(7,'catalin','072233','Prieteni')
        
    #adaug entitati in repo
        self.repo.adauga_entitate(self.contact1)
        self.repo.adauga_entitate(self.contact2)
        self.repo.adauga_entitate(self.contact3)
        
    def tearDown(self):
    #Golesc continutul fisierului dupa fiecare test
        fisier = open('./fisier_test.txt','w')
        fisier.seek(0)
        fisier.truncate()
        fisier.close()
        
    def test_get_all(self):
        
        self.assertEqual(self.repo.get_all(), [self.contact1,self.contact2,self.contact3])
        
    def test_adauga_entitate(self):
        
        with self.assertRaises(RepoError):
            self.repo.adauga_entitate(self.contact4)
            
        self.repo.adauga_entitate(self.contact5)
        self.repo.adauga_entitate(self.contact6)
        self.assertEqual(self.repo.get_all(), [self.contact1,self.contact2,self.contact3,self.contact5,self.contact6])
        
    def test_cauta_entitate(self):
        
        self.assertEqual(self.repo.cauta_entitate(self.contact6), -1)
        self.assertEqual(self.repo.cauta_entitate(self.contact1), 0)
        self.assertEqual(self.repo.cauta_entitate(self.contact3), 2)
        
        self.repo.adauga_entitate(self.contact6)
        self.assertEqual(self.repo.cauta_entitate(self.contact6), 3)
        
if __name__=='__main__':
    unittest.main()


