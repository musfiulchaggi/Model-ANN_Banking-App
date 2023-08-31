cara menggunakan model : 

- pastikan seluruh file dalam satu folder

- run script.py menggunakan cmd (syarat => python sudah terinstall && memiliki library [tensorflow, numpy, panda, flask, joblib])

- API di localhost:port(5000) dan function(predict) => http://127.0.0.1:5000/predict

- data yg dikirimkan (method:POST) => ['CreditScore'(int),'Tenure'(int),'NumOfProducts'(int),'Age'(int),'Estimated_Salary' => ($USD / year)(float),'Gender'(male/female)]
