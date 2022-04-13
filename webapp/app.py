from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads,IMAGES

import imgprocessing as i
import pickle

app = Flask(__name__)

photos =  UploadSet("photos",IMAGES)

app.config["UPLOADED_PHOTOS_DEST"] = "static/images"
configure_uploads(app,photos)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template('frm.html')

@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method == "POST" and "photo" in request.files:
        filename = photos.save(request.files["photo"],name="xray.jpg")
        print(filename)
        x = i.getPixelAsRowVector()
        ## Load pkl file.
        ## Predict the result.
        ## Return the result.
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)