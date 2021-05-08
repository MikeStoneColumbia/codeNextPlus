from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buttonPressed/<btn>')
def press(btn):
    print('button ' + str(btn) + ' was pressed')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1')