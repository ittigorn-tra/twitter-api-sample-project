<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.771 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β31
* Sun Sep 19 2021 23:11:16 GMT-0700 (PDT)
* Source doc: README.md
----->



# Sample Project for Anymind


## Notes from the author

First of all, thank you for the opportunity for me to express myself code-wise. Throughout the last few days I spent reading FastAPI docs and sifting through solutions online, I had a lot of fun and it really opened up a new world for me. Besides many new tools, aspects and practices I’m starting to adapt myself to, I found that FastAPI is more feature-rich and easier to use than Flask that I’ve been using before for all my prior projects.

Although functional, This project is still far from well-structured or at least not met my own standard that I’d be proud of just yet. There are still many aspects that I’d like to keep improving even after I’ve submitted it. Some of which are:



1. Implement a login system and a security scheme such as JWT.
2. I need to learn more about routing and being more organized.
3. Though there are some basic tests in the project, I want to learn more on writing tests that are more thorough.
4. Using .env file and loading configs this way is new to me and I intend to keep improving it from here on up.
5. Explore more on async features of this library.
6. Enable this project to run on docker / Google Cloud Run.

Lastly,** please comment **on my work. I’ve been working solo for quite a long time. Despite the fact that I want to work with other people with similar sets of interests, my current working environment doesn’t offer much. With this sample project, it’s a great chance for me to improve my skills towards working in tandem with other like-minded people.


## Prerequisite



1. Miniconda (recommended) or Anaconda installed on the machine


## Running on local machine


### Windows



1. Clone project on to local machine
2. Change directory to the project root
3. Copy “local.env” file and rename it to “.env”
4. Set up conda environment
    1. Open Miniconda/Anaconda prompt
    2. Change directory to the project root
    3. Execute command `conda env create -y -f “setting_up\env_requirements\windows\conda.yml”`
    4. Close the console
5. Double-click “run_local_api.bat”
6. API can be reached by calling “localhost”


##### Notes



* “run_local_api.bat” batch script uses the default port 80 so there’s no need to specify port number. Please edit the batch script if you wish to change the port number
* “run_local_api.bat” batch script is set to have the option “--reload” turned on for ease of development. Please edit the batch script if you wish to change this.


### Linux



1. Clone project on to local machine
2. Change directory to the project root
3. Copy “local.env” file and rename it to “.env”
4. Set up conda environment
    1. Change directory to the project root
    2. Execute command `conda env create -y -f setting_up/env_requirements/linux/conda.yml`
5. Activate the conda environment by executing the following command `source activate anymind`
6. Execute the following command to run the API `uvicorn app.main:app --port 8000`
7. API can be reached by calling “localhost:8000”


##### Notes



* Please add “--host 0.0.0.0”  to the command when running the server if you wish to reach the API from another machine


### Mac



8. Clone project on to local machine
9. Change directory to the project root
10. Copy “local.env” file and rename it to “.env”
11. Set up conda environment
    3. Change directory to the project root
    4. Execute command `conda env create -y -f setting_up/env_requirements/mac/conda.yml`
12. Activate the conda environment by executing the following command `source activate anymind`
13. Execute the following command to run the API `uvicorn app.main:app --port 8000`
14. API can be reached by calling “localhost:8000”


##### Notes



* Please add “--host 0.0.0.0”  to the command when running the server if you wish to reach the API from another machine


## API Documentation

API docs are auto-generated and can be viewed / test interactively via Swagger UI by visiting `localhost/docs`

OpenAPI json file can also be downloaded on the page


## Testing


### Windows



1. Double-click `run_pytest.bat` 

    Note: make sure you’ve previously created the conda environment for this project.

2. Run `run_reinit_db_data.bat` to undo all changes in the development database


### Linux / Mac



1. Activate conda environment.
2. Run `pytest` in the project root folder.
3. Undo all changes in the development database
    1. `cd scripts`
    2. `python reinitialize_db_data.py`


## Firestore Console

Viewing / editing data can be done by visiting the Firestore Console via the link below.

Please send me an email to [ittigorn.tra@gmail.com](mailto:ittigorn.tra@gmail.com) if you wish to have your privilege elevated for more available actions on the database.

[https://console.firebase.google.com/u/0/project/anymind-dev](https://console.firebase.google.com/u/0/project/anymind-dev)


## Useful Tips for Development


### Jupyter Notebook


##### `notebooks/Delete all customers accounts and logs.ipynb`



* Clear all customer / accounts / logs data from development database


##### `notebooks/Load initial data.ipynb`



* Insert initial sample data from `resources/initial_data.json` into development database


### Windows batch files


##### `activate_env.bat`



* This batch file opens a command line and automatically activates the conda environment for you.


##### `run_jupyter.bat`



* This batch file automatically activates the conda environment for you and launches Jupyter Notebook with `/notebooks` as working directory.


##### `run_pytest.bat`



* This batch file automatically activates the conda environment for you and runs pytest.


##### `run_local_api.bat`



* This batch file automatically activates the conda environment for you and launches a development server on your local machine.


##### `run_reinit_db_data.bat`



* This batch file automatically activates the conda environment for you, delete all customers, accounts on development database and re-insert initial data as defined in `resources/initial_data.json`.


## Miscellaneous


### Markdown Converter

Add-on for converting Google Docs to markdown is available at the link below:

[https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607](https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607)


#### How to use:



1. Go to the link posted above
2. Install and give the add-on the permissions it needs
3. Open the target Google Docs file
4. Click “Add-ons” on the menu bar
5. Find “Docs to Markdown” -> “Convert”, a panel will open on the right
6. (optional) Select “Suppress top comment”
7. Click “Markdown” on the recently opened panel, the converted markdown should be automatically copied to your clipboard


#### Notes:



* Single-cell table will be converted to a code block
* See [https://github.com/evbacher/gd2md-html/wiki](https://github.com/evbacher/gd2md-html/wiki) for docs