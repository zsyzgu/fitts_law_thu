from flask import Flask

app = Flask(__name__,static_url_path='') 

@app.route('/') 
def home(): 
      return app.send_static_file('Fitts.html')

if __name__ == '__main__':
      app.run(host = '0.0.0.0', port = 3838)
