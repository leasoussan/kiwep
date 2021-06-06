import django
# os to interact with computer
import os
from faker import Faker
import random
# setting the env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiwep.settings')
# this line will check for the setting to know where to save it
django.setup()
# after the above step >> we can import models
from accounts.models import *
from content.models import *
from backend.models import *

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model








fields_list = ['Economics', 'Digital', 'Commercial', 'Artisitic', 'Fashion', 'Other', 'Leadership', 'SelfLearner','TeamPLayer' ]
skill_type = ['hard', 'soft']

def pop_field(skill_type):
    skill = random.choice(skill_type)
    for f in fields_list:
        f = Field.objects.get_or_create(name=f, skills_type=skill)


        print(f"the Field {f} was created")



institution_category_list = ['School', 'University', 'Institution', 'organization', 'Independent', 'None-Profit']

def pop_institution_category_list(institution_category_list):
    for institution in institution_category_list:
        institution = InstitutionCategory.objects.get_or_create(
            name =institution,
            fields = random.choice(Field.objects.all())
        )

        print(f"the Institution Category {institution} was created")

# pop_institution_category_list(institution_category_list)


#
# cities = {'country':'israel', 'city': 'Tel-aviv',('country':'Israel', 'city': 'Paris') }
#
# def pop_cities(list):
#     for country,city in cities.items():
#         country = City.objects.get_or_create(name = city, country=country)



def pop_country():
    country =Country.objects.get_or_create(name='Israel')
    country2 =Country.objects.get_or_create(name='France')

    print(f"the Country  {country} {country2} was created")



def pop_city():
    city = City.objects.get_or_create(name='Tel-aviv', country = Country.objects.filter(name='Israel')),

    print(f"the City  {city} was created")







fields_list = ['Economics', 'Digital', 'Commercial', 'Artisitic', 'Fashion', 'Other', 'Leadership', 'SelfLearner','TeamPLayer' ]
skill_type = ['hard', 'soft']

def pop_field(skill_type):
    skill = random.choice(skill_type)
    for f in fields_list:
        f = Field.objects.get_or_create(name=f, skills_type=skill)

        print(f"the Field {f} was created")



def pop_level(n):
    for i in range(n):
        level= Level.objects.get_or_create(name=i, rating='3')



groups = ['3rd', '4th', '5th', '6th']


def pop_group(groups):
    for group in groups:
        group = Group.objects.get_or_create(name=group,
        number_of_participants = '5',
        institution = random.choice(Institution.objects.all())
)




skills_list = ['Develop', 'writing', 'elaborating', 'research', 'Communicating']


def pop_skills(n):
    skill = random.choice(skills_list)
    for skill in skills_list:
        skill = Skills(name = skill)
        skill.save()

        skill.field.add(random.choice(list(Field.objects.all())))




def pop_student_soft_skills_rating(n):
    for  soft in skills:
        student = random.choice(Student.objects.all())
        skill = random.choice(Skills.objects.all())
        rating = random.randint(1,10)
        team =  random.choice(Team.objects.all())
        comment = "You did well, with time we all can do better:)"

        soft = StudentSoftSkillRating(
            student=student,
            skill = skill,
            rating = rating,
            team=team,
            comment = comment
        )

        soft.save()

    print(f'Student Rating Board:{student.id}')




pop_field(fields_list)

pop_institution_category_list(institution_category_list)


pop_country()


pop_city()

groups = ['3rd', '4th', '5th', '6th']

pop_level(4)
pop_group(groups)


pop_skills(skills_list)
