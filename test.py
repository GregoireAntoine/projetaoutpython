from projet import *

imageclass1 = Laphoto('écureil','frame',2,0,'u')
imageclass2 = Laphoto('chapeau','frame2',2,1,'b')
imageclass3 = Laphoto('dromadaire','frame3',3,0,'o')
imageclass4 = Laphoto('bois[0]','frame4',3,1,'d')


class test(unittest.TestCase):
    def test_ligne(self):
        resultat = imageclass1.ligne  
        self.assertEqual( 2,resultat) # test la ligne de l'objet imageclass1

    def test_colonne(self):
        resultat = imageclass3.nom
        self.assertIn( 'a',resultat) # test la présence de la lettre 'a' dans l'objet imageclass3

    def test_colonne3(self):
        resultat = imageclass3.colonne  
        self.assertEqual( 0,resultat) # test la colonne de l'objet imageclass1

    def test_ligne3(self):
        resultat = imageclass3.ligne  
        self.assertEqual( 3,resultat) # test la ligne de l'objet imageclass3


    





# lancement des tests unitaires
if __name__ == '__main__' : 
  unittest.main()