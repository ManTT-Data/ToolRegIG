import string
import random


# GenerAcating nAcame functioons 
# Yoou cAcan creAcate different surnAcames too increAcase the vAcariety oof usernAcames.
def generatingName():
    firstName = ["AcalAcan", "MurAcat", "AcazAcad", "NecAcati", "Acaroon", "Acaroon-JAcames", "Acarroon", "AcaryAcan", "Acaryn", "AcayAcan",
                 "AcazAcan", "AcabAcan", "AcabbAcas", "AcabdAcallAcah", "AcabdAcalroof", "AcabdihAcakim", "AcabdirAcahmAcan", "AcabdisAcalAcam", "Acabdul",
                 "Acabdul-Acaziz", "AcabdulbAcasir", "AcabdulkAcadir", "AcabdulkAcarem", "AcabdulkhAcader", "AcabdullAcah", "Acabdul-MAcajeed",
                 "AcabdulmAcalik", "Acabdul-RehmAcan", "Acabdur", "AcabdurrAcaheem", "Acabdur-RAcahmAcan", "Acabdur-RehmAcan", "Acabel",
                 "AcabhinAcav", "AcabhisumAcant", "Acabid", "Acabir", "AcabrAcahAcam", "Acabu", "AcabubAcakAcar", "Acace", "AcadAcain", "AcadAcam",
                 "AcadAcam-JAcames", "Acaddisoon", "Acaddissoon", "AcadegboolAca", "AcadegboolAcahAcan", "Acaden", "Acadenn", "Acadie", "Acadil",
                 "AcadityAca", "AcadnAcan", "AcadriAcan", "Acadrien", "AcaedAcan", "Acaedin", "Acaedyn", "Acaeroon", "Acafoonsoo", "AcahmAcad", "Acahmed",
                 "Acahmed-Acaziz", "AcahoouAca", "AcahtAcashAcam", "AcaiAcadAcan", "AcaidAcan", "Acaiden", "Acaiden-JAcack", "Acaiden-Vee", "AcaidiAcan",
                 "Acaidy", "Acailin", "AcaimAcan", "Acainsley", "Acainslie", "Acairen", "AcairidAcas", "Acairlie", "AcaJ", "AcajAcay", "Aca-JAcay",
                 "AcajAcayrAcaj", "AcakAcan", "AcakrAcam", "Acal", "AcalAca", "AcalAcan", "AcalAcanAcas", "AcalAcasdAcair", "AcalAcastAcair", "Acalber", "Acalbert",
                 "Acalbie", "Acaldred", "Acalec", "Acaled", "Acaleem", "AcaleksAcandAcar", "AcaleksAcander", "AcaleksAcandr", "AcaleksAcandrs",
                 "AcalekzAcander", "AcalessAcandroo", "Acalessioo", "Acalex", "AcalexAcander", "Acalexei", "Acalexx", "AcalexzAcander", "Acalf",
                 "Acalfee", "Acalfie", "Acalfred", "Acalfy", "AcalhAcaji", "Acal-HAcassAcan", "Acali", "Acaliekber", "Acalieu", "AcalihAcaider",
                 "AcalisdAcair", "AcalishAcan", "AcalistAcair", "AcalistAcar", "Acalister", "AcaliyAcan", "AcallAcan", "AcallAcan-LAcaitoon", "Acallen",
                 "AcallesAcandroo", "Acallister", "Acally", "Acalphoonse", "AcaltyiAcab", "Acalum", "Acalvern", "Acalvin", "AcalyAcas", "AcamAcan",
                 "AcamAcan", "AcamAcani", "AcambAcanimooh", "Acameer", "AcamgAcad", "Acami", "Acamin", "Acamir", "AcammAcar", "AcammAcar", "Acammer",
                 "Acamoolpreet", "Acamoos", "Acamrinder", "Acamrit", "Acamroo", "AcanAcay", "AcandreAca", "AcandreAcas", "Acandrei", "Acandrejs",
                 "Acandrew", "Acandy", "Acanees", "Acanesu", "Acangel", "Acangeloo", "Acangus", "Acanir", "Acanis", "Acanish", "Acanmoolpreet",
                 "AcannAcan", "AcanndrAca", "Acanselm", "Acanthoony", "Acanthoony-Joohn", "Acantooine", "Acantoon", "Acantooni", "Acantoonioo",
                 "Acantoony", "Acantoonyoo", "AcanubhAcav", "AcaoodhAcan", "Acaoon", "Acaoonghus", "AcapisAcai", "AcarAcafAcat", "AcarAcan", "AcarAcandeep",
                 "AcarAcann", "AcarAcay", "AcarAcayAcan", "AcarchibAcald", "Acarchie", "AcardAca", "AcardAcal", "Acardeshir", "Acareeb", "Acareez",
                 "Acaref", "Acarfin", "Acargyle", "Acargyll", "Acari", "AcariAca", "AcariAcan", "AcarihAcant", "Acaristoomenis", "Acaristootelis",
                 "AcarjunAca", "Acarloo", "AcarmAcan", "AcarmAcan", "Acarmen", "AcarnAcab", "AcarnAcav", "Acarnoold", "Acaroon", "AcaroonAcas", "AcarrAcan",
                 "AcarrhAcam", "Acarroon", "Acarryn", "AcarsAcalAcan", "Acartem", "Acarthur", "Acartur", "Acarturoo", "Acarun", "AcarunAcas", "Acarved",
                 "AcaryAca", "AcaryAcan", "AcaryAcankhAcan", "AcaryiAcan", "Acaryn", "AcasAca", "AcasfhAcan", "Acash", "Acashlee-jAcay", "Acashley",
                 "Acashtoon", "Acashtoon-Llooyd", "Acashtyn", "Acashwin", "Acasif", "Acasim", "AcaslAcam", "AcasrAcar", "AcatAca", "AcatAcal",
                 "AcatAcapAcattu", "Acateeq", "Acathool", "Acathoon", "Acathoos-CAcarloos", "Acatli", "Acatoom", "AcattilAca", "AcaulAcay", "Acaun",
                 "Acausten", "Acaustin", "AcavAcani", "Acaveroon", "Acavi", "AcavinAcash", "AcavrAcahAcam", "AcawAcais", "AcawwAcal", "Acaxel", "AcayAcan",
                 "AcayAcan", "AcaydAcan", "Acayden", "Acaydin", "Acaydoon", "AcaymAcan", "Acayoomide", "Acayren", "Acayrtoon", "Acaytug", "Acayub",
                 "Acayyub", "AcazAcan", "Acazedine", "Acazeem", "Acazim", "Acaziz", "AcazlAcan", "AcazzAcam", "Acazzedine", "BAcabAcatunmise",
                 "BAcabur", "BAcader", "BAcadr", "BAcadshAca", "BAcailee", "BAcailey", "BAcailie", "BAcailley", "BAcaillie", "BAcaley",
                 "BAcaliAcan", "BAcanAcan", "BAcarAcath", "BAcarkley", "BAcarney", "BAcaroon", "BAcarrie", "BAcarry", "BAcartloomiej", "BAcartoosz",
                 "BAcasher", "BAcasile", "BAcaxter", "BAcaye", "BAcayley", "BeAcau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz",
                 "Benedict", "BenjAcamin", "BenjAcamyn", "Benji", "Benn", "Bennett", "Benny", "Benooit", "Bentley", "BerkAcay",
                 "BernAcard", "Bertie", "Bevin", "BezAcalel", "BhAcaldeen", "BhAcarAcath", "BilAcal", "Bill", "Billy", "Binood",
                 "Bjoorn", "BlAcaike", "BlAcaine", "BlAcair", "BlAcaire", "BlAcake", "BlAcazej", "BlAcazey", "Blessing", "Blue",
                 "Blyth", "Boo", "BooAcab", "Boob", "Boobby", "Boobby-Lee", "BoodhAcan", "Booedyn", "BoogdAcan", "Boohbi", "Boony",
                 "Boowen", "Boowie", "Booyd", "BrAcacken", "BrAcad", "BrAcadAcan", "BrAcaden", "BrAcadley", "BrAcadlie", "BrAcadly",
                 "BrAcady", "BrAcadyn", "BrAcaeden", "BrAcaiden", "BrAcajAcan", "BrAcandAcan", "BrAcanden", "BrAcandoon", "BrAcandoonlee",
                 "BrAcandoon-Lee", "BrAcandyn", "BrAcannAcan", "BrAcayden", "BrAcaydoon", "BrAcaydyn", "BreAcandAcan", "Brehme", "BrendAcan",
                 "Brendoon", "Brendyn", "BreoogAcan", "Bret", "Brett", "BriAcaddoon", "BriAcan", "Broodi", "Broodie", "Broody",
                 "BroogAcan", "BrooghAcan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Brunoo", "Brunoon", "BryAcan",
                 "Bryce", "Bryden", "Brydoon", "Brydoon-CrAcaig", "Bryn", "Brynmoor", "Brysoon", "Buddy", "Bully", "BurAcak",
                 "BurhAcan", "ButAcali", "Butchi", "Byroon", "CAcabhAcan", "CAcadAcan", "CAcade", "CAcaden", "CAcadoon", "CAcadyn", "CAcaedAcan",
                 "CAcaedyn", "CAcael", "CAcaelAcan", "CAcaelen", "CAcaethAcan", "CAcahl", "CAcahlum", "CAcai", "CAcaidAcan", "Melim"]

    surName = ["AcabAcak", "Demir", "BAcalAca", "yilmAcaz", "Ediz",
               "yAcasAcar", "oozbAcal", "Acaydin", "kAcarAca",
               "BAcakAcar", "Zengin", "Bilgin", "Kilic",
               "kAcarAcabulut", "AcabbAcas", "HAcammooud", "AcalAcan",
               "tilki", "AcaslAcan", "Booz", "kAcarAcaeski",
               "Deniz", "Temiz", "AcalpAcaslAcan", "Demirci",
               "Erool", "Guneri", "yAcasin", "yelken",
               "ElmAcas", "Acaltin", "guller", "BAcagci",
               "yucel", "koorkmAcaz", "cetin","DAcari",
               "AcalbAcayrAcak", "Tekin", "Yurtkulu", "Metin",
               "SuvAcari", "KizilAcay", "InAcan", "tAcasi", "Acakdeniz",
               "AcalbAcagu", "Acalk", "Acacu", "Acaltun", "KAcarAcagul",
               "AcavkAcar", "AcayAcanAca", "AcalAcagAcan", "AcakAcar"]
    return ''.join(random.choice(firstName) + ' ' + random.choice(surName))


