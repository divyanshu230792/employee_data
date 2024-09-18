from flask import Flask,render_template,jsonify,request
from utils import load_dataset,Emp_Data
import config as cfg
app=Flask(__name__)
@app.route('/Gender_opt')
def Gender_opt():
    df=load_dataset()
    return jsonify(list(df['Gender'].unique()))

@app.route('/Position_opt')
def Position_opt():
    df=load_dataset()
    return jsonify(list(df['Position'].unique()))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    data=request.form
    Gender=data['Gender']
    Experience=data['Experience']
    Position=data['Position']

    sall_pred=Emp_Data()
    salary_prediction=sall_pred.Sal_prediction(Gender,Experience,Position)
    print(f'predictd sal of emp:{salary_prediction}')
    return jsonify({'pred slry':salary_prediction})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=cfg.FLASK_PORT_NO)
