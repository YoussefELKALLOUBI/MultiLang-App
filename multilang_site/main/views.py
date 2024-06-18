from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import openai

from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Définir la clé API OpenAI
openai.api_key = "sk-proj-Hr3kioMTiuVIr2CMFCgnT3BlbkFJcaSWsFlVHGshhHnraN2X"

# Créer un cache simple pour les réponses
chat_cache = {}

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        
        # Vérifier si la question est déjà dans le cache
        if question in chat_cache:
            answer = chat_cache[question]
        else:
            try:
                response = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question}
                    ],
                    max_tokens=150
                )
                answer = response.choices[0].message['content'].strip()
                # Stocker la réponse dans le cache
                chat_cache[question] = answer
            except openai.error.RateLimitError:
                answer = "Vous avez dépassé votre quota d'utilisation de l'API. Veuillez réessayer plus tard."

        return render(request, 'main/chatbot.html', {'answer': answer})

    return render(request, 'main/chatbot.html')


def switch_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in dict(settings.LANGUAGES):
            activate(language)
    # Redirection vers la page précédente ou une page par défaut
    return redirect(request.META.get('HTTP_REFERER', '/'))

