=====
Diet
=====

Diet is a Django app to record diet information for wechat user.

Quick start
----

1. Add "diet" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'diet',
    )

2. Include the diet URLconf in your project urls.py like this::

    url(r'^diet/', include('diet.urls')),

3. Run `python manage.py migrate` to create the diet models.

4. Start the development server and visit http://127.0.0.1:8000/diet/.

