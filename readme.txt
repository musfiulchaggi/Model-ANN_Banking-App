pendapatan amerika
https://finance.detik.com/berita-ekonomi-bisnis/d-6253592/10-negara-dengan-gaji-terbesar-di-dunia-ada-ri#:~:text=4.%20Amerika%20Serikat&text=Dalam%20sebulan%2C%20rata%2Drata%20gaji%20yang%20diperoleh%20yaitu%20US%24,55%2C1%20juta%20per%20bulan.
https://www.ceicdata.com/id/indicator/united-states/annual-household-income-per-capita

pendapatan indonesia
https://databoks.katadata.co.id/datapublish/2023/02/06/pendapatan-penduduk-indonesia-tumbuh-1396-menjadi-rp71-juta-per-tahun-pada-2022#:~:text=Badan%20Pusat%20Statistik%20(BPS)%20melaporkan,%2C96%25%20dari%20tahun%20sebelumnya.

cara menggunakan model : 

- pastikan seluruh file dalam satu folder

- run script.py menggunakan cmd (syarat => python sudah terinstall && memiliki library [tensorflow, numpy, panda, flask, joblib])

- API di localhost:port(5000) dan function(predict) => http://127.0.0.1:5000/predict

- data yg dikirimkan (method:POST) => ['CreditScore'(int),'Tenure'(int),'NumOfProducts'(int),'Age'(int),'Estimated_Salary' => ($USD / year)(float),'Gender'(male/female)]