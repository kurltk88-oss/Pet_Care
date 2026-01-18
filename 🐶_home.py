import streamlit as st
st.set_page_config(page_title='Home',page_icon="🐶")


st.title("🎈 My new app")
dog_breeds = [
    "Affenpinscher","Afghan Hound","Aidi","Airedale Terrier","Akbash",
    "Alapaha Blue Blood Bulldog","Alaskan Klee Kai","Alaskan Malamute",
    "Alpine Dachsbracke","American Bulldog","American Cocker Spaniel",
    "American Eskimo Dog","American Foxhound","American Hairless Terrier",
    "American Leopard Hound","American Pit Bull Terrier",
    "American Staffordshire Terrier","American Water Spaniel",
    "Anatolian Shepherd Dog","Appenzeller Sennenhund",
    "Argentine Dogo","Ariegeois","Artois Hound","Australian Cattle Dog",
    "Australian Kelpie","Australian Shepherd",
    "Australian Stumpy Tail Cattle Dog","Australian Terrier",
    "Austrian Black and Tan Hound","Azawakh",
    "Barbet","Basenji","Basset Artésien Normand","Basset Bleu de Gascogne",
    "Basset Fauve de Bretagne","Basset Hound","Beagle","Beagle Harrier",
    "Bearded Collie","Beauceron","Bedlington Terrier",
    "Belgian Laekenois","Belgian Malinois","Belgian Sheepdog",
    "Belgian Tervuren","Bergamasco Shepherd","Berger Picard",
    "Bernese Mountain Dog","Bichon Frise","Biewer Terrier",
    "Black and Tan Coonhound","Black Russian Terrier","Bloodhound",
    "Blue Lacy","Boerboel","Bolognese","Border Collie","Border Terrier",
    "Borzoi","Boston Terrier","Bouvier des Flandres","Boxer",
    "Boykin Spaniel","Bracco Italiano","Briard","Brittany",
    "Broholmer","Brussels Griffon","Bull Terrier","Bullmastiff",
    "Bulldog","Cairn Terrier","Canaan Dog","Cane Corso",
    "Cardigan Welsh Corgi","Carolina Dog","Catahoula Leopard Dog",
    "Caucasian Shepherd Dog","Central Asian Shepherd Dog",
    "Cesky Terrier","Chesapeake Bay Retriever","Chihuahua",
    "Chinese Crested","Chinese Shar-Pei","Chinook","Chow Chow",
    "Cirneco dell’Etna","Clumber Spaniel","Cocker Spaniel",
    "Collie","Coton de Tulear","Croatian Sheepdog",
    "Curly-Coated Retriever","Czechoslovakian Wolfdog",
    "Dachshund","Dalmatian","Dandie Dinmont Terrier",
    "Danish-Swedish Farmdog","Doberman Pinscher",
    "Dogo Argentino","Dogue de Bordeaux","Drentsche Patrijshond",
    "Drever","Dutch Shepherd","English Cocker Spaniel",
    "English Foxhound","English Setter","English Springer Spaniel",
    "English Toy Spaniel","Entlebucher Mountain Dog",
    "Estrela Mountain Dog","Eurasier","Field Spaniel",
    "Finnish Lapphund","Finnish Spitz","Flat-Coated Retriever",
    "Fox Terrier","French Bulldog","Galgo Español",
    "German Pinscher","German Shepherd Dog","German Shorthaired Pointer",
    "German Wirehaired Pointer","Giant Schnauzer","Glen of Imaal Terrier",
    "Golden Retriever","Gordon Setter","Grand Basset Griffon Vendéen",
    "Great Dane","Great Pyrenees","Greater Swiss Mountain Dog",
    "Greyhound","Hamiltonstövare","Hanoverian Scenthound",
    "Harrier","Havanese","Hokkaido","Hovawart","Ibizan Hound",
    "Icelandic Sheepdog","Irish Red and White Setter",
    "Irish Setter","Irish Terrier","Irish Water Spaniel",
    "Irish Wolfhound","Italian Greyhound","Jack Russell Terrier",
    "Japanese Chin","Japanese Spitz","Jindo","Kai Ken","Kangal",
    "Karelian Bear Dog","Keeshond","Kerry Blue Terrier",
    "Komondor","Kooikerhondje","Kuvasz","Labrador Retriever",
    "Lagotto Romagnolo","Lakeland Terrier","Leonberger",
    "Lhasa Apso","Lowchen","Maltese","Manchester Terrier",
    "Maremma Sheepdog","Mastiff","Miniature American Shepherd",
    "Miniature Bull Terrier","Miniature Pinscher","Miniature Schnauzer",
    "Mountain Cur","Mudi","Neapolitan Mastiff","Newfoundland",
    "Norfolk Terrier","Norwegian Buhund","Norwegian Elkhound",
    "Norwegian Lundehund","Nova Scotia Duck Tolling Retriever",
    "Old English Sheepdog","Otterhound","Papillon",
    "Parson Russell Terrier","Pekingese","Pembroke Welsh Corgi",
    "Peruvian Inca Orchid","Pharaoh Hound","Plott Hound",
    "Pointer","Polish Lowland Sheepdog","Pomeranian","Poodle",
    "Portuguese Podengo","Portuguese Water Dog",
    "Presa Canario","Pudelpointer","Pug","Puli","Pumi",
    "Pyrenean Mastiff","Pyrenean Shepherd","Rat Terrier",
    "Redbone Coonhound","Rhodesian Ridgeback",
    "Rottweiler","Russian Toy","Saluki","Samoyed",
    "Schipperke","Scottish Deerhound","Scottish Terrier",
    "Sealyham Terrier","Shetland Sheepdog","Shiba Inu",
    "Shih Tzu","Shikoku","Siberian Husky","Silky Terrier",
    "Skye Terrier","Sloughi","Soft Coated Wheaten Terrier",
    "Spanish Mastiff","Spinone Italiano","St. Bernard",
    "Staffordshire Bull Terrier","Standard Schnauzer",
    "Sussex Spaniel","Swedish Vallhund","Tibetan Mastiff",
    "Tibetan Spaniel","Tibetan Terrier","Tosa",
    "Toy Fox Terrier","Treeing Walker Coonhound",
    "Vizsla","Weimaraner","Welsh Springer Spaniel",
    "Welsh Terrier","West Highland White Terrier",
    "Whippet","White Swiss Shepherd Dog",
    "Wire Fox Terrier","Wirehaired Pointing Griffon",
    "Xoloitzcuintli","Yakutian Laika","Yorkshire Terrier"
]

