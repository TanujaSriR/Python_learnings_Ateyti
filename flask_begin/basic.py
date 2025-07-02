from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <h2>Enter your name:</h2>
        <form method="post" action="/greet">
            <input type="text" name="name" placeholder="Your Name" required>
            <button type="submit">Greet Me</button>
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return f'<h2>Hello, {name}!</h2><a href="/">Go back</a>'

if __name__ == '__main__':
    app.run(debug=True)
