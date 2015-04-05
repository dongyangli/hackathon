import os
from flask import Flask, render_template
from flask import request
import CreateCsvTable
from CreateCsvTable import createTable

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
	paragraph = []

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
		files = []
		if selectmultipleSecurity and selectmultipleField and startDate and endDate and radios:
			files = createTable(selectmultipleSecurity, selectmultipleField, startDate, endDate, radios)

		return render_template("test.html", title = title, paragraph=paragraph, files = files)
	except Exception, e:
		return str(e)


@app.route('/download', methods=['POST', 'GET'])
def download():
	filename = request.form.get("button")
	csv = ""
	with open(filename, 'r') as content_file:
		contents = content_file.readlines()
		for line in contents:
			csv += str(line)
	return csv

# launch
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
