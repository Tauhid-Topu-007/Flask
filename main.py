from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route("/")
def hello_world():
    print(url_for('static', filename='style.css'))
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']

        # Here you would check database
        return f"Welcome {name}"
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)