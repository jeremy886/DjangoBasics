Intro:

    A practice project: learners_cafe


v0.01
=====

    * superuser: jeremy password: AiFee2oo
    * start an app (courses)
    * add home view


v0.02
=====

    * add Course to Admin
    * add static file settings
    * change template file and directory for home page
    * update home page using static files
    * add a hello world page: http://127.0.0.1:8000/hello/
    * add a new welcome page: http://127.0.0.1:8000/
    * add base template file, css file

v0.03
=====

    * add a new model Step that has a many-to-one relationship with Course
    * register Step as inlines of Course in Admin
    * to see: http://localhost:8000/admin/courses/course/


v0.04
=====

    * add url to course list page
    * add course list page (template + view)

v0.05
=====

    * make course list clickable: http://localhost:8000/courses/
    * * add detail course page and url: http://localhost:8000/courses/courses/3/

v0.06
=====

    * ordering Course's Step

v0.07
=====

    * You don't need a use get_object_or_404(User, username="ken") like a function view.
    * use template filter "title" for Step's title

v0.08
=====

    * add Content to Step model and allow this field to be blank and with a default value ""
    * python manage.py makemigrations courses && python manage.py migrate courses
    * add Content detail view, add the view to urlpatterns
    * apply linebreaks to content detail template

v0.09
=====

    * add many links to all templates to enable better navigation
    * now you can visit every page by http://localhost:8000/
    * use app_name to add namespace to url tag


v0.10
=====

    * change step detail view from a function view to a class based view