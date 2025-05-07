# from flask import Flask, render_template, request, send_file
# import os
# from utils import (
#     convert_docx_to_pdf, convert_pdf_to_docx, extract_text_from_pdf,
#     extract_text_from_audio, extract_text_from_image, compress_pdf,
#     split_pdf, merge_pdfs, encrypt_pdf, pdf_to_image,
#     images_to_pdf, summarize_text, video_to_audio, audio_translation
# )
#
# app = Flask(__name__)
# UPLOAD_FOLDER = "uploads/"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # ==================== Conversion Features ====================
#
# @app.route('/convert', methods=['POST'])
# def convert():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#
#     if file.filename.endswith('.docx'):
#         output_path = file_path.replace('.docx', '.pdf')
#         convert_docx_to_pdf(file_path, output_path)
#     elif file.filename.endswith('.pdf'):
#         output_path = file_path.replace('.pdf', '.docx')
#         convert_pdf_to_docx(file_path, output_path)
#     else:
#         return "Unsupported file format"
#
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/pdf_to_image', methods=['POST'])
# def pdf_to_img():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_paths = pdf_to_image(file_path)
#     return render_template('index.html', split_files=output_paths)
#
# @app.route('/image_to_pdf', methods=['POST'])
# def img_to_pdf():
#     files = request.files.getlist('images')
#     output_path = os.path.join(UPLOAD_FOLDER, 'combined.pdf')
#     images_to_pdf(files, output_path)
#     return render_template('index.html', download_file='combined.pdf')
#
# # ==================== Text Extraction Features ====================
#
# @app.route('/extract_text', methods=['POST'])
# def extract_text():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#
#     if file.filename.endswith('.pdf'):
#         text_output = extract_text_from_pdf(file_path)
#     elif file.filename.endswith(('.jpg', '.jpeg', '.png')):
#         text_output = extract_text_from_image(file_path)
#     elif file.filename.endswith(('.wav', '.mp3', '.mp4')):
#         text_output = extract_text_from_audio(file_path)
#     else:
#         return "Unsupported file format"
#
#     return render_template('index.html', text_output=text_output)
#
# @app.route('/summarize_text', methods=['POST'])
# def summarize():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     summarized_text = summarize_text(file_path)
#     return render_template('index.html', text_output=summarized_text)
#
# # ==================== PDF Manipulation Features ====================
#
# @app.route('/pdf_compress', methods=['POST'])
# def pdf_compress():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_path = file_path.replace('.pdf', '_compressed.pdf')
#     compress_pdf(file_path, output_path)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/pdf_split', methods=['POST'])
# def pdf_split():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     split_files = split_pdf(file_path)
#     return render_template('index.html', split_files=split_files)
#
# @app.route('/pdf_merge', methods=['POST'])
# def pdf_merge():
#     files = request.files.getlist('files')
#     file_paths = [os.path.join(UPLOAD_FOLDER, file.filename) for file in files]
#     for file, path in zip(files, file_paths):
#         file.save(path)
#
#     output_path = os.path.join(UPLOAD_FOLDER, 'merged.pdf')
#     merge_pdfs(file_paths, output_path)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/pdf_encrypt', methods=['POST'])
# def pdf_encrypt():
#     file = request.files['file']
#     password = request.form['password']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_path = file_path.replace('.pdf', '_encrypted.pdf')
#     encrypt_pdf(file_path, output_path, password)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# # ==================== Audio & Video Features ====================
#
# @app.route('/video_to_audio', methods=['POST'])
# def video_audio():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_path = file_path.replace('.mp4', '.wav')
#     video_to_audio(file_path, output_path)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/audio_translate', methods=['POST'])
# def translate_audio():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     translated_text = audio_translation(file_path)
#     return render_template('index.html', text_output=translated_text)
#
# # ==================== File Download Feature ====================
#
# @app.route('/download/<filename>')
# def download(filename):
#     file_path = os.path.join(UPLOAD_FOLDER, filename)
#     return send_file(file_path, as_attachment=True)
#
# if __name__ == '__main__':
#     app.run(debug=True)

