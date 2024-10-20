from flask import Flask, render_template

app = Flask(__name__)

# Route for the intro page
@app.route('/')
def intro():
    return render_template('intro.html')

# Route for the main celebration page
@app.route('/celebrate')
def celebrate():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
