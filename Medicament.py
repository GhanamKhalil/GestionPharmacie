class Medicament:
    def __init__(self):
        self.RefMedicament=""
        self.Description=""
        self.FormeMedicament=""
        self.Prix=0.0
        self.Quantite=0
    def __str__(self):
        ph=f"{self.RefMedicament};{self.Description};{self.FormeMedicament};{self.Prix};{self.Quantite}"
        return ph