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
2. Set up a virtual environment if needed.
3. Install the required libraries with the command `pip install -r requirements.txt`.
4. Set the environment variable with `set FLASK_APP=main.py`.
5. Launch the site with `flask run`. The site should be live at `localhost:5000`.

## Database Schema
All songs are stored as a single database object, with lyric slides seperated by two newlines `\n\n`.  

![image](https://user-images.githubusercontent.com/12347266/39738406-90c80e62-52bd-11e8-9d72-3a3bdf909565.png)
