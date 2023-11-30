#super class
class documentaire() :
    __NbO = 0
    def __init__(self, titre, datesortie) : 
        self.__titre = titre 
        self.__datesortie = datesortie 
        documentaire.__NbO = documentaire.__NbO + 1
        self.__code = documentaire.__NbO

#getters and setters
    def getcode(self) :
        return self.__code
    
    def gettitre(self) :
        return self.__titre
    
    def getdatesortie(self) :
        return self.__datesortie
    
    def getNbO(self) :
        return documentaire.__NbO
    
    def setcode(self, code) :
        self.__code = code 

    def settitre(self, titre) :
        self.__titre = titre

    def setdatesortie(self, datesortie) :
        self.__datesortie = datesortie

#methodes
    def ToString(self) :
        return ("code = ", self.getcode(), "titre = ", self.gettitre(), "date de sortie = ", self.getdatesortie())
    
    def equals(self, D) :
        code1 = self.getcode()
        code2 = D.getcode()
        if code1 == code2 :
            return True
        else :
            return False 

#subclass
class examplaire(documentaire) :
    def __init__(self, titre, datesortie, numero, dateachat):
        super().__init__(titre, datesortie)
        self.__numero = numero 
        self.__dateachat = dateachat

#getters and setters 
    def getnumero(self) :
        return self.__numero 
    
    def getdateachat(self) : 
        return self.__dateachat
    
    def setnumero(self, numero) :
        self.__numero = numero 

    def setdateachat(self, dateachat) :
        self.__dateachat = dateachat

#methodes
    def ToString(self):
        return (super().ToString(), "numero = ", self.getnumero(), "date d'achat = ", self.getdateachat())
    
    def equals(self, D):
        numero1 = self.getnumero()
        numero2 = D.getnumero()
        if numero1 == numero2 :
            return True
        else :
            return False

#making_first_object
dcm1 = documentaire(titre="Oussama", datesortie= 22/11/2023)
print("le titre est : ", dcm1.gettitre())
print("la date de sortie est : ", dcm1.getdatesortie())















