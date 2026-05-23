from flask import Flask,render_template,url_for

app = Flask(__name__,static_folder='assets',static_url_path='/assets')

@app.route("/")
def hello_world():
    #static file=>dynamically generate the url
    print(url_for('static', filename='style2.css'))
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)