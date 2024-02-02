from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help='Specifies the user')
        
    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        greeting = f'hi {name}, Good morning'
        self.stdout.write(self.style.SUCCESS(greeting))