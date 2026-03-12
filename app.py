from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# -----------------------------
# GET CAREERS FROM DATABASE
# -----------------------------
def get_careers():

    conn = sqlite3.connect("careers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM careers")

    careers = cursor.fetchall()

    conn.close()

    return careers


# -----------------------------
# AI MATCH CALCULATION
# -----------------------------
def calculate_match(user_skills, user_interests):

    careers = get_careers()

    results = []

    # set prevents duplicate careers
    added_careers = set()

    for career in careers:

        name = career[1]
        skills = career[2].split(",")

        score = 0

        # check skill match
        for skill in user_skills:
            if skill.strip().lower() in skills:
                score += 30

        # check interest match
        for interest in user_interests:
            if interest.strip().lower() in skills:
                score += 20

        # limit score
        if score > 100:
            score = 100

        # add result only if:
        # 1) score > 0
        # 2) career not already added
        if score > 0 and name not in added_careers:

            results.append({
                "career": name,
                "score": score,
                "course": career[3],
                "link": career[4],
                "skills_needed": ", ".join(skills)
            })

            added_careers.add(name)

    # sort by score
    results.sort(key=lambda x: x["score"], reverse=True)

    # show only top careers (clean UI)
    return results[:8]


# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():

    return render_template("index.html")


# -----------------------------
# RECOMMENDATION PAGE
# -----------------------------
@app.route("/recommend", methods=["POST"])
def recommend():

    grade = request.form["grade"]

    skills = request.form["skills"].lower().split(",")

    interests = request.form["interests"].lower().split(",")

    results = calculate_match(skills, interests)

    return render_template("result.html", results=results, grade=grade)


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":

    app.run(debug=True)