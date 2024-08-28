import os
from werkzeug.utils import secure_filename
def save_uploaded_file(upload_folder, file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)
    with open(filepath, "wb") as buffer:
        buffer.write(file.file.read())
    return filepath
