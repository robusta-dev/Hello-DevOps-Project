# Kubernetes

To deploy applications in Kubernetes, you need a Kubernetes cluster. Local or on the cloud shouldn't matter. If you want to install a local **k3d** cluster, follow this [guide](https://k3d.io/v5.4.7/#installation). 

## Kubernetes Pod
Pods are the smallest objects in Kubernetes. Each pod have one main container and other helper(side-car) containers. 

### Creating a pod

Here are the instructions to creating a yaml file to run a Pod.

1. Choose the api version specific to a pod. 
2. Mention the type of Kubernetes object, in this case a Pod. 
3. Give your pod a name, and one or more tags to identify/ group similar applications. 
4. Add details about the image to be used, open ports and memory limits. Read why you should not be using [CPU limits](https://home.robusta.dev/blog/stop-using-cpu-limits).

### Pod YAML

``` yaml linenums="1" title="meme-pod.yaml"
apiVersion: v1
kind: Pod
metadata: 
name: meme-app
labels:
    app: k8s-memes
spec:
containers:
- name: k8s-meme-app
    image: DockerHubUserName/buildxtest2:latest
    ports:
    - containerPort: 5000
        protocol: TCP
    resources:
    limits:
        memory: "128Mi"
```
Save this code into a file or change directory to `/kubernetes` and run `#!yaml kubectl apply -f meme-pod.yaml`.

### Port-forwarding

`port-forward` is a temporary method to expose the application to the outside world.

```bash linenums="1"
kubectl port-forward pod/meme-app 5000:5000
```
If the pod is deleted and recreated, terminal is closed, or you close the port-forward, your application cannot be accessed.

### Deleting a pod

Use `#!yaml kubectl delete -f meme-pod.yaml`

## Kubernetes Replicasets

ReplicaSets are the next level abstraction over Pods, it makes sure you always have `n` replicas all the time. It can also manage pod/pods created already by using the pod label.

### Creating a ReplicaSet

The instructions are similar to a Pod, but here you also give Kubernetes a template with instructions to create a pod other than details about ReplicaSet. 

``` yaml linenums="1" title="meme-replicaset.yaml"
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: meme-replicaset
  labels: 
    app: meme-app-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: meme-app-replicaset
  template:
    metadata:
      labels:
        app: meme-app-replicaset
    spec:
      containers:
        - name: meme-app
          image: pavangudiwada/buildxtest2:latest
          ports:
            - containerPort: 5000
              protocol: TCP
          resources:
            limits:
              memory: "128Mi"
```
`#!yaml replicas: 3` - Kubernetes will maintain 3 pods with the given pod template at all times.

`#!yaml selector.matchLabels.app = meme-app-replicaset` - If there are other pods with the same label, the ReplicaSet will include them in the 3 replicas and manage them too.

## Services

When a ReplicaSet is managing pods, and one of them goes down. How do you make sure traffic is routed to others? How do you manage to connect to different pods and communicate with them. **Services** to your rescue. 

A service manages communication between multiple pods seamlessly.

### Creating a service

```yaml linenums="1" title="meme-service.yaml"

apiVersion: v1
kind: Service
metadata:
  name: meme-service
spec:
  type: ClusterIP
  ports:
    - port: 5000
  selector:
    app: meme-app-replicaset
```
```bash linenums="1"
kubectl apply -f meme-service.yaml
```
The service is automatically attached to the ReplicaSet using `#!yaml selector.app = meme-app-replicaset`. 

### Testing the Service

A **ClusterIP** service makes a pod accessable to other pods in the same cluster. Let's test if our service is actually working. 

Run `#!yaml kubectl describe service meme-service`

```yaml linenums="1" title="output"

-> kubectl describe service meme-service

Name:              meme-service
Namespace:         default
Labels:            <none>
Annotations:       <none>
Selector:          app=meme-app-deployment
Type:              ClusterIP
IP Family Policy:  SingleStack
IP Families:       IPv4
IP:                10.43.64.228
IPs:               10.43.64.228
Port:              <unset>  5000/TCP
TargetPort:        5000/TCP
Endpoints:         10.42.0.14:5000,10.42.0.18:5000
Session Affinity:  None
Events:            <none>
```
Since we created two replicas we have two `Endpoints:`

Exec into one of the pods using
```bash linenums="1"
kubectl exec -it meme-replicaset-XXXXX -- /bin/bash
```
To get data from the **http** endpoint we will use **curl**, let's first install it in the pod.

```bash linenums="1"
apt update && apt -y install curl
```
Run `#!bash curl http://IP:Port`, use the **endpoints**.

```html linenums="1" hl_lines="15" 
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Meme Generator</title>
</head>
<body>
    <center>
        <h1>Meme Generator Project</h1>
        <form action="/" method="POST" enctype="multipart/form-data">
            <div>
                <img src="https://preview.redd.it/z19naccatiia1.jpg?width=640&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=e8d575c4030c4790090cf9670c23d71449b598f6" style="min-width: 200px; max-width: 800px; min-height: 500px; max-height: 600px;">
            </div>
            <button type="submit" style="padding: 5px;">Generate meme</button>
            <div>
                Running on <b>meme-replicaset-64d4855c47</b> a <b>Linux</b>, <b>x86_64</b> architecture machine
            </div>  
        </form>
    </center>
</body>
```
In the output, line **15** shows you the name of the pod that is serving the application.

### Cleaning up
```bash linenums="1"
kubectl delete -f meme-replicaset.yaml meme-service.yaml
```

That's it! 🎉 You now deployed a python application on Kubernetes.