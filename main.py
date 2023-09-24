# to-dos:
# DONT DO LATE :DDDD
# ADD GIF FOR EACH OF MY PROJECTS
# REALLY MAKE A BETTER DESIGN WILL ASK RAFA
# Option to download a resume or CV
# ADD IMAGES AND BETTER STYLE OF THE HUB
# CHANGE THE HOME PAGE TO ONLY SHOW STUFF ABT ME AND THEN THE MENU ON TOP WILL TAKE U TO DIFFERENT PARTS
# PROFESSOR JUST RECOMMENDED TO ADD A CONTACT FORM CODE I WILL ADD THIS TONITE AND DONT SLEEP (Again....)

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/')
def home():
    return render_template('index.html', resume=resume)


if __name__ == '__main__':
    resume = {
        "name": "Mario A Pinzon C.",
        "email": "tvpower89@hotmail.com",
        "phone": "510-205-2572",
        "linkedin": "https://www.linkedin.com/in/mario-pinzon-86b3411b7/",
        "github": "https://github.com/tvpower89",

    }
    app.run()
