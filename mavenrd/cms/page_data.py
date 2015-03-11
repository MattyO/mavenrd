from cms.models import Post
from common.forms import ContactForm
from mavenrd import settings

def blog():
    return {"posts": Post.objects.filter(active=True).order_by('-created_at') }

def global_data():
    return {'tracking': settings.TRACKING_WIDGET}
