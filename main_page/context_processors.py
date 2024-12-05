from .models import Contact


def contact_processor(request):
    contact = Contact.objects.all()
    return {"contact": contact}
