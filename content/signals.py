from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed, pre_delete
from .models import *


@receiver(pre_save, sender = 'content.CollectiveMission')




#TODO This part should be changed to a DEACTIVATE and not delete, that we could keep track on what has been done
@receiver(pre_delete, sender='content.ProjectMissionRating')
def update_team_delete_mission(sender, instance, *args,  **kwargs):
    mission = instance.mission
    for team in instance.project.team_set.all():
        if instance.mission.mission_type == 't_m':
            CollectiveProjectMission.objects.get(mission=mission, team=team).delete()

        elif instance.mission.mission_type == 's_m':
            IndividualProjectMission.objects.get(mission=mission, team=team).delete()

    # if not reverse:
    #     if action == 'post_remove':
    #         CollectiveProjectMission.objects.filter(team__in=instance.team_set.all()).filter(mission_id__in=pk_set).delete()

    #     elif action == 'post_add':
    #         project = instance
    #         for team in project.team_set.all():
    #             for mission in project.mission.filter(id__in= pk_set):
    #                 CollectiveProjectMission.objects.create(mission=mission, team=team )


# When team is created we are initiating the mission of the team
# @receiver(post_save, sender=Team)
# def team_mission_attribution(sender, created, instance, *args, **kwargs):
#     if created:
#         for mission in instance.project.missions.all():
#             if mission.mission_type == 's_m':
#                 IndividualProjectMission.objects.create(mission=mission, team=instance, due_date=timezone.now())
#
#             elif mission.mission_type == 't_m':
#                 CollectiveProjectMission.objects.create(mission=mission, team=instance, due_date=timezone.now())

# created check if it's new or note
# instance is team as we have the signal on the team creat missions project so this is the instance we are dealing with

# related name is to change the default access from othermodel_set to the ne realted name.
# for ex in Team: we have FK to project, by default to access all team with the same project we ll go from
# project.team_set.all>>.the related name >> if related name == teams ; then we all do project.teams.all
# it's like a tag /lable to call without needing to go backward.




# m2m_changed have acition attribute that have to be handled
# reverse : if we want to remove a project from a mission (and not mission form a project) - as it's a many to many relation

# @receiver(post_save, sender='content.ProjectMissionRating')
# def update_team_mission_attribution(sender, created, instance, *args,  **kwargs):
#     if created:
#         mission = instance.mission
#         for team in instance.project.team_set.all():
#             if instance.mission.mission_type == 't_m':
#                 CollectiveProjectMission.objects.create(mission=mission, team=team)
#
#             elif instance.mission.mission_type == 's_m':
#                 IndividualProjectMission.objects.create(mission=mission, team=team)


