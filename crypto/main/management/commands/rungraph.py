from django.core.management.base import BaseCommand
from main.graph import run_graph


class Command(BaseCommand):
    def handle(self):
        print(data.head(2))
