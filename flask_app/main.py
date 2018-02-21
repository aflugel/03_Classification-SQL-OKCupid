from flask import Flask, request, render_template
from py_sports_fan import fan_or_not

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_sportfan/', methods=['GET', 'POST'])
def render_message():

    # user-entered answers
    questions = ['q17', 'q55', 'q56', 'q57', 'q65', 'q70', 'q71', 'q87', 'q105', 'q114',
       'q123', 'q134', 'q136', 'q175', 'q210', 'q219', 'q301', 'q308', 'q325',
       'q341', 'q393', 'q403', 'q501', 'q527', 'q553', 'q784', 'q838', 'q1112',
       'q1119', 'q1440', 'q1454', 'q1597', 'q1815', 'q4018', 'q5417', 'q6258',
       'q6867', 'q8054', 'q12964', 'q14913', 'q15280', 'q16713', 'q19075',
       'q20418', 'q20530', 'q23834', 'q24125', 'q25228', 'q27477', 'q44639',
       'q48372', 'q60100', 'q60852', 'q61786', 'q80041', 'q156913', 'q156914',
       'q179268', 'q313640', 'q358014', 'q358077', 'q358084', 'q158', 'q1766',
       'q18594', 'q27164', 'q34094']

    # hold all amounts as floats
    answers = []

    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(questions):
        user_input = request.form[ing]
        answers.append(user_input)

    # show user final message
    final_message = fan_or_not(answers)
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) #port='8080')