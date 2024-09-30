from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
OWN_EMAIL = "pytest213@gmail.com"
OWN_PASSWORD = "gigx mrzc ezip zqbc"
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone =request.form["phone"]
        message = request.form["message"]
        email_message = f"Subject:New Form\n\nName : {name}\neMail : {email}\nTelephone Number : {phone}\nMessage : \n{message}\n"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
            connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_EMAIL,
                                msg=email_message)
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
