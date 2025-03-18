import random
import pandas as pd

# Deduplicated word list with additional English words replacing Italian words
WORD_LIST = list(set([
    "sun", "moon", "star", "sky", "cloud", "tree", "river", "stone", "mountain", "ocean",
    "fire", "wind", "earth", "light", "shadow", "bird", "flower", "grass", "storm", "rain",
    "dream", "hope", "love", "peace", "joy", "fear", "pain", "heart", "soul", "mind",
    "sol", "luna", "estrella", "cielo", "nube", "arbol", "rio", "piedra", "montana", "oceano",
    "fuego", "viento", "tierra", "luz", "sombra", "pajaro", "flor", "hierba", "tormenta", "lluvia",
    "sueno", "esperanza", "amor", "paz", "alegria", "miedo", "dolor", "corazon", "alma", "mente",
    "soleil", "lune", "etoile", "ciel", "nuage", "arbre", "riviere", "pierre", "montagne", "ocean",
    "feu", "vent", "terre", "lumiere", "ombre", "oiseau", "fleur", "herbe", "tempete", "pluie",
    "reve", "espoir", "amour", "paix", "joie", "peur", "douleur", "coeur", "ame", "esprit",
    "sunrise", "sunset", "twilight", "mist", "wave", "stormy", "breeze", "thunder", "fog",
    "valley", "canyon", "meadow", "cliff", "island", "harbor", "desert", "prairie", "lake", "spring",
    "glow", "eclipse", "mirage", "horizon", "whisper", "echo", "ember", "blaze", "ripple", "tidal",
    "sunbeam", "raindrop", "frost", "dew", "crystal", "gale", "cyclone", "cascade", "raven", "dawn",
    "twinkle", "shimmer", "reflection", "bloom", "petal", "vine", "willow", "branch", "seashore", "drift",
    "harmony", "serenity", "tranquility", "wisdom", "kindness", "courage", "bravery", "melody", "lyric", "whimsy",
    "orun", "osupa", "irawo", "oju", "awan", "igi", "odo", "okuta", "oke", "omi",
    "ina", "afefe", "ile", "imole", "ojiji", "eye", "ododo", "koriko", "iji", "ojo",
    "ala", "ireti", "ife", "alafia", "ayo", "iberu", "irora", "okan", "emi", "okanmind"
]))

# Limits for word use
MAX_FIRST = 10
MAX_SECOND = 10

def generate_unique_pairs(word_list, pair_count=2000):
    first_count, second_count = {}, {}  # Track how often each word is used
    pairs = set()  # Store unique word pairs

    available_words = list(word_list)  # Unique words only
    max_attempts = pair_count * 50  # Prevent infinite loops

    attempts = 0
    while len(pairs) < pair_count and attempts < max_attempts:
        word1, word2 = random.sample(available_words, 2)  # Pick two distinct words

        # Sort to ensure uniqueness (e.g., "moonstar" == "starmoon")
        word_pair = tuple(sorted([word1, word2]))

        # Ensure limits are not exceeded
        if first_count.get(word1, 0) < MAX_FIRST and second_count.get(word2, 0) < MAX_SECOND:
            if word_pair not in pairs:
                pairs.add(word_pair)
                first_count[word1] = first_count.get(word1, 0) + 1
                second_count[word2] = second_count.get(word2, 0) + 1
        attempts += 1

    if len(pairs) < pair_count:
        print(f"Warning: Only generated {len(pairs)} pairs due to constraints.")

    return sorted(["".join(pair) for pair in pairs])  # Convert tuples to strings

def save_words_to_excel(word_list, filename="output_word_pairs.xlsx"):
    """Save combined words to an Excel file, sorted alphabetically."""
    try:
        df = pd.DataFrame(word_list, columns=["Word Pairs"])
        df.to_excel(filename, index=False)
        print(f"Successfully saved {len(word_list)} word pairs to '{filename}'.")
    except Exception as e:
        print(f"Error saving to Excel: {e}
