from setuptools import setup, find_packages
setup(
    name = "django-annoying",
    version = "0.5",
    packages = find_packages(),
    author = "Anderson",
    author_email = "self.anderson@gmail.com",
    description = "This is django application that try to eliminate annoying things in Django framework.",
    long_description = """
        **Features:**

            - render_to decorator - reduce typing in django views.
            - signals decorator - allow use signals as decorators.
            - ajax_request decorator - returns JsonResponse with this dict as content.
            - get_object_or_None function - similar to get_object_or_404, but returns None if object not found.
            - AutoOneToOne field - creates related object on first call if it doesnt exists yet.
            - HttpResponseReload - reload and stay on same page from where request was made.

                     

        **Installation instruction:**

             - Copy annoying directory to your django project or put in on PYTHONPATH
             - Also you can run sudo python setup.py install or sudo easy_install django-annoying

                              

        **Download:**

            - hg clone http://hg.assembla.com/django-annoying

    """,
    license = "BSD",
    keywords = "django",
    url = "http://www.assembla.com/spaces/django-annoying",
)

