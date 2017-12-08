# Python_Projects
This file contains a collection of projects from studying Python at Coding Dojo.

_The following are my personal notes_


# Django Project Notes:

## Running Django VE: source bin/activate
Starting Server in folder containing manage.py: 
 - python manage.py makemigrations (sets up models/database) 
 - python manage.py migrate (enables session & models link)
 - python manage.py runserver (runs server)

## Make project folders and files:

Navigate to project folder:

 - django-admin startproject project_name
 
Navigate into project folders

 - cd project_name
 - mkdir apps
 
Navigate into apps

 - cd apps
 - touch __init__.py
 - python ../manage.py startapp app_name
 
Navigate into app_name

 - cd app_name
 - touch urls.py
 - mkdir templates
 - mkdir static
 
Navigate into templates or static

 - mkdir app_name
 
Navigate into app_name

 - touch index.html or style.css (depending on parent folder)

### Modify files:
Open _settings.py_ inside project folder (..Project_Name/Project_Name/settings.py) and make the following changes:
 - Ln 34: move contents down a line and add ‘apps.app_name’, * don’t forget the comma!*
    - **Note that if you created multiple apps inside your apps folder, you will need to add them here
 - Change ln 110 to read: TIME_ZONE = 'US/Pacific'**
 
Open _urls.py_ inside project folder (..Project_Name/Project_Name/urls.py) and make the following changes:
 - Ln 16: add , include
 - Ln 20: change to read url(r'^', include('apps.app_name.urls', namespace=’somename’))
 
***Note that if you created multiple apps inside your apps folder, you will need to add them here***

Open _views.py_ inside app folder (Project_Name/apps/app_name/views.py) 
 - Ln 1: add , HttpResponse, redirect, (and any other requirements)
 
Add all pages to be shown here such as:	
	 - def index(request):
		return render(request, “index.html”)
	 - def show(request):
   		return render(request, "success.html")
      
Open _urls.py_ inside apps/app_name folder (Project_Name/apps/app_name/urls.py) and add the following:
  ***NOTE: add each new “def” section from the view.py file here and don’t forget a comma after each one!!***

from django.conf.urls import url           //This gives us access to the function url
from . import views           
urlpatterns = [
url(r'^$', views.index), 
url(r’users$’, views.show)   
]
	
Note: _users_ matches the html action name in templates and show matches the def in views

### Static Content:

Navigate into (..apps/app_name) folder

 - mkdir static
 - cd static
 - mkdir app_name
 
Save static files like .css inside

***NOTE: If you have different types of static files, you should nest multiple folders in the static folder like css, js or images folders***

CSS: Open html you want to style and add the following:
    {% load staticfiles %} //this tells Django to be ready for static content
      <link rel="stylesheet" href="{% static 'style.css' %}"media="screen" title="no    title"  charset="utf-8"> 

Note: this tells it where to look, note the you may have to add css/style.css if you have a nested css folder in your static folder

#### Static content should be nested as follows:
 - Folder: first_app <= created as a result to the call to 'startapp'
    - Folder: templates
      - Folder: first_app
        - Files: *.html
      
    - Folder: static
      - Folder: first_app
        - Folder: css
        - Folder: js
        - Folder: images

### POST format:

In _html_, add csrf_token to _form_ section:
```python
<form action="/do_thing" method="post">
	{% csrf_token %}
	<input type="text" name="some_name">
	<input type="submit" value="submit">
</form>
```

In apps _views.py_ (Project_Name/apps/app_name/views.py), add a new def and include POST or GET (depending on method, caps sensitive) as an IF/ELSE statement:

```python
def create(request):
	if request.method == "POST":
		return redirect("/do_thing")
	else:
		return redirect("/do_other_thing")
```
***Don’t forget to add new def to views.py!***

### Session format:

In apps views.py (Project_Name/apps/app_name/views.py), add a new def and include request.session:

```python
def create(request):
	if request.method == "POST":
		request.session[‘key_name’] =
request.POST[‘some_name’]	
return redirect("/do_thing")
else:
	return redirect("/do_other_thing"))
```

In _html_, add request.session.key_name to _form_ section:

```python
{{ request.session.key_name }}
<form action="/do_thing" method="post">
		{% csrf_token %}
		<input type="text" name="some_name">
```

