export APP_CONFIG_FILE=/var/www/passbook/config/__init__.py

if [ ! -d "./instance/passbook.db" ]
then
    touch instance/passbook.db
	sqlite3 instance/passbook.db < app/schema.sql 
#export FLASK_APP=app/__init__.py
#flask run
python3 run.py