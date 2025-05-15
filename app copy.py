from flask import Flask, render_template
import os

app = Flask(__name__)

# Path to your images folder
IMAGE_FOLDER = os.path.join('static', 'images')

@app.route('/')
def slideshow():
    # Get list of images (500+)
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.jpg', '.png', '.jpeg'))]
    images = [os.path.join(IMAGE_FOLDER, img) for img in images]  # Full path
    print(images)
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)