import random
from collections import defaultdict

# Cleaned word list (ASCII only) from English, Spanish (plain), French (plain), Italian (plain), Portuguese (plain), Latin, German, Nigerian
WORD_LIST = [
    # English
    "sun", "moon", "star", "sky", "cloud", "tree", "river", "stone", "mountain", "ocean",
    "fire", "wind", "earth", "light", "shadow", "bird", "flower", "grass", "storm", "rain",
    "dream", "hope", "love", "peace", "joy", "fear", "pain", "heart", "soul", "mind",

    # Spanish (no accents)
    "sol", "luna", "estrella", "cielo", "nube", "arbol", "rio", "piedra", "montana", "oceano",
    "fuego", "viento", "tierra", "luz", "sombra", "pajaro", "flor", "hierba", "tormenta", "lluvia",
    "sueno", "esperanza", "amor", "paz", "alegria", "miedo", "dolor", "corazon", "alma", "mente",

    # French (plain)
    "soleil", "lune", "etoile", "ciel", "nuage", "arbre", "riviere", "pierre", "montagne", "ocean",
    "feu", "vent", "terre", "lumiere", "ombre", "oiseau", "fleur", "herbe", "tempete", "pluie",
    "reve", "espoir", "amour", "paix", "joie", "peur", "douleur", "coeur", "ame", "esprit",

    # Italian
    "sole", "luna", "stella", "cielo", "nuvola", "albero", "fiume", "pietra", "montagna", "oceano",
    "fuoco", "vento", "terra", "luce", "ombra", "uccello", "fiore", "erba", "tempesta", "pioggia",
    "sogno", "speranza", "amore", "pace", "gioia", "paura", "dolore", "cuore", "anima", "mente",

    # Portuguese (plain)
    "sol", "lua", "estrela", "ceu", "nuvem", "arvore", "rio", "pedra", "montanha", "oceano",
    "fogo", "vento", "terra", "luz", "sombra", "passaro", "flor", "grama", "tempestade", "chuva",
    "sonho", "esperanca", "amor", "paz", "alegria", "medo", "dor", "coracao", "alma", "mente",

    # Latin
    "sol", "luna", "stella", "caelum", "nubes", "arbor", "flumen", "lapis", "mons", "mare",
    "ignis", "ventus", "terra", "lux", "umbra", "avis", "flos", "herba", "procella", "pluvia",
    "somnium", "spes", "amor", "pax", "gaudium", "timor", "dolor", "cor", "anima", "mens",

    # German (plain)
    "sonne", "mond", "stern", "himmel", "wolke", "baum", "fluss", "stein", "berg", "ozean",
    "feuer", "wind", "erde", "licht", "schatten", "vogel", "blume", "gras", "sturm", "regen",
    "traum", "hoffnung", "liebe", "frieden", "freude", "angst", "schmerz", "herz", "seele", "geist",

    # Nigerian (Yoruba and Hausa simplified, no tones)
    "orun", "osupa", "irawo", "oju", "awan", "igi", "odo", "okuta", "oke", "omi",
    "ina", "afefe", "ile", "imole", "ojiji", "eye", "ododo", "koriko", "iji", "ojo",
    "ala", "ireti", "ife", "alafia", "ayo", "iberu", "irora", "okan", "emi", "okanmind"
]

# Limits for word use
MAX_FIRST = 10
MAX_SECOND = 10

def generate_unique_pairs(word_list, pair_count=2000):
    first_count = defaultdict(int)   # Count as first word
    second_count = defaultdict(int) # Count as second word
    pairs = set()  # Store unique pairs

    available_words = list(set(word_list))  # Unique words
    max_attempts = pair_count * 50  # Safety net

    attempts = 0
    while len(pairs) < pair_count and attempts < max_attempts:
        word1, word2 = random.sample(available_words, 2)  # Pick different words

        # Ensure limits not exceeded
        if first_count[word1] < MAX_FIRST and second_count[word2] < MAX_SECOND:
            combined = word1 + word2
            if combined not in pairs:  # Ensure uniqueness
                pairs.add(combined)
                first_count[word1] += 1
                second_count[word2] += 1
        attempts += 1

    if len(pairs) < pair_count:
        print(f"Warning: Only generated {len(pairs)} pairs due to constraints.")

    return list(pairs)

def save_words_to_file(word_list, filename="output_2000_combined_words.txt"):
    """Save combined words to file as plain ASCII text."""
    with open(filename, "w", encoding="ascii") as file:
        for word in word_list:
            file.write(word + "\n")

def main():
    combined_words = generate_unique_pairs(WORD_LIST, 2000)
    save_words_to_file(combined_words)
    print(f"Generated {len(combined_words)} unique word pairs. Saved to 'output_2000_combined_words.txt'.")

if __name__ == "__main__":
    main()
