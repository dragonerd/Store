from flask import Flask, render_template
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
  webbrowser.open_new_tab('http://127.0.0.1:5000')
  app.run(debug=True)