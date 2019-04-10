import json
from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('example-jobs.json') as f:
    job_list = json.loads(f.read())

@app.route('/')
def jobs():
    return render_template('jobs.html', job_list=job_list)

app.run()
