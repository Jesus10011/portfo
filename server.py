from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")  # Reduce code by making it dynamic
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data): # .txt database
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data): # .csv database
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() # Convert form's data into a dictionary
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


# @app.route("/index.html")
# def my_index():
#     return render_template('index.html')

# @app.route("/works.html")
# def my_works():
#     return render_template('works.html')

# # In the case of repeated routes, only the first will show
# @app.route("/about.html")
# def about_me():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact_me():
#     return render_template('contact.html')
