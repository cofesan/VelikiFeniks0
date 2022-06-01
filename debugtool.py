from flask import Flask
app = Flask(__name__)
@app.route('/')
def debug(debug=True):
     while True:
          return 'Debug tool for arcane by velikiFeniks'
     
if __name__ == '__main__':
     app.run(debug=True, port=80, host='0.0.0.0')
