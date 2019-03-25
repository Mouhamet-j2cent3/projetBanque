class Banque:
     def __init__(self,numerocarte):
         self.numerocarte=numerocarte

     def get_numerocarte(self):
             return self. numerocarte

     def __set__(self, numerocarte):
         self.numerocarte=numerocarte

     def verifiercarte(self,numerocarte):
          '''c'est une classe abstrait'''