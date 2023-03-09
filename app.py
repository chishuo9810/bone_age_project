from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = r'C:\Users\chish\OneDrive\桌面\專題\HTML\static' # 設定上傳的資料夾路徑
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif']) # 允許的檔案格式

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/boneAgePredict.html', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 檢查是否有上傳檔案
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # 如果使用者沒有選擇檔案，則會file.filename為空字串
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # 如果檔案是允許的檔案格式，則將檔案存儲到指定的文件夾中
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully')
            return redirect(url_for('upload_file'))
    return render_template('boneagewebsite.html')
@app.route('/', methods=['GET', 'POST'])
def front_page():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
