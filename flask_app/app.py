from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()

        if not name:
            error = "Name is required."
        elif len(name) < 2:
            error = "Name must be at least 2 characters long."
        elif not name.isalpha():
            error = "Name must contain only alphabetic characters."
        elif not age:
            error = "Age is required."
        elif not age.isdigit():
            error = "Age must be a number."
        else:
            return render_template('form.html', name=name, age=age)

    return render_template('form.html', error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)