from faker import Faker
fake = Faker()
from .models import *
import random
import datetime

def create_fake_students():
    for i in range(0 , 100):
        Student.objects.create(
            student_name = fake.name(),
            student_age = random.randint(18 , 30),
            student_birthday = datetime.date.today(), 
            student_info = fake.address(),
        )
