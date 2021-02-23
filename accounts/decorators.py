from .modelds import Student, Speaker, Representative


def check_profile(user):
    if user.usertype == 'student':
        return Student.objects.filet(user=user).exists()

    elif user.usertype  == 'speaker':  
        return Speaker.objects.filet(user=user).exists()

         

    elif user.usertype == 'institution':
        return Representative.objects.filet(user=user).exists()
