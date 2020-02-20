'''
Created on 1 feb. 2020

@author: Alex
'''
#teste
from teste.testeValid import TestValid
from teste.testeRepo import TestRepo
from teste.testeService import TestService

#validare
from validari.validation import ValidContact
validConctact = ValidContact()

#repository
from infrastructure.repository import RepositoryFile
from domain.entitati import Contact
repoContact = RepositoryFile('./agenda.txt',Contact)

#service
from business.service import ServiceContact
srvContact = ServiceContact(repoContact,validConctact)

#UI
from prezentare.console import Console
ui = Console(srvContact)
ui.run()