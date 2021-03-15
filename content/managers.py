from .models import *

# ----------------------------------------------Project---Manager__queryset

class ProjectModelQuerySet(models.QuerySet):
    def speaker_projects(self):
        return self.filter(speaker= self.request.user)



class ProjectModelManager(models.Manager):

    def get_queryset(self):
        return ProjectModelQuerySet(self.model, using = self._db) 

    def speaker_project(self):
        return self.get_queryset().speaker_projects() 


   

# ----------------------------------------------Team---Manager__queryset


class TeamModelQuerySet(models.QuerySet):


    def get_speaker_teams(self):
        return self.filter(manager = self.request.user)
    
    

class TeamModelManager(models.Manager):

    def get_queryset(self):
        return TeamModelQuerySet(self.model, using =self._db)
        
    def speaker_teams(self):
        return self.get_queryset().get_speaker_teams()

    




# ---------------------------------TeamProjectMission---Manager__queryset

class TeamProjectMissionQuerySet(models.QuerySet):
    
    def team_available_mission(self):
        return self.filter(attributed_to = None)

    # def mission_attributed_to(self):
    #     return self.attributed_to()


class TeamProjectMissionModelManager(models.Manager):
    def get_queryset(self):
        return TeamProjectMissionQuerySet(self.model, using=self._db)

    def team_available_mission(self):
        return self.get_queryset().team_available_mission()


# ---------------------------------Mission---Manager__queryset

class MissionQuerySet(models.QuerySet):
    def speaker_missions(self):
        return self.filter(owner = self.request.user)

    


class MissionModelManager(models.Manager):
    
    def get_queryset(self):
        return MissionQuerySet(self.model, using = self._db)

    def speaker_missions(self):
        return self.get_queryset().speaker_missions()

    

# ---------------------------------Resource ---Manager__queryset

class ResourceQuerySet(models.QuerySet):
    def get_speaker_resources(self):
        return self.filter(owner = self.request.user)


class ResourceModelManager(models.Manager):

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)

    def get_speaker_resources(self):
        return self.get_queryset().get_speaker_resources()