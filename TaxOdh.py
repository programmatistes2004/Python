import webbrowser
from MesiTelos3 import (elenxos_polis,dromologia,axiotheata)
#Συνάρτηση μετατροπής της πόλης για τον καιρό
def metatrop1(poli2):
    """ Σε αυτή την συνάρτηση μετατρέπουμε τα δεδομένα που έχει δώσει ο χρήστης για την πόλη σε αγγλικούς
    χαρακτήρες ώστε να μπορέσουμε να τους χρησημοποιήσουμε στο API της openweathermap, το οποίο μας δίνει
    δεδομένα για το καιρό μιας πόλης """
    if poli2 == "Θήβα":
        agk="Thebes"
        return agk
    elif poli2 == "Λιβαδειά":
        agk="Levadeia"
        return agk
    elif poli2 == "Άμφισσα":
        agk="Amfissa"
        return agk
    elif poli2 == "Δελφοί":
        agk="Delphi"
        return agk
    elif poli2 == "Αγρίνιο" :
        agk="Agrinio"
        return agk
    elif poli2 == "Μεσολόγγι":
        agk="Missolonghi"
        return agk
    elif poli2 == "Ναύπακτος":
        agk="Naupactus"
        return agk
    elif poli2 == "Βόνιτσα":
        agk="Vonitsa"
        return agk
    elif poli2 == "Καρπενήσι":
        agk="Karpenissi"
        return agk
    elif poli2=="Δομιανοί":
        agk = "Domiani"
        return agk
    elif poli2 == "Λαμία":
        agk = "Lamia"
        return agk
    elif poli2 == "Αταλάντη":
        agk = "Atalanti"
        return agk
    elif poli2 == "Χαλκίδα":
        agk = "Chalcis"
        return agk
    elif poli2 == "Ερέτρια":
        agk = "Eretria"
        return agk
    elif poli2 == "Κάρυστος":
        agk = "Karystos"
        return agk
    elif poli2 == "Αθήνα":
        agk = "Athens"
        return agk
    elif poli2 == "Πειραιάς":
        agk = "Pireus"
        return agk
#συνάρτηση για την εμφάνιση του καιρού
def kairos (poli2,poli):
    import requests
    """Σε αυτή την συνάρτηση χρησιμοποιούμε την βιβλιοθήκη request για να μπορέσουμε να επικοινωνήσουμε με το API 
    open wearther map για να πάρουμε δεδομένα καιρού και να τα τυπόσουμε στον χρήστη  """
    city = poli2
    api_key = '5216301f8bd2fee607afc86af9be3a8d'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temp_avg = data['main']['temp']
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']
    print(f'Η τωρινή θερμοκρασία στην {poli} ειναι  {temp_avg:.1f}°C')
    print(f'Η μέγιστη θερμκρασία στην {poli} ειναι {temp_max:.1f}°C')
    print(f'Η ελάχιστη θερμοκρασία στην {poli} ειναι {temp_min:.1f}°C')
