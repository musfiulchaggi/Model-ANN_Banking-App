from flask import Flask, request, jsonify
import sys
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
import numpy as np

X_train_new = pd.read_csv('X_train.csv')
sc = MinMaxScaler()
sc = sc.fit(X_train_new)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        CreditScore = int(request.form.get('CreditScore'))
        Tenure = int(request.form.get('Tenure'))
        NumOfProducts = int(request.form.get('NumOfProducts'))
        Age_category = int(request.form.get('Age'))
        New_Estimated_Salary = float(request.form.get('Estimated_Salary'))
        Gender = request.form.get('Gender')
        if Gender.strip():
            if Gender == 'male':
                Gender_Female = 0
                Gender_Male = 1 
            elif Gender == 'female':
                Gender_Female = 1
                Gender_Male = 0
        else:
            return jsonify({'Error': ["There's No valid input in line."]})
        data = {
            'CreditScore': [CreditScore],
            'Age': [Age_category],
            'Tenure': [Tenure],
            'NumOfProducts': [NumOfProducts],
            'New_Estimated_Salary': [New_Estimated_Salary],
            'Gender_Female': [Gender_Female],
            'Gender_Male': [Gender_Male],
        }
        
        data = pd.DataFrame(data)
        
#       Scaling Data
        datascaled =sc.transform(data)

        classifier = joblib.load('classifier_dipakai.pkl')
        prediction = classifier.predict([datascaled])
        
        Prediction_input = 'Lancar'
        prediksi = 1
        
        if(prediction[0][0] < 0.5):
            prediksi = 0
            Prediction_input = 'Tidak Lancar'
        
        Confident_input = prediction[0][0]
        
        #         Membaca data dari file CSV ke dalam DataFrame
        df = pd.read_csv('HistReqsApi.csv')

#         Membuat dictionary dengan data baru yang akan ditambahkan
        new_data = {
            'CreditScore': [CreditScore],
            'Age_category': [Age_category],
            'Tenure': [Tenure],
            'NumOfProducts': [NumOfProducts],
            'New_Estimated_Salary': [New_Estimated_Salary],
            'Gender_Female': [Gender_Female],
            'Gender_Male': [Gender_Male],
            'Prediction' : [Prediction_input],
            'Confident' : [Confident_input]
        }

#         Menambahkan data baru ke dalam DataFrame
        new_df = pd.concat([df, pd.DataFrame(new_data)])

#         Menampilkan DataFrame setelah penambahan data
        print("\nDataFrame Setelah Penambahan Data:")
        print(new_df)

#         Menyimpan DataFrame ke dalam file CSV
        new_df.to_csv('HistReqsApi.csv', index=False)

        
        return jsonify({'success':200,'status': prediksi,'confidence':str(prediction[0][0])})
    except ValueError:
        print("There's No Valid input in line.")
        return jsonify({'success':0,'Error': "There's No valid input in line."})
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return jsonify({'success':0,'Error': "Unexpected error."})
        raise 

if __name__ == '__main__':
     app.run(host="127.0.0.1",port="5000")