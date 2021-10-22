from flask import Flask, render_template
from flask_bootstrap import Bootstrap
 
app = Flask(__name__)
bootstrap = Bootstrap(app)
 
 
@app.route('/user/<name>')
def user(name):
  return render_template('mon.html', name=name)
 
 
if __name__ == '__main__':
  app.run()