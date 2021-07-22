from flask_mail import Message
from flask import render_template
from app import mail
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)

# sender_email = '.....@gmail.com'
subject_pref = 'Title:'
sender_email = 'jumaallanie@gmail.com'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jumaallanie@gmail.com'
app.config['MAIL_PASSWORD'] = 'ajaylee254'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

def mail_message(subject,template,to,**kwargs):
    # sender_email = 'jumaallanie@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    # email.html = render_template(template + ".html",**kwargs)
    mail.send(email)



if __name__ == '__main__':
    app.run()