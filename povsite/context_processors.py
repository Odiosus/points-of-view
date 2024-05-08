from gallery.models import StartPage


def start_page_logo(request):
    start_page = StartPage.objects.first()
    return {'logo_header': start_page.logo_header}