class Pharmacie:
    def __init__(self):
        self.NomPharmacie = ""
        self.Adresse = ""
        self.ListeMedicaments = []

    def RechercherMedicament(self, ref):
        for i in range(len(self.ListeMedicaments)):
            if self.ListeMedicaments[i].RefMedicament == ref:
                return i
        else:
            return -1

    def AjouterMedicament(self, mec):
        if self.RechercherMedicament(mec.RefMedicament) == -1:
            self.ListeMedicaments.append(mec)
            return True
        else:

            return False

    def SupprimerMedicament(self, ref):
        b=self.RechercherMedicament(ref)
        if b != -1 :
            self.ListeMedicaments.pop(b)
            return True
        else:
            return False

    def ModifierMedicament(self,mec):
        i=self.RechercherMedicament(mec.RefMedicament)
        if i != -1:
            self.ListeMedicaments[i]=mec
            return True
        else:
            return False