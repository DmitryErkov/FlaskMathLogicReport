from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def math_logic_report():
    return render_template('math_logic_report.html')


if __name__ == '__main__':
    app.run()