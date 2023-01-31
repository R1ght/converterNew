from flask import Flask, render_template, request, Response, render_template
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/jpgtopng", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")

@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png():
    image = request.files['image']
    if not image:
        return "Please upload an image", 400
    if 'image/jpeg' not in image.content_type:
        return "File is not a JPEG image", 400
    try:
        # Open image and convert it to PNG
        img = Image.open(image)
        img = img.convert('RGB')
        png_img = BytesIO()
        img.save(png_img, format='PNG')
        png_img.seek(0)
    except Exception as e:
        return str(e), 500
    # Create response object with PNG image as attachment
    response = Response(png_img, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    return response

@app.route("/pngtojpg", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")

@app.route('/api/pngtojpg', methods=['POST'])
def png_to_jpg():
    image = request.files['image']
    if not image:
        return "Please upload an image", 400
    if 'image/png' not in image.content_type:
        return "File is not a PNG image", 400
    try:
        # Open image and convert it to JPG
        img = Image.open(image)
        jpg_img = img.convert('RGB')
        byte_io = BytesIO()
        jpg_img.save(byte_io, format='JPEG')
        byte_io.seek(0)
    except Exception as e:
        return str(e), 500
    # Create response object with JPG image as attachment
    response = Response(byte_io, content_type='image/jpg')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.jpg')
    return response


@app.route("/webptopng", methods=["GET"])
def webtopng():
    return render_template("webptopng.html")

@app.route('/api/webptopng', methods=['POST'])
def webp_to_png():
    image = request.files['image']
    if not image:
        return "Please upload an image", 400
    if 'image/webp' not in image.content_type:
        return "File is not a WEBP image", 400
    try:
        # Open image and convert it to PNG
        img = Image.open(image)
        png_img = BytesIO()
        img.save(png_img, format='PNG')
        png_img.seek(0)
    except Exception as e:
        return str(e), 500
    # Create response object with PNG image as attachment
    response = Response(png_img, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    return response

@app.route("/bmptopng", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")

@app.route('/api/bmptopng', methods=['POST'])
def bmp_to_png():
    image = request.files['image']
    if not image:
        return "Please upload an image", 400
    if 'image/bmp' not in image.content_type:
        return "File is not a BMP image", 400
    try:
        # Open image and convert it to PNG
        img = Image.open(image)
        png_img = BytesIO()
        img.save(png_img, format='PNG')
        png_img.seek(0)
    except Exception as e:
        return str(e), 500
    # Create response object with PNG image as attachment
    response = Response(png_img, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    return response

@app.route("/pngtopdf", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")

@app.route('/api/pngtopdf', methods=['POST'])
def png_to_pdf():
    image = request.files['image']
    if not image:
        return "Please upload an image", 400
    if 'image/png' not in image.content_type:
        return "File is not a PNG image", 400
    try:
        # Open image and convert it to PDF
        img = Image.open(image)
        pdf_img = img.convert('RGB')
        byte_io = BytesIO()
        pdf_img.save(byte_io, format='PDF')
        byte_io.seek(0)
    except Exception as e:
        return str(e), 500
    # Create response object with PDF image as attachment
    response = Response(byte_io, content_type='application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.pdf')
    return response


@app.route("/tifftopdf", methods=["GET"])
def tifftopdf():
    return render_template("tifftopdf.html")

@app.route('/api/tifftopdf', methods=['POST'])
def tiff_to_pdf():
    image = request.files['image']
    if not image:
        return "Please upload an image", 400
    if 'image/tiff' not in image.content_type:
        return "File is not a TIFF image", 400
    try:
        # Open image and convert it to PDF
        img = Image.open(image)
        pdf_buffer = BytesIO()
        img.save(pdf_buffer, format='PDF')
    except Exception as e:
        return str(e), 500
    pdf_buffer.seek(0)
    # Create response object with PDF image as attachment
    response = Response(pdf_buffer.read())
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == "__main__":
    app.run(debug=True)
    #app.run()