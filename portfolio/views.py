from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views import View
from .utils import *
# Create your views here.

class indexView(View):
    def get(self,request):
        return render(request, 'about_me.html',)
    def post(self,request):
        return render(request, 'about_me.html',)

class resume_page(View):
    def get(self,request):
        return render(request, 'resume.html',)
    def post(self,request):
        form_data = request.POST
        receiver_email = form_data['email']
        message = form_data['email']
        if '@' in receiver_email: 
            sender_email = "matani.ts1@gmail.com"
            subject = "Thank You for Requesting Matan's Resume"
            body = """
            Dear Friend/Recruiter,
            Thank you for requesting my resume.
            I would greatly appreciate the opportunity to connect with you over the phone, regardless of the outcome.
            Please feel free to reach me at (+972) 55-2568621.
            Looking forward to hearing from you.
            Best regards,
            Matan
            """
            attachment_path = r"portfolio\resume_file\matanTzurResume.pdf"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            login = "matani.ts1@gmail.com"
            password = "qnjm msja ywun bfnm"
            send_email_with_attachment(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, login, password)
            return render(request, 'resume_email_sent.html',)
    
class blog_page(View):
    def get(self,request):
        return render(request, 'blog.html',)
    def post(self,request):
        return render(request, 'blog.html',)
    
class projects_page(View):
    def get(self,request):
        return render(request, 'my_projects.html',)
    def post(self,request):
        return render(request, 'my_projects.html',)
    
class riddles_page(View):
    def get(self,request):
        return render(request, 'my_riddles.html',)
    def post(self,request):
        return render(request, 'my_riddles.html',)

class games_page(View):
    def get(self,request):
        return render(request, 'my_games.html',)
    def post(self,request):
        return render(request, 'my_games.html',)
    

class recepies_page(View):
    def get(self,request):
        return render(request, 'my_recipies.html',)
    def post(self,request):
        return render(request, 'my_recipies.html',)
