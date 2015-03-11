from cms.models import Post
from common.forms import ContactForm
from mavenrd import settings

def blog():
    return {"posts": Post.objects.filter(active=True).order_by('-created_at') }

def global_data():
    return {'tracking': '''
<script type="text/javascript">
  var _gauges = _gauges || [];
  (function() {
    var t   = document.createElement('script');
    t.type  = 'text/javascript';
    t.async = true;
    t.id    = 'gauges-tracker';
    t.setAttribute('data-site-id', \''''+settings.TRACKING_ID+'''\');
    t.setAttribute('data-track-path', 'https://track.gaug.es/track.gif');
    t.src = 'https://track.gaug.es/track.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(t, s);
  })();
</script>
    '''}
