from .models import Student, Speaker, Representative



def check_profile(user):
    if user.get_user_type == 'student':
        return Student.objects.filter(user=user).exists()

    elif user.get_user_type == 'speaker':  
        return Speaker.objects.filter(user=user).exists()

    
    elif user.get_user_type == 'representative':
        return Representative.objects.filter(user=user).exists()
