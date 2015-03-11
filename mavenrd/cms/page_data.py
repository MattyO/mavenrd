from cms.models import Post
from common.forms import ContactForm
def blog():
    return {"posts": Post.objects.filter(active=True).order_by('-created_at') }
