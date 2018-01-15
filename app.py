from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/dt2556', methods=['GET'])
def dorrie():
    return render_template('dorrie.html')


if __name__ == '__main__':
    app.run()
