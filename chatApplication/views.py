from os import uname_result

from django.contrib.auth.models import User
from django.http import JsonResponse
from django_short_url.views import get_surl
from django.template.loader import render_to_string
from django.shortcuts import render
from django_short_url.models import ShortURL
from . import forms
from rest_framework import status
import jwt
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from .redis import Redis
redis = Redis()


class Registration(APIView):

    def get(self, request, *args, **kwargs):
        form = forms.RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request, *args, **kwargs):

        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        import pdb
        pdb.set_trace()
        # serializer = RegistrationSerializer(data=request.data)
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user_obj = User(username=username, password=password, email=email)
        user_obj.set_password(password)

        user_obj.is_active = False
        user_obj.save()
        token = jwt.encode({'id': user_obj.id}, 'secret', algorithm='HS256').decode('utf-8')
        surl = get_surl(token)
        surl = surl.split('/')
        # send_mail(subject, message, from_email, to_email[], fail_silently=TRUE)
        message = render_to_string('activate.html', {
            'user': user_obj, 'domain': get_current_site(request).domain ,
            'token': surl[2]
        })
        subject = f'activation link from {get_current_site(request).domain}'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['shrutizarbade22@gmail.com']
        send_mail(subject, message, from_email, to_email, fail_silently=True)
        response = {
            "success": True,
            "message": "Registration done successfully",
            "data": []
        }

        return JsonResponse(data=response, status=200)


def activate(request, token):
    smd = {
        'success': 'Fail',
        'message': 'Unsuccessfully in activating account',
        'data': []
    }
    import pdb
    pdb.set_trace()
    short_url_obj = ShortURL.objects.get(surl=token)
    token = short_url_obj.lurl
    payload = jwt.decode(token, 'secret', algorithm='HS256')
    id = payload['id']
    user = User.objects.get(pk=id)

    if user:
        user.is_active = True
        user.save()
        smd['success'], smd['message'] = 'Success', 'Successfully Activated Account'
        return JsonResponse(data=smd, status=status.HTTP_200_OK)
    else:
        return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):

    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        smd = {
            'success': False,
            'message': 'something went wrong',
            'data': []
        }
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if user is not None:
            token = jwt.encode({'id': user.id}, 'secret', algorithm='HS256').decode('utf-8')
            smd = {
                'success': True,
                'message': 'log in successfully',
                'data': [token]
            }
            redis.set(user.id, token)

            return JsonResponse(data=smd, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def post(self, request, *args, **kwargs):
        smd = {
            'success': False,
            'message': 'something went wrong',
            'data': []
        }
        import pdb
        pdb.set_trace()
        token1 = request.META['HTTP_TOKEN']
        payload = jwt.decode(token1, 'secret', algorithms='HS256')
        user_id = payload.get('id')
        redis.delete(user_id)
        smd = {
            'success': True,
            'message': 'logout successfully',
            'data': []
        }
        return JsonResponse(data=smd, status=status.HTTP_200_OK)


class ForgotPassword(APIView):

    def post(self, request, *args, **kwargs):
        smd = {'success': False,
               'message': 'something went wrong',
        }
        email = request.data.get('email')
        user = User(email=email)
        if email.is_valid:
            token = jwt.encode({'id': user.id}, 'secret', algorithm='HS256')
            surl = get_surl(token)
            surl = surl.split('/')
            message = render_to_string('reset.html', {
                'user': user, 'domain': get_current_site(request).domain,
                'token': surl[2]
            })
            subject = f'reset link from {get_current_site(request).domain}'
            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email]
            send_mail(subject, message, from_email, to_email, fail_silently=True)
            smd = {
                'success': True,
                'message': 'successfully reset password'
            }
            return JsonResponse(data=smd, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):

    def post(self, request, token):
        smd = {
            'success': 'Fail',
            'message': 'Something went Wrong',
            'data': []
        }
        # import pdb
        # pdb.set_trace()
        password = request.data('password')
        short_url_obj = ShortURL.objects.get(surl=token)
        token = short_url_obj.lurl
        payload = jwt.decode(token, 'secret', algorithm='HS256')
        id = payload['id']
        new_password = User(password=password)
        new_password.set_password(password)
        new_password.save()
        smd = {'success': 'Success',
               'message': 'Password reset Successfully',
               'data': []
        }
        return JsonResponse(data=smd, status=status.HTTP_200_OK)
