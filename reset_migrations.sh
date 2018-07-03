find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm instance/passbook.db
flask db init
flask db migrate -m "new table"
flask db upgrade