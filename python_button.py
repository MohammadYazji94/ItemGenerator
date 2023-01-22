from flask import request


# Python-Button Methode
def python_response():
    """
    Handle a request from the client when the "Python" button is clicked.

    Returns:
        str: A string containing valid Python code defining two dictionaries:
        "tss_plans" and "tss_meta".
    """
    data = request.form.to_dict()
    del data["submit"]
    activities = list(v for k, v in data.items() if "activity" in k.lower())
    points = list(v for k, v in data.items() if "points" in k.lower())
    kate = list(v for k, v in data.items() if "cate" in k.lower())
    list3 = list(zip(activities, zip(points)))
    str(kate)
    res = dict()
    res = {idx: idx + 1 and val for idx, val in enumerate(kate)}
    result = {}
    for key, value in res.items():
        if value not in result.values():
            result[key] = value
    name = request.form["name"]
    tss_plans = (
        'tss_plans = {\\<br>"'
        + name
        + '":<br>'
        + str(dict(list3))
        .replace("{'", '["')
        .replace("':", "")
        .replace("('", "[")
        .replace("',)", ']"')
        .replace("'", '"')
        .replace("}", "]")
        + "<br>}"
        + "<br><br>"
    )
    tss_meta = (
        'tss_meta = {\\<br>"' + name + "#CATEGORIES" + '":<br>' + str(result) + "<br>}"
    )
    return tss_plans + tss_meta