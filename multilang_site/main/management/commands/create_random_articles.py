# monapp/management/commands/create_articles.py

from django.core.management.base import BaseCommand
from main.models import Article  # Remplacez "monapp" par le nom de votre application Django

class Command(BaseCommand):
    help = 'Crée des instances d\'articles dans la base de données'

    def handle(self, *args, **kwargs):
        self.stdout.write('Création des articles...')

        # Logique pour créer les articles
        Article.objects.create(
            title='Premier article',
            content='Contenu du premier article...',
            publication_date='2024-06-20'
        )

        Article.objects.create(
            title='Deuxième article',
            content='Contenu du deuxième article...',
            publication_date='2024-06-21'
        )

        self.stdout.write(self.style.SUCCESS('Les articles ont été créés avec succès.'))
