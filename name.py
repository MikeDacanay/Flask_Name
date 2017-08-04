from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
	name=request.form['name']
	print name
	return redirect('/')
app.run(debug=True)