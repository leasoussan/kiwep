from .models import *

# ----------------------------------------------Project---Manager__queryset

class ProjectModelQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""

    def speaker_projects(self):
        return self.filter(speaker= self.request.user)



class ProjectModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return ProjectModelQuerySet(self.model, using = self._db) 

    def speaker_projects(self):
        return self.get_queryset().speaker_projects() 


   

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

class CollectiveProjectMissionQuerySet(models.QuerySet):
    pass




class CollectiveProjectMissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return CollectiveProjectMissionQuerySet(self.model, using=self._db)
    



    

# ---------------------------------------------------------Individual Project Mission Model Manager

class IndividualProjectMissionQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""

    def get_attributed_mission(self):
        return self.exclude(attributed_to = None)


    def is_my_mission(self, user):
        return self.filter(attributed_to = user)

    def get_student_missions(self):
        return self.filter(mission='s_m')

    def team_available_mission(self):
        return self.filter(attributed_to = None)

    

class IndividualProjectMissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return IndividualProjectMissionQuerySet(self.model, using=self._db)


    def team_available_mission(self):
        return self.get_queryset().team_available_mission()

    def get_student_missions(self):
        return self.get_queryset().get_student_missions()



    def get_attributed_mission(self):

        return self.get_queryset().get_attributed_mission()


    def is_my_mission(self, user):
        return self.get_queryset().is_my_mission(user)




# -----------------------------------------------------Mission Manager  QUerySet

class MissionQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""

    def speaker_missions(self):
        return self.filter(owner = self.request.user)

    


class MissionModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return MissionQuerySet(self.model, using = self._db)

    def speaker_missions(self):
        return self.get_queryset().speaker_missions()

    

# ---------------------------------Resource ---Manager__queryset

class ResourceQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""

    def get_speaker_resources(self):
        return self.filter(owner = self.request.user)


class ResourceModelManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)

    def get_speaker_resources(self):
        return self.get_queryset().get_speaker_resources()