from .models import *

# ----------------------------------------------Project---Manager__queryset

class ProjectModelQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""


    def personal_templates(self):
        return self.filter(is_template=True, is_global= False)

    def personal_projects(self):
        return self.filter(is_template=False)

    """FOR STUDENT TO SEE TEAM HE CAN JOIN """
    def available_projects(self):
        return self.filter(is_template=False, is_global=False, team__isnull=True )

    def global_template_projects(self):
        return self.filter(is_template=True, is_global=True)

class ProjectModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return ProjectModelQuerySet(self.model, using = self._db) 

    def personal_templates(self):
        return self.get_queryset().personal_templates()

    def personal_projects(self):
        return self.get_queryset().personal_projects()

    """FOR STUDENT TO SEE TEAM HE CAN JOIN """
    def available_projects(self):
        return self.get_queryset().available_projects()

    def global_template_projects(self):
        return self.get_queryset().global_template_projects()
   

# ----------------------------------------------Team---Manager__queryset


class TeamModelQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""


    def get_speaker_teams(self):
        return self.filter(manager=self.request.user)



class TeamModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return TeamModelQuerySet(self.model, using =self._db)
        
    def speaker_teams(self):
        return self.get_queryset().get_speaker_teams()

    




# ---------------------------------CollectiveProjectMission---Manager__queryset

class CollectiveMissionQuerySet(models.QuerySet):
    # def get_individual_collective_mission(self, mission):
    #     return self.filter(mission__parent_mission=mission)
    pass


class CollectiveMissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return CollectiveMissionQuerySet(self.model, using=self._db)

    # def get_individual_collective_mission(self, mission):
    #     return self.get_queryset().get_individual_collective_mission(mission)


# ---------------------------------Collective  INDIVIDUAL ProjectMission---Manager__queryset
# # TODO Cant it be donn as it a trhought table?
# class CollectiveIndividualMissionQuerySet(models.QuerySet):
#     """Get Manager for Collective Individual Mission"""
#
#
#
# class CollectiveIndividualMissionModelManager(models.Manager):
#     """ Managers are a way to get specifi data from a Model with the help of a queryset """
#
#     def get_queryset(self):
#         return CollectiveIndividualMissionQuerySet(self.model, using=self._db)
#


# ---------------------------------------------------------Individual Project Mission Model Manager

class IndividualMissionQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""



    def is_my_mission(self, user):
        return self.filter(attributed_to = user)

    def get_student_missions(self):
        return self.filter(mission='s_m')


    # def attributed_mission(self):
    #     return self.filter(attributed_to = True)

class IndividualMissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return IndividualMissionQuerySet(self.model, using=self._db)


    def get_student_missions(self):
        return self.get_queryset().get_student_missions()




    def is_my_mission(self, user):
        return self.get_queryset().is_my_mission(user)

    # def attributed_mission(self, project):
    #     return self.get_queryset().attributed_mission(project)
    #

# -----------------------------------------------------Mission Manager  QUerySet

class MissionQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""


    def individual(self):
        return self.filter(mission_type='i')

    def collective(self):
        return self.filter(mission_type='c')

    def collective_individual(self):
        return self.filter(mission_type='ci')

    def available_mission(self):
        return self.filter(individualmission__attributed_to__isnull=True)

    def get_attributed_mission(self):
        return self.exclude(individualmission__attributed_to__isnull=True).order_by('-stage')
    # 'stage' will be creshendo (- do the other way arround)


class MissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return MissionQuerySet(self.model, using= self._db)

    def individual(self):
        return self.get_queryset().individual()

    def collective(self):
        return self.get_queryset().collective()

    def collective_individual(self):
        return self.get_queryset().collective_individual()


    def available_mission(self):
        return self.get_queryset().individual().available_mission()

    def get_attributed_mission(self):
        return self.get_queryset().get_attributed_mission()

# ---------------------------------Resource ---Manager__queryset

class ResourceQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""

    def get_speaker_resources(self, user):
        return self.filter(owner=user)

    def get_project_resources(self, project):
        return self.filter(project__resources=project)

class ResourceModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)

    def get_speaker_resources(self):
        return self.get_queryset().get_speaker_resources()


    def get_project_resources(self, project):
        return self.get_queryset().get_project_resources()