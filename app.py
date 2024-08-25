from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store (could be replaced with a database)
expenses = []

# Home Page - Display all expenses
@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

# Add Expense Page
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        expenses.append({'description': description, 'amount': amount, 'category': category})
        return redirect(url_for('index'))
    return render_template('add_expense.html')

# Edit Expense Page
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_expense(index):
    if request.method == 'POST':
        expenses[index]['description'] = request.form['description']
        expenses[index]['amount'] = float(request.form['amount'])
        expenses[index]['category'] = request.form['category']
        return redirect(url_for('index'))
    return render_template('edit_expense.html', expense=expenses[index], index=index)

# Delete Expense
@app.route('/delete/<int:index>')
def delete_expense(index):
    del expenses[index]
    return redirect(url_for('index'))

# View Expense Page
@app.route('/view/<int:index>')
def view_expense(index):
    return render_template('view_expenses.html', expense=expenses[index])

if __name__ == '__main__':
    app.run(debug=True)
