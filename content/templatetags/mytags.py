from django import template



register = template.Library()

def return_objects_name(value):
    return value.__class__.__name__


def return_class_name(value):
    return  value._meta.verbose_name.title()



@register.filter
def student_missions(mission_qs, student):

    """ """
    return mission_qs.filter(attributed_to =student)



@register.filter
def collective_student_missions(mission_qs, team):

    """ """
    print(mission_qs.filter(parent_mission__team=team))
    return mission_qs.filter(parent_mission__team=team)





# this lign it to call templates the function according to the left name 
register.filter('return_objects_name', return_objects_name)
register.filter('return_class_name', return_class_name)


