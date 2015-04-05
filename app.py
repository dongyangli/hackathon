import os
from flask import Flask, render_template
from flask import request

# initialization
app = Flask(__name__)
app.config.update(
	DEBUG = True,
)

# controllers
@app.route("/about", methods=['POST', 'GET'])
def about():

	title = "About Us"
	paragraph = ["Hi, have fun!", "goodbye"]
		
	try:
		return render_template("about.html", title = title, paragraph=paragraph)
	except Exception, e:
		return str(e)

@app.route('/', methods=['POST', 'GET'])
def homepage():

	title = "display input result"
	paragraph = ["so for nothing"]

	selectmultipleSecurity = request.form.getlist("selectmultipleSecurity")
	if selectmultipleSecurity:
		for security in selectmultipleSecurity:
			paragraph.append(security)

	selectmultipleField = request.form.getlist("selectmultipleField")
	if selectmultipleField:
		for field in selectmultipleField:
			paragraph.append(field)

	startDate = request.form.get("startDate")
	if startDate:
		paragraph.append(startDate)

	endDate = request.form.get("endDate")
	if endDate:
		paragraph.append(endDate)

	radios = request.form.get("radios")
	if radios:
		paragraph.append(radios)

	try:
		return render_template("test.html", title = title, paragraph=paragraph)
	except Exception, e:
		return str(e)
# launch
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
