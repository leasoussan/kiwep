from .modelds import Student, Speaker, Representative




def get_user_profile_form(request, usertype): 
    
    data = request.POST or None 

    if  usertype == 'student':
        profile_form = StudentProfileCreationForm(data)
       

    elif usertype  == 'speaker':  
        profile_form =SpeakerProfileCreationForm(data)
    

    elif usertype == 'representative':
        profile_form =  RepresentativeProfileCreationForm(data)
    
    return profile_form



def check_profile(usertype):
    if usertype == 'student':
        return Student.objects.filet(user=user).exists()

    elif usertype  == 'speaker':  
        return Speaker.objects.filet(user=user).exists()

    
    elif usertype == 'representative':
        return Representative.objects.filet(user=user).exists()
