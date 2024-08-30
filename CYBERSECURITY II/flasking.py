from flask import Flask, render_template, request
import os

# Define o caminho para o diretório 'my_templates' dentro da pasta 'CYBERSECURITY II'
template_dir = os.path.join(os.path.dirname(__file__), 'my_templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('xss.html')

@app.route('/about-me', methods=['GET', 'POST'])
def about_me():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('xss_input', '')
    return render_template('about_me.html', user_input=user_input)

@app.route('/login', methods=['GET', 'POST'])
def about_me():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('username', '')
    return render_template('login.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
