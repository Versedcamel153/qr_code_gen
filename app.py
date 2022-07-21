from flask import Flask, render_template, request, send_file
import base64
import qrcode
from PIL import Image

app = Flask(__name__)
def create_qr():
    if request.method == 'POST':
        raw = request.form['raw_data']
       
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size= 2,
            border=2
        )
        data = qr.add_data(raw)
        img = qr.make_image(data)
        img.save('static/img.png')
  
    return "ok"


@app.route('/', methods=('GET', 'POST'))
def index():
    name = create_qr()
    return render_template("index.html", name=name)

@app.route('/download')
def download():
    path = "static/img.png"
    save = send_file(path, as_attachment= True)
    return save

if __name__ == "__main__":
    app.run()
