from flask import Blueprint, render_template, request  # Importe les outils Flask nécessaires : Blueprint pour organiser l'app, render_template pour afficher une page HTML, et request pour accéder aux données du formulaire
import requests  # Importe la bibliothèque requests pour faire des appels HTTP (ici vers une API de traduction)

main = Blueprint('main', __name__)  # Crée un blueprint Flask appelé 'main', pour organiser les routes dans un fichier séparé

@main.route('/', methods=['GET', 'POST'])  # Déclare une route pour la racine du site ("/"), qui accepte les méthodes GET (affichage) et POST (soumission du formulaire)
def index():  # Fonction qui s'exécute quand on accède à la route "/"
    translated_text = ''  # Initialisation de la variable qui contiendra le texte traduit
    original_text = ''  # Initialisation du texte original saisi par l'utilisateur
    source_lang = 'en'  # Langue source par défaut : anglais
    target_lang = 'fr'  # Langue cible par défaut : français

    if request.method == 'POST':  # Si le formulaire a été soumis (méthode POST)
        original_text = request.form.get('text')  # Récupère le texte à traduire depuis le champ du formulaire
        source_lang = request.form.get('source')  # Récupère la langue source choisie
        target_lang = request.form.get('target')  # Récupère la langue cible choisie

        if original_text:  # Si un texte a bien été saisi
            try:
                url = "https://api.mymemory.translated.net/get"  # URL de l'API de traduction
                params = {
                    'q': original_text,  # Texte à traduire
                    'langpair': f'{source_lang}|{target_lang}'  # Format attendu par l'API : source|cible
                }

                response = requests.get(url, params=params)  # Envoie la requête GET à l’API avec les paramètres
                data = response.json()  # Récupère la réponse JSON de l’API

                if 'responseData' in data and 'translatedText' in data['responseData']:  # Si la réponse contient bien le texte traduit
                    translated_text = data['responseData']['translatedText']  # Récupère le texte traduit depuis la réponse
                else:
                    translated_text = f"[Erreur API] Réponse inattendue : {data}"  # Si la structure de la réponse est inattendue

            except Exception as e:  # Si une erreur survient (problème de connexion, etc.)
                translated_text = f"[Erreur Exception] {str(e)}"  # Affiche l’erreur capturée

    return render_template('index.html',
                           original_text=original_text,  # Envoie le texte original à la page HTML
                           translated_text=translated_text,  # Envoie le texte traduit à la page HTML
                           source_lang=source_lang,  # Envoie la langue source sélectionnée
                           target_lang=target_lang)  # Envoie la langue cible sélectionnée
