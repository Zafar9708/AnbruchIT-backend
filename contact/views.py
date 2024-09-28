from django.shortcuts import render

# Create your views here.
# contact/views.py
import json
from django.http import JsonResponse
from django.views import View
from .models import ContactForm,ContactUs
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

@method_decorator(csrf_exempt, name='dispatch')
class ContactView(View):
    def post(self, request):
        try:
            data = request.body.decode('utf-8')
            json_data = json.loads(data)
            company_name = json_data.get('company_name')
            your_name = json_data.get('your_name')
            email = json_data.get('email')
            message = json_data.get('message')

            # Save to the database
            contact_form = ContactForm.objects.create(
                company_name=company_name,
                your_name=your_name,
                email=email,
                message=message
            )

            # Send email
            subject = f"New message from {your_name} ({company_name})"
            email_message = f"Message from {your_name} ({email}):\n\n{message}"
            recipient_list = ['zekhlaque@kloudrac.com']  # Your email address
            send_mail(subject, email_message, settings.EMAIL_HOST_USER, recipient_list)

            return JsonResponse({'success': True}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def get(self, request):
        return JsonResponse({'message': 'This endpoint is for POST requests only.'}, status=200)
    



@method_decorator(csrf_exempt, name='dispatch')
class ContactViews(View):
   def post(self, request):
    try:
        data = request.body.decode('utf-8')
        print(f"Received data: {data}")  # Debug line
        json_data = json.loads(data)
        name = json_data.get('name')
        email = json_data.get('email')
        message = json_data.get('message')

        contact_form = ContactUs.objects.create(
            name=name,
            email=email,
            message=message
        )

        subject = f"New message from {name}"
        email_message = f"Message from {name} ({email}):\n\n{message}"
        recipient_list = ['zekhlaque@kloudrac.com']
        send_mail(subject, email_message, settings.EMAIL_HOST_USER, recipient_list)

        return JsonResponse({'success': True}, status=201)

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debug line
        return JsonResponse({'error': str(e)}, status=400)

    


