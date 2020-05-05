# Variables décimales.
ip_adress = input("Entrez une adresse ip : ")
ss_nw_mask = input("Entrez un masque de sous-réseau : ")

# Variables listes.
ip_adress_list = ip_adress.split(".")
ss_nw_mask_list = ss_nw_mask.split(".")

# Variables binaires.
ip_adress_bin = []
ss_nw_mask_bin = []

for elt in ip_adress_list:
    mot_final = []
    mot_final_conv = ""
    mot_depart = int(elt)
    while mot_depart > 0:
        mot_final.append(mot_depart % 2)
        mot_depart = int(mot_depart / 2)
    while len(mot_final) < 8:
        mot_final.append(0)
    mot_final.reverse()
    for elt in mot_final:
        mot_final_conv += str(elt)
    ip_adress_bin.append(mot_final_conv)

for elt in ss_nw_mask_list:
    mot_final = []
    mot_final_conv = ""
    mot_depart = int(elt)
    while mot_depart > 0:
        mot_final.append(mot_depart % 2)
        mot_depart = int(mot_depart / 2)
    while len(mot_final) < 8:
        mot_final.append(0)
    mot_final.reverse()
    for elt in mot_final:
        mot_final_conv += str(elt)
    ss_nw_mask_bin.append(mot_final_conv)

# Et logique.
nw_adress_bin = []
nw_adress_bin_octet = ""
for i in range(0, len(ip_adress_bin)):
    nw_adress_bin_octet = ""
    for j in range(0, len(ip_adress_bin[i])):
        if ip_adress_bin[i][j] + ss_nw_mask_bin[i][j] == "11":
            nw_adress_bin_octet += "1"
        else:
            nw_adress_bin_octet += "0"
    nw_adress_bin.append(nw_adress_bin_octet)

nw_adress = []
for octet in nw_adress_bin:
    mot_final = 0
    mot_depart = octet
    mot_a_traduire = []
    for i in range(0, len(mot_depart), 1):
        mot_a_traduire.append(int(mot_depart[i]))
    mot_a_traduire.reverse()
    for i in range(0, len(mot_a_traduire), 1):
        mot_final += mot_a_traduire[i] * 2 ** i
    nw_adress.append(mot_final)

nw_adress_final = ""
for num in nw_adress:
    nw_adress_final += str(num)
    nw_adress_final += "."
nw_adress_final = nw_adress_final[:-1]

print()

# Vérification classe.
if nw_adress[0] <= 127:
    print("Adresse de classe A.")
    if ss_nw_mask_list[0] == "255":
        print("Sous-réseau par défaut.")
    else:
        print("Sous-réseau personnalisé.")
elif 128 <= nw_adress[0] <= 191:
    print("Adresse de classe B.")
    if ss_nw_mask_list[0] == "255" and ss_nw_mask_list[1] == "255":
        print("Sous-réseau par défaut.")
    else:
        print("Sous-réseau personnalisé.")
elif 192 <= nw_adress[0] <= 223:
    print("Adresse de classe C.")
    if ss_nw_mask_list[0] == "255" and ss_nw_mask_list[1] == "255" and ss_nw_mask_list[2] == "255":
        print("Sous-réseau par défaut.")
    else:
        print("Sous-réseau personnalisé.")
elif 224 <= nw_adress[0] <= 239:
    print("Adresse de classe D.")
elif 240 <= nw_adress[0] <= 255:
    print("Adresse de classe E.")

# Adresses particulières.
if nw_adress[0] == 0:
    print("Adresse par défaut.")
elif nw_adress[0] == 127:
    print("Localhost.")
elif nw_adress[0] == 169 and nw_adress[1] == 154:
    print("Adresse APIPA.")

print("L'adresse du réseau est : {}".format(nw_adress_final))