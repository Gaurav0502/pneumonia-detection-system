from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frm.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    print(upload_file)
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)