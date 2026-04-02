from flask import Flask
from flask import render_template
app = Flask(__name__) #   crea app

@app.route("/about")       #   URL definito

def about():
    return render_template("index.html")


app.run(debug=True) # Avvio del server