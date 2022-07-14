from django.core.management.base import BaseCommand
from main.scripts import get_data


class Command(BaseCommand):
    def handle(self, **options):
        get_data()
