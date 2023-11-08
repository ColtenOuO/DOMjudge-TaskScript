import os
from flask import Flask,render_template,request
UPLOAD_FOLDER='uploads'

app = Flask (__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
@app.route("/")
def ooof():
    return render_template('index2.html')


@app.route('/upload', methods=['POST'])
def upload():
    memory_limit = request.form['memoryLimit']
    time_limit = request.form['timeLimit']

    # 處理文件上傳，你可以使用 request.files 來訪問上傳的文件
    test_data_file = request.files['testdata']
    testname = "test_data.zip"
    description_file = request.files['description']
    #desname = description_file.filename
    desname = "statement.pdf"
    test_data_file.save(os.path.join(app.config['UPLOAD_FOLDER'],testname))
    description_file.save(os.path.join(app.config['UPLOAD_FOLDER'],desname))
    # 在這裡你可以進一步處理上傳的文件，例如保存到特定位置

  #  os.system("unzip ./uploads/test_data.zip")
  #  os.system("mkdir ./problem_package")
  #  os.system("mkdir ./problem_package/secret")
  #  os.system("mv ./uploads/statement.pdf .")
    

    return '上傳成功！'

if __name__ == '__main__':
    app.run(debug=True)