#Συνάρτηση για τα εστιατόρια
def estiatoria(poli2):
    """Σε αυτή την συνάρτηση χρησημοποιούμε τις εντολές if και elif και την βιβλιοθήκη webbrowserr
    για να ελέγξουμε ποιά πόλη έχει επιλέξει ο χρηστης ώστε να του δώσουμε σωστές πληροφορίες για τα εστιατόρια
    μέσο της σελίδας του trip advisor"""
    poli2 = elenxos_polis(poli)
    if poli2 == "Θήβα":
        webbrowser.open_new_tab('https://www.tripadvisor.com/Restaurants-g814414-Thiva_Boeotia_Region_Central_Greece.html')
    elif poli2 == "Λιβαδειά":
        webbrowser.open_new_tab('https://www.google.gr/maps/search/%CE%B1%CE%BC%CF%86%CE%B9%CF%83%CF%83%CE%B1+%CE%B5%CF%83%CF%84%CE%B9%CE%B1%CF%84%CE%BF%CF%81%CE%B9%CE%B1/@38.5268357,22.3737959,16z/data=!3m1!4b1')
    elif poli2 == "Άμφισσα":
        webbrowser.open_new_tab('https://www.google.gr/maps/search/%CE%B1%CE%BC%CF%86%CE%B9%CF%83%CF%83%CE%B1+%CE%B5%CF%83%CF%84%CE%B9%CE%B1%CF%84%CE%BF%CF%81%CE%B9%CE%B1/@38.5268357,22.3737959,16z/data=!3m1!4b1')
    elif poli2 == "Δελφοί":
        webbrowser.open_new_tab('https://www.tripadvisor.com/Restaurants-g189408-Delphi_Phocis_Region_Central_Greece.html')
    elif poli2 == "Αγρίνιο":
        webbrowser.open_new_tab('https://www.tripadvisor.com/Restaurants-g667823-Agrinio_Aetolia_Acarnania_Region_West_Greece.html')
    elif poli2 == "Μεσολόγγι":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g1787090-Mesolongion_Aetolia_Acarnania_Region_West_Greece.html')
    elif poli2 == "Ναύπακτος":
        webbrowser.open_new_tab('https://www.google.gr/maps/search/%CE%9D%CE%B1%CF%85%CF%80%CE%B1%CE%BA%CF%84%CE%BF%CF%82+%CE%B5%CF%83%CF%84%CE%B9%CE%B1%CF%84%CE%BF%CF%81%CE%B9%CE%B1/@38.390996,21.8117491,14z/data=!3m1!4b1')
    elif poli2 == "Βόνιτσα":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g3216426-Vonitsa_Aetolia_Acarnania_Region_West_Greece.html')
    elif poli2 == "Καρπενήσι":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g793702-Karpenisi_Evrytania_Region_Central_Greece.html')
    elif poli2 == "Δομιανοί":
        webbrowser.open_new_tab('https://www.google.gr/maps/search/%CE%B4%CE%BF%CE%BC%CE%B9%CE%B1%CE%BD%CE%BF%CE%B9++%CE%B5%CF%83%CF%84%CE%B9%CE%B1%CF%84%CE%BF%CF%81%CE%B9%CE%B1/@39.0434828,21.6701003,11z/data=!3m1!4b1')
    elif poli2 == "Λαμία":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g970269-Lamia_Phthiotis_Region_Central_Greece.html')
    elif poli2 == "Αταλάντη":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g6958927-Atalandi_Phthiotis_Region_Central_Greece.html')
    elif poli2 == "Χαλκίδα":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g189455-Khalkis_Euboea_Region_Central_Greece.html')
    elif poli2 == "Ερέτρια":
        webbrowser.open_new_tab('https://www.google.gr/maps/search/%CE%B5%CF%81%CE%B5%CF%84%CF%81%CE%B9%CE%B1+%CE%B5%CF%83%CF%84%CE%B9%CE%B1%CF%84%CE%BF%CF%81%CE%B9%CE%B1/@38.3932878,23.7928049,15z/data=!3m1!4b1')
    elif poli2 == "Κάρυστος":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g1146717-Karystos_Euboea_Region_Central_Greece.html')
    elif poli2 == "Αθήνα":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g189400-Athens_Attica.html')
    elif poli2 == "Πειραιάς":
        webbrowser.open_new_tab('https://www.tripadvisor.com.gr/Restaurants-g189403-Piraeus_Piraeus_Region_Attica.html')






