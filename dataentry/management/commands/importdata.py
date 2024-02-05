from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
import csv
from django.apps import apps
# proposed command - python manage.py importdata file_path model_name

class Command(BaseCommand):
    help = "import data from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('file-path', type=str, help="path to the CSV file")
        parser.add_argument('model_name', type=str, help="Name of the model")
        
    def handle(self, *args, **kwargs):
        #logic goes here
        file_path = kwargs['file-path']
        model_name = kwargs['model_name'].capitalize()
        #search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            #Try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue # model not found in this app, continue searching in next apps
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any apps')
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from csv successfully'))
        
        
        