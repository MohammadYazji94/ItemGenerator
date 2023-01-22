from flask import Flask, render_template, request
from json_button import json_response
from python_button import python_response
from sql_button import sql_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    app.config["JSON_SORT_KEYS"] = False
    # Hier können neue ELemente zum Dictionary hinzufügt werden, um neue Buttons zu erstellen
    response_handlers = {"JSON": json_response, "Python": python_response, "SQL":sql_response}
    # Es wird überprüft, ob request.methode "POST" ist, um die richtige Methode aufzurufen
    if request.method == "POST":
        submit = request.form["submit"]
        if submit in response_handlers:
            return response_handlers[submit]()
    return render_template("main.html")


# Die folgenden Zeilen k�nnen auf pythonanywhere gel�scht werden
if __name__ == "__main__":
    import os

    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
