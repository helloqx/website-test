# Worship Slide Generator

## Contents

* [About the Project](#about-the-project)
* [Installation Instructions](#installation-instructions)
* [Database Schema](#database-schema)
## About the Project
Worship Slide Generator provides a simple point-and-click interface for creating worship slides easily and on-the-go.

The live version of the site can be found at https://praise-the-lord.herokuapp.com.

## Installation Instructions
1. Clone the repo.
```
git clone https://github.com/helloqx/worship-slide-generator.git
```
2. Set up a virtual environment if needed.
```
python3 -m venv venv
(Mac):     source venv/bin/activate 
(Windows): venv\Scripts\activate
```
3. Install the required libraries.
```
pip install -r requirements.txt
```
4. Set the environment variable. It is suggested to put these lines inside `venv/bin/activate` or `venv\Scripts\activate.bat` for convenience.
```
(Mac):     export FLASK_APP=main.py
(Windows): set FLASK_APP=main.py
```
5. Edit the `RESET_DATABASE` in `./config.py` to read:
```
RESET_DATABASE = os.environ.get('RESET_DATABASE') or "True"
```
and populate the database with 
```
python song_populator.py
```
6. Launch the site. The site should be live at `localhost:5000`.
```
flask run
```


## Database Schema
![image](https://user-images.githubusercontent.com/12347266/39959385-53477486-5643-11e8-8eb6-3700009cfa76.png)
### Songs
All songs are stored as a single database object, with lyric slides seperated by two newlines `\n\n`.  
### Users
`is_admin` will be modified to a role string soon. Latest slides are stored as a string of song ids. 