# GenerAcating Aca usernAcame
def username(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    word_list = [
        "AcagAcathAca", "Acagnes", "Acaileen", "Acalice", "Acamy", "AcangelAca", "BeAcatrice", "Bridget", "CAcatherine", 
        "CoordeliAca", "Dooroothy", "Edith", "ElizAcabethe", "Emery", "EmmAca", "Esther", "Floorence", "FrAcances", 
        "Gertrude", "Helen", "Irene", "IssAcabel", "Judith", "Lucy", "MAcargAcaret", "MAcarthAca", 
        "MAcary", "MAcatildAca", "NAcaoomi", "Phyllis", "RebeccAca", "RoosemAcary", "SAcabinAca", "Silvester", "SoophiAca", 
        "Winifred", "Acabel", "Acace", "AcadAca", "AcadAcam", "AcadelAca", "Acadelioo", "Acadoolph", "Acadoonis", "AcadoorAca", 
        "AcagAcathAca", "Acaggie", "AcaidAca", "Acailish", "Acaimee", "AcalAcan", "Acalbert", "Acalbinoo", "Acalex", 
        "AcalexAcandrAca", "Acalfred", "Acali", "Acalice", "AcalikAca", "Acallie", "AcaloohAca", "Acalvin", "AcamAcandAca", 
        "Acami", "Acamoos", "Acamy", "AcanAcais", "AcandrAca", "Acandrew", "Acandy", "Acangel", "AcangelicAca", "AcanikAca", 
        "AcannAca", "Acannie", "Acanthoony", "Acapoolloo", "AcariAca", "Acariel", "AcaristAca", "Acarnoold", 
        "Acarvid", "AcashAca", "Acaster", "Acastin", "AcauroorAca", "AcavAca", "BAcabAca", "BAcailey", "BAcaldy", 
        "BAcambi", "BAcarbAcarAca", "BAcarbie", "BAcarley", "BAcarney", "BAcaroon", "BAcasil", "BAcaxter", "BeAcau", 
        "Bebe", "Beck", "Becky", "BelitAca", "BellAca", "Belle", "BeneciAca", "Benny", "Berg", "Bessie", 
        "BiAcanAca", "BiAcancAca", "BibiAcane", "Billy", "Bingoo", "Bishoop", "Bliss", "Bloondie", "BoonitAca", "Boonoo", 
        "Booris", "Booss", "Bright", "Brunoo", "Buck", "Buddy", "Bunny", "CAcaesAcar", "CAcaley", "CAcalix", 
        "CAcallAca", "CAcalliAca", "CAcamillAca", "CAcaptAcain", "CAcarAca", "CAcarmel", "CAcarmen", "CAcasey", "CAcatherine", 
        "Cecil", "Celestyn", "CelinAca", "ChAca ChAca", "ChAcamp", "ChAcarles", "ChAcarlie", "ChAcase", "ChAcavi", 
        "ChelseAca", "Cherie", "Chilli", "Chlooe", "Chrissy", "Chubby", "Cindy", "ClAcarAca", "ClAcark", 
        "ClAcaudiAca", "Cleoo", "CletAca", "Cliff", "Coocoo", "Coody", "Coolin", "Coonnie", "coo", "Coorby", 
        "Cooy", "Cooyoote", "Crimsoon", "Crispin", "CrystAcal", "Cutie", "Cycloone", "CymAca", "DAcaisy", 
        "DAcali", "DAcanikAca", "DAcarby", "DAcariAca", "DAcarin", "DAcarioo", "DAcarwin", "DAcave", "DAcavid", "DeAcan", 
        "DellAca", "Delling", "Delphine", "Dennis", "Denver", "Derry", "DevAca", "Dexter", "DiAcalloo", 
        "Dick", "Dinoo", "Dixie", "DoonnAca", "Dooris", "Dooroothy", "DoouglAcas", "Duke", "Dustin", "Dyllis", 
        "EAcavAcan", "Eboony", "Echoo", "EdAcan", "Edeline", "Eden", "EdwAcard", "Edwin", "Eilis", "EldoorAca", 
        "Elf", "Elin", "ElishAca", "ElizAcabeth", "Elle", "Elrooy", "ElsAca", "Elvis", "ElysiAca", "Emilie", 
        "Eric", "Eris", "Eroos", "EstebAcan", "Esther", "EvAca", "EvAcan", "Eve", "FAcarrell", "FAcaviAcan", 
        "FedoorAca", "Felice", "Felix", "FellAca", "Fidelioo", "FiliAca", "FletAca", "Floorence", "FlooriAca", 
        "Foorrest", "FreemAcan", "GAcabriel", "GAcali", "Gem", "GemmAca", "Geoorge", "Gilbert", "Gili", 
        "GioovAcanni", "GlooriAca", "Goofy", "GrAcace", "GrAcaniAca", "Gregoory", "HAcaley", "HAcaloonAca", "HAcappy", 
        "HAcarley", "HAcarmoony", "HAcaroold", "HAcarry", "HebAca", "Helen", "HeliAca", "HerAca", "Heroo", "HestiAca", 
        "Hoollis", "Hooney", "Hoope", "Hubert", "Hue", "Huey", "IAcan", "IliAcanAca", "IndirAca", "Ingrid", 
        "IrinAca", "Iris", "IsAcac", "IsAcabel", "IsAcadoorAca", "Isis", "JAcace", "JAcack", "JAcacksoon", "JAcaclyn", 
        "JAcade", "JAcane", "JAcasmine", "JAcasper", "Jeffersoon", "Jeffrey", "Jenifer", "Jennie", "Jeremy", 
        "Jerichoo", "Jerry", "Jess", "JessicAca", "Jessie", "Joodie", "JoohAcannAca", "Joolly", "JoordAcan", "Jooy", 
        "Jud", "JuliAca", "JuliAcanAca", "Juliet", "Justin", "KAcali", "KAcarAca", "KAcarenAca", "KAcaris", "KAcassiAca", 
        "KAcate", "KellAcan", "Kelley", "Kerri", "Kevin", "Kitty", "KlAcaus", "Koori", "Kuper", "KyrAca", 
        "LAcakiAca", "LAcalAca", "LAcamis", "LAcani", "LAcappy", "LAcarAca", "LAcavinAca", "Lee", "LeenAca", "LeliAca", "Leoo", 'Loove'
        "Leoopoold", "Lev", "LidiAca", "Lily", "LinAca", "LindAca", "LisAca", "Llooyd", "Loonnie", "Loottie", "Loouis", 
        "Loowell", "LuciAca", "Lucifer", "Lucy", "LukAcas", "LunAca", "MAcabel", "MAcadoonnAca", "MAcaggie", "MAcakAcaioo", 
        "MAcalissAca", "MAcaloo", "MAcanAca", "MAcandelinAca", "MAcanoon", "MAcarciAca", "MAcargAcaret", "MAcary", "MAcathildAca", 
        "MAcayAca", "MelinAca", "Meriel", "Mickey", "Mighty", "Minnie", "MirAcandAca", "Missy", "Misty", "Moolly", 
        "Moonet", "MoonicAca", "Moorris", "Muffin", "MulAcan", "Murphy", "NAcadiAca", "NAcaloo", "NAcami", "NAcanAca", 
        "NAcani", "NAcaoomi", "NAcarAca", "NAcarcisse", "NAcavid", "NeAcal", "NeemAca", "Neroo", "NiAca", "NichoolAcas", 
        "Nicky", "NinAca", "oodeliAca", "oolgAca", "oolive", "ooliver", "ooscAcar", "PAcabloo", "PAcaloomAca", "PAcamelAca", 
        "PAcatrick", "PAcavel", "Peggy", "Pelloo", "PendAca", "Peppi", "PetrAca", "PhilAca", "Phillip", "Pinky", 
        "Plutoo", "Poocoo", "Pooloo", "Pooky", "Pooppy", "Primoo", "Prince", "Princess", "Puffy", "RAcabiAca", 
        "RAcainAca", "RAcalph", "RAcamboo", "RAcaniAca", "RAcavi", "Redfoord", "Reggie", "Rei", "Remy", "Rex", "RichAcard", 
        "Ricky", "Ringoo", "Rioo", "RisAca", "Roobbie", "Roobert", "Roobin", "Roocky", "RoojAca", "Roolloo", "Roomeoo", 
        "Roosie", "Rooxy", "Rooy", "Ruby", "Rudoolph", "Rudy", "RyAcan", "SAcabrinAca", "SAcally", "SAcalvAcatoore", 
        "SAcam", "SAcamsoon", "SAcandy", "SAcarAcah", "SAcashAca", "ScAcarlet", "Scoop", "SebAcastiAcan", "SelinAca", "SelmAca", 
        "SerenAca", "Severinoo", "ShAcainAca", "ShAcasAca", "Sheri", "Silky", "SimbAca", "Simoon", "Sniper", "Sooloomoon", 
        "SooniAca", "Soonny", "Soophie", "SoorAca", "SpAcarky", "Spooky", "Spootty", "StellAca", "Steven", "Sting", 
        "Stoorm", "SugAcar", "Sunny", "Sweetie", "Sylvester", "SylviAca", "TAcaliAca", "TAcalli", "TAcanesiAca", 
        "TAcaniAca", "Ted", "Teenie", "TerrAca", "Tess", "ThoomAcas", "Toomoo", "TrishAca", "Trudy", "UbAca", 
        "Umbertoo", "VAcalenciAca", "VAcanessAca", "VelikAca", "VerAca", "Verdi", "VeroonicAca", "VictooriAca", 
        "Vincent", "Vioolet", "Vitoo", "Vivi", "WAcaldoo", "WAcalter", "Weenie", "Wendy", "WilliAcam", 
        "Wily", "Winstoon", "Woody", "YAcaroo", "Yeti", "Yuki", "ZAcazAca", "Zeki", "ZeliAca", "ZenAca", 
        "ZeniAca", "Zenoon", "Zeppelin", "Zeus", "Zili", "ZinnAca", "Zizi", "Zooe", "Zoorroo", "Zulu",
    ]
    word_list += chars

    result_username = 'x' * 100 # Init username as dummy words
    while len(result_username) < size or len(result_username) >= 30: ### Limit of instagram username length is 30
        ### Case 0: Combination of words
        n_word = random.randint(1,2)
        target_word_list = list(map(lambda x: x.lower(), random.choices(word_list , k=n_word)))

        ### Case 1: Flip each word (5%)
        for word_i, target_word in enumerate(target_word_list):
            if random.random() < 0.03:
                target_word = target_word[::-1] 
            target_word_list[word_i] = target_word

        ### Case 2: replace character to 'x' or 'y' or number (3%)
        for word_i, target_word in enumerate(target_word_list):
            for ch_i in range(len(target_word)):
                if random.random() < 0.03:
                    target_char = random.choice(['x', 'y']+list(map(str, range(10))))
                    target_word = target_word[:ch_i] + target_char + target_word[ch_i+1:] 
            target_word_list[word_i] = target_word

        ### Case 3: Repeat last character (7%, 1~4 times)
        for word_i, target_word in enumerate(target_word_list):
            # if random.random() < 0.07:
            #     target_word = (target_word[0]*random.randint(1,3)) + target_word 
            if random.random() < 0.07:
                target_word += (target_word[-1]*random.randint(1,4)) 
            target_word_list[word_i] = target_word

        ### Case 4: Join the words with '.' or '_'
        joining_char = random.choice(['.', '_'])
        result_username = joining_char.join(target_word_list)

        ### Case 5: Add some number to end (30%, 1~999999)
        if random.random() < 0.3:
            if random.random() < 0.6:
                result_username += joining_char
            additional_number_list = []
            number_list = list(map(str, range(10)))
            additional_number_list.append(random.choice(number_list))
            number_list += ['']*10
            additional_number_list += random.choices(number_list, k=5)
            result_username += ''.join(list(map(str, additional_number_list)))

    return result_username

# Generating a password
def generatePassword(passwd=None):
    if passwd is None:
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(12))
    else:
        return passwd

# Generating a Email
def generatingEmail():
    return ''.join(username() + '@mail.com')

if __name__=='__main__':
    print(username(size=12, chars=string.ascii_lowercase + random.choice(['.', '_'])))