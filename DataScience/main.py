from dataset import class_dataset
from missingValue import class_missingValue
from classifier import *
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


import numpy as np
if __name__ == '__main__':
    """
        load dataset
        glcm : all fitur  
        dissimilarity : dis fitur
    """

    """
    Memanggil Dataset frekuensi
    """
    dataset = class_dataset(dataset_name="frekuensi")

    """
    missing value
    """
    data = class_missingValue(dataset, pick="median")

    "preprocesing (normalisasi)"


    """
    model RFC 0.2
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.2, random_state=42)
    # rfc = class_rfc(X_train, y_train)
    # rfc.model()
    # y_pred = rfc.predict(X_test)

    """
    model NB 0.2
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.2, random_state=42)
    # nb = class_NB(X_train, y_train)
    # nb.model()
    # y_pred = nb.predict(X_test)


    """
    model MNB 0.2
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.2, random_state=42)
    # mnb = class_MNB(X_train, y_train)
    # mnb.model()
    # y_pred = mnb.predict(X_test)

    """
    model BNB 0.2
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.2, random_state=42)
    # bnb = class_bnb(X_train, y_train)
    # bnb.model()
    # y_pred = bnb.predict(X_test)



    """
    model RFC 0.3
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.3, random_state=42)
    # rfc = class_rfc(X_train, y_train)
    # rfc.model()
    # y_pred = rfc.predict(X_test)

    """
    model NB 0.3
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.3, random_state=42)
    # nb = class_NB(X_train, y_train)
    # nb.model()
    # y_pred = nb.predict(X_test)

    """
    model MNB 0.3
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.3, random_state=42)
    # mnb = class_MNB(X_train, y_train)
    # mnb.model()
    # y_pred = mnb.predict(X_test)

    """
    model BNB 0.3
    """
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.3, random_state=42)
    # bnb = class_bnb(X_train, y_train)
    # bnb.model()
    # y_pred = bnb.predict(X_test)



    # dataset = class_dataset(dataset_name="dissimilarity")

    # missing value
    # data = class_missingValue(dataset, pick="mean")

    # preprocessing (normalisasi)

    # model SVM
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.16, random_state=42)
    # svm = class_SVM(X_train, y_train)
    # svm.model()
    # y_pred = (np.rint(svm.predict(X_test))).astype(int)

    # model NB
    # X_train, X_test, y_train, y_test = train_test_split(
    #     data.X, data.y, test_size=0.17, random_state=42)
    # nb = class_NB(X_train, y_train)
    # nb.model()
    # y_pred = nb.predict(X_test)

    # kfold with NB
    # data.y = np.array([data.y[1] for i in data.y])
    # kf = KFold(n_splits=3, random_state=None, shuffle=False)
    # acc = []
    # for train_index, test_index in kf.split(data.X):
    #     X_train, X_test = data.X[train_index], data.X[test_index]
    #     y_train, y_test = data.y[train_index], data.y[test_index]
    #     nb = class_NB(X_train, y_train)
    #     nb.model()
    #     y_pred = nb.predict(X_test)
    #     acc.append(accuracy_score(y_test, y_pred))

    # model KNN
    X_train, X_test, y_train, y_test = train_test_split(
        data.X, data.y, test_size=0.2, random_state=42)
    knn = class_KNN(X_train, y_train)
    knn.model(14)
    y_pred = knn.predict(X_test)

    """
    evaluasi
        """
    acc = accuracy_score(y_test, y_pred)
    print("accuracy : ", acc)

    # evaluasi
    # acc = accuracy_score(y_test, y_pred)
    # print("accuracy : ", acc)

    # """
    # Dataset Alkohol
    # """
    # dataset = class_dataset(dataset_name="alkohol")


    # # missing value
    # data = class_missingValue(dataset, pick="mean")
    # data.y = (np.rint(data.y)).astype(int)

    # model SVM
    # X_train, X_test, y_train, y_test = train_test_split(
    #   data.X, data.y, test_size=0.1, random_state=18)
    # svm = class_SVM(X_train, y_train)
    # svm.model()
    # y_pred = (np.rint(svm.predict(X_test))).astype(int)

    # model KNN
    # X_train, X_test, y_train, y_test = train_test_split(
    #    data.X, data.y, test_size=0.5, random_state=18)
    # knn = class_KNN(X_train, y_train)
    # knn.model(13)
    # y_pred = knn.predict(X_test)


    # evaluasi
    # acc = accuracy_score(y_test, y_pred)
    # print("accuracy : ", acc)
