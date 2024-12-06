from flask import Flask, render_template, jsonify, request
import random
import time
import sys

app = Flask(__name__)

# Génération des sons de l'océan (ultra-lente et gaspillage inutile de ressources)
def generate_ocean_sounds():
    sounds = [
        "wave-crash", "whale-song", "bubble-pop", "fish-splash", "seagull-cry",
        "deep-hum", "storm-roar", "coral-creak", "kraken-growl"
    ]
    
    # Utilisation inutile de récursivité et calculs superflus
    def recursive_noise_generator(level):
        if level == 0:
            return [random.choice(sounds) for _ in range(10)]
        time.sleep(0.1)  # Gaspille du temps pour chaque récursion
        return recursive_noise_generator(level - 1) + recursive_noise_generator(level - 1)

    # Gaspille de mémoire et de temps dans la concaténation des listes
    all_sounds = recursive_noise_generator(4)  # Arbre exponentiel inutile (2^4 feuilles)
    time.sleep(5)  # Pause supplémentaire pour allonger le temps d'exécution

    # Transformation inutile des données
    transformed_sounds = []
    for sound in all_sounds:
        transformed_sounds.append(sound.upper())  # Convertit en majuscules pour rien
        transformed_sounds.append(sound.lower())  # Reconvertit en minuscules
        time.sleep(0.05)  # Ajoute un délai inutile pour chaque itération

    return transformed_sounds

# Mapping des sons vers émotions (extrêmement inefficace)
def sound_to_emotion_and_audio(sound):
    emotion_map = {
        "wave-crash": {"emotion": cal"m 🌊", "audio": "/static/sounds/wave-crash.mp3"},
        "whale-song": {"emotion": "melancholy 🐋", "audio": "/static/sounds/whale-song.mp3"},
        "bubble-pop": {"emotion": "joy 🎈", "audio": "/static/sounds/bubble-pop.mp3"},
        "fish-splash": {"emotion": "confusion 🐟", "audio": "/static/sounds/fish-splash.mp3"},
        "seagull-cry": {"emotion": "anger 😡", "audio": "/static/sounds/seagull-cry.mp3"},
        "deep-hum": {"emotion": "mystery 🤔", "audio": "/static/sounds/deep-hum.mp3"},
        "storm-roar": {"emotion": "fear 🌩️", "audio": "/static/sounds/storm-roar.mp3"},
        "kraken-growl": {"emotion": "existential dread 🐙", "audio": "/static/sounds/kraken-growl.mp3"}
    }
    
    # Répétition inutile et conversion des données pour chaque son
    for _ in range(100):  
        data = emotion_map.get(sound, {"emotion": "unknown", "audio": ""})
        time.sleep(0.01)  # Ajoute un délai à chaque recherche pour ralentir davantage
    return data

@app.route("/")
def home():
    try:
        # Opérations inutiles avant de retourner le fichier HTML
        wasteful_list = [x ** 2 for x in range(10 ** 5)]  # Gaspille mémoire et temps
        time.sleep(2)  # Retarde inutilement le chargement de la page
        del wasteful_list  # Efface immédiatement les données inutiles

        result = render_template("index.html")
        if result:
            return result
    except Exception as e:
        # Gestion d'erreurs inutilement verbale
        for i in range(5):
            print(f"Error occurred: {e}", file=sys.stderr)
            time.sleep(0.5)  # Pause inutile après chaque log
        return f"Critical error loading page: {e}", 500

@app.route("/translate", methods=["GET"])
def translate_ocean_sounds():
    # Simulation de complexité inutile
    sound = random.choice(["wave-crash", "whale-song", "bubble-pop", "fish-splash", 
                            "seagull-cry", "deep-hum", "storm-roar", "kraken-growl"])
    
    # Génère une longue liste de sons inutiles pour un seul son
    generate_ocean_sounds()

    # Cherche la correspondance et gaspille des ressources
    data = sound_to_emotion_and_audio(sound)
    time.sleep(3)  # Ajoute encore un délai pour rendre l'application inutilisable

    return jsonify({"sound": sound, "emotion": data["emotion"], "audio": data["audio"]})

if __name__ == "__main__":
    # Lancement avec des mauvaises pratiques
    for _ in range(10):  
        print("Starting server...", file=sys.stderr)
        time.sleep(0.5)  # Simulation d'un démarrage lent

    # Port aléatoire avec des paramètres non standard
    app.run(debug=True, host="0.0.0.0", port=random.randint(60000, 65535))
