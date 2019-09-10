import bleach
from datetime import datetime
from flask import Flask, Markup, render_template
from info import projects

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET'])
def main():
    return render_template('main.html', projects=projects)


@app.route("/cv", methods=['GET'])
def cv():
    return render_template('cv.html', projects=projects)


@app.route("/<id>/<project>", methods=['GET'])
def detail(project, id):
    return render_template('detail.html', project=projects[int(id)])


@app.template_filter('newline')
def _breakline(text):
    return Markup(text.replace('\n', '<br>'))


@app.template_filter('strftime')
def _filter_datetime(date):
    return datetime.strftime(date, '%x')


@app.template_filter('linkify')
def _filter_links(text):
    return bleach.linkify(text)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
