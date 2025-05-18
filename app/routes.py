from flask import Blueprint, render_template, request
import requests

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    original_text = ''
    source_lang = 'en'
    target_lang = 'fr'

    if request.method == 'POST':
        original_text = request.form.get('text')
        source_lang = request.form.get('source')
        target_lang = request.form.get('target')

        if original_text:
            try:
                url = "https://api.mymemory.translated.net/get"
                params = {
                    'q': original_text,
                    'langpair': f'{source_lang}|{target_lang}'
                }

                response = requests.get(url, params=params)
                data = response.json()

                if 'responseData' in data and 'translatedText' in data['responseData']:
                    translated_text = data['responseData']['translatedText']
                else:
                    translated_text = f"[Erreur API] Réponse inattendue : {data}"

            except Exception as e:
                translated_text = f"[Erreur Exception] {str(e)}"

    return render_template('index.html',
                           original_text=original_text,
                           translated_text=translated_text,
                           source_lang=source_lang,
                           target_lang=target_lang)
