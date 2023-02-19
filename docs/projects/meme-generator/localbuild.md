# Build the project locally

We will use the Python project code and build the meme generator locally to understand what it does and how to run it.

## Setup python

1. Download the repo, change the directory to meme generator
    ```bash linenums="1"
    git clone :repo
    cd reponame/projects/meme-generator
    ```
2. Install python virtual environment. It lets us run install python packages without affecting our default python installation.
    ```py linenums="1"
    python install venv venv # (1)
    ```
    1. Learn how to use virtual environments here

3. Install required packages specified in the `requirements.txt`.

    ```py linenums="1"
    pip install -r requirements.txt
    ```

## Run the app

`main.py` is our Python application, `templates` contains some HTML required for the web application. 

Use `python main.py` to start the application. Navigate to [http://localhost:5000](http://localhost:5000)

Vola!!🎉 There we have our meme-generator running. Well, done.👏

Next lets containerize the app. 