# Create the container

We will use a simple Python Flask application. When run, the application gets and displays a meme from Reddit in your browser.

## Initial Setup

Download the repo with our code and switch to `hello-devops-project/code/meme-generator/`
    ```bash linenums="1"
    git clone https://github.com/robusta-dev/Hello-DevOps-Project.git
    cd hello-devops-project/code/meme-generator/
    ```
## Run Python application locally - Optional

Run `./buildlocally.sh` to install the required packages and run the application. Navigate to [http://localhost:5000](http://localhost:5000) to see our app exposed on port `5000`.


## Create the Dockerfile

A **Dockerfile** contains instructions to recreate the local installation and generates a Docker image using it.

To do this, we will follow these steps

1. Get a Docker image with python preinstalled
2. Copy the project code into it
3. Install required packages
4. Run the application when the container starts

With the instructions from the previous step, we create this Dockerfile
    ``` docker linenums="1" title="Dockerfile"
    FROM python:3.10-slim 
    COPY . .
    RUN pip install --no-cache-dir -r requirements.txt
    CMD ["python", "main.py"]
    ```

## Build the Docker image
A Docker image is created using our `Dockerfile`, a single image can be used to create one or more containers.

Run the following command to build the docker image
```yaml linenums="1"
docker build -t python-app:v1 . # (1)!
```

1.  `-t` - Tag your app, in this case `v1`. Create multiple versions of the same image with different tags.

    `.` - Build the Dockerfile in the current directory. 

??? success "Output"

    ![Docker Build Output](./images/dockerbuildoutput.png)



## Run the container
Let's run the image and create a container
```yaml linenums="1"
docker run -p 5000:5000 python-app:v1 # (1)!
```

1. `-p` - Specifies docker to attach a port in your container to your localhost.

??? success "Output"

    ![Docker Run Output](./images/dockerrunoutput.png)



Navigate to [http://localhost:5000](http://localhost:5000) to see the running app.
???+ note
    Since we did not use the detached mode `-d`, the application ends as soon as you use `CTRL+C` or close your terminal. 

Vola!!🎉 There we have your first Docker container. Well, done.👏
