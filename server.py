from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    val1 = int(request.form['strawberry'])
    val2 = int(request.form['raspberry'])
    val3 = int(request.form['apple'])
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    valTotal = val1 + val2 + val3
    return render_template("checkout.html", val1=val1, val2=val2, val3= val3, valTotal=valTotal, firstName=firstName, lastName=lastName, studentId=studentId, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    