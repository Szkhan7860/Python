from flask import Flask, render_template, request
import sys
from io import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    code = ""
    if request.method == 'POST':
        code = request.form['code']
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        try:
            exec(code)
            output = redirected_output.getvalue()
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = old_stdout
    return render_template('index.html', code=code, output=output)

if __name__ == '__main__':
    app.run(debug=True)
  
