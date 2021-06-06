
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
from django.core.exceptions import ObjectDoesNotExist

from django.forms.models import model_to_dict

import json
import urllib
import requests

fak = Faker()


MyUser = get_user_model()








instit_name =['KIWEP']

def pop_institution(n):
    for institut in range(n):
        representative = random.choice(Representative.objects.filter(institution = None))
        name = random.choice(instit_name)
        category = random.choice(InstitutionCategory.objects.all())
        field = random.choice(list(Field.objects.all()))
        profile_pic = 'images/default.png'
        address = 'undefine Adress yet'
        city = random.choice(list(City.objects.all()))
        contact_name = 'Unknown'
        phone_number = '+97654321'
        email = 'artizen18@@gmail.com'
        website = 'www.google.com'
        description = 'School for the people'

        institut = Institution(
            name = name,
            category = category,
            field = field,
            profile_pic = profile_pic,
            address = address,
            city = city,
            joined_date = timezone.now(),
            contact_name = contact_name,
            phone_number = phone_number,
            email = email,
            website = website,
            description = description,
            representative =representative
        )
        institut.save()

        print(f"the City  {city} was created")



def pop_representative(n):
    for i in range(n):
        user = MyUser.objects.create(
            first_name = fak.first_name(),
            last_name =fak.last_name(),
            email = 'artizen18@gmail.com',
            password = '123456',
            phone_number = '+972 500000000',
            profile_pic = 'media/profile/avatar.png',
            city = random.choice(City.objects.all())
        ),

        user.save()
        rep_profile = Representative.objects.create(
            user=user

        )
        rep_profile.save()

        print(f'Reprensentative Created Profile:{rep_profile.id}')

        # finished
    print(f"Finished...{n}speaker  entries populated.")







def pop_speaker(n):
    for i in range(n):
        user = MyUser.objects.create_user(
            first_name = fak.first_name(),
            last_name =fak.last_name(),
            email = 'artizen18@gmail.com',
            username =  fak.user_name(),
            password = '123456',
            phone_number = '+972 500000000',
            profile_pic = 'media/profile/avatar.png',
            city = City.objects.get(name='Tel-aviv')
            )
        user.save()

        speaker_profile = Speaker.objects.create(
            user = user,
            )
        speaker_profile.save()
        speaker_profile.institution.add(random.choice(Institution.objects.all()))
        speaker_profile.group.add(random.choice(Group.objects.all()))
        print(f'Speaker Created Profile:{speaker_profile.id}')

    # finished
    print(f"Finished...{n}speaker  entries populated.")









def pop_student(n):
    for i in range(n):
        user = MyUser.objects.create_user(
            first_name = fak.first_name(),
            last_name =fak.last_name(),
            email = 'artizen18@gmail.com',
            username =  fak.user_name(),
            password = '123456',
            phone_number = '+972 500000000',
            profile_pic = 'media/profile/avatar.png',
            city = City.objects.get(name='Tel-aviv'),

            )
        user.save()

        student_profile = Student.objects.create(
            class_level= random.choice(Group.objects.all()),
            field = random.choice(Field.objects.all()),
            dob= '09-07-1986',
            user = user,

        )
        student_profile.save()


        print(f'Student Created Profile:{student_profile.id}')

    # finished
    print(f"Finished...{n} students populated.")







def pop_resources(n):
    for r in range(n):
        name = 'Resource {resource}'
        link = "www.google.com"
        image =  'image/default.png'
        file_rsc = 'null'
        text = 'This is aresource about.......'
        owner = random.choice(MyUser.objects.all())
        field =  random.choice(Field.objects.all())

        r = Resource(name=name, link=link, image=image, file_rsc=file_rsc, text=text,owner=owner, field=field)
        r.save()
        print(f'resource :{r.name} was created')

    print(f"Finished...{n} Resource populated.")




bool = [True, False ]