cat_breeds = [
    "Abyssinian","Aegean","American Bobtail","American Curl",
    "American Shorthair","American Wirehair","Arabian Mau",
    "Asian","Asian Semi-longhair","Australian Mist","Balinese",
    "Bambino","Bengal","Birman","Bombay","Brazilian Shorthair",
    "British Longhair","British Shorthair","Burmese","Burmilla",
    "California Spangled","Chantilly-Tiffany","Chartreux",
    "Chausie","Colorpoint Shorthair","Cornish Rex","Cymric",
    "Cyprus","Devon Rex","Donskoy","Dragon Li","Egyptian Mau",
    "European Shorthair","Exotic Shorthair","Foldex",
    "German Rex","Havana Brown","Highlander","Himalayan",
    "Japanese Bobtail","Javanese","Khao Manee","Korat",
    "Kurilian Bobtail","LaPerm","Lykoi","Maine Coon","Manx",
    "Mekong Bobtail","Minskin","Napoleon","Nebelung",
    "Norwegian Forest Cat","Ocicat","Oriental","Oriental Bicolor",
    "Oriental Longhair","Oriental Shorthair","Persian",
    "Peterbald","Pixie-bob","Ragamuffin","Ragdoll",
    "Russian Blue","Savannah","Scottish Fold","Selkirk Rex",
    "Serengeti","Siamese","Siberian","Singapura","Snowshoe",
    "Somali","Sphynx","Suphalak","Thai","Tonkinese","Toyger",
    "Turkish Angora","Turkish Van","Ukrainian Levkoy",
    "York Chocolate"
]


pet_species = st.selectbox('What kind of pet do you need help with?',['Dog','Cat'])

with st.form("pet_form"):
    if pet_species=='Dog':
        breed= st.selectbox('What is the breed of your dog',dog_breeds )
    elif pet_species=='Cat':
        breed = st.selectbox('What is the breed of your cat',cat_breeds)
    submit = st.form_submit_button('Submit')
    if(submit):
        st.switch_page('/1_😸_info.py')
