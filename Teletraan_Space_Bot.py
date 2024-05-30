import re

# Teletraan 1 -  Chatbot με ειδίκευση σε διαστημικές γνώσεις 
# ics22059 - Μαρία Θεοδώρα Φωλίνα

# Πρότυπα προτάσεων που αναγνωρίζει το chatbot.
# Μέσω του regex στις προτάσεις εξασφαλίζουμε ένα εκτεταμένο εύρος εισόδου από τον χρήστη, ομαδοποιώντας τις απαντήσεις του chatbot.
# Χρησιμοποιούνται σύμβολα που εφαρμόζουν την διάζευξη, την δυνατότητα ύπαρξης προαιρετικών λέξεων και την αποθήκευση λέξης για αναζήτηση σε λεξικά.
# Αυτό παρέχει ακόμα ένα επίπεδο αλληλεπίδρασης και επικοινωνίας με τον χρήστη. 
patterns = {
    r'hello|hi|hey': 'Hello! What can I help you with today?',
    r'(what|which) (?:planet )?is (.*)': '{0} is {1}',
    r'what temperature does (.*) have': 'The temperature of {0} is {temperature}',
    r'find the distance between (.*) and (.*)': 'The distance between {0} and {1} is {distance} million kilometers.',
    r'find the distance from the sun to (.*)': 'The distance from the Sun to {0} is {distance} million kilometers.',
    r'what can you do': 'I can provide information about our solar system. Feel free to ask!',
    r'who are you': 'My name is Teletraan 1, inspired from a supercomputer from a famous comic series. My job is to help you navigate the universe.',
    r'bye|goodbye': 'Goodbye! If you have more questions later, don\'t hesitate to ask.',
    r'(tell me|give me) (a|some|an)(?: (?:interesting|fascinating|cool|amazing|awesome))? (?:space )?fact(s)?': 'Sure! Did you know that {space_fact}?',
}

# Λεξικά πληροφοριών που χρησιμοποιεί το Teletraan 1. 
# Ως μελλοντική βελτίωση του chatbot θα μπορούσε να αποτελέσει η χρήση online βάσης δεδομένων για την ανάκτηση και αποθήκευση περισσότερων πληροφοριών.
space_facts = [
    "the Sun contains 99.8% of the total mass of the entire solar system",
    "Neutron stars are so dense that a teaspoonful would weigh more than all the people on Earth combined",
    "Jupiter's Great Red Spot is a storm that has been raging for at least 400 years",
    "there are more stars in the universe than grains of sand on all the beaches on Earth",
    "Venus is the hottest planet in our solar system, with surface temperatures reaching about 900°F (475°C)"
]

solar_system_facts = {
    'mercury': 'the closest planet to the Sun.',
    'venus': 'the second planet from the Sun and the hottest planet in our solar system.',
    'earth': 'the third planet from the Sun and the only known planet to support life.',
    'mars': 'the fourth planet from the Sun, often called the "Red Planet" due to its reddish appearance.',
    'jupiter': 'the largest planet in our solar system.',
    'saturn': 'known for its distinctive rings made of ice and dust.',
    'uranus': 'the seventh planet from the Sun and rotates on its side.',
    'neptune': 'the eighth planet from the Sun and the farthest planet in our solar system.',
    'pluto': 'formerly considered the ninth planet but is now classified as a dwarf planet.'
}

planet_info = {
    'mercury': {'distance': 57.9, 'temperature': '430°C'},
    'venus': {'distance': 108.2, 'temperature': '471°C'},
    'earth': {'distance': 149.6, 'temperature': '14°C'},
    'mars': {'distance': 227.9, 'temperature': '-63°C'},
    'jupiter': {'distance': 778.6, 'temperature': '-108°C'},
    'saturn': {'distance': 1433.5, 'temperature': '-139°C'},
    'uranus': {'distance': 2872.5, 'temperature': '-197°C'},
    'neptune': {'distance': 4495.1, 'temperature': '-201°C'},
    'pluto': {'distance': 5906.4, 'temperature': '-229°C'}
}

# Συνάρτηση που ανατρέχει στην λίστα των space facts και επιστρέφει ένα γεγονός στην τύχη
def get_random_space_fact():
    import random
    return random.choice(space_facts)

