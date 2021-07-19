from .models import *

# ----------------------------------------------Project---Manager__queryset

class ProjectModelQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""


    def personal_templates(self):
        return self.filter(is_template=True)

    def personal_projects(self):
        return self.filter(is_template=False)

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


    def global_template_projects(self):
        return self.get_queryset().global_template_projects()
   

# ----------------------------------------------Team---Manager__queryset


class TeamModelQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""


    def get_speaker_teams(self):
        return self.filter(manager = self.request.user)
    
    

class TeamModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return TeamModelQuerySet(self.model, using =self._db)
        
    def speaker_teams(self):
        return self.get_queryset().get_speaker_teams()

    




# ---------------------------------CollectiveProjectMission---Manager__queryset

class CollectiveMissionQuerySet(models.QuerySet):
    pass




class CollectiveMissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return CollectiveMissionQuerySet(self.model, using=self._db)
    



    

# ---------------------------------------------------------Individual Project Mission Model Manager

class IndividualMissionQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""

    def get_attributed_mission(self):
        return self.exclude(attributed_to = None).order_by('-stage')
    # 'stage' will be creshendo (- do the other way arround)


    def is_my_mission(self, user):
        return self.filter(attributed_to = user)

    def get_student_missions(self):
        return self.filter(mission='s_m')

    def available_mission(self):
        return self.filter(attributed_to=None)

    def attributed_mission(self):
        return self.filter(attributed_to = True)

class IndividualMissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return IndividualMissionQuerySet(self.model, using=self._db)


    def available_mission(self):
        return self.get_queryset().available_mission()

    def get_student_missions(self):
        return self.get_queryset().get_student_missions()



    def get_attributed_mission(self):
        return self.get_queryset().get_attributed_mission()


    def is_my_mission(self, user):
        return self.get_queryset().is_my_mission(user)

    def attributed_mission(self, project):
        return self.get_queryset().attributed_mission(project)


# -----------------------------------------------------Mission Manager  QUerySet

class MissionQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""



    def individual(self):
        return self.filter(mission_type='i')

    def collective(self):
        return self.filter(mission_type='c')

    def collective_individual(self):
        return self.filter(mission_type='ci')





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