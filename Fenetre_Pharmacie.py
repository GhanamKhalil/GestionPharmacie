from tkinter import *
from tkinter.ttk import *
from Medicament import *
from Pharmacie import *
from tkinter import messagebox


class Fenetre_Pharmacie(Tk):

    Pha = Pharmacie()

    def __init__(self):
        super().__init__()
        self.iconphoto(False,PhotoImage(file="emoji.png"))

        self.title(" Gestion Pharmacie")
        self.geometry("550x380")
        self.InitializeComponents()

    def InitializeComponents(self):
        self.lab_ref = Label(self, text="Ref Médicament").place(x=20, y=30)
        self.var_ent_ref = StringVar(self)
        self.ent_ref= Entry(self,textvariable=self.var_ent_ref)
        self.ent_ref.place(x=140, y=30)

        self.lab_des = Label(self, text="Description").place(x=20, y=70)

        self.var_ent_des = StringVar(self)

        self.ent_des = Entry(self, textvariable=self.var_ent_des)
        self.ent_des.place(x=140, y=70)


        # Les Boutons
        btn_Vider = Button(self, text="Vider", command=self.Button_Vider_Click ,width=20)
        btn_Vider.place(x=400, y=20)

        btn_Rechercher = Button(self, text="Rechercher", command=self.Button_Rechercher_Click ,width=20)
        btn_Rechercher.place(x=400, y=50)

        btn_Ajouter = Button(self, text="Ajouter", command=self.Button_Ajouter_Click ,width=20)
        btn_Ajouter.place(x=400, y=80)

        btn_Modifier = Button(self, text="Modifier", command=self.Button_modifier_click ,width=20)
        btn_Modifier.place(x=400, y=110)

        btn_Supprimer = Button(self, text="Supprimer", command=self.Button_Supprimer_Click ,width=20)
        btn_Supprimer.place(x=400, y=140)

        #Frame et Radio Button ------------------------------------------------------------------
        self.ForMed = LabelFrame(self, text="Forme de Médicament", width=240 , height=120)
        self.ForMed.place(x=10, y=120)

        self.radio = IntVar(self)
        self.rad_Comp = Radiobutton(self, text="Comprimé", value=1, variable=self.radio)
        self.rad_Comp.place(x=40, y=140)

        self.rad_Sir = Radiobutton(self, text="Sirop", value=2, variable=self.radio)
        self.rad_Sir.place(x=40, y=160)

        self.rad_Pom = Radiobutton(self, text="Pommade", value=3, variable=self.radio)
        self.rad_Pom.place(x=40, y=180)

        self.rad_Inj = Radiobutton(self, text="Injection ", value=4, variable=self.radio)
        self.rad_Inj.place(x=40, y=200)
        #--------------------------------------------------------------------------------------------------------

        self.lab_prMed = Label(self, text="Prix Médicament").place(x=30, y=270)
        self.var_ent_prMed = StringVar(self)
        self.ent_prMed = Entry(self, textvariable=self.var_ent_prMed)
        self.ent_prMed.place(x=140, y=270)

        self.lab_qtMed = Label(self, text="Quantité ").place(x=30, y=300)
        self.var_ent_qtMed = StringVar(self)
        self.ent_qtMed = Entry(self, textvariable=self.var_ent_qtMed)
        self.ent_qtMed.place(x=140, y=300)

        #------------------ List des Médicaments ------------------
        self.btn_ListMed = Button(self, text="Afficher les Médicaments", width=25, command=self.Button_listMedicament_Afficher_Click)
        self.btn_ListMed.place(x=30, y=340)



        #------------------ Sauvgarder les Médicaments dans un fichier ------------------
        self.btn_File_Save = Button(self, text="Exporter Vers Fichier", width=20, command=self.Button_Exporter_Ficher_Click)
        self.btn_File_Save.place(x=400, y=170)


    #Le bouton Vider
    def Button_Vider_Click(self):
        self.var_ent_ref.set("")
        self.var_ent_des.set("")
        self.var_ent_prMed.set("")
        self.var_ent_qtMed.set("")
        self.radio.set(0)


    def Button_Rechercher_Click(self):
        ref = self.var_ent_ref.get()
        isExiste = Fenetre_Pharmacie.Pha.RechercherMedicament(ref)

        if isExiste != -1 :

            list=Fenetre_Pharmacie.Pha.ListeMedicaments[isExiste]

            self.var_ent_des.set(list.Description)

            self.var_ent_prMed.set(list.Prix)

            self.var_ent_qtMed.set(list.Quantite)

            if list.FormeMedicament == "Comprimé":
                self.radio.set(1)

            if list.FormeMedicament == "Sirop":
                self.radio.set(2)
            if list.FormeMedicament == "Pommade":
                self.radio.set(3)
            if list.FormeMedicament == "Injection":
                self.radio.set(4)
            messagebox.showinfo("Rechercher Médicament","Médicament est  Existé")
        if isExiste == -1:
            messagebox.showwarning("Rechercher Médicament","Médicament n'est pas Existé")

    #Le bouton Ajouter
    def Button_Ajouter_Click(self):
        Ref_Med = self.var_ent_ref.get()
        Des_Med = self.var_ent_des.get()
        Pri_Med = float(self.var_ent_prMed.get())
        Qat_Med = int(self.var_ent_qtMed.get())
        Form_Med = ""
        if self.radio.get() == 1:
            Form_Med = "Comprimé"
        if self.radio.get() == 2:
            Form_Med = "Sirop"
        if self.radio.get() == 3:
            Form_Med = "Pommade"
        if self.radio.get() == 4:
            Form_Med = "Injection"

        Medical = Medicament()

        Medical.RefMedicament = Ref_Med
        Medical.Description = Des_Med
        Medical.FormeMedicament = Form_Med
        Medical.Prix = Pri_Med
        Medical.Quantite = Qat_Med

        isExiste = Fenetre_Pharmacie.Pha.AjouterMedicament(Medical)

        if isExiste == True:
            messagebox.showinfo("Ajouter Médicament", "Médicament est Ajouté ")
        if isExiste == False:
            messagebox.showwarning("Ajouter Médicament", "Médicament est déja existe")

    def Button_modifier_click(self):
        med=Medicament()
        med.RefMedicament=self.var_ent_ref.get()
        med.Description=self.var_ent_des.get()
        med.Prix=self.var_ent_prMed.get()
        med.Quantite=self.var_ent_qtMed.get()
        if self.radio.get() == 1:
            med.FormeMedicament = "Comprimé"
        if self.radio.get() == 2:
            med.FormeMedicament  = "Sirop"
        if self.radio.get() == 3:
            med.FormeMedicament = "Pommade"
        if self.radio.get()== 4:
            med.FormeMedicament= "Injection"

        mod=Fenetre_Pharmacie.Pha.ModifierMedicament(med)


    def Button_Supprimer_Click(self):
        ref = self.var_ent_ref.get()
        isExiste = Fenetre_Pharmacie.Pha.SupprimerMedicament(ref)

        if isExiste == True:
            messagebox.showinfo("Supprimer Médicament", "Médicament est Supprimé ")
        if isExiste == False:
            messagebox.showwarning("Supprimer Médicament", "Médicament n'est pas existe")


    def Button_listMedicament_Afficher_Click(self):
        self.geometry("550x500")
        self.Var_ListMed = StringVar(self)
        self.List_Med = Listbox(self, listvariable=self.Var_ListMed, width=50, height=5)
        self.List_Med.place(x=30, y=370)

        listMedicament = []
        SaveFile = open("Medicament.txt", "r")
        for medical in SaveFile.readlines():
            listMedicament.append(medical)
        SaveFile.close()
        for mec in Fenetre_Pharmacie.Pha.ListeMedicaments:
            listMedicament.append(mec)

        self.Var_ListMed.set(listMedicament)

    #Le bouton Exporter Vers Fichier qui écrit la liste des médicaments dans le fichier texte : Medicaments.txt
    def Button_Exporter_Ficher_Click(self):
        SaveFile=open("Medicament.txt","a")
        for medical in Fenetre_Pharmacie.Pha.ListeMedicaments:
            SaveFile.write(str(medical))

        SaveFile.close()
        messagebox.showinfo("Sauvegarder des médicaments", "Les médicaments sont Sauvegardés")