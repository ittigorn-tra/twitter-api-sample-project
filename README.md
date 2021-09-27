<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.942 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β31
* Mon Sep 27 2021 05:55:54 GMT-0700 (PDT)
* Source doc: README.md
----->



# Twitter API Sample Project


## Notes from the author

First of all, thank you for the opportunity for me to express myself code-wise. Throughout the last few days I spent reading Twitter API docs and sifting through solutions online, I had a lot of fun and it really opened up a new world for me. Besides many new tools, aspects and practices I’m starting to adapt myself to, I found that interacting with social media is fun.

Although functional, This project is still far from well-structured or at least not met my own standard that I’d be proud of just yet. There are still many aspects that I’d like to keep improving even after I’ve submitted it. Some of which are:



1. Implement a login system and a security scheme such as JWT.
2. Though there are some basic tests in the project, I want to learn more on writing tests that are more thorough.
3. Offer more options for each endpoint such as minimum retweeting count

Lastly,** please comment **on my work. Thank you.


## Prerequisite



1. Miniconda (recommended) or Anaconda installed on the machine


## Running on local machine


### Windows



1. Clone project on to local machine
2. Change directory to the project root
3. Copy “local.env” file and rename it to “.env”
4. Open the file `.env` and replace the value of `TWITTER_BEARER_TOKEN` to the one you’ve received from me (the project author)
5. Set up conda environment
    1. Open Miniconda/Anaconda prompt
    2. Change directory to the project root
    3. Execute command `conda env create -y -f “setting_up\env_requirements\windows\conda.yml”`
    4. Close the console
6. Double-click “run_local_api.bat”
7. API can be reached by calling “localhost”


##### Notes



* “run_local_api.bat” batch script uses the default port 80 so there’s no need to specify port number. Please edit the batch script if you wish to change the port number
* “run_local_api.bat” batch script is set to have the option “--reload” turned on for ease of development. Please edit the batch script if you wish to change this.


### Linux



1. Clone project on to local machine
2. Change directory to the project root
3. Copy “local.env” file and rename it to “.env”
4. Open the file `.env` and replace the value of `TWITTER_BEARER_TOKEN` to the one you’ve received from me (the project author)
5. Set up conda environment
    1. Change directory to the project root
    2. Execute command `conda env create -y -f setting_up/env_requirements/linux/conda.yml`
6. Activate the conda environment by executing the following command `source activate twitter-api-sample-project`
7. Execute the following command to run the API `uvicorn app.main:app --port 8000`
8. API can be reached by calling “localhost:8000”


##### Notes



* Please add “--host 0.0.0.0”  to the command when running the server if you wish to reach the API from another machine


### Mac



1. Clone project on to local machine
2. Change directory to the project root
3. Copy “local.env” file and rename it to “.env”
4. Open the file `.env` and replace the value of `TWITTER_BEARER_TOKEN` to the one you’ve received from me (the project author)
5. Set up conda environment
    1. Change directory to the project root
    2. Execute command `conda env create -y -f setting_up/env_requirements/mac/conda.yml`
6. Activate the conda environment by executing the following command `source activate twitter-api-sample-project`
7. Execute the following command to run the API `uvicorn app.main:app --port 8000`
8. API can be reached by calling “localhost:8000”


##### Notes



* Please add “--host 0.0.0.0”  to the command when running the server if you wish to reach the API from another machine


## API Documentation

API docs are auto-generated and can be viewed / test interactively via Swagger UI by visiting:

[http://localhost/docs](http://localhost/docs)

OpenAPI json file can also be downloaded on the page mentioned above.


## Testing


### Windows



1. Double-click `run_pytest.bat` 

    Note: make sure you’ve previously created the conda environment for this project.



### Linux / Mac



1. Activate conda environment.
2. Run `pytest` in the project root folder.


## Useful Tips for Development


### Postman

Postman collection can be found in `postman/`


### Windows batch files


##### `activate_env.bat`



* This batch file opens a command line and automatically activates the conda environment for you.


##### `run_jupyter.bat`



* This batch file automatically activates the conda environment for you and launches Jupyter Notebook with `/notebooks` as working directory.


##### `run_pytest.bat`



* This batch file automatically activates the conda environment for you and runs pytest.


##### `run_local_api.bat`



* This batch file automatically activates the conda environment for you and launches a development server on your local machine.


## Miscellaneous


### Twitter API v2 Sample Code

[https://github.com/twitterdev/Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code)


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