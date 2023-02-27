mig:
	python3 manage.py makemigrations
	echo "Migrations created successfully, boss"
	python3 manage.py migrate
	echo "Migrations migrated successfully, boss"

admin:
	python3 manage.py createsuperuser