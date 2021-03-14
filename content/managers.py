from .models import *



class ProjectModelManager(models.Manager):
    def get_speaker_projects(self, user ):
        return self.get_queryset().filter(owner= user)

    # def get_student_projects(self, user):
    #     return self.get_queryset().filter(team__participants=user)
    



class TeamModelManager(models.Manager):
    def get_speaker_teams(self, user):
        return self.get_queryset().filter(manager = user)

    
    def get_available_mission(self):
            
        pass

class MissionModelManager(models.Manager):
    def get_speaker_missions(self, user):
        return self.get_queryset().filter(speaker = user)

    
    


class ResourceModelManager(models.Manager):
    def get_speaker_resources(self, user):
        return self.get_queryset().filter(speaker = user)