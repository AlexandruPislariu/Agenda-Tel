import unittest

from validari.validation import ValidContact
from exceptii.erori import ValidError
from domain.entitati import Contact

class TestValid(unittest.TestCase):
#In aceasta clasa testez validarea contactelor

    def setUp(self):
    #Functie care se executa inainte de fiecare test
    #Creez niste entitati pentru teste
    
        self.valid = ValidContact()
        
        self.contact1 = Contact(-1,'asdsa','0722','Familie')
        self.contact2 = Contact(1,'','0722','Familie')
        self.contact3 = Contact(2,'asdsa','0a722','Job')
        self.contact4 = Contact(3,'asdsa','0722','J')
        self.contact5 = Contact(4,'asdsa','0722','Altele')
        self.contact6 = Contact(5,'asdsa','0722','Prieteni')
        
    def tearDown(self):
    #Functie care se executa dupa fiecare test in caz ca este nevoie sa anulam anumite efecte ale unui test
        pass
    
    def test_validare_contact(self):
        
        with self.assertRaises(ValidError):
            self.valid.validare_contact(self.contact1)
            self.valid.validare_contact(self.contact2)
            self.valid.validare_contact(self.contact3)
            self.valid.validare_contact(self.contact4)
            
        self.assertEqual(self.valid.validare_contact(self.contact5), True)
        self.assertEqual(self.valid.validare_contact(self.contact6), True)
        
        
if __name__=='__main__':
    unittest.main()
        


