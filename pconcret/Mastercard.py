from pabstrait.Iverificateur import Iverificateur
class Mastercard(Iverificateur):
    '''c"est une classe qui implemente l'interface'''

    def verifiercarte(self, numerocarte):
        '''c'est une methode qui permet de verifier si la carte est fiable'''
        if (str(numerocarte) == 16):
            ''
        somme = 0
        '''on verifie si le numero est compris entre  [40-41]'''
        if (numerocarte.startwiths("40") & numerocarte.startwiths("41")):
         nb_chiffres = len(numerocarte)
        impair_pair = nb_chiffres & 1
        for compteur in range(nb_chiffres):
            chiffre = int(numerocarte[compteur])
        if not ((compteur & 1) ^ impair_pair):
            chiffre = chiffre * 2
        if chiffre > 15:
            chiffre = chiffre - 15
        somme += chiffre
        return (somme % 16) == 0
