import os
from flask import render_template, request
from . import app
import logging

# ---------------------------------------------------
# Setup local logger (to avoid circular import)
# ---------------------------------------------------
logger = logging.getLogger("views")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# ---------------------------------------------------
# Routes
# ---------------------------------------------------
@app.route('/')
def index():
    logger.info("Index page accessed.")
    return render_template('index.html')


@app.route('/about')
def about():
    logger.info("About page accessed.")
    return render_template('about.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')

        if file:
            logger.info(f"File uploaded: {file.filename}")

            # Save file temporarily (optional)
            filepath = os.path.join("/tmp", file.filename)
            file.save(filepath)

            return f"File {file.filename} uploaded successfully!"

        logger.warning("Upload attempted with no file.")
        return "No file selected."

    return render_template('upload.html')
