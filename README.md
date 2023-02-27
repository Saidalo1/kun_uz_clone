# Django online shop API.

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" alt=""/>
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white"  alt=""/>
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoft-sql-server&logoColor=white"  alt=""/>
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white"  alt=""/>
</p>


<hr class="dotted">
It is an online store API system built on Django Rest Framework. It contains everything you need to add products and use as a quality store.

## Screenshots

### Swagger (blogs, elastic search)
![App Screenshot](https://imgur.com/hIe39n1.png)
### Blogs
![App Screenshot](https://imgur.com/mpODdkO.png)

## About this Project:

I'll be happy if you provide any feedback or code improvements or suggestions.

Connect with me at:

<p align='center'>

  <a href="https://www.linkedin.com/in/saidalo-saidakhmedov-7b8311185/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://stackoverflow.com/users/17614591/saidalo">
    <img src="https://img.shields.io/badge/stackoverflow-%23E4405F.svg?&style=for-the-badge&logo=stackoverflow&logoColor=white" />        
  </a>&nbsp;&nbsp;

</p>

<p align='center'>
  📫 How to reach me: <a href='mailto:saidakhmedovsaidalo@gmail.com'>saidakhmedovsaidalo@gmail.com</a>
</p>

## Some technical information:

- Django - 4.1.7
- Django Rest Framework - 3.14.0
- Django Ckeditor - 6.5.1
- Django Environ - 0.9.0
- Django Elasticsearch Dsl Drf - 0.22.5
- pytest-django - 4.5.2

## To Install:

Cloning the Repository:

```
$ git clone github.com/Saidalo1/kun_uz_clone.git
$ cd kun_uz_clone
```

Installing the environment control:

```
$ pip install virtualenv
$ virtualenv env
```

Activating the environment:

on Windows:

```
env\Scripts\activate
```

on Mac OS / Linux:

```
$ source env/bin/activate
```

Installing dependencies:

```
$ pip install -r requirements/base.txt
```

Create a .env file on ecom folder (/root/.env) setting all requirements without using space after "=".

Copy and paste on our .env file:

```
# Debug
DEBUG=TRUE_OR_FALSE

# Secret key
SECRET_KEY=YOUR_SECRET_KEY

# Database settings
DATABASE_NAME=YOUR_DATABASE_NAME
DATABASE_USER=YOUR_DATABASE_USER
DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
DATABASE_HOST=YOUR_DATABASE_HOST
DATABASE_PORT=YOUR_DATABASE_PORT

```

Installing MAKE:

On Mac OS & Linux:

```
sudo apt install make
sudo apt install build-essential
```

On Windows:

```
1. Press Win + X keys together to open the Power menu.
2. Select Windows Powershell(Admin).
3. Type the command ‘Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))' and press Enter
4. Downloads and installs chocolatey as available from their official source: https://community.chocolatey.org/courses/installation/installing?method=installing-chocolatey#powershell
5. Type choco to verify if the installation worked.
6. Now, type the command ‘choco install make‘ to install Make.
7. Go to the installation directory C:\Program Files(x86)\GnuWin32\ to confirm the installation worked.
```

Install ElasticSearch:

Linux:
```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-linux-x86_64.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-linux-x86_64.tar.gz.sha512
shasum -a 512 -c elasticsearch-8.6.2-linux-x86_64.tar.gz.sha512 
tar -xzf elasticsearch-8.6.2-linux-x86_64.tar.gz
cd elasticsearch-8.6.2/ 
./bin/elasticsearch
```

Windows:
```
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-windows-x86_64.zip

cd C:\elasticsearch-8.6.2
.\bin\elasticsearch.bat
```


Type this command to make migrations and migrate:

```
make mig
```

Create a super user:

```
$ make admin
```

Finishing running server:

```
$ python manage.py runserver
```

To test project:
```
$ pytest
```


## Contributing

You can send how many PR's do you want, I'll be glad to analyse and accept them! And if you have any question about the
project...

📫Email-me: <a href='mailto:saidakhmedovsaidalo@gmail.com'>saidakhmedovsaidalo@gmail.com</a>

 <a href="https://www.linkedin.com/in/saidalo-saidakhmedov-7b8311185/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>&nbsp;&nbsp;

Thank you!

## License

<a href="https://github.com/Saidalo1/kun_uz_clone/blob/master/LICENSE.md">
    <img alt="NPM" src="https://img.shields.io/npm/l/license?style=for-the-badge">
</a>&nbsp;&nbsp;

This project is licensed under the MIT License - see
the [LICENSE.md](https://github.com/Saidalo1/kun_uz_clone/blob/master/LICENSE.md) file for details.
