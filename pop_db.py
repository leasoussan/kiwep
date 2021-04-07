
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




fields_list = ['Economics', 'Digital', 'Commercial', 'Artisitic', 'Fashion', 'Other']



def pop_field(fields_list):
    for f in fields_list:
        f = Field.objects.get_or_create(name=f)
    
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













def pop_country():
    country =Country.objects.get_or_create(name='israel')
    country2 =Country.objects.get_or_create(name='USA')
    
    print(f"the Country  {country} {country2} was created")



def pop_city():
    city = City.objects.get_or_create(name='Tel-aviv', country = Country.objects.get(name='israel')), 
    
    print(f"the City  {city} was created")









instit_name = ['new School', 'old School']
def pop_institution(n):
    for institut in range(n):
        representative = random.choice(Representative.objects.filter(institution = None))
        name = random.choice(instit_name)
        category = random.choice(InstitutionCategory.objects.all())
        field = random.choice(list(Field.objects.all()))
        profile_pic = 'images/default.png'
        address = 'undefine Adress yet'
        city = random.choice(list(City.objects.all()))
        joined_date = '09/08/2002'
        contact_name = 'Unknown'
        phone_number = '+97654321'
        email = 'art@gmail.com'
        website = 'www.google.com'
        description = 'School for the people'

        institut = Institution(
            name = name,
            category = category,
            field = field,
            profile_pic = profile_pic,
            address = address,
            city = city,
            joined_date = joined_date,
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
            email = fak.email(),
            
            username =  fak.user_name(),
            password = '123456',
            phone_number = '+972 500000000',
            profile_pic = 'media/profile/avatar.png',
            city = random.choice(City.objects.all()))
        user.save()

        rep_profile = Representative.objects.create(
    


            user = user,       
        )
        rep_profile.save()

        print(f'Reprensentative Created Profile:{rep_profile.id}')

        # finished
    print(f"Finished...{n}speaker  entries populated.")


groups = ['3rd', '4th', '5th', '6th']


def pop_level(n):
    for i in range(n):
        level= Level.objects.get_or_create(name=i, rating='3')


def pop_group(groups):
    for group in groups:
        group = Group.objects.get_or_create(name=group,
        number_of_participants = '5',

        institution = random.choice(Institution.objects.all())
)




def pop_speaker(n):
    for i in range(n):
        user = MyUser.objects.create_user(
            first_name = fak.first_name(),
            last_name =fak.last_name(),
            email = fak.email(),
            
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
            email = fak.email(),
            
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
            dob= '1987-09-09',
            user = user,       
        )
        student_profile.save()
        

        print(f'Student Created Profile:{student_profile.id}')

    # finished
    print(f"Finished...{n} students populated.")



def pop_resources(n):
    for resource in range(n):
        name = 'Mesource {n}'
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




subjects_list= ['Leadership', 'SelfLearner','TeamPLayer' ]

def pop_subjects(subjects_list):
    for subject in subjects_list:
        Subjects.objects.get_or_create(name = subject)



def pop_acquired_skills(n):
    for skill in range(n):
        skill = SkillsAcquired.objects.get_or_create(
            name = 'NewSkills', 
            subject = random.choice(Subjects.objects.all()),
            points = 3 )


STAGE_CHOICE = ['Start','Middle', 'Final']

def pop_missions(n):
    for mission in range(n):
        name = f'Mission {mission}'
        field =  random.choice(Field.objects.all())  
        level = random.choice(Level.objects.all())
        stage =  random.choice(STAGE_CHOICE)
        description = 'This mission you have to .....about.......'
        resources = random.choices(Resource.objects.all())
        owner = random.choice(MyUser.objects.all())
        points = 3
        acquried_skill = random.choice(SkillsAcquired.objects.all())
        
        m = Mission(
            name=name, 
            field=field, 
            level=level, 
            stage=stage, 
            description=description,
            owner=owner, 
            points = points,
            acquried_skill = acquried_skill 
            )
        m.save()
        m.resources.add(random.choice(list(Resource.objects.all())))
        print(f'mission:{m.id} was created')

    print(f"Finished...{n} Mission populated.")



def pop_project(n):
    for project in range(n+1):
        name = f"Proejct{project}"
        description = "This Project is about Blbalabal"
        time_to_complet = random.randrange(60, 120, 10)
        field = random.choice(Field.objects.all())
        difficulty = random.choice(Level.objects.all())
        completed = False
        speaker = random.choice(Speaker.objects.all())
        
        p = Project(
            name = name,
            description = description,
            time_to_complet = time_to_complet,
            field = field,
            difficulty = difficulty,
            completed = completed,
            speaker = speaker,
            title = "title",
            points = random.randint(1,4)
        ) 
        p.save()
  
        print(f'Project:{p.id}')

    
    print(f"Finished...{n} Projects populated.")


def pop_team(n):
    for team in range(n):
        name = "project {n}"
        project = random.choice(Project.objects.all())
        start_date = ('2021-09-09')
        due_date = ('2021-10-10')
        group_Institution = random.choice(Group.objects.all())
        final_project = 'file to upload per participant'
        manager = random.choice(Speaker.objects.all())
    
        t = Team(
            name=name,
            project = project,
            start_date =start_date,
            due_date = due_date,
            group_Institution = group_Institution,
          
            manager = manager,
        )

        t.save()
        members = list(Student.objects.all())

        t.participants.add(*random.sample(members, 4))
        print(f'Team:{t.id}')

# * to unpack a list (as we cant give a list) 
# ** to unpack a dict
#  
    print(f"Finished...{n} Teams populated.")



def pop_mission_projects(n):
    for project in range(n):
        team = random.choice(Team.objects.all())
        mission = random.choice(Mission.objects.all())
        completed = False
        created_date = '2020-09-08'
        due_date = '2020-10-10'
        attributed_to = random.choice(Student.objects.all())

        mp = TeamProjectMission(
            team=team,
            mission=mission,
            completed=completed,
            created_date=created_date,
            due_date=due_date,
            attributed_to=attributed_to

        )
        mp.save()
        print(f'mp:{mp.id}')


# -------------------------------------------------





# pop_field(fields_list)
   


# pop_institution_category_list(institution_category_list)


# pop_country()
  

# pop_city()

# pop_representative(2)


# pop_institution(2)


# groups = ['3rd', '4th', '5th', '6th']

# pop_level(4)
# pop_group(groups)


# pop_speaker(5)
    

# pop_student(30)




# pop_resources(20)

# pop_subjects(subjects_list)
# pop_acquired_skills(5)

# pop_missions(20)


# pop_project(6)

# pop_team(4)
pop_mission_projects(20)


