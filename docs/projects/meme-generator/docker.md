# Docker

The next step is to containerize the Python application, this helps us distribute a packaged version with all the required dependencies.

To do this, we will use a `Dockerfile`, a special type of file that lets you define instructions to build your container. Let's write down the instructions we used to run the application locally. 

1. Install Python
2. Create a python virtual environment
3. Install dependencies
4. Run python main.py file
5. Access the application on localhost:port 


## Planning the Dockerfile

Now the instructions to build a docker file roughly translate to this..

1. Get a new Python image - A Linux image with python installed, hence a new virtual environment is not required for our current application.
2. Copy the required files into the container
3. Install dependencies using **pip**
4. Run `python main.py` to start the application
5. Access the application on localhost:port


## Building a Docker image

### Creating a Dockerfile

With the instructions from the previous step, we create this Dockerfile
    ``` docker linenums="1" title="Dockerfile"
    FROM python:3.10-slim

    WORKDIR /app
    COPY . .

    RUN pip install --no-cache-dir -r requirements.txt
    CMD ["python", "main.py"]
    ```
### Dockerignore

If you followed the instructions to build the application locally, you might have the `venv` folder in your current directory. `COPY . . ` copies everything in the current directory into the image. This increases the size of the image and is unnecessary.
    ```docker linenums="1" title=".dockerignore"
    venv
    ```

### Docker build

Run the following commands to build the docker image
    ```docker linenums="1"
    docker build -t meme-application:v1 . 
    ```
    `-t` lets you add a tag to the application, in this case `v1`. This helps you create multiple versions of the same image with different tags.
    `.` - Build the docker file in the current directory. 

Let's run the image and create a container
    ```docker linenums="1"
    docker run -p 5000:5000 meme-application:v1
    ```
        `-p` - Specifies docker to attach a port in your container to your localhost.


???+ note
    Since we did not use the detached mode `-d`, the application ends as soon as you use `CTRL+C` or close your terminal. 
 

Use [localhost:5000](http://localhost:5000) to access our application.

## Application Distribution

At this point, we have the containerized application locally. But we want others to be able to download and use it. We will use **Docker Hub** to publish our application for everyone to access it. 

### Docker login

Docker hub is a repository of docker images. This makes the distribution of the application seamless. You also need a username to **tag** your image and push it to Docker Hub. 

Create an account on Docker Hub and use `docker login` to log into your account locally.

### Deploying to Docker hub

Build the application 
    ```docker linenums="1"
    docker build -t DockerHubUserName/meme-application:v1 . 
    ```
Push to dockerhub
    ```docker linenums="1"
    docker push DockerHubUserName/meme-application:v1 
    ```
**👏** Now anyone can use your application! Next, lets deploy it on Kubernetes.  

