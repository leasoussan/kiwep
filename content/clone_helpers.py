from content.models import *
from django.utils import timezone


def clone_mission_skills(mission, new_mission):
    # TODO: create function
    pass


def clone_project_skills(project, new_project):
    # TODO: create function
    pass


def clone_chapter(chapter):
    chapter.id=None
    chapter.save()
    print('chapter_order', chapter.order)
    return chapter


def clone_project_chapters(project, new_project):
    for chapter in project.chapter_set.all():
        new_chapter = clone_chapter(chapter)
        new_chapter.order = chapter.order+1
        new_chapter.project_id = new_project
        clone_missions(project, new_project)
        new_chapter.save()
        print('new_chapter_save')

def clone_mission_fields(mission, new_mission):
    # TODO: create function
    pass


def clone_project_fields(project, new_project):
    # TODO: create function
    pass

def clone_resource(resource):
    # print('resource_old',resource.id)
    resource.id = None
    resource.save()
    # print('new_res_id',resource.id)
    return resource


def clone_mission_resources(mission, new_mission):
    print('clone resources function')
    for resource in mission.resource_set.all():
        print('new_mission_res', new_mission)
        new_resource = clone_resource(resource)
        new_resource.mission = new_mission
        new_resource.project = new_mission.project
        new_resource.save()
        print("save")
        return new_resource

def clone_mission(mission, new_proj):
    if mission.mission_type == 'i':
        new_mission = IndividualMission.objects.create(
            id=None,
            name=mission.name,
            project_id=new_proj.id,
            order=mission.order,

            created_date=None,
            due_date=timezone.now(),
            mission_type='i',
            owner_id=mission.project.speaker.user.id,
            attributed_to=None,
            description=mission.description
        )
        new_mission.save()

    elif mission.mission_type == 'c':
        attributed_to = []
        new_mission = CollectiveMission.objects.create(
            id=None,
            name=mission.name,
            project_id=new_proj.id,
            order=mission.order,
            created_date=None,
            due_date=timezone.now(),
            mission_type='c',
            owner_id=mission.project.speaker.user.id,
            description=mission.description
        )
        new_mission.save()
        # new_mission.attributed_to.set(attributed_to)
        print('mission cloned, starting on resources')
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
        project.title += ' - copy'
        project.name += ' - copy'
    project.save()
    old_proj = Project.objects.get(id=original_id)
    # clone_missions(old_proj, project)
    clone_project_chapters(old_proj, project)
    clone_proj_resources(old_proj, project)
    return project


def bulk_add(mission, *projects):
    for project in projects:
        clone_mission(mission, project)