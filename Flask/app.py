from flask import Flask
from flask import render_template

app = Flask(__name__) #   crea app

# @app.route("/")       #   URL principale
# def hello_world():
#     return "Ciao"


@app.route("/")       #   URL definito

def about():
    return render_template("index.html")
  
app.run(debug=True, use_debugger=False, use_reloader=False) # Avvio del server