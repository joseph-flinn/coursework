## Snake Eyes
This is Python Flask SaaS application to learn more about the different pieces that
are needed to build SaaS software. The project is built and contained with docker and
docker-compose. Flask Blueprints were used to build out the frontend. If I redo this 
project, I would like to separate the frontend into a strictly frontend framework 
leaving the backend in Flask so that the project is more modular and a little easier 
to scale. Python Celery backed by Redis is used for handling tasks. 

##### Personal Goals
- Learn Flask 
- Learn to build a user system 
- Learn to build a secure authentication system 
- Learn to integrate into third-party payment systems

### Pre-Installation 
- The docker-compose environment variables can be found in .env
- Add your `.env` from the `.env.example` file and add your `instance/settings.py` to 
overwrite the default `config/settings.py` file. 
- Install the cli tool `pip install --editable .`

### Installation
- `docker-compose up --build`
- The web application will be found at \<docker-machine-ip\>:8000

### CLI Tool
Manual documentation coming soon...
