from setuptools import setup, find_packages

setup(
    name="mama-ng-contentstore",
    version="0.1",
    url='http://github.com/praekelt/mama-ng-contentstore',
    license='BSD',
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages(),
    install_requires=[
        'dj-database-url',
        'dj-static',
        'django-filter',
        'django-messaging-contentstore==0.1.7',
        'Django==1.8',
        'djangorestframework',
        'gunicorn',
        'psycopg2',
        'raven==5.1.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
