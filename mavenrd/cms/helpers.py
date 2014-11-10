from cms.models import Page
from mavenrd import settings
def nav():
    return { 'pages': Page.objects.filter(active=True) }

def standard_context():
    nav_thing = nav()
    nav_thing['pages'] = filter(lambda page: page.slug != "index", nav_thing['pages'])
    return { 'nav': nav_thing, 'app_name' : settings.SITE_NAME }
