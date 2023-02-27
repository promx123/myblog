from applications.home.models import Home

#proceso para recuperar telofono e email del registro home

def home_contact(request):#siempre de esta forma para hacer un procesors
    home = Home.objects.latest('created')
    
    return {
        'phone': home.phone,
        'correo':home.contact_email,
    }
    