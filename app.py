from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/prep.html/<string:file_name>')
def library(file_name):
    return render_template(file_name+'.html')


if __name__ == '__main__':
    app.run(debug=True,port=5000)
