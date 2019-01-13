### Install Project

#### 1. Install Python
```console
brew install python3
```
#### 2. Install Virtual Environment
```console
sudo pip3 install virtualenv
```
#### 3. Make project folder and setup virtual environment
```console
mkdir project
```
copy this project in project folder

#### 4. Project Settings
Go to mysite/settings.py and line 142, 143
```python
EMAIL_HOST_USER = 'yourgmail@gmail.com'
EMAIL_HOST_PASSWORD = 'your gmail password'
```
Update it to your gmail informations.<br>
Login your gmail in web browser.<br>
And go to this url. https://myaccount.google.com/lesssecureapps <br>
Set the option <code>Allow less secure apps:</code> to <code>ON</code>

```console
cd project
virtualenv venv -p python3
source venv/bin/activate
cd mysite
python manage.py makemigrations
python manage.py migrate

```
Create admin user by command
```console
python manage.py createsuperuser
```
Input username, email, password and enter 'y'.

#### 5. Run the server
```console
python manage.py runserver
```
Check localhost:8000 in web browser.<br>
Check localhost:8000/admin for admin site.
