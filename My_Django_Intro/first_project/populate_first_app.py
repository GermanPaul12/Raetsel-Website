'''
This Script is used to generate fake data to populate the database
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# FAKE POP SCRIPT

from faker import Faker
from first_app.models import Topic,Website,AccessRecord
import random

faker = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get the topic for the entry
        top = add_topic()
        # Create the fake data for the entry
        fake_url = faker.url()
        fake_date = faker.date()
        fake_name = faker.company()
        # Create new website entry
        website = Website.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        # Create a fake AccessRecord 
        access_record = AccessRecord.objects.get_or_create(name=website,date=fake_date)[0]
        
        
if __name__ == '__main__':
    print("Populating script!")
    populate(10)
    print("Populating complete!")        