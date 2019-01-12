from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import HiarcUser, STATUSES, MAJORS, SEMESTERS

import json
import requests

class HiarcUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    real_name = forms.CharField(required=True, max_length=20)
    status = forms.CharField(required=True, widget=forms.Select(choices=STATUSES))
    semester = forms.CharField(required=True, widget=forms.Select(choices=SEMESTERS))
    major  = forms.CharField(required=True, widget=forms.Select(choices=MAJORS))
    phone_number = forms.CharField(required=True, max_length=20)
    motivation = forms.CharField(required=True, widget=forms.Textarea)
    portfolio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = HiarcUser
        fields = ("email", "real_name", "status", "semester", "major", "phone_number", "motivation", "portfolio", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(HiarcUserCreationForm, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        user.real_name = self.cleaned_data["real_name"]
        user.status = self.cleaned_data["status"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.motivation = self.cleaned_data["motivation"]
        user.portfolio = self.cleaned_data["portfolio"]

        '''
        webhook_url = system.environment['SLACK_WEBHOOK_URL']
        message = "회원가입 신청이 들어왔습니다. \n이름 : {}\n 이메일 : {} \n학과/학번/학년 : {}\n 자세한 사항은 관리자페이지에서 확인해보세요.".format(user.real_name, user.email, user.status)
        slack_data = { "text": message, "color": "#FAA3E3"} 

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        '''

        if commit:
            user.save()
        return user