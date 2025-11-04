from flask import Flask, render_template, render_template_string, send_from_directory
import os

app = Flask(__name__)

goob_fold = r"D:\gon_host\images" #insert your path to the images here

images = {'.png', '.jpg', '.jpeg', '.webp'}

video = {'.webm', '.gif', '.mp4', '.avi', '.mov', '.mkv'}

@app.route('/')

def index(): 
    return render_template('index.html')

@app.route('/images')
def show_images():
    files = [f for f in os.listdir(goob_fold)if os.path.splitext(f)[1].lower() in images]
    return render_template('image.html', files=files)

@app.route('/videos')
def show_videos():
    files = [f for f in os.listdir(goob_fold) if os.path.splitext(f)[1].lower() in video]
    return render_template('video.html', files=files)

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(goob_fold, filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