def pop_project(n):
    for project in range(n+1):
        name = "Kiwep {n}"
        title = "Welcome to Kiwep Project "
        required_skills = "desire to learn"
        acquired_skills = "Digital"
        description = "This Project is about Blbalabal"
        time_to_complete = random.randrange(60, 120, 10)
        difficulty = random.choice(Level.objects.all())
        speaker = random.choice(Speaker.objects.all())


        p = Project(
            name = name,
            title =title,
            description = description,
            time_to_complet = time_to_complete,
            difficulty = difficulty,
            completed = False,
            speaker = speaker,
            points = random.randint(1,4),
            is_template= random.choice(bool),
            is_global = random.choice(bool),
            is_premium= random.choice(bool)
        )
        p.save()

        field = list(Field.objects.all())
        required_skills= list(Skills.objects.all())
        acquired_skills = list(Skills.objects.all())
        missions = list(Mission.objects.all())
        p.field.add(*random.sample(field, 2))
        p.acquried_skills.add(*random.sample(acquired_skills,2))
        p.required_skills.add(*random.sample(required_skills,2))
        p.missions.add(*random.sample(missions, 4))

        print(f'Project:{p.id}')


    print(f"Finished...{n} Projects populated.")





MISSION_TYPE=('s_m', 't_m')
RESPONSE_TYPE = ('link', 'video', 'doc', 'power_p', 'image')








STAGE_CHOICE = ['Start','Middle', 'Final']
def pop_missions(n):
    for mission in range(n):
        name = f'Mission {mission}'
        project = random.choice(Project.objects.all())
        stage = random.choice(STAGE_CHOICE)
        field =  random.choice(Field.objects.all())
        level = random.choice(Level.objects.all())
        response_type =  random.choice(RESPONSE_TYPE)
        description = 'This mission you have to .....about.......'
        resources = random.choices(Resource.objects.all())
        owner = random.choice(MyUser.objects.all())
        points = 3



        m = Mission(
            name=name,
            field=field,
            level=level,

            description=description,
            owner=owner,
            points = points,
            response_type = response_type,
            created_date= timezone.now()
            completed = False
            )
        m.save()
        m.resources.add(random.choice(list(Resource.objects.all())))
        m.acquried_skill.add(random.choice(Skills.objects.all()))
        print(f'mission:{m.id} was created')

    print(f"Finished...{n} Mission populated.")




def pop_project_mission_rating():
    project = Project.objects.get(name="Kiwep")
    for project_mission in project.mission:

        p_rating = ProjectMissionRating(
        project = project,
        mission = project_mission,
        pourcentage = (random.randint(10,100)/100),
        )

        p_rating.save()
        p_rating.hard_skills.add(random.choice(Skills.objects.all()))

        print(f'populated kiwep with hard skills rating')


def hard_skills_rating():
    pass


def pop_team(n):
    for team in range(n):
        name = "team {team}"
        project = random.choice(Project.objects.all())
        start_date = ('2021-09-09')
        group_Institution = random.choice(Group.objects.all())
        final_project = 'file to upload per participant'
        manager = random.choice(Speaker.objects.all())
        stage =  random.choice(STAGE_CHOICE)
        t = Team(
            name=name,
            project=project,
            start_date=start_date,
            group_Institution=group_Institution,
            manager=manager,
        )
        t.save()
        members = list(Student.objects.all())

        t.participants.add(*random.sample(members, 4))
        print(f'Team:{t.id}')

# * to unpack a list (as we cant give a list)
# ** to unpack a dict
#
    print(f"Finished...{n} Teams populated.")



def pop_student_mission_project(n):
    for project in range(n):
        team = random.choice(Team.objects.all())
        mission = random.choice(Mission.objects.all())
        completed = False
        created_date = '2020-09-08'
        due_date = '2020-10-10'


        mp = IndividualMission(
            team=team,
            mission=mission,
            completed=completed,
            created_date=created_date,
            due_date=due_date,

        )
        mp.save()
        mp.attributed_to.add(random.choice(Student.objects.all()))

        print(f'mp:{mp.id}')


# -------------------------------------------------
def pop_mission_collective_projects(n):
    for project in range(n):
        team = random.choice(Team.objects.all())
        mission = random.choice(Mission.objects.all())
        completed = False
        created_date = '2020-09-08'
        due_date = '2020-10-10'


        cm = CollectiveMission(
            team=team,
            mission=mission,
            completed=completed,
            created_date=created_date,
            due_date=due_date,


        )
        cm.save()
        cm.attributed_to.add(random.choice(Student.objects.all()))
        print(f'mp:{cm.id}')


# ----------------------------------------------------------------------

# ----------------------------------------------------
pop_representative(2)


pop_institution(2)



pop_speaker(5)


pop_student(30)

pop_resources(20)

pop_missions(20)


pop_project(6)
pop_project_mission_rating()
pop_team(4)
pop_student_soft_skills_rating(20)
pop_mission_projects(20)


pop_student_mission_project(10)
pop_mission_collective_projects(10)


# pop_institution_category_list(institution_category_list)














