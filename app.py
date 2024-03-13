from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data to store expenses
expenses = []

@app.route('/')
def index():
    total_spent = sum(expense['amount'] for expense in expenses)
    return render_template('index.html', expenses=expenses, total_spent=total_spent)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        expenses.append({'description': description, 'amount': amount})
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
