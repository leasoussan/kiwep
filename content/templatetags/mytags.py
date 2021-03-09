from django import template



register = template.Library()

def return_objects_name(value):
    return value.__class__.__name__






def return_class_name(value):
    return  value._meta.verbose_name.title()



# this lign it to call templates the function according to the left name 
register.filter('return_objects_name', return_objects_name)
register.filter('return_class_name', return_class_name)
