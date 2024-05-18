from flask import Flask, request, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
  if 'image' not in request.files:
    return "No image uploaded", 400

  image_file = request.files['image']
  if image_file.filename == "":
    return "No selected image", 400

  if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

  image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename))
  return f"Image uploaded successfully: {image_file.filename}"

@app.route('/download/<image_name>')
def download_image(image_name):

  if not os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], image_name)):
    return "Image not found", 404


  return send_file(os.path.join(app.config['UPLOAD_FOLDER'], image_name), as_attachment=True), 200

if __name__ == '__main__':
  app.run(debug=True)
