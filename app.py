from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lagos',
    'salary': 'N550,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Abuja',
    'salary': 'N600,000'
  },
  {
    'id': 6,
    'title': 'Frontend Engineer',
    'location': 'Portharcourt',
    
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Calabar',
    'salary': 'N1,220,000'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)