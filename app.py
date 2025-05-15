from flask import Flask, render_template
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')

def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg','.arw'))

@app.route('/')
def slideshow():
    try:
        all_files = os.listdir(IMAGE_FOLDER)
        images = [f for f in all_files if is_image_file(f)]
        
        # Optional: limit number of images shown
        # images = images[:100]

        full_paths = [os.path.join(IMAGE_FOLDER, img).replace("\\", "/") for img in images]
        
        print(f"✅ Found {len(full_paths)} images:")
        print(full_paths[:5])  # Print first 5 to verify
        
        return render_template('index.html', images=full_paths)
    except Exception as e:
        print("❌ Error reading image folder:", str(e))
        return "Error loading images", 500

if __name__ == '__main__':
    app.run(debug=True)