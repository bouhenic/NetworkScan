import json
import os
import re
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("600x300")
root.title("SCANNER RESEAU")

var_réseau = tk.StringVar()

def scan():
    #Scan du réseau en utilisant arp-scan à installer préalablement, le résultat est copié en fichier texte resulktat.txt
    resultat = os.system(f"arp-scan {var_réseau.get()} > resultat.txt")
    with open("./resultat.txt", "r") as f:#ouverture de resulktat.txt
        contenu = f.read() #lecture du fichier
        regex = re.compile("(([0-9]{1,3}\.){3}[0-9]{1,3})\s([a-fA-F0-9:]{17})\s(\w*\,*)") #regex IP,MAC et HOST
        resultat = regex.findall(contenu) #recherche des matchs entre regex et contenu (fichier texte)
        nbrmatch = len(resultat)#détermination du nombre de match
        IP = ""

        for i in range(nbrmatch):
            IP += resultat[i][0] + "\n" #lecture des matchs IP set stockage dans la variable IP
            varip.set(f"{IP}")

        MAC = ""
        for i in range(nbrmatch):
            MAC += resultat[i][2] + "\n" #lecture des matchs MAC set stockage dans la variable MAC
            varmac.set(f"{MAC}")

        HOST = ""
        for i in range(nbrmatch):
            HOST += resultat[i][3] + "\n" #lecture des matchs MAC set stockage dans la variable MAC
            varhost.set(f"{HOST}")

#détermination des frames
frame_quitter=ttk.Frame(root)
frame_quitter.pack(fill="x",side="bottom",ipady=20)
frame_button=ttk.Frame(root)
frame_button.pack(fill="x",side="bottom")
frame_ip=ttk.Frame(root)
frame_ip.pack(fill="both",side="left",expand="true",pady=10)
frame_mac = ttk.Frame(root)
frame_mac.pack(fill="both",side="left",expand="true",pady=10)
frame_host = ttk.Frame(root)
frame_host.pack(fill="both",side="left",expand="true",pady=10)

varip=tk.StringVar()
varmac=tk.StringVar()
varhost=tk.StringVar()

Nom_addIP=tk.Label(frame_ip,text="ADRESSE IP :",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(side="top",fill="both")
adressesIp=tk.Message(frame_ip,textvariable=varip).pack(side="top",fill="both")
Nom_addMAC=tk.Label(frame_mac,text="ADRESSE MAC :",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(side="top",fill="both")
adressesMAC=tk.Message(frame_mac,textvariable=varmac).pack(side="top",fill="both")
Nom_host=tk.Label(frame_host,text="HOST :",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(side="top",fill="both")
host=tk.Message(frame_host,textvariable=varhost).pack(side="top",fill="both")

Nom_reseau=tk.Label(frame_button,text="IP RESEAU CIDR :",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(side="left",fill="both",expand="true")
entry_reseau = tk.Entry(frame_button,textvariable=var_réseau,width=20).pack(side="left",fill="both",expand="true")
bouton_envoyer = ttk.Button(frame_button,text="SCANNER", command=scan)
bouton_envoyer.pack(side="left",expand="true")

bouton_quitter = ttk.Button(frame_quitter,text="QUITTER", command=root.destroy)
bouton_quitter.pack(side="left",expand="true")

root.mainloop()