Useful info:

- del request.session['key'] will delete session key if it exists, throws a keyError if it doesn’t. 
- Use along with try and except since it’s better to ask for forgiveness than permission.
- Session in Django gets saved even if we leave the browser!

### Context Variables format:

In   _views.py_:
from django.shortcuts 

```python
import render, HttpResponse, redirect
def show_ninja(request, id):
				#id got passed in through the url parameter!
	context = {
'id' : id
}
return render(request, '/myproject/show.html', context)
```
	
In index.html(or other .html)
```python
{{id}}
```

In urls.py

```python
from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^/en/(?P<id>\d+)$', views.show), 	//format given in tutorial
	url(r'^users/(?P<djangoversion>[0-9]\.[0-9])/topics/http/urls/$', views.index)  						//this is another format, 
]
```

To find out django version: print (djangoversion)

### Models: 
***Each time you make a new model, make you to run:***
 - python manage.py makemigrations
 - python manage.py migrate

Models house all the functions that we need to use in our views.py file. 
1. ADD ‘django_extensions’, to settings under ‘apps.app_name’,
2. models.py file (Project_Name/apps/app_name/models.py)

```python
  from __future__ import unicode_literals 	#automatic line
  from django.db import models		#automatic line 
  class User(models.Model):
  	first_name = models.CharField(max_length=45) 
   	last_name = models.CharField(max_length=45) 
   	password = models.CharField(max_length=100)
   	created_at = models.DateTimeField(auto_now_add = True)
   	updated_at = models.DateTimeField(auto_now = True)
  class Post(models.Model):
    	title = models.CharField(max_length=45)
    	message = models.TextField(max_length=1000)
     	user_id = models.ForeignKey(User)
      	created_at = models.DateTimeField(auto_now_add = True)
      	updated_at = models.DateTimeField(auto_now = True)
```
*** Notice the association made with ForeignKey for a one-to-many Relationship. There can be many posts to one User in this example***

3. SAVE then run python manage.py makemigrations
4. Run python ../mange.py migrate

Terminal can interact with the mode(using Book as an example:
1. >>> python manage.py shell
2. >>> from apps.app_name.models import Books)python
3. >>> Book.objects.all
4. >>> Book.objects.create(title = “Cat in the Hat”, author = “Dr. Susse”)
5. >>> Book.objects.all

NOTE: “models.CharField” is equivalent to VARCHAR(30) in MySQL. Can be:
 - CharField(max_length=int) - Any text a user may enter
 - TextField - text without a max length
 - IntergerField, BooleanField - Holds integers or booleans, respectively
 - DateTimeField - This field can take two very useful optional parameters, auto_now_add=True, which adds the current date/time when object is created, and auto_now=True, which automatically updates any time the object is modified.
 - ForeignKey, ManyToManyField, OneToOneField - indicate a relationship between models (anything that would require a JOIN statement in SQL). ForeignKey is for one-to-many relationships and goes in the model on the "many" side, just as the foreign key column goes in the SQL table on the "many" side.

More at: Django: https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types	

_View.py_ file, import each function:
 ```python
from .models import Function_name, (add more for each function)
def index(request):
	print User.objects.all()
# A list of objects (or an empty list)
User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
 # Creates a user object
 print User.objects.all()
 # A list of objects (or an empty list)
 u = User.objects.get(id=1)
 print u.first_name
 u.first_name = "Joey"
 u.save()
  j = User.objects.get(id=1)
  print j.first_name
  # Gets the user with an id of 1, changes name and saves to DB, then retrieves again...
  print User.objects.get(first_name="mike")
  # Gets the user with a first_name of 'mike' *** THIS MIGHT NEED TO    
  BE CHANGED ***
 users = User.objects.raw("SELECT * from {{appname}}_user")
  # Uses raw SQL query to grab all users (equivalent to
  User.objects.all()), which we iterate through below for user in users:
  print user.first_name
  return HttpResponse("ok")
```

NOTES: 
 - Model_name.objects.raw(“SELECT * from {{appname}}_model_name”) uses raw SQL query to grab all users (equivalent to User.objects.all())
 - If you need to create a raw query and aren't sure what the table name is, find it by printing the following: 
 ```python 
 Model_name._meta.db_table
```

