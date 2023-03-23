# 🔥Your First Kubernetes Pod
In this project, we will deploy a Docker container on Kubernetes. One of the benefits of Kubernetes is that it will make sure your application is running all the time. For example, if your Docker container stops, you have to manually restart it. But with Kubernetes it's done automatically.

## 🎯 What you'll learn
* Writing a Kubernetes Pod YAML.
* Creating your first Pod.
* Port-forwarding the Pod to view your application. 

## 🛑 Prerequisites
* Kubernetes cluster, local or in the cloud. If you want to install a local **k3d** cluster, follow this [guide](https://k3d.io/v5.4.7/#installation).
* [Docker](https://docs.docker.com/get-docker/) & [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) installed on your machine.

## Introduction
To run a container on Kubernetes we use a Pod. A Pod is an abstraction over a container. Each Pod has one main container and one or more helper(side-car) containers.

## Create a Pod YAML

To create an Kubernetes object we write specific instructions. In this case its a Pod. Once you are done, give this file to kubernetes and it takes care of the rest.

1. A Pod is created using the `apiVersion` `v1`. 

```yaml linenums="1"
apiVersion: v1
kind: Pod
```
2. Metadata helps you identify Kubernetes objects. Labels are used to group similar objects. Example: All objects related to the meme app are grouped using the label `k8s-memes`. 

```yaml linenums="1"
metadata: 
name: meme-app
labels:
    app: k8s-memes
```
3. Using `spec` we specify the containers we want to define, what Docker image they use, ports we need to open etc.

```yaml linenums="1"
spec:
containers:
- name: k8s-meme-app
    image: pavangudiwada/dockerimage:v1 # (1)!
    ports:
    - containerPort: 5000 # (2)!
        protocol: TCP
    resources: # (3)!
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
```

1.  You can add your own Docker image using `DockerHubUserName/ImageName:Tag`

2. Port the application is to be exposed on and using what protocol.  

3. Define the amount of CPU and memory a pod can use. Learn more about them [here](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/). Also read ["Stop Using CPU Limits"](https://home.robusta.dev/blog/stop-using-cpu-limits) to understand the misconceptions around CPU limits. 


This is the result of the previous steps. Save it to a file called `first-pod.yaml`
``` yaml linenums="1" title="first-pod.yaml"
apiVersion: v1
kind: Pod
metadata: 
name: meme-app
labels:
    app: k8s-memes
spec:
containers:
- name: k8s-meme-app
    image: pavangudiwada/dockerimage:v1
    ports:
    - containerPort: 5000
        protocol: TCP
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
```

## Deploy the Pod

Next, lets use the Kubernetes Pod YAML to create our Pod. 

Run `#!yaml kubectl apply -f first-pod.yaml` to create a Pod with all our specifications. 


## View the Pod

The Pod could take a few seconds to start running. You can see this using `#!yaml kubectl get pod meme-app` 

??? success "Output"
    ``` bash

     ❯ kubectl get pod meme-app                                                                  
     NAME       READY   STATUS    RESTARTS   AGE
     meme-app   1/1     Running   0          11s
    ```


## Access the application

`port-forward` is a feature to expose any port of a Pod locally. It only works as long as the Pod is running and the terminal is open.

```bash linenums="1"
kubectl port-forward pod/meme-app 5000:5000
```
Navigate to [http://localhost:5000](http://localhost:5000) to see the running app.

??? success "Output"

    ![Application running in the Pod](./images/memegeneratorexample.png)

Voilà!!🎉 There, we have your first Kubernetes Pod. Well, done.👏

## Delete the Pod

If you no longer need a Pod, you can use `#!yaml kubectl delete -f meme-pod.yaml`. Alternatively, `#!yaml kubectl delete pod meme-app` can also be used. 


## ❓3 Questions to check your Kubernetes Pod understanding
1. How do you see which Pods are running?
2. What is the difference between a container and a Pod?
3. Can you run a container on Kubernetes without a Pod?

## 🥷3 Steps to master Kubernetes Pod
1. Create a Pod using [this](https://hub.docker.com/r/pavangudiwada/reactapp) Docker image and expose port `3000`.
2. Follow [this](https://kubernetes.io/docs/concepts/workloads/pods/) guide by Kubernetes to understand Pods in depth. 
3. Read about `kubectl create` command. 