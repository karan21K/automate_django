from django.core.management.base import BaseCommand
from dataentry.models import Student
# I want to add data to the database using the custom command
class Command(BaseCommand):
    help = 'it will insert data to the database'
    
    def handle(self, *args, **kwargs):
        #logic goes here
        dataset = [
            {'roll_no': 1002, 'name': 'sachin', 'age':21},
            {'roll_no': 1006, 'name': 'michel', 'age':22},
            {'roll_no': 1004, 'name': 'mike', 'age':23},
            {'roll_no': 1005, 'name': 'joseph', 'age':25}
            ]
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name = data['name'], age = data['age'])
            else:
               self.stdout.write(self.style.WARNING(f'Student with roll_no {roll_no} already exists!')) 
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))
    
    