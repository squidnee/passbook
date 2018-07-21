rm -r migrations
rm instance/passbook.db
flask db init
flask db migrate -m "new table"
flask db upgrade