from Tests.testCRUD import testAdaugaRezervare
from Tests.testDomain import testRezervare


def runAllTests():
    testRezervare()
    testAdaugaRezervare()