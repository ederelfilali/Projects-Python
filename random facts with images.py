import random
import requests
from PIL import Image, ImageTk
import tkinter as tk


sports_facts = [
    {
        "fact": "The fastest recorded tennis serve was 163.7 mph (263.4 km/h), achieved by Samuel Groth.",
        "image_url": "https://images.squarespace-cdn.com/content/v1/5a97763275f9eeee0b6f77f0/c22b88d1-1ca5-4306-b7c4-cf0ab6b3855f/How+To+Add+More+Power+To+Your+Tennis+Serve.jpg"
    },
    {
        "fact": "Michael Phelps holds the record for the most Olympic medals, with a total of 28 medals.",
        "image_url": "https://image-cdn.essentiallysports.com/wp-content/uploads/Michael-Phelps-FI-3.jpeg"
    },
    {
        "fact": "The highest-scoring NBA game in history occurred on December 13, 1983, with the Detroit Pistons defeating the Denver Nuggets 186-184 in triple-overtime.",
        "image_url": "https://static.owayo-cdn.com/newhp/img/magazin/basketballdunkEN/practice-regimen-perfect-slam-dunk-670px.jpg"
    },
]



def fetch_image(image_url):
    response = requests.get(image_url, stream=True)
    response.raise_for_status()
    image = Image.open(response.raw)
    return image


def generate_random_fact():
    fact = random.choice(sports_facts)
    image_url = fact["image_url"]
    image = fetch_image(image_url)
    return fact["fact"], image


window = tk.Tk()


canvas = tk.Canvas(window, width=1280, height=720)
canvas.pack()
def display_random_fact():
    canvas.delete("all")

    random_fact, random_image = generate_random_fact()

    resized_image = random_image.resize((1280, 720))
    tk_image = ImageTk.PhotoImage(resized_image)
    #canvas.config(width=resized_image.width, height=resized_image.height) (just a test !)
    canvas.image = tk_image

    canvas.create_image(resized_image.width/2, resized_image.height/2, image=tk_image)
    canvas.create_text(resized_image.width/2, resized_image.height+20, text=random_fact, font=("Arial", 14), width=300, anchor="s")


display_random_fact()

button = tk.Button(window, text="Generate New Fact", command=display_random_fact)
button.pack()

window.mainloop()