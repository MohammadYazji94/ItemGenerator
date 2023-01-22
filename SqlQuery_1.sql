-- Erstellen einer neuen Tabelle "plan":
CREATE TABLE plans (
    plan_ID INTEGER PRIMARY KEY,
    plan_Name VARCHAR(255)
);

-- Erstellen einer neuen Tabelle "details":
CREATE TABLE details (
    detail_id INTEGER PRIMARY KEY,
    plan_ID INTEGER,
    category VARCHAR(255),
    activity VARCHAR(255),
    points INTEGER,
    FOREIGN KEY (plan_ID) REFERENCES plans(plan_ID)
);

-- Fügen eines neuen Plan hinzu:
INSERT INTO plans (plan_name)
VALUES ('My New Plan');

-- Fügen einer neuen Aktivität hinzu:
INSERT INTO details (plan_ID, category, activity, points)
VALUES (1, 'Schlafen', '9 Stunden', 20);

-- Fügen einer neuen Aktivität hinzu:
INSERT INTO details (plan_ID, category, activity, points)
VALUES (1, 'Ernährung', 'Vollkornprodukte', 05);