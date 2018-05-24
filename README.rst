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