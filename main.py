from flask import Flask, render_template, request,jsonify

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route("/")
def hello_world():
    # Get query string parameters
    name = request.args.get('name', default="anonymous")
    subject = request.args.get('subject', default="Not specified")
    age = request.args.get('age', default=None)
    city = request.args.get('city', default=None)
    
    # Get all parameters
    all_params = dict(request.args)
    
    return render_template("index.html", 
                         name=name, 
                         subject=subject,
                         age=age,
                         city=city,
                         all_params=all_params)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get('username')
        password = request.form.get('password')
        
        # Get query parameters
        redirect_to = request.args.get('next', default='/')
        
        return f"""
        <html>
        <body style='font-family: Arial; text-align: center; margin-top: 100px;'>
            <h2>Welcome {name}! ✅</h2>
            <p>You have successfully logged in.</p>
            <a href='{redirect_to}' style='color: blue; text-decoration: none;'>← Go back</a>
        </body>
        </html>
        """
    else:
        return render_template("login.html")

@app.route("/profile")
def profile():
    # Get user info from query string
    name = request.args.get('name', 'User')
    age = request.args.get('age', 'Not provided')
    city = request.args.get('city', 'Not provided')
    
    return render_template("profile.html", name=name, age=age, city=city)

@app.errorhandler(404)
def page_not_found(e):
    return """
    <html>
    <body style='font-family: Arial; text-align: center; margin-top: 100px;'>
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
        <a href='/' style='color: blue; text-decoration: none;'>← Go Home</a>
    </body>
    </html>
    """, 404

if __name__ == "__main__":
    app.run(debug=True)