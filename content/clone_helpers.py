from content.models import *
from django.utils import timezone

def clone_resource(resource):
    resource.id = None
    resource.save()
    return resource

def clone_mission_resources(mission, new_mission):
    for resource in mission.resource_set.all():
        new_resource = clone_resource(resource)
        new_resource.mission = new_mission
        new_resource.project = new_mission.project
        new_resource.save()
    

def clone_mission(mission, new_proj):
    if mission.mission_type == 'i':
            new_mission = IndividualMission.objects.create(
                id=None,
                name = mission.name,
                project_id = new_proj.id,
                created_date = None,
                due_date = timezone.now(),
                mission_type='i',
                owner_id= mission.project.speaker.user.id,
                attributed_to=None,
                description=mission.description
            )
    elif mission.mission_type == 'c':
        attributed_to = []
        new_mission = CollectiveMission.objects.create(
            id=None,
            name=mission.name,
            project_id=new_proj.id,
            created_date=None,
            due_date=timezone.now(),
            mission_type='c',
            owner_id=mission.project.speaker.user.id,
            description=mission.description
        )
        new_mission.attributed_to.set(attributed_to)
 
    clone_mission_resources(mission, new_mission)

    return new_mission

def clone_missions(proj, new_proj):
    for mission in proj.mission_set.all():
        clone_mission(mission, new_proj)


def clone_proj_resources(proj, new_proj):
    for resource in proj.resource_set.filter(mission__isnull=True):
        new_resource = clone_resource(resource)
        new_resource.project = new_proj
        new_resource.save()

def check_if_allowed_to_clone(project, speaker):
    return True

def clone_project(project, speaker):
    if not check_if_allowed_to_clone(project, speaker):
        return False
    original_id = project.id
    project.id = None
    project.save()
    project.completed = False

    if project.is_template:
        project.is_template = False
        project.is_global = False
        project.is_premium = False
        project.speaker = speaker
    project.save()
    old_proj = Project.objects.get(id=original_id)
    clone_missions(old_proj, project)
    clone_proj_resources(old_proj, project)


def bulk_add(mission, *projects):
    for project in projects:
        clone_mission(mission, project)