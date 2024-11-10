from flask import Flask, redirect, render_template, url_for, request, redirect
app = Flask(__name__)
import csv


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'something went wrong.  Try again!'