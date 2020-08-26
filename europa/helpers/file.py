from werkzeug.utils import secure_filename
import uuid
import os

ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(request):
    file = request.files['stream_audio']
    if file.filename == '':
        return None
    if file and allowed_file(file.filename):
        file.filename = str(uuid.uuid1()) + ".wav"
        filename = secure_filename(file.filename)
        file.save(filename)
        #TODO: save file to temp folder
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return True