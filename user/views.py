from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from .models import *
from django.db.models import Count, Case, When, F, Value, FloatField, ExpressionWrapper, IntegerField
from django.db.models.functions import NullIf, Cast
from .forms import ProfileImageForm
#################### index####################################### 
def index(request):
	data = ""
	if request.user.is_authenticated:
		data = User.objects.get(username=request.user.username).__dict__
	return render(request, 'user/index.html', {
		'title':'index',
		'userdata' : data
		})

########### register here ##################################### 
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system #################################### 
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms################################################### 
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})










def about(request):
	return render(request, 'Aboutus/png.html')

def course_list(request):
	courseData = [x.__dict__ for x in Courses.objects.all()]
	for el in courseData:
		el['Course_description'] = el['Course_description'][:100]
	return render(request, 'course_list/courseListPage.html' ,{
		"courseData":courseData
	})











def pprofile(request,username):
	if request.user.is_authenticated:
		try:
			userdata = User.objects.get(username=username)
			profiledata = ""
			if userdata:
				userdata = userdata.__dict__
				profiledata = profile.objects.get(uid = userdata['id'])
			
			return render(request, 'profile/profile.html' ,{
				"userdata" : userdata,
				"profiledata":profiledata
			})
		except :
			messages.info(request, "User does not exist")
			return redirect('index')
	else:
		return redirect('login')










def course(request, courseid):
	course = Courses.objects.get(Course_ID = courseid).__dict__
	topicdata = [Topics.objects.get(Topic_ID=tid).__dict__ for tid in str(CTtable.objects.get(Course_ID=course['Course_ID']).__dict__['Topics_IDs']).split(',')]
	enrollementStatus = False
	progressData = ""





	if request.user.is_authenticated:
		# print(request.user.id)
		progressDatas = [x.__dict__ for x in Progress.objects.filter(User_ID = 1)]
		for val in progressDatas:
			# print(val,course)
			if str(val['Course_ID_id']) == course['Course_ID']:
				progressData = val
				enrollementStatus = True


				# ---------------------------------------------------
				# Only if the user is logged in and enrolled in the course
				# Following id to save the progress
				if request.method == "POST":
					print(request.POST)
					print(topicdata)





	# print(course['Image_link'])
	return render(request, 'courses/general.html', {
		"courseData":course,
		"topicdatas_basic":topicdata,
		"topicdatas_inter":"",
		"topicdatas_adv":"",
		"isEnrolled":enrollementStatus,
		"progressData":progressData
	})

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, F, FloatField, ExpressionWrapper, Func
from .models import profile, Progress
from .forms import ProfileImageForm

class CountIds(Func):
    function = 'count_ids'
    output_field = IntegerField()

def user_profile_with_progress(request, username):
    # Retrieve the profile based on the username
    user_profile = get_object_or_404(profile, uid__username=username)
    
    # Retrieve the courses enrolled by the user along with the completion data
    courses_with_completion = Progress.objects.filter(User_ID=user_profile).annotate(
        total_topics_count=CountIds('Course_ID__ct_cid__Topics_IDs'),
        completed_topics_count=CountIds('Completed_topic_IDs'),
        completion_percentage=Cast(
            ExpressionWrapper(
                (F('completed_topics_count') * 100.0) / F('total_topics_count'),
                output_field=FloatField()
            ),
            output_field=IntegerField()  # Target field type
        )
    ).values('Course_ID', 'Course_ID__Course_name', 'completion_percentage')

    # Check if the form is submitted
    if request.method == 'POST':
        # Instantiate the form with the POST data and files
        form = ProfileImageForm(request.POST, request.FILES, instance=user_profile)
        # Check if the form is valid
        if form.is_valid():
            # Save the form to update the user profile with the uploaded image
            form.save()
            # Redirect to the user profile page
            return redirect('user_profile_with_progress', username=username)
    else:
        # If the request method is not POST, instantiate an empty form
        form = ProfileImageForm()

    # Prepare the data to be passed to the template
    context = {
        'user_profile': user_profile,
        'courses_with_completion': courses_with_completion,
        'form': form,  # Pass the form to the template
    }

    # Render the template with the data
    return render(request, 'profile/profile.html', context)