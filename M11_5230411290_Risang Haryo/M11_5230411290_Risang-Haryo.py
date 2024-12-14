import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

import os

def preprocessingData(filename):
    label_encoder = LabelEncoder()
    
    # Baca Data
    df = pd.read_excel(filename)
    
    # Mengisi Missing value dengan rata-rata setiap kolom
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            df[column].fillna(df[column].mean(), inplace=True)
            
    # Mengisi Missing value dengan modus di dataframe
    object_column = df.select_dtypes(include="object").columns
    
    for column in object_column:
        df[column].fillna(df[column].mode()[0], inplace=True)
        df[column] = label_encoder.fit_transform(df[column])

    # Menentukan Feature dan Label
    feature = df.iloc[:, :9].values
    label = df.iloc[:, 9].values

    # Min Max Scale
    scaler = MinMaxScaler()
    feature = scaler.fit_transform(feature)

    # Splitting Data Training dan Data Test
    x_train, x_test, y_train, y_test = train_test_split(feature, label, random_state=42, test_size=0.2)

    # Model Naive_Bayes
    GNB = GaussianNB()
    GNB.fit(x_train, y_train)
    pred = GNB.predict(x_test)
    accuracy = accuracy_score(y_test, pred)

    # Model KNN
    KNN = KNeighborsClassifier()
    KNN.fit(x_train, y_train)
    pred = KNN.predict(x_test)
    accuracy2 = accuracy_score(y_test, pred)
    
    return accuracy, accuracy2

def main():
    while True:
        os.system("clear")
        filename = input("Masukkan Nama File: ")
        accuracy_gaussian, accuracy_knn = preprocessingData(filename)
        while True:
            os.system("clear")
            print("Pilih model yang ingin digunakan:")
            print("1. Gaussian")
            print("2. KNN")
            print("3. Keluar")
            input_user = input("Masukkan pilihan Anda (1/2/3): ")
            if input_user == "1":
                print(f"Skor Akurasi Model Gaussian: {accuracy_gaussian}")
            elif input_user == "2":
                print(f"Skor Akurasi Model KNN: {accuracy_knn}")
            elif input_user == "3":
                break
            os.system("pause")
        break
    os.system("pause")
                
            
if __name__ == "__main__":
    main()