Displaying on Templates
```
<h1>Users</h1>
<table>
  <tr>
    <th>ID</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Age</th>
  </tr>
  {% for user in users %}
    <tr>
      <td>{{ user.id }}</td>
      <td>{{ user.first_name }}</td>
      <td>{{ user.last_name }}</td>
      <td>{{ user.age }}</td>
    </tr>
  {% endfor %}
</table>
```

Another example:
```python
in models.py
	 from __future__ import unicode_literals
	 from django.db import models


class Blog(models.Model):
  title = models.CharField(max_length=100)
  blog = models.TextField(max_length=1000)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
class Comment(models.Model):
  blog = models.ForeignKey(Blog)
  comment = models.TextField(max_length=1000)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
```

in index.html:
```
	<h1> Welcome to my Blogs </h1>
  {% for blog in blogs %}
	  <h5> {{ blog.title }}</h5>
   	<p>{{ blog.blog }}</p>
	{% for comment in blog.comment_set.all %}    		//gets comments
		{{comment.comment}}
	{% endfor %}
 <form action="/comment/{{blog.id}}" method="post">
   {% csrf_token %}
   <textarea name="comment" rows="8" cols="80"></textarea>
   <input type="submit" value="Enter Comment">
  </form>
{% endfor %}

  <form action="/blogs" method="post">
   {% csrf_token %}
   <label for “ ”> Title </label>
   <input type="text" name="title">
   <textarea name="blog" rows="8" cols="80"></textarea>
   <input type="submit" value="Enter Blog">
  </form>
```
in urls.py

from django.conf.urls import url
from . import views
url_patterns = [
  url(r'^$', views.index, name="index"),
  url(r'^blogs$', views.blogs),
  url(r’^comments/(?P<id>\d+)$, views.comments)
	]

in views.py
```python
from django.shortcuts import render, redirect
from .models import Blog, Comment
  	def index(request):
 	 	context = {
    		"blogs": Blog.objects.all()		 # select * from Blog
		  }
  		return render(request, 'test_app/index.html', context)
 def blogs(request):
		 # using ORM
 		Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
 	 # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
  		return redirect('/')
def comments (request, id):
		Blog = Blog.objects.get(id=id)
		Comment.objects.create(comment=request.POST[‘comment’], blog=blog
		return redirect(“/”)
```

### Queries
Additional query documentation: https://docs.djangoproject.com/en/1.10/topics/db/queries/

 - The following is known as a magic method which concatenates two objects into a string: 
def __str__(self):
    return self.first_name + " " + self.last_name
 - .get(field="val") ie: user = User.objects.get(id=6) returns the one object that matches a given condition. Will error if more than one match or no matches found. Works best on ID numbers.
 - .filter(field="val"...)  ie: user = User.objects.filter(last_name="Thomas") returns all (a query set) of the records where a given condition is true. Here's how we'd find all of the "Thomas"es:
 - .exclude(field="val"...) ie:  user = User.objects.exclude(last_name="Thomas")
print("QUERY RESULT:", user)
 is the opposite of .filter: It returns all of the records where a given condition is false. Here's every user NOT surnamed "Thomas"
 - user = User.objects.filter(first_name__startswith="S") #note dunder score/bar
  print("QUERY RESULT:", user)
 - user = User.objects.exclude(first_name__contains="E") #note dunder score/bar
  print("QUERY RESULT:", user)
 - user = User.objects.filter(age__gt=80)   #older than 80
  print("QUERY RESULT:", user)
 - user = User.objects.filter(age__gte=80) # 80 and those older
  print("QUERY RESULT:", user)

 Queries can be chained together:
 - user = User.objects.filter(last_name__contains="o").exclude(first_name__contains="o")
  print("QUERY RESULT:", user)
 - user = User.objects.filter(last_name__contains="o").exclude(first_name__contains="o")
  print("QUERY RESULT:", user)
 - If it's the same type of query, instead of being chained you can combine multiple arguments to the function:
  user = User.objects.filter(age__lt=70, first_name__startswith="S")
  print("QUERY RESULT:", user)
 - Conditions are joined with AND:
user = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
  print("QUERY RESULT:", user)

