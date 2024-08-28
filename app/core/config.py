import os

UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'static/output/'

# Ensure folders exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
