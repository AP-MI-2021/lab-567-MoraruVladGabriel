from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testaMajoClasa, testIeftinire, testDetermPretMaximClasa, testOrdonareDescDupaPret\
    , testSumaPretNume
from Tests.testUndoRedo import testUndoRedo

def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testaMajoClasa()
    testIeftinire()
    testDetermPretMaximClasa()
    testOrdonareDescDupaPret()
    testSumaPretNume()
    testUndoRedo()