#################################################################################################################################

# from flask import Flask, render_template, request, send_file
# import os
# from utils import (
#     convert_docx_to_pdf, convert_pdf_to_docx, extract_text_from_pdf,
#     extract_text_from_audio, extract_text_from_image, compress_pdf,
#     split_pdf, merge_pdfs, encrypt_pdf, pdf_to_image,
#     images_to_pdf, summarize_text, video_to_audio, audio_translation
# )
#
# app = Flask(__name__)
# UPLOAD_FOLDER = "uploads/"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # ==================== Conversion Features ====================
#
# @app.route('/convert', methods=['POST'])
# def convert():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#
#     if file.filename.endswith('.docx'):
#         output_path = file_path.replace('.docx', '.pdf')
#         convert_docx_to_pdf(file_path, output_path)
#     elif file.filename.endswith('.pdf'):
#         output_path = file_path.replace('.pdf', '.docx')
#         convert_pdf_to_docx(file_path, output_path)
#     else:
#         return "Unsupported file format"
#
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/pdf_to_image', methods=['POST'])
# def pdf_to_img():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_paths = pdf_to_image(file_path)
#     return render_template('index.html', split_files=output_paths)
#
# @app.route('/image_to_pdf', methods=['POST'])
# def img_to_pdf():
#     files = request.files.getlist('images')
#     output_path = os.path.join(UPLOAD_FOLDER, 'combined.pdf')
#     images_to_pdf(files, output_path)
#     return render_template('index.html', download_file='combined.pdf')
#
# # ==================== Text Extraction Features ====================
#
# @app.route('/extract_text', methods=['POST'])
# def extract_text():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#
#     if file.filename.endswith('.pdf'):
#         text_output = extract_text_from_pdf(file_path)
#     elif file.filename.endswith(('.jpg', '.jpeg', '.png')):
#         text_output = extract_text_from_image(file_path)
#     elif file.filename.endswith(('.wav', '.mp3', '.mp4')):
#         text_output = extract_text_from_audio(file_path)
#     else:
#         return "Unsupported file format"
#
#     return render_template('index.html', text_output=text_output)
#
# @app.route('/summarize_text', methods=['POST'])
# def summarize():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     summarized_text = summarize_text(file_path)
#     return render_template('index.html', text_output=summarized_text)
#
# # ==================== PDF Manipulation Features ====================
#
# @app.route('/pdf_compress', methods=['POST'])
# def pdf_compress():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_path = file_path.replace('.pdf', '_compressed.pdf')
#     compress_pdf(file_path, output_path)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/pdf_split', methods=['POST'])
# def pdf_split():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     split_files = split_pdf(file_path)
#     return render_template('index.html', split_files=split_files)
#
# @app.route('/pdf_merge', methods=['POST'])
# def pdf_merge():
#     files = request.files.getlist('files')
#     file_paths = [os.path.join(UPLOAD_FOLDER, file.filename) for file in files]
#     for file, path in zip(files, file_paths):
#         file.save(path)
#
#     output_path = os.path.join(UPLOAD_FOLDER, 'merged.pdf')
#     merge_pdfs(file_paths, output_path)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/pdf_encrypt', methods=['POST'])
# def pdf_encrypt():
#     file = request.files['file']
#     password = request.form['password']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_path = file_path.replace('.pdf', '_encrypted.pdf')
#     encrypt_pdf(file_path, output_path, password)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# # ==================== Audio & Video Features ====================
#
# @app.route('/video_to_audio', methods=['POST'])
# def video_audio():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     output_path = file_path.replace('.mp4', '.wav')
#     video_to_audio(file_path, output_path)
#     return render_template('index.html', download_file=os.path.basename(output_path))
#
# @app.route('/audio_translate', methods=['POST'])
# def translate_audio():
#     file = request.files['file']
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     translated_text = audio_translation(file_path)
#     return render_template('index.html', text_output=translated_text)
#
# # ==================== File Download Feature ====================
#
# @app.route('/download/<filename>')
# def download(filename):
#     file_path = os.path.join(UPLOAD_FOLDER, filename)
#     return send_file(file_path, as_attachment=True)
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, send_file
import os
from utils import (
    convert_docx_to_pdf, convert_pdf_to_docx, extract_text_from_pdf,
    extract_text_from_audio, extract_text_from_image, compress_pdf,
    split_pdf, merge_pdfs, encrypt_pdf, pdf_to_image,
    images_to_pdf, summarize_text, video_to_audio, audio_translation
)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


