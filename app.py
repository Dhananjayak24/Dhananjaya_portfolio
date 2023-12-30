from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html', particulars=PARTICULARS)


PARTICULARS = [{
    'title': 'EDUCATION',
    'img': 'static/qualification.jpg',
    'line_1': 'MSc Bioinformatics',
    'line_2': '2022 - 2024',
    'line_3': 'BSc Fisheries Science',
    'line_4': '2016 - 2020'
}, {
    'title': 'EXPERIENCE',
    'img': 'static/experience.jpg',
    'line_1': 'Quality Control Technologist',
    'line_2': '2020 - 2022',
    'line_3': 'Blueline Foods India Pvt Ltd'
}, {
    'title': 'PROJECTS',
    'img': 'static/projects.jpg',
    'line_1': 'Dynamic Web Development with Python and CSS',
    'line_2': 'Binary Classification of Breast cancer data using ML',
    'line_3': 'Web Scraping using Python',
    'line_4': 'Linux programming'
}, {
    'title': 'SKILLS',
    'img': 'static/skills.jpg',
    'line_1': 'Python, html, CSS, MySQL, NoSQL',
    'line_2': 'Git, Github, Replit, R Programming',
    'line_3': 'Linux, Perl, Seaborn, Matplotlib, Pandas'
}, {
    'title': 'HOBBIES',
    'img': 'static/hobbies.jpg',
    'line_1': 'Solo Travelling, Reading, Short-film Making',
    'line_2': 'Breeding fishes, Aquascaping'
}, {
    'title': 'SOCIAL PRESENCE',
    'img': 'static/social_presence.jpg',
    'line_1': 'LinkedIn',
    'line_2': 'Github'
}]


@app.route("/api/particulars")
def list_particulars():
  return jsonify(PARTICULARS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
