from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from tasks import add

app = Flask(__name__)

#업로드 HTML 렌더링
@app.route('/')
def home_page():
   return render_template('index.html')

#파일 업로드 처리
@app.route('/celery_test')
def celery_test():
   add.delay(100, 101)
   return "The celery was ran on background"

if __name__ == '__main__':
    #서버 실행
   app.run(host='0.0.0.0', debug = True)
