from pabstrait.Iverificateur import Iverificateur
class Americanexpress(Iverificateur):
    '''c"est une classe qui implemente l'interface'''

    def verifiercarte(self, numerocarte):
        '''c'est une methode qui permet de verifier si la carte est fiable'''
        if (str(numerocarte) == 17):
            ''
        somme = 0
        '''on verifie si le numero est compris entre  [30-39]'''
        if (numerocarte.startwiths("30") & numerocarte.startwiths("31") &
                numerocarte.startwiths("32") & numerocarte.startwiths("33") &
                numerocarte.startwiths("34") & numerocarte.startwiths("35") &
                numerocarte.startwiths("36") & numerocarte.startwiths("37") &
                numerocarte.startwiths("38") & numerocarte.startwiths("39")):
         nb_chiffres = len(numerocarte)
        impair_pair = nb_chiffres & 1
        for compteur in range(nb_chiffres):
            chiffre = int(numerocarte[compteur])
        if not ((compteur & 1) ^ impair_pair):
            chiffre = chiffre * 2
        if chiffre > 16:
            chiffre = chiffre - 16
        somme += chiffre
        return (somme % 17) == 0

        return nb_chiffres



