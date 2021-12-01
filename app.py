from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

fnamelist = [
    "Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
    "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah"
]
lnamelist = [
    "SMITH", "JOHNSON", "WILLIAMS", "JONES", "BROWN", "DAVIS", "MILLER", "WILSON", "MOORE", "TAYLOR",
    "ANDERSON", "THOMAS", "JACKSON", "WHITE", "HARRIS", "MARTIN", "THOMPSON", "GARCIA", "MARTINEZ", "ROBINSON"
]
emaillist = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com"]

def generate_email(name):
    symb = ["", ".", "-", "_"]
    e = random.randint(0,3)
    emailsymb = symb[random.randint(0,3)]
    domain = emaillist[e]
    temp = name.split(" ")
    email = temp[0] + emailsymb + temp[1] + "@" + domain
    return email

def generate_name():
    f = random.randint(0,19)
    l = random.randint(0,19)
    return (fnamelist[f] + " " + lnamelist[l]).lower()

def generate_password():
    pswd_chars = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
        "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-",
        "+", "=", "?", ".", ",", ">", "<", ";", ":"
    ]
    pswd = ""
    for x in range(0,12):
        r = random.randint(0,56)
        pswd += pswd_chars[r]

    return pswd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:num>/', methods=["GET"])
def generate_user(num):
    retjson = []
    for x in range(0, num):
        name = generate_name()
        email = generate_email(name)
        pswd = generate_password()
        j = {
            'name':name,
            'email':email,
            'password':pswd
        }
        retjson.append(j)
    return jsonify(retjson)

if __name__ == '__main__':
    app.run(debug=True)