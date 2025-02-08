from flask import Flask,request,render_template
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['post'])
def predict():
        cgpa = float(request.form.get('cgpa'))
        ssc = float(request.form.get('ssc'))
        hsc = float(request.form.get('hsc'))
        internship = int(request.form.get('internship'))
        project = int(request.form.get('projects'))
        workshop = int(request.form.get('workshop'))
        aptitude = float(request.form.get('aptitude'))
        softskills = float(request.form.get('softskills'))
        extra = 1 if request.form.get('extra') == "yes" else 0
        training = 1 if request.form.get('training') == "yes" else 0 

        total=model.predict([[cgpa,internship,project,workshop,aptitude,softskills,extra,training,ssc,hsc]])

        if (total[0]==1.0):
             total="You will be Placed"
             return render_template('placed.html', result=total)
        else:
             total="You will Not be Placed"
             return render_template('not_placed.html', result=total)
       



if __name__ =='__main__':
    app.run(debug=True)