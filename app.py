from app import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to hold todo items (in-memory, for demo purposes)
todos = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form['todo']
    if todo_item:
        todos.append(todo_item)
    return redirect(url_for('dashboard'))

@app.route('/delete_todo/<int:index>', methods=['GET'])
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
