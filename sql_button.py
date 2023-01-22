from flask import request

def sql_response():
    """
    Handle a request from the client when the "SQL" button is clicked.

    Returns:
        str: A string containing valid SQL statements.
    """
    data = request.form.to_dict()
    del data["submit"]
    activities = list(v for k, v in data.items() if "activity" in k.lower())
    points = list(v for k, v in data.items() if "points" in k.lower())
    kate = list(v for k, v in data.items() if "cate" in k.lower())
    name = request.form["name"]
    sql_statements = (
        "<p style='color:red'>Erstellen einer neuen Tabelle 'plans':</p>"
        "CREATE TABLE IF NOT EXISTS plans (<br/>&emsp;plan_id INTEGER PRIMARY KEY,<br/>&emsp;plan_name VARCHAR(255)<br/>);<br/>""<br/><br/>"

        "<p style='color:red'>Erstellen einer neuen Tabelle 'details':</p>"
        "CREATE TABLE IF NOT EXISTS details (<br/>&emsp;detail_id INTEGER PRIMARY KEY,<br/>&emsp;plan_id INTEGER,<br/>&emsp;category VARCHAR(255),<br/>&emsp;activity VARCHAR(255),<br/>&emsp;points INTEGER,<br/>&emsp;FOREIGN KEY (plan_id) REFERENCES plans(plan_id)<br/>);<br/>""<br/><br/>"

        "<p style='color:red'>Plan_name bestimmen:</p>"
        "INSERT INTO plans (plan_name)<br/>VALUES ('"+ name +"');<br/><br/><br/>"

        "<p style='color:red'>Neue Aktivitaeten hinzufuegen:</p>"
    )
    for i in range(len(activities)):
        #ids = str(i+1)
        sql_statements += (
            #f"INSERT INTO details (plan_id, category, activity, points) VALUES ({ids}, '{activities[i]}', {points[i]}, '{kate[i]}');<br/>"
            f"INSERT INTO details (plan_id, category, activity, points)<br/>VALUES (1, '{kate[i]}', '{activities[i]}', {points[i]});<br/><br/>"
        )
    return sql_statements