# XurdeBlog
This is a blog created with flask and the clean blog template from bootstrap . This is a really interesting project , I created this after the day i learned Flask.
It was created in 3 hours and was a fun to make project , You can easily clone into this repository and modify it as per your requirement .

## Features
* Working Contact Form
* Admin Dashboard
* User can Add , Edit or Delete posts via the admin dashboard
* User can customize the blog as per there convenience through settings.json

## How to use?
First you need to clone the repository
```bash
git clone https://github.com/DevXurde/XurdeBlog.git
```
Change directory
```bash
cd XurdeBlog
```
Install requirement
```bash
pip install -r requirements.txt
```
Running app.py
```bash
python3 app.py
```
Now open your browser and paste this link 
```bash
http://localhost:8080/
```

## Customizing
You can't customize everthing via settings.json, it looks something like this
```json
{
    "version": 1.0,
    "license": "MIT",
    "host": "localhost",
    "port": 8080,
    "name": "Xurde",
    "db_name": "database.db",
    "secret_key": "eefefe",
    "admin_user": "user",
    "admin_password": "1234",
    "copyright_year": "2021",
    "no_of_posts_home": 3,
    "admin_email": "youremail@gmail.com",
    "admin_email_password": "yourpassword"
}
```
You can change anything as per your convinience, like you can change the title by editing 
```json
"name": "Your-Name",
```

Hope everything worked out for you!

# Thank You