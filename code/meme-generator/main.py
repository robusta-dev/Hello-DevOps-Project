from flask import Flask, render_template
import json
import requests
import random
import platform

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def generator():
    sub_reddit = ["Kubernetes", "dockermemes", "ProgrammerHumor"] #subreddits to get memes from
    url = "https://meme-api.com/gimme/" + random.choice(sub_reddit) 
    meme_data = json.loads(requests.get(url).text)
    meme_image = meme_data["preview"][-1] #get a medium size meme image

    host = platform.uname() #details about the host
    
    return render_template("index.html", meme_image=meme_image, host_name=host.node, host_type=host.system, host_arch=host.machine)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")