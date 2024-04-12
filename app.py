from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/give')
def give():
    return render_template('give.html')

@app.route('/field')
def field():
    return render_template('field.html')

@app.errorhandler(404)
def error(e):
    return render_template('error.html'),404

if __name__ == '__main__':
    app.run(debug=True)