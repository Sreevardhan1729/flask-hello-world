from flask import Flask, request, jsonify
from flask_cors import cross_origin
from model import load_model
from pdf_utils import pdf_to_text
from preprocess import preprocess
app = Flask(__name__)



model_path = "./model"
model = load_model(model_path=model_path)

@app.route('/compare', methods=['POST'])
@cross_origin()
def compare():
    job_desc = request.form.get('job_description','')
    
    resume_file = request.files.get('resume')
    if resume_file:
        resume_text = pdf_to_text(resume_file=resume_file)
    else:
        return jsonify({"error": "Resume Required is required"}), 400
    if not job_desc:
        return jsonify({"error": "Job description text is required"}), 400
    
    resume = preprocess(model,resume_text)
    job = preprocess(model, job_desc)
    jobskills = list(set(job.get("SKILLS", [])))
    resumeskills = list(set(resume.get("SKILLS", [])))
    common = []
    noncommon = []
    for i in jobskills:
        if(i in resumeskills):
            common.append(i)
        else:
            noncommon.append(i)
    return jsonify([common,noncommon])


@app.route('/jobdetails',methods=['POST'])
@cross_origin()
def jobDetails():
    job_desc = request.form.get('job_description','')
    job = preprocess(model,job_desc)
    exp = ["EXPERIENCE","experience","Experience"]
    jobdetails = {key: sorted(list(value)) if isinstance(value, set) else value for key, value in job.items() if key not in exp}
    return jsonify(jobdetails)


if __name__ == '__main__':
    app.run(debug=True)