# ==================== Conversion Features ====================

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    if file.filename.endswith('.docx'):
        output_path = file_path.replace('.docx', '.pdf')
        convert_docx_to_pdf(file_path, output_path)
    elif file.filename.endswith('.pdf'):
        output_path = file_path.replace('.pdf', '.docx')
        convert_pdf_to_docx(file_path, output_path)
    else:
        return "Unsupported file format"

    return render_template('index.html', download_file=os.path.basename(output_path))


@app.route('/pdf_to_image', methods=['POST'])
def pdf_to_img():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    output_paths = pdf_to_image(file_path)
    return render_template('index.html', split_files=output_paths)


@app.route('/image_to_pdf', methods=['POST'])
def img_to_pdf():
    files = request.files.getlist('images')
    file_paths = [os.path.join(UPLOAD_FOLDER, file.filename) for file in files]
    for file, path in zip(files, file_paths):
        file.save(path)

    output_path = os.path.join(UPLOAD_FOLDER, 'combined.pdf')
    images_to_pdf(file_paths, output_path)
    return render_template('index.html', download_file='combined.pdf')


# ==================== Text Extraction Features ====================

@app.route('/extract_text', methods=['POST'])
def extract_text():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    if file.filename.endswith('.pdf'):
        text_output = extract_text_from_pdf(file_path)
    elif file.filename.endswith(('.jpg', '.jpeg', '.png')):
        text_output = extract_text_from_image(file_path)
    elif file.filename.endswith(('.wav', '.mp3', '.mp4')):
        text_output = extract_text_from_audio(file_path)
    else:
        return "Unsupported file format"

    return render_template('index.html', text_output=text_output)


@app.route('/summarize_text', methods=['POST'])
def summarize():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    summarized_text = summarize_text(file_path)
    return render_template('index.html', text_output=summarized_text)


# ==================== PDF Manipulation Features ====================

@app.route('/pdf_compress', methods=['POST'])
def pdf_compress():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    output_path = file_path.replace('.pdf', '_compressed.pdf')
    compress_pdf(file_path, output_path)
    return render_template('index.html', download_file=os.path.basename(output_path))


@app.route('/pdf_split', methods=['POST'])
def pdf_split():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    split_files = split_pdf(file_path)
    return render_template('index.html', split_files=split_files)


@app.route('/pdf_merge', methods=['POST'])
def pdf_merge():
    files = request.files.getlist('files')
    file_paths = [os.path.join(UPLOAD_FOLDER, file.filename) for file in files]
    for file, path in zip(files, file_paths):
        file.save(path)

    output_path = os.path.join(UPLOAD_FOLDER, 'merged.pdf')
    merge_pdfs(file_paths, output_path)
    return render_template('index.html', download_file=os.path.basename(output_path))


@app.route('/pdf_encrypt', methods=['POST'])
def pdf_encrypt():
    file = request.files['file']
    password = request.form['password']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    output_path = file_path.replace('.pdf', '_encrypted.pdf')
    encrypt_pdf(file_path, output_path, password)
    return render_template('index.html', download_file=os.path.basename(output_path))


# ==================== Audio & Video Features ====================

@app.route('/video_to_audio', methods=['POST'])
def video_audio():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    output_path = file_path.replace('.mp4', '.wav')
    video_to_audio(file_path, output_path)
    return render_template('index.html', download_file=os.path.basename(output_path))


@app.route('/audio_translate', methods=['POST'])
def translate_audio():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    translated_text = audio_translation(file_path)
    return render_template('index.html', text_output=translated_text)


# ==================== File Download Feature ====================

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
