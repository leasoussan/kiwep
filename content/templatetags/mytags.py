from django import template



register = template.Library()

def return_objects_name(value):
    return value.__class__.__name__


def return_class_name(value):
    return  value._meta.verbose_name.title()



@register.filter
def student_missions(mission_qs, student):

    """ """
    return mission_qs.filter(attributed_to=student)



@register.filter
def collective_student_missions(mission_qs, team):

    """ """

    return mission_qs.filter(parent_mission__team=team)

@register.filter
def student_available_projects(team_qs, student):
    return team_qs.filter(manager__group=student.class_level_id)




def get_mission_type(mission):
    return mission.get_mission_type(mission)



def get_speaker_answer_board(answers_qs, speaker):
    return answers_qs.filter(project__team__manager=speaker)


# this lign it to call templates the function according to the left name 
register.filter('return_objects_name', return_objects_name)
register.filter('return_class_name', return_class_name)
register.filter('get_mission_type', get_mission_type)
register.filter('get_speaker_answer_board', get_speaker_answer_board)

