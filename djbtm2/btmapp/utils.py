from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email_view(email):
    subject = "this is subject from send email view of util.py"
    message = " this is message from send email view of util.py"
    from_email = "ak958655@gmail.com" # host email 
    recipient_list = ["meabhinav555@gmail.com"]

    #  render html email from the template
    html_message = render_to_string("bill_email_template.html")

    # create plain text  version by stripping html tage
    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        return HttpResponse("email send successfully ")

    except Exception as e:

        return HttpResponse(f"Error sending email")
