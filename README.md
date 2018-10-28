# World Happiness Web Application

<p align="center"> 
<img src="https://github.com/ania4data/World_happiness_app/blob/master/worldhappinessapp/static/img/webapp_snapshot.png", style="width:70%">
</p>

# App layout

```
├── data
│   ├── 2015.csv
│   ├── 2016.csv
│   ├── 2017.csv
│   └── Untitled.ipynb
├── LICENSE
├── Procfile
├── README.md
├── requirements.txt
├── worldhappinessapp
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── routes.cpython-36.pyc
│   ├── routes.py
│   ├── static
│   │   └── img
│   │       ├── githublogo.png
│   │       ├── linkedinlogo.png
│   │       ├── mediumlogo.png
│   │       ├── webapp_snapshot.png
│   │       └── worldhappiness.jpg
│   └── templates
│       └── index.html
├── worldhappiness.py
└── wrangling_scripts
    ├── __pycache__
    │   └── wrangle_data.cpython-36.pyc
    └── wrangle_data.py

```

## General repository content:

- Data folder: contain 2015 to 2017 world happines csv data
- Server Gateway: `Procfile` connect the app to `Gunicorn` ("Green Unicorn" is a Python Web Server Gateway Interface HTTP server)
- Dependency data: `requirements.txt`
- Static folder: all static images in the app
- wrangling_scripts: contain `wrangle_data.py` where all csv files are processed into plotly plots
- templates: contain `index.html` file for rendering web layout and structure
- `__init__.py`: initialize flask as `app`
- `rountes.py`: get the plotly figures from backend wrangle_data.py and send it as JSON dump tp frontend using flask (render_template) 
- `worldhappiness.py`: connect `app` toeither local host or public address


## Basic Usage for command line:

- Clone the repository use: `git clone https://github.com/ania4data/World_happiness_app.git`
- Create a virtual enviroment where `requirements.txt` is located: 
```
conda update python
python3 -m venv name_of_your_choosing
source name_of_your_choosing/bin/activate
pip install --upgrade pip
pip install -r requirements.txt                      # install packages in requirement
```

## How run the app in your browser (local host):

While in virtual envoroment, make sure `worldhappiness.py` file has following lines:

```
from worldhappinessapp import app
app.run(host='0.0.0.0', port=3001, debug=True)
```
In command line where `worldhappinessapp` located run:

```
python worldhappinessapp.py
```
copy ```http://0.0.0.0:3001/``` to your browser and you are good to go!


## How run the current app in your browser as a public addresss:

Just use:

https://worldhappiness-webapp.herokuapp.com/


## How upload the app to Heroku to a new public address:

After cloning the repository and making changes you like, to upload the all to a public URL under `Heroku` server first make sure:

```
from worldhappinessapp import app
#app.run(host='0.0.0.0', port=3001, debug=True)   #this local host need to be disabled
```
After opening an account on *heroku.com*,  Install Heroku:

```
sudo snap install --classic heroku      #install heroku
heroku login     # Enter username and password of your account
```
In the path where this `README.md` file located git commit the whole app:

```
git init                                     # initialize
git add .
git commit -m "first commit"                 # commit
heroku create name_of_app_of_your_choosing   # repeat this line until your app in unique to get accepted by heroku
git remote -v                                # check if the paths created (git and URL)
git push heroku master                       # at this stage your requirements.txt get downloaded, make sure all version are accepted. if not make a version change
```

If the last step is successful you will have  URL/git path with following addresses:

```
https://name_of_app_of_your_choosing.herokuapp.com
https://git.heroku.com/name_of_app_of_your_choosing.git
```

