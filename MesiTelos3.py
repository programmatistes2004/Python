import webbrowser

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# συναρτήσεις προγράμματος

#Σε αυτή την συνάρτηση ελέγχουμε την ορθογραφία της πόλης να είναι σωστή και μετά επιστρέφουμε σωστό αποτέλεσμα
def elenxos_polis(polis):
    flag = 0 # Η μεταβλητή flag αντιπροσωπευεί μια σημαία στην οποία πέρνει την τιμή 1 οταν ο χρήστης έχει βάλει μία από τις πόλεις παρακάτω
    while flag == 0:  # Μέσα στην while εχει γραφτεί ο αλγόριθμος του ελέγχου για την ορθογραφία
        if polis == "Λιβαδεία" or polis == "Λιβαδεια" or polis == "λιβαδεία" or polis == "λιβαδεια": #Χρησημοποιούμε τις εντολές if elif για να ελέγξουμε ποία πόλη έχει βάλει ο χρήστης
            flag = 1
            polis = "Λιβαδειά"
            return polis # Χρησημοποιούμε την εντολή return για να στείλουμε τα διορθομένα δεδομένα μας πίσω στο κύριο πρόγραμμα για να μπορέσουμε να τα χρησημοποιήσουμε στο υπόλοιπο πρόγραμμα
        elif polis == "Άμφισσα" or polis == "Αμφισσα" or polis == "άμφισσα" or polis == "αμφισσα":
            flag = 1
            polis = "Άμφισσα"
            return polis
        elif polis == "Δελφοί" or polis == "Δελφοι" or polis == "δελφοί" or polis == "δελφοι":
            flag = 1
            polis = "Δελφοί"
            return polis
        elif polis == "Αγρίνιο" or polis == "αγρινιο" or polis == "Αγρινιο" or polis == "αγρίνιο":
            flag = 1
            polis = "Αγρίνιο"
            return polis
        elif polis == "Μεσολλόγγι" or polis == "Μεσολλογγι" or polis == "μεσολλόγγι" or polis == "μεσολλογγι":
            flag = 1
            polis = "Μεσολλόγγι"
            return polis
        elif polis == "Ναύπακτος" or polis == "ναύπακτος" or polis == "Ναυπατκος" or polis == "ναυπακτος":
            flag = 1
            polis = "Ναύπακτος"
            return polis
        elif polis == "Βόνιτσα" or polis == "βονιτσα" or polis == "Βονιτσα" or polis == "βόνιτσα":
            flag = 1
            polis = "Βόνιτσα"
            return polis
        elif polis == "Καρπενήσι" or polis == "Καρπενησι" or polis == "καρπενησι" or polis == "καρπενήσι":
            flag = 1
            polis = "Καρπενήσι"
            return polis
        elif polis == "Δομιανοί" or polis == "Δομιανοι" or polis == "δομιανοί" or polis == "δομιανοι":
            flag = 1
            polis = "Δομιανοί"
            return polis
        elif polis == "Λαμία" or polis == "Λαμια" or polis == "λαμια" or polis == "λαμία":
            flag = 1
            polis = "Λαμία"
            return polis
        elif polis == "Αταλάντη" or polis == "Αταλαντη" or polis == "αταλάντη" or polis == "αταλαντη":
            flag = 1
            polis = "Αταλάντη"
            return polis
        elif polis == "Χαλκίδα" or polis == "Χαλκιδα" or polis == "χαλκίδα" or polis == "Χαλκιδα":
            flag = 1
            polis = "Χαλκίδα"
            return polis
        elif polis == "Θήβα" or polis == "Θηβα" or polis == "θήβα" or polis == "θηβα":
            flag = 1
            polis = "Θήβα"
            return polis
        elif polis == "Ερέτρια" or polis == "ερετρια" or polis == "ερέτρια" or polis == "Ερετρια":
            flag = 1
            polis = "Ερέτρια "
        elif polis == "Κάρυστος" or polis == "Καρυστος" or polis == "καρυστος" or polis == "κάρυστος":
            flag = 1
            polis = "Κάρυστος"
        elif polis == "Αθήνα" or polis == "Αθηνα" or polis == "αθήνα" or polis == "αθηνα":
            flag = 1
            polis = "Αθήνα"
            return polis
        elif polis == "Πειραιάς" or polis == "πειραιάς" or polis == "Πειραιας" or polis == "πειραιας":
            flag = 1
            polis = "Πειραιάς"
            return polis
        else:
            if polis == "θιβα" or polis == "θίβα" or polis == "Θύβα" or polis == "Θίβα" or polis == "Θιβα" or polis == "Θυβα" or polis == "θυβα" or polis == "θύβα":
                apan = input("Μηπως εννοουσατε Θήβα; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Θήβα"
                    return polis
            elif polis == "Λαμήα" or polis == "Λαμηα" or polis == "λαμήα" or polis == "λαμηα" or polis == "Λαμύα" or polis == "Λαμυα" or polis == "λαμύα" or polis == "λαμυα":
                apan = input("Μηπως εννοουσατε Λαμία; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Λαμία"
                    return polis
            elif polis == "αταλαντι" or polis == "αταλάντι" or polis == "Αταλαντι" or polis == "Αταλάντι" or polis == "αταλλαντη" or polis == "αταλλάντη" or polis == "Αταλλάντη" or polis == "Αταλλαντη":
                apan = input("Μηπως εννοούσατε Αταλάντη; ")
                if apan == "Ναι" or apan == "ναι":
                    flag = 1
                    polis = "Αταλάντη"
                    return polis

            elif polis == "χαλκήδα" or polis == "χαλκηδα" or polis == "Χαλκηδα" or polis == "Χαλκήδα" or polis == "χαλκυδα" or polis == "χαλκύδα" or polis == "Χαλκύδα" or polis == "Χαλκυδα":
                apan = input("Μηπως εννοούσατε Αταλάντη; ")
                if apan == "Ναι" or apan == "ναι":
                    flag = 1
                    polis = "Χαλκίδα"
                    return polis

            elif polis == "αιρετρια" or polis == "αιρέτρια" or polis == "Αιρετρια" or polis == "Αιρέτρια" or polis == "εραιτρια" or polis == "εραίτρια" or polis == "Εραιτρια" or polis == "Εραίτρια":
                apan = input("Mηπως εννοούσατε Ερέτρια; ")
                if apan == "Ναι" or apan == "ναι":
                    flag = 1
                    polis = "Ερέτρια"
                    return polis
            elif polis == "καριστος" or polis == "Καριστος" or polis == "Καρηστος" or polis == "καρηστος":
                apan = input("Μήπως εννοούσατε Κάρυστος; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Κάρυστος"
                    return polis
            elif polis == "ΑΘινα" or polis == "αθινα" or polis == "ΑΘυνα" or polis == "αθυνα":
                apan = input("Μηπως εννοούσατε Αθήνα; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Αθήνα"
                    return polis
            elif polis == "πηραιας" or polis == "Πηραιας" or polis == "πιραιας" or polis == "Πιραιας" or polis == "Πυραιας" or polis == "πειρεας" or polis == "Πειρεας":
                apan = input("Μηπως εννοούσατε Πειραιάς; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Πειραιάς"
                    return polis
            elif polis == "Μεσολογι" or polis == "μεσολογι" or polis == "Μεσολλογι" or polis == "μεσoλλογι" or polis == "μεσολογγι" or polis == "Μεσολογγι":
                apan = input("Μήπως εννοούσατε Πειραιάς; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Mεσσολόγγι"
                    return polis
            elif polis == "αγρυνιο" or polis == "Αγρυνιο" or polis == "αγρηνιο" or polis == "Αγρηνιο":
                apan = input("Μήπως εννοούσατε Αγρίνιο; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Αγρίνιο"
                    return polis
            elif polis == "Βονητσα" or polis == "βονητσα" or polis == "βονυτσα" or polis == "Βονυτσα":
                apan = input("Μήπως εννοούσατε Βόνιτσα; ")
                if apan == "Ναι" or polis == "ναι":
                    flag = 1
                    polis = "Βόνιτσα"
                    return polis
            elif polis == "Λιβαδια" or polis == "λιβαδια" or polis == "Λιβαδυα" or polis == "λιβαδυα":
                apan = input("Μήπως εννοούσατε Λιβαδειά; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Λιβαδειά"
                    return polis
            elif polis == "αμφισα" or polis == "Αμφισα":
                apan = input("Μήπως εννοούσατε Αμφίσσα; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Άμφισσα"
                    return polis
            elif polis == "Δελφι" or polis == "δελφι" or polis == "δελφυ" or polis == "Δελφυ":
                apan = input("Μήπως εννοούσατε Δελφοί; ")
                if apan == "Ναι" or apan == "ναι":
                    flag = 1
                    polis = "Δελφοί"
                    return polis
            elif polis == "καρπενιση" or polis == "Καρπενιση" or polis == "Καρπενυση" or polis == "καρπενυση" or polis == "καρπενυσι":
                apan = input("Mηπως εννοούσατε Καρπερνήσι; ")
                if apan == "ναι" or apan == "Ναι":
                    flag = 1
                    polis = "Καρπενήσι"
                    return polis
            elif flag == 0:
                polis = input("Δώστε σωστά γραμμένη μια πόλη: ")
#Ελενχος για την ημερα
def Elenxos():
    """Σε αυτή την συνάρτηση ελέγχουμε αν είναι σωστά γραμμένη η τιμή, η μεταβλητή της ημέρας """
    mera1 = input(" Ποιά μέρα θέλετε να ταξιδέψετε ")
    fla=0
    while fla==0 :
        if mera1 in ["Σάββατο","Κυριακή","Δευτέρα","Τρίτη","Τετάρτη","Πέμπτη","Παρασκέυη","Σαββατο","Κυριακη","Δευτερα","Τριτη"]:
            fla=1


        elif mera1 in ["Τεταρτη","Πεμπτη","Παρασκευη","σάββατο","κυριακή" ,"δευτέρα","τρίτη","τετάρτη","πέμπτη","παρασκέυη","σαββατο" ]:
            fla=1

        elif mera1 in ["κυριακη","δευτερα","Τεταρτη","τριτη","Πεμπτη","παρασκευη","τεταρτη","πεμπτη"]:
            fla=1

        else :
            mera1 = input("Δώστε σωστά γραμμένα την μέρα ")
            fla=0
        return mera1

# Έχουμε την συνάρτηση για τα δρομολόγια
def dromologia(polis):
    poli_taksidi2 = " "
    mera = Elenxos()
    poli2 = elenxos_polis(polis)
    if poli2 == "Αθήνα":
        poli_taksidi = input("Δώστε που θέλετε να ταξιδέψετε: ")
        poli_taksidi2 = elenxos_polis(poli_taksidi)
    #πόλεις προς Αθήνα
    if mera == "Δευτέρα" or mera == "Τρίτη" or mera == "Τετάρτη" or mera == "Πέμπτη" or mera == "Παρασκέυη" or "Δευτερα" or mera == "Τριτη" or mera == "Τεταρτη" or mera == "Πεμπτη" or mera == "Παρασκευη" or "δευτέρα" or mera == "τρίτη" or mera == "τετάρτη" or mera == "πέμπτη" or mera == "παρασκέυη" or "δευτερα" or mera == "τριτη" or mera == "τεταρτη" or mera == "πεμπτη" or mera == "παρασκευη": # Εδω χρεισημοποιουμε την if για να δουμε πια μερα θελει να ταξιδεψει ο χρηστης απο τις πρωτες 5 μερες της εβδδομαδας
        if poli2 == "Δελφοί": #εδώ όπως και στο υπόλοιπο κομμάτι της συνάρτητης χρησημοποιούμε τις εντολές if και elif για να ελέγξουμε ποία πόλη έχει βάλει ο χρήστης για να του δώσουμε το σωστό αποτέλεσμα στα δρομολόγια
            print("Μέσω ΚΤΕΛ : 05:30 πμ , 11:00 πμ , 4:00 μμ, 6:30 μμ")
        elif poli2 == "Λαμία":
            print("Μέσω ΚΤΕΛ : 05:15 πμ , 05:30 πμ , 7:00 πμ , 9:00 πμ , 11:00 πμ , 1:00 μμ , 3:00 μμ , 3:15 μμ , 4:00 μμ , 5:30 μμ ,7:00 μμ , 9:15 μμ")
        elif poli2 == "Αγρίνιο":
            print("Μεσω ΚΤΕΛ : 4:00 πμ ,8:15 πμ , 9:30 πμ , 1:00 μμ , 3:00 μμ , 5:00 μμ , 7:00 μμ")
            if mera == "Δευτέρα":
                print("Μέσω ΚΤΕΛ για Καρπενήσι : 12.30μμ ")
            elif mera == "Παρασκεύη" :
                print("Μέσω ΚΤΕΛ για Νάυπακτο , Λαμία : 2.00μμ")
        elif poli2 == "Μεσσολόγγι":
            print("Μεσω ΚΤΕΛ : 4:30 πμ , 9:30 πμ , 2:00 μμ , 4:50μμ , 7:30")
        elif poli2 == "Ναύπακτος":
            print("Μεσω ΚΤΕΛ : 10:00 πμ , 5:00 μμ ")
        elif poli2 == "Βόνιτσα":
            print("Μεσω ΚΤΕΛ : 6:30 πμ , 8:00 πμ , 12:30 μμ ,3:15 μμ ")
        elif poli2 == "Χαλκίδα":
            print("Μεσω ΚΤΕΛ : 5:30 πμ , 6:30 πμ , 7:30 πμ , 8:30 πμ , 9:00 πμ , 10:00 πμ , 11:00 πμ , 12:00 μμ  , 1:00 μμ , 2:00 μμ , 3:00 μμ , 4:00 μμ , 5:00 μμ 6:00 , 7:00 μμ , 8:00 μμ , 9:00 μμ")
        elif poli2 == "Κάρυστος":
            print("Μεσω ΚΤΕΛ  για Χαλκίδα: 5:30 πμ ")
        elif poli2 == "Ερέτρια":
            print(   "Μεσω ΚΤΕΛ: 6:20 πμ , 7:20 πμ , 8:20 πμ , 9:20 πμ , 10:20 πμ , 12:20 πμ , 2:45 μμ , 4:20 μμ , 6:20 μμ , 8:20 μμ")
        elif poli2 == "Θήβα":
            print("Μεσω ΚΤΕΛ: 8:50 πμ , 10:50 πμ , 12:50 πμ , 1:50 μμ , 2:50 μμ , 3:50 μμ , 5:50 μμ , 8:50 μμ")
        elif poli2 == "Λιβαδειά":
            print("Μεσω ΚΤΕΛ: 5:30 πμ , 7:00 πμ , 8:00 πμ , 10:00 πμ , 12:00 πμ , 2:00 μμ , 4:00 μμ , 6:00 μμ")
        elif poli2 == "Καρπενήσι":
            print("Μεσω ΚΤΕΛ: 9:00 πμ")
        elif poli2 == "Άμφισσα":
            print("Μεσω ΚΤΕΛ: 5:00 πμ , 10:45 πμ , 3:30 μμ , 6:00 μμ")
        elif poli2 == "Δομιανοί":
            print("Μεσω ΚΤΕΛ για Καρπενήσι: 7:00 πμ , 4:00 μμ")
        elif poli2 == "Αταλάντη":
            print("Μεσω ΚΤΕΛ: 6:20 πμ , 1:45 μμ , 3:45 μμ")
        elif poli2 == "Πειραιάς":
            print("Μεσω αστικού για Αθήνα: 12.00πμ , 11.35μμ")
        # αθηνα για πολεις
        elif poli2=="Αθήνα" :
            if poli_taksidi2 == "Δελφοί":
                print("Μέσω ΚΤΕΛ : 08:30 πμ, 10:30 πμ , 3:00 μμ, 6:00 μμ")
            elif poli_taksidi2 == "Λαμία":
                print("Μέσω ΚΤΕΛ : 06:30 πμ , 9:00 πμ , 2:15 μμ , 3:15 μμ , 4:15 μμ , 5:30 μμ , 6:30 μμ , 9:30 μμ ")
                print("Μέσω ΚΤΕΛ (μέσω Μώλου): 11:00 πμ , 1:00 μμ , 9:30 μμ")
            elif poli_taksidi2 == "Αγρίνιο":
                print("Μεσω ΚΤΕΛ : 7:00 πμ , 9:00 πμ , 11:00 πμ , 1:00 μμ , 2:30 μμ , 4:00 μμ , 6:00 μμ , 8:00 μμ")
            elif poli_taksidi2 == "Μεσσολόγγι":
                print("Μεσω ΚΤΕΛ (μέσω Αντιρρίου): 7:00 πμ , 8:00 πμ , 11:00 πμ , 2:30 μμ , 5:00 μμ , 8:00 μμ")
            elif poli_taksidi2 == "Ναύπακτος":
                print("Μεσω ΚΤΕΛ : 6:30 πμ , 3:30 μμ ")
            elif poli_taksidi2 == "Βόνιτσα":
                print("Μεσω ΚΤΕΛ : 8:00 πμ , 1:00 μμ , 5:00 μμ ")
            elif poli_taksidi2 == "Χαλκίδα":
                print( "Μεσω ΚΤΕΛ : 6:30 πμ , 8:00 πμ , 9:00 πμ , 10:00 πμ , 11:00 πμ , 12:00 μμ , 1:00 μμ , 2:00 μμ , 3:00 μμ , 3:30 μμ , 4:00 μμ , 4:30 μμ, 5:00 μμ , 5:30 μμ , 6:00 , 7:00 μμ , 8:00 μμ , 9:00 μμ, 10:00")
            elif poli_taksidi2 == "Κάρυστος":
                print("Μεσω Χαλκίδας με ΚΤΕΛ  : 5.30 μμ ")
            elif poli_taksidi2 == "Ερέτρια":
                print("Μεσω ΚΤΕΛ: 9:00 πμ , 11:00 πμ , 12:00 πμ , 1:00 μμ , 2:00 μμ , 3:00 μμ , 5:00 μμ , 7:00 μμ")
            elif poli_taksidi2 == "Θήβα":
                print(  "Μεσω ΚΤΕΛ: 6:45 , 8:00 πμ , 9:00 πμ , 11:00 πμ , 1:00 μμ , 2:00 μμ , 3:00 μμ , 4:00 μμ , 6:00 μμ , 7:00 μμ , 8:15 μμ")
            elif poli_taksidi2 == "Λιβαδειά":
                print("Μεσω ΚΤΕΛ: 7:30 πμ , 10:30 πμ , 1:30 μμ , 3:00 μμ , 4:00 μμ , 6:00 μμ , 7:30 μμ , 9:00 μμ")
            elif poli_taksidi2 == "Καρπενήσι":
                print("Μεσω ΚΤΕΛ: 7:45 πμ")
            elif poli_taksidi2 == "Άμφισσα":
                print("Μεσω ΚΤΕΛ: 8:30 πμ , 10:30 πμ , 3:00 μμ , 6:00 μμ")
            elif poli_taksidi2 == "Δομιανοί":
                print("Μεσω ΚΤΕΛ για Καρπενήσι: 7:00 πμ , 4:00 μμ")
            elif poli_taksidi2 == "Αταλάντη":
                print("Μεσω ΚΤΕΛ: 6:30 πμ , 1:00 μμ , 7:45 μμ")
            elif poli_taksidi2 == "Καμένα Βούρλα":
                print("Μεσω ΚΤΕΛ: 11:00 μμ")
            elif poli_taksidi2 == "Πειραιάς":
                print("Μέσω πλοίου για Μαρμάρι : 9.30πμ , 6.00μμ")
    elif mera == "Σάββατο" or mera == "Κυριακή" or "Σαββατο" or mera == "Κυριακη" or "σαββατο" or mera == "κυριακη" or "σάββατο" or mera == "κυριακή":
        if poli2 == "Δελφοί":
            print("Μέσω ΚΤΕΛ : 11:00 πμ , 4:00 μμ, 6:30 μμ")
        elif poli2 == "Λαμία":
            print("Μέσω ΚΤΕΛ : 05:15 πμ , 05:30 πμ , 7:00 πμ , 9:00 πμ , 11:00 πμ , 1:00 μμ , 3:00 μμ , 3:15 μμ , 4:00 μμ , 5:30 μμ ,7:00 μμ , 9:15 μμ")
        elif poli2 == "Αγρίνιο":
            print("Μεσω ΚΤΕΛ : 8:15 πμ , 9:30 πμ , 1:00 μμ , 3:00 μμ , 5:00 μμ , 7:00 μμ")
            print("Μέσω ΚΤΕΛ για Βόνιτσα : 5.00πμ , 9.30πμ , 1.00μμ , 3.00μμ , 4.45μμ , 7.30μμ , 8.00μμ")
            if mera == "Σάββατο":
                print("Μέσω ΚΤΕΛ για Νάυπακτο , Λαμία : 2.00μμ")
        elif poli2 == "Μεσσολόγγι":
            print("Μεσω ΚΤΕΛ : 9:30 πμ , 2:00 μμ , 4:50μμ , 7:30μμ")
        elif poli2 == "Ναύπακτος":
            print("Μεσω ΚΤΕΛ : 10:00 πμ , 5:00 μμ ")
        elif poli2 == "Βόνιτσα":
            print("Μεσω ΚΤΕΛ : 6:30 πμ , 8:00 πμ , 12:30 μμ ,3:15 μμ ")
        elif poli2 == "Χαλκίδα":
            print("Μεσω ΚΤΕΛ : 5:30 πμ , 6:30 πμ , 7:30 πμ , 8:30 πμ , 9:00 πμ , 10:00 πμ , 11:00 πμ , 12:00 μμ  , 1:00 μμ , 2:00 μμ , 3:00 μμ , 4:00 μμ , 5:00 μμ 6:00 , 7:00 μμ , 8:00 μμ , 9:00 μμ")
        elif poli2 == "Κάρυστος":
            print("Μεσω ΚΤΕΛ για Χαλκίδα: 5:30 πμ ")
        elif poli2 == "Ερέτρια":
            print("Μεσω ΚΤΕΛ: 6:20 πμ , 7:20 πμ , 8:20 πμ , 9:20 πμ , 10:20 πμ , 12:20 πμ , 2:45 μμ , 4:20 μμ , 6:20 μμ , 8:20 μμ")
        elif poli2 == "Θήβα":
            print("Μεσω ΚΤΕΛ: 8:50 πμ , 10:50 πμ , 1:50 μμ , 3:50 μμ , 5:50 μμ , 8:50 μμ")
        elif poli2 == "Λιβαδειά":
            print("Μεσω ΚΤΕΛ: 7:00 πμ , 12:00 πμ, 4:00 μμ , 6:00 μμ")
        elif poli2 == "Καρπενήσι":
            print("Μεσω ΚΤΕΛ: 9:00 πμ")
        elif poli2 == "Άμφισσα":
            print("Μεσω ΚΤΕΛ: 10:45 πμ , 3:30 μμ , 6:00 μμ")
        elif poli2 == "Δομιανοί":
            print("Μεσω ΚΤΕΛ για Καρπενήσι: 7:00 πμ , 4:00 μμ")
        elif poli2 == "Αταλάντη":
            print("Μεσω ΚΤΕΛ: 1:45 μμ , 3:45 μμ")
        elif poli2 == "Καμένα Βούρλα":
            print("Μεσω ΚΤΕΛ: 4:00 μμ")
        elif poli2 == "Πειραιάς":
            print("Μεσω αστικού για Αθήνα: 12.00πμ , 11.35μμ")
            print("Μέσω πλοίου για Μαρμάρι: 9.30πμ , 6.00μμ")
        else:

            if poli_taksidi2 == "Δελφοί":
                print("Μέσω ΚΤΕΛ : 08:30 πμ, 10:30 πμ , 6:00 μμ")
            elif poli_taksidi2 == "Λαμία":
                print("Μέσω ΚΤΕΛ :  08:00 πμ , 9:00 πμ , 2:15 μμ , 3:15 μμ , 4:15 μμ , 5:30 μμ , 6:30 μμ , 9:30 μμ ")
                print("Μέσω ΚΤΕΛ (μέσω Μώλου): 11:00 πμ , 1:00 μμ , 9:30 μμ")
            elif poli_taksidi2 == "Αγρίνιο":
                print("Μεσω ΚΤΕΛ :, 9:00 πμ , 11:00 πμ , 1:00 μμ , 2:30 μμ , 4:00 μμ , 6:00 μμ , 8:00 μμ , 9.30μμ")
            elif poli_taksidi2 == "Μεσσολόγγι":
                print("Μεσω ΚΤΕΛ (μέσω Αντιρρίου): 7:00 πμ , 8:00 πμ , 11:00 πμ , 2:30 μμ , 5:00 μμ , 8:00 μμ , 9.30μμ")
            elif poli_taksidi2 == "Ναύπακτος":
                print("Μεσω ΚΤΕΛ : 6:30 πμ , 3:30 μμ ")
            elif poli_taksidi2 == "Βόνιτσα":
                print("Μεσω ΚΤΕΛ : 8:00 πμ , 1:00 μμ , 5:00 μμ ")
            elif poli_taksidi2 == "Χαλκίδα":
                print("Μεσω ΚΤΕΛ : 6:30 πμ , 8:00 πμ , 9:00 πμ , 10:00 πμ , 11:00 πμ , 12:00 μμ , 1:00 μμ , 2:00 μμ , 3:00 μμ , 3:30 μμ , 4:00 μμ , 4:30 μμ, 5:00 μμ , 5:30 μμ , 6:00 , 7:00 μμ , 8:00 μμ , 9:00 μμ, 10:00")
            elif poli_taksidi2 == "Κάρυστος":
                print("Μεσω Χαλκίδας με ΚΤΕΛ  : 12:00 μμ ")
            elif poli_taksidi2 == "Ερέτρια":
                print("Μεσω ΚΤΕΛ: 9:00 πμ , 11:00 πμ , 12:00 πμ , 1:00  μμ, 2:00 μμ , 3:00 μμ , 5:00 μμ , 7:00 μμ")
            elif poli_taksidi2 == "Θήβα":
                print("Μεσω ΚΤΕΛ: 9:00 πμ , 11:00 πμ , 1:00 μμ , 4:00 μμ , 6:00 μμ , 7:00 μμ , 8:15 μμ")
            elif poli_taksidi2 == "Λιβαδειά":
                print("Μεσω ΚΤΕΛ: 9:30 πμ , 11:30 πμ , 3:30 μμ ,5.30μμ , 7:30 μμ , 9:00 μμ")
            elif poli_taksidi2 == "Καρπενήσι":
                print("Μεσω ΚΤΕΛ: 7:45 πμ , 5.15μμ")
            elif poli_taksidi2 == "Άμφισσα":
                print("Μεσω ΚΤΕΛ: 8:30 πμ , 10:30 πμ , 3:00 μμ , 6:00 μμ")
            elif poli_taksidi2 == "Δομιανοί":
                print("Μεσω ΚΤΕΛ για Καρπενήσι: 9:00 πμ , 1:00 μμ")
            elif poli_taksidi2 == "Αταλάντη":
                print("Μεσω ΚΤΕΛ:  1:00 μμ , 3.30 μμ")
            elif poli_taksidi2 == "Πειραιάς":
                print("Μεσω αστικού για Αθήνα: 12.00πμ και κάθε 10 λεπτά, 11.35μμ")

#Αυτή εδώ είναι η συνάρτηση που ελέγχει ποία πόλη έχει βάλει για του δώσουμε σωστές πληροφορίες για τα αξιοθέατα της
def axiotheata(poli2):
    poli2 = elenxos_polis(poli2)
    if poli2 == "Λιβαδειά" or poli2 == "Θήβα":
        webbrowser.open_new_tab(
            'https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/ESyP001T4mBMoZcliOcQqosB-RY2CD6UpzvW9yYapEJCrw?e=z0Ne8J')

        """εδω χρησιμοποιπουμε την βιβλιοθηκη webbrowser 
        για να ανοιξουμε ενα συνδεσμο στον οποιο εχουμε φτιαξει 
        μια απλη παρουσιαση στο powerpoint για τα αξιοθεατα το ιδιο κανουμε παρακατω
                 """

    elif poli2 == "Άμφισσα" or poli2 == "Δελφοί":
        webbrowser.open_new_tab('https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/EboGcZueQhNLjTsD21X_whEBICWpYYQrgY5Vr1gQvHz6nQ?e=KGn5uy')

    elif poli2 == "Αγρίνιο" or poli2 == "Μεσολλόγγι" or poli2 == "Ναύπακτος" or poli2 == "Βόνιτσα":
        webbrowser.open_new_tab( 'https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/EeG_YGb7wpJPgDCYL_DjALEBkqeupov3R72uPbcnukb1eA?e=YVRUwY')
    elif poli2 == "Καρπενήσι" or poli2 == "Δομιανοί":
        webbrowser.open_new_tab(      'https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/EVaMzHf-uMZCn8xvTmRry58Bq3VkDtaknikdnzlAdn_GAA?e=ttYcTm')
    elif poli2 == "Λαμία" or poli2 == "Καμένα Βούρλα" or poli2 == "Αταλάντη":
        webbrowser.open_new_tab(   'https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/EUIWAEkaf15AoU-_BOF9WBcB6UGLhyqmtvOuGS6f1ykncg?e=mITkO2')
    elif poli2 == "Χαλκίδα" or poli2 == "Ερέτρια" or poli2 == "Κάρυστος":
        webbrowser.open_new_tab(
            'https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/EXCUUAmsXblIv6Ag47I1Fv8B2_iZLQavgj3JUohwiDR2IQ?e=ZdaTub')
    elif poli2 == "Αθήνα" or poli2 == "Πειραιάς":
        webbrowser.open_new_tab(
            'https://ioniogr0-my.sharepoint.com/:p:/g/personal/inf2022025_ionio_gr/EZtDl2EDKG9FkOOtiKv0poMBXQdDOJtZFX4pEt95y8rcNg?e=DdEzIl')








