from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	template = "index.html"
	return render_template(template)


# IF this script is run from command line
if __name__ == "__main__":
	# first up the Flask test sever
	app.run(debug=True, use_reloader=True)

