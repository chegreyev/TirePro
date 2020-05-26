from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from dotenv import load_dotenv

import os

User = get_user_model()
load_dotenv()

def email_client(request):
    username = request.POST.get('username')
    client = User.objects.get(username=username)
    # msg_html = render_to_string('templates/account/email/feedback.txt', {'client': client})
    template_email_text = ''
    return send_mail('Thank you for the feedback , we really appreciate it.', template_email_text, f'{os.getenv("EMAIL_HOST_USER")}', [f'{client.email}'],  fail_silently=False)
