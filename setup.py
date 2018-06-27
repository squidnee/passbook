from setuptools import setup, find_packages

setup(
    name='passbook',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_login',
        'flask-sqlalchemy',
        'flask_bcrypt',
        'flask_wtf',
        'flask-migrate',
        'Flask-Script',
        'flask-cors',
        'psycopg2',
        'pyview'
    ],
    zip_safe=False
)