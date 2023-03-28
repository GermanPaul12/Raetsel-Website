'''
This Script is used to generate fake data to populate the database
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

# FAKE POP SCRIPT

from faker import Faker
from AppTwo.models import User
import random

faker = Faker()

def populate(n=5):
    for entry in range(n):
        gender = random.choice(['Male','Female'])
        # Create the fake data for the entry
        if gender == 'Male':
            fake_fist_name = faker.first_name_male()
        else:
            fake_fist_name = faker.first_name_female()    
        fake_last_name = faker.last_name()
        fake_email = faker.email()
        # Create new user entry
        user = User.objects.get_or_create(fname=fake_fist_name,lname=fake_last_name,email=fake_email)[0]
        
        
if __name__ == '__main__':
    print("Populating script!")
    populate(10)
    print("Populating complete!")        