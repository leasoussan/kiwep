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








fields_list = ['Problem solving','Autonomy', 'Rigor', 'Initiative', 'Team spirit', 'Leadership', 'Communication', 'Creativity', 'Emotional intelligence', 'Critical spirit', 'Self confidence', 'Flexibility', 'Time management', 'Stress management', 'Fiability', 'Determination', 'Stress management', 'Empathy']
skill_type = ['hard', 'soft']

def pop_field(skill_type):
    # skill = random.choice(skill_type)
    skill = 'soft'
    for f in fields_list:
        f = Field.objects.get_or_create(name=f, skills_type=skill)


        print(f"the Field {f} was created")



institution_category_list = ['High-School', 'University', 'organization']

def pop_institution_category_list(institution_category_list):
    for institution in institution_category_list:
        institution_i = InstitutionCategory.objects.get_or_create(
            name =institution,
        )
        fields = list(Field.objects.all())
        print(fields)
        institution_i.fields.add(*random.sample(fields, 2))

        print(f"the Institution Category {institution_i} was created")

# pop_institution_category_list(institution_category_list)


#
# cities = {'country':'israel', 'city': 'Tel-aviv',('country':'Israel', 'city': 'Paris') }
#
# def pop_cities(list):
#     for country,city in cities.items():
#         country = City.objects.get_or_create(name = city, country=country)


countries =['Israel', 'France', 'United Kingdom' , 'United State' ]
def pop_country():
    for country in countries:
        country = Country.objects.get_or_create(name=country)

        print(f"the Country  {country} was created")



def pop_city():
    city1 = City.objects.get_or_create(name='tel-aviv', country = Country.objects.filter(name='Israel')[0]),
    city2 = City.objects.get_or_create(name='paris', country=Country.objects.filter(name='France')[0]),
    print(f"the City  {city1}  {city2}was created")







fields_list_hard = ['No Code' , 'Personal development', 'Entrepreneurship']


def pop_field_hard():
    skill = 'hard'
    for f in fields_list_hard:
        f = Field.objects.get_or_create(name=f, skills_type=skill)

    print(f"the Field {f} was created")



def pop_level(n):
    for i in range(n):
        level= Level.objects.get_or_create(name=i, rating='3')

        print(f'level:{i} was created')









skills_list = ['Develop', 'writing', 'elaborating', 'research', 'Communicating']

def pop_skills(n):

    for skill in skills_list:
        skill = Skills(name=skill)
        skill.save()
        skill.field.add(random.choice(list(Field.objects.all())))
        print(f'Skill:{skill.id} was created')

#
# def pop_student_soft_skills_rating(n):
#     for soft in skills:
#         student = random.choice(Student.objects.all())
#         skill = random.choice(Skills.objects.all())
#         rating = random.randint(1,10)
#         team =  random.choice(Team.objects.all())
#         comment = "You did well, with time we all can do better:)"
#
#         student = StudentSoftSkillRating.objects.get_or_create(
#             student=student,
#             skill=skill,
#             rating=rating,
#             team=team,
#             comment=comment
#         )
#
#         soft.save()
#
#     print(f'Student Rating Board:{student.id}')




pop_field(fields_list)
pop_field_hard()
# pop_institution_category_list(institution_category_list)

pop_country()
pop_city()


pop_level(4)


pop_skills(skills_list)