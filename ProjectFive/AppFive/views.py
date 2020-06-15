from django.shortcuts import render
from AppFive.forms import UserForm,UserProfileForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'AppFive/index.html')


@login_required
def loginpage(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return render(request,'AppFive/loginpage.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'AppFive/registration.html',
                          context={'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):

     if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(username=username,password=password)

         if user:

             if user.is_active:
                 login(request,user)
                 return HttpResponseRedirect(reverse('loginpage'))
             else:
                return HttpResponse('Account Not Available')

         else:
            print('someone tried to login and failed.')
            print('username: {} and password: {}'.format(username,password))

            return HttpResponse("Invalid Login Details")
     else:
         return render(request,'AppFive/login.html',context={})