# Συνάρτηση που υπολογίζει την απόλυτη τιμή της απόστασης δύο πλανητών.
# Εξασφαλίζει, επίσης, ότι ο αριθμός που θα επιστρέψει θα έχει μέχρι δύο δεκαδικά ψηφία, για να είναι ευκολότερο στην ανάγνωση.
def calculate_distance(planet1, planet2):
    distance = abs(planet_info[planet1]['distance'] - planet_info[planet2]['distance'])
    return "{:.2f}".format(distance)

# Η κύρια συνάρτηση που τρέχει το πρόγραμμα για να υλοποιηθεί το chatbot.
# Αναγνωρίζει λέξεις κλειδιά στην απάντηση που θα δώσει το chatbot αλλά και από το κείμενο εισόδου του χρήστη.
# Δέχεται το κείμενο εισόδου του χρήστη και απαντά με βάση προκαθορισμένα μοτίβα και πληροφορίες.
# Διατρέχει κάθε συνδιασμό μοτίβου-απάντησης στο λεξικό 'patterns' και αν εντοπίσει γνωστό μοτίβο, απαντάει ανάλογα.
# Αν όχι, δίνει μια γενική απάντηση για τον χρήστη, λέγοντας του ότι μπορεί να το ρωτήσει οτιδήποτε για το διάστημα.
def chatbot(input_text):
    for pattern, response in patterns.items():
        match = re.match(pattern, input_text, re.IGNORECASE)
        if match:
            if '{space_fact}' in response:
                return response.format(space_fact=get_random_space_fact())
            elif '{temperature}' in response: 
                planet_name = match.group(1).strip().lower()
                if planet_name in planet_info: #Ελέγχει αν υπάρχει στο λεξικό
                    # Φροντίζει πάντα το όνομα του πλανήτη να αρχίζει με κεφαλαίο στην απάντηση που επιστρέφει
                    return response.format(planet_name.capitalize(), temperature=planet_info[planet_name]['temperature'])
                else:
                    return "I'm sorry, I don't have information about the temperature of that planet."
            elif '{distance}' in response:
                # Το συγκεκριμένο if ελέγχει ποιά περίπτωση από τις δύο είναι: απόσταση από τον Ήλιο ή μεταξύ πλανητών.
                if 'from the sun' in input_text:
                    planet = match.group(1).strip().lower()
                    return response.format(planet.capitalize(), distance=planet_info[planet]['distance'])
                else:
                    planet1 = match.group(1).strip().lower()
                    planet2 = match.group(2).strip().lower()
                    # Εναλλακτική απάντηση σε περίπτωση που η απόσταση αδύναται να υπολογιστεί, διότι ο χρήστης θέλει να υπολογίσει την απόσταση από τον ίδιο πλανήτη.
                    if planet1 == planet2: 
                        return "You can't calculate the distance on the same planet!"
                    return response.format(planet1.capitalize(), planet2.capitalize(), distance=calculate_distance(planet1, planet2))
            elif '{0}' in response:
                planet_name = match.group(2).strip().lower()
                if planet_name in solar_system_facts:
                    return response.format(planet_name.capitalize(), solar_system_facts[planet_name])
                elif planet_name in planet_info:
                    return response.format(planet_name.capitalize(), planet_info[planet_name])
                else:
                    return "I'm sorry, I don't have information about that."
            else:
                return response
    return "I'm here to help. Please feel free to ask me anything about our solar system."

# Αυτή η συνάρτηση αποτελεί το σημείο εκκίνησης για το πρόγραμμα chatbot.
# Η διαδικασία αυτή επαναλαμβάνεται όσο ο χρήστης δεν έχει εισάγει την λέξη "bye" ή "goodbye"
def main():
    print("  -- Welcome to Teletraan 1 - Your Solar System Guide & Chatbot! -- ")
    print(" >> You can start asking questions. Type 'bye' to end the session. <<")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye' or user_input.lower() == 'goodbye':
            print(chatbot(user_input))
            break
        else:
            print("Teletraan 1:", chatbot(user_input))

if __name__ == "__main__":
    main()
