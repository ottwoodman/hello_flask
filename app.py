import os

from flask import Flask


def create_app():
    return Flask(__name__)


app = create_app()


# 測試
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello Flask!'
  

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


