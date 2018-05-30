Forms:

    A practice project: learners_cafe

    * Using Forms
    * superuser: jeremy password: AiFee2oo
    * app: courses

v0.11
=====

present the form
----------------

    #. at the project level, create forms.py and add SuggestionForm
    #. add SuggestionForm in views.py
    #. add a URL to the view
    #. add a template for the view using form.as_p

    settings.py:

    * set up EMAIL_BACKEND

deal with the submission
------------------------

    #. add csrf, post method, submit to the template
    #. use form_valid to email it to the webmaster and add a message
    #. then redirect to the success_url (back to the original form)
    #. update the template to show the success message

try
---

    * http://127.0.0.1:8000/suggestion/


v0.11.1
========

    * improve: use reverse_lazy() for success_url in the SuggestionFormView


v0.12
=====

New Models
----------

    * change Step into an abstract model
    * create two child models of Step: Reading and Quiz
    * be careful about migration: (add Reading here)
        1. add abstract = True to class Meta
        2. comment out Step related code in admin.py
        3. python manage.py makemigrations courses / python manage.py make migrate courses
        4. go back to admin.py and change Step to Reading
        5. manually migrate tables (Step to Reading)

    * add Quiz and add it to Admin
        1. same steps as above but we don't need to run the SQL command.
        2. fix Admin: verbose_name_plural = "Quizzes"

    * show both Text and Quiz inside a course
        1. use get_context_data()
        2. adjust the templates

    * change the name of Reading to Text
        1. rename the model to Text in models.py
        2. comment out related code in admin.py
        3. python manage.py make migrations courses
            Did you rename the courses.Reading model to Text? [y/N] y
        4. python manage.py make migrate courses
        5. change Reading to Text in admin.py and uncomment the code
        6. fix CourseDetailView in views.py (change reading_set to text_set)

    * show steps: Text and Quiz
        1. add two views in urlpatterns (text and quiz)
        2. add get_absolute_url() to Text and Quiz Model
        3. change reverse url lookup in the template to step.get_absolute_url
        4. add template_name = "courses/step_detail.html" to TextDetailView and QuizDetailView

Models
------

    - Course
        - Text(Step)
        - Quiz(Step)


v0.13
=====

    * correct Quiz field total_choices to total_questions
    * create Question class, python manage.py makemigrations courses
    * create Answer class, python manage.py makemigrations courses && python manage.py migrate courses
    * same process for adding MultipleChoiceQuestion and TrueFalseQuestion

Models
------

    - Course
        - Text(Step)
        - Quiz(Step)
        - Question
            - MultipleChoiceQuestion
            - TrueFalseQuestion
            - Answer


v0.14
=====

    * Add ModelForm QuizForm, MultipleChoiceQuestionForm, TrueFalseQuestionForm in forms.py
    * Add Material from materializecss.com
    * Add QuizCreateView and modify related urlpatterns, templates

v0.15
=====

    * Add QuizEditView and related urlpatterns and template


v0.16
=====

    * remove Materialize CSS (prepare for CSS grid)

v0.17
=====

    * fix QuizCreateView form_valid and make SuccessMessageMixin working


v0.18
=====

    * restore Materialize CSS

v0.19
=====

    * create two paths in urls.py for two Question types to use CreateView more easily

v0.20

    * customize a form html output in question_edit.html to enable Material CSS checkbox
    * add create view and edit view for multiple-choice and true-false questions