"""Εδώ έχουμε το κύριο πρόγραμμα"""
flo2=0
epilogi=""
poli = input(" Δώστε την πόλη για την οποία θελετε πληροφορίες ")
""" Εδώ ο χρήστης βάζει τα δεδομένα στην μεταβλητή polis και μετά καλούμε την συνάρτηση elenxos_polis για να διορθόσουμε τα ορθογραφικά"""
poli = elenxos_polis(poli)
AgkP = metatrop1(poli)
"""Εδώ πέρνουμε τα διορθομένα δεδομένα της πόλης και τα μετατρέπουμε σε αγγλικούς χαρακτήρες ώστε να τα χρησημοποιήσουμε στην συνάρτηση του καιρού """
flag0=0
"""Χρησημοποιούμε την μεταβλητή flag0 σαν μια σημαία στην οποία όταν της δωθεί η τιμή 1 
θα σταματήσει το πρόγραμμα και αυτό το καθορίζουν οι εντολές if και elif δηλαδή 
ανάλογα με το τι θέλει ο χρήστης αν θέλει να σταματήσει να το χρησιμοποιεί
το πρόγραμμα απλά βάζει τιμή απο 1 εως 5 για το τι θέλει στην μεταβλητή 'epilogi' αυτό θα το δούμε παρακάτω"""
c=0
poli_tax2=""
while flag0==0 :
    #πρωτη φορα που θα τρεχει

    if c==0:

        print("Επιλογές πληροφοριών \n 1 Δρομολόγια ανα πόλη \n 2 Αλλαγή πόλης \n 3 Αξιοθέατα \n 4 Καιρός \n 5 Εστιατόρια \n 0 Τερματισμό προγράμματος ")

        flo=0
        while flo==0 :

            epilogi = input("")
            c+=1
            while flo == 0:
                if epilogi in ["1", "2", "3", "4", "5", "0"]:
                    flo = 1
                else:
                    print("Δώστε έναν από τους αριθμούς των επιλογών (0 /5) /n")
                    epilogi = input("")

        if epilogi == "1":
            mphke=0


            if mphke==0 :

                dromologia(poli)


            c += 1
        elif epilogi == "2":
            poli = input(" Δώστε την πόλη για την οποία θελετε πληροφορίες ")
            c += 1
            AgkP = metatrop1(poli)
            flo2=1
        elif epilogi == "3":
            poli2=poli
            axiotheata(poli)
            c += 1
        elif epilogi=="4":
            AgkP = metatrop1(poli)
            poli2 = AgkP
            kairos(poli2,poli)
            c += 1
        elif epilogi=="5" :
            estiatoria(poli)
        elif epilogi == "0":
            flag0 = 1
        else:
            flag0=1
#για τις υπολοιπες
    while flag0==0 :
        flo=0
        if c>=1 :
         if flag0 == 0 :
            if flo2!=1:
                print("\n Θέλετε να συνεχίστε με παραπάνω πληροφορίες; ")
                den_psinetai=input("")
            elif flo2==1 :
                den_psinetai="Ναι"
            if den_psinetai == "Ναι" or den_psinetai =="ναι" or den_psinetai =='ΝΑΙ':
                print("Επιλογές πληροφοριών \n 1 Δρομολόγια ανα πόλη \n 2 Αλλαγή πόλης \n 3 Αξιοθέατα \n 4 Καιρός \n 5 Εστιατόρια \n 0 Τερματισμό προγράμματος ")
                epilogi=input("")
                while flo==0:
                    if epilogi in ["1", "2", "3", "4", "5", "0"]:
                        flo = 1
                    else:
                        print("Δώστε έναν από τους αριθμούς των επιλογών (0 /5) /n")
                        epilogi=input("")
                if epilogi == "1":
                    dromologia(poli)
                    c += 1
                    flo2=0
                elif epilogi == "2":
                    poli = input(" Δώστε την πόλη για την οποία θέλετε πληροφορίες ")
                    c += 1
                    poli=elenxos_polis(poli)
                    AgkP = metatrop1(poli)
                    flo2=1
                elif epilogi=="3":
                    axiotheata(poli)
                    c+=1
                    flo2=0
                elif epilogi=="4":
                    poli2 = AgkP
                    kairos(poli2,poli)
                    c+=1
                    flo2=0
                elif epilogi=="5":
                    estiatoria(poli)
                    flo2=0
                elif epilogi == "0":
                    flag0 = 1
                    flo2=0

            else:
                flag0=1


