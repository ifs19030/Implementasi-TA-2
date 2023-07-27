from flask import Flask, render_template, url_for, redirect, request
import pickle
import csv
import os
import pandas as pd
import numpy as np
app = Flask(__name__)

# Load model Algoritma Genetika dari file .pkl
with open('model-pniel.pkl', 'rb') as file:
    model_genetika = pickle.load(file)

# Halaman utama
@app.route("/")
def index():
    return render_template("index.html")

# Halaman hasil
@app.route("/best_solution", methods=['POST'])
def best_solution():
    # return "Hello"
    print('open')
    value = int(request.form['id_asrama'])
    print(value)
    list_asrama = ['Pniel', 'Antiokia', 'Kapernaum', 'Silo', 'Mambre', 'Mahanaim', 'Nazareth', 'Kana']

    # value_mahasiswa = request.form['data_mahasiswa']
    # print(value_mahasiswa)
    print('mid')
    csv_file = request.files['csv_file']
    print(csv_file)
    if csv_file and csv_file.filename.endswith('.csv'):
        csv_data = csv_file.read().decode('utf-8')   

        # Pastikan model_genetika memiliki fungsi optimasi() untuk melakukan optimasi
        hasil_optimasi =  model_genetika.best_solution(value, csv_data)
        return render_template('result.html', nama_asrama=list_asrama[value], hasil_optimasi=hasil_optimasi)

    return "File Upload or processing failed"

if __name__ == "__main__":
    app.run(debug=True)
