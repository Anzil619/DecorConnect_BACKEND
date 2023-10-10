from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_firm_approval_email(user_email):
    subject = 'Firm Approval Confirmation'
    from_email = 'anzilaz24@gmail.com'  # Set your sender email address
    recipient_list = [user_email]

    # Load the email template and render it with context if needed
    html_message = render_to_string('user/firm/firm_approved_email.html', {})
    
    email = EmailMessage(subject, html_message, from_email, recipient_list)  # Use html_message here
    email.content_subtype = 'html'  # Set the content type to HTML
    # email.attach_file('path/to/attachment.pdf')  # Attach any files if needed
    email.send()    
    