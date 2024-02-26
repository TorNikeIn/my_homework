from flask import Flask, render_template
import webbrowser
import threading
from models import CardData

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/posts")
def posts():
    craft_1 = CardData("Flowers and Girl", "Digital Painting", "Digital", "https://cdn.pixabay.com/photo/2015/11/03/10/23/watercolor-1020509_1280.jpg")
    craft_2 = CardData("Road Signs", "Digital Painting", "Digital", "https://cdn.pixabay.com/photo/2020/10/14/18/35/sign-post-5655110_1280.png")
    craft_3 = CardData("Fish", "Poster of Fish", "Digital", "https://cdn.pixabay.com/photo/2013/10/25/20/46/mosaic-200864_1280.jpg")
    craft_4 = CardData("Raindeer", "Poster of Deer", "Digital", "https://cdn.pixabay.com/photo/2018/03/30/15/11/deer-3275594_1280.jpg")
    craft_list = [craft_1, craft_2, craft_3, craft_4]
    return render_template("posts.html", craft_list=craft_list)

def open_browser():
    webbrowser.open(f"http://localhost:5000")

if __name__ == "__main__":
    threading.Timer(1.25, open_browser).start()  # Waits for 1.25 seconds before opening the browser
    app.run(port=5000, debug=True)
