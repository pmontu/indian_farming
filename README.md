# Indian Farming

## API

### Endpoints

* Signup by POST http://indian-farming.herokuapp.com//user/
* Admin View of Signed up users by GET http://indian-farming.herokuapp.com//user/
* Logged in Farmer Submit Produce/Logged in Customer Submit Future Order by POST http://indian-farming.herokuapp.com//account/
* Admin Analytics View by GET http://indian-farming.herokuapp.com//account/

## Seup

	git clone https://github.com/pmontu/indian_farming.git
	cd indian_farming
	mkvirtualenv indian_farming
	pip install -r requirements.txt
	./manage.py migrate
	./manage.py runserver