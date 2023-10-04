"""Compare different classifiers."""
import warnings

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import csv
from data_process import *

warnings.filterwarnings("ignore")

clf_names = ('Near. Neigh.', 'SVM', 'Decision Tree', 'Random Forest', 'Neural Net')  # classifier names
clfs = (KNeighborsClassifier(n_neighbors=100, weights='distance'), SVC(), DecisionTreeClassifier(),
        RandomForestClassifier(), MLPClassifier())  # classifier objects


def train_clf(x_train, y_train, clf):
    """
    Train classifier.
    :param x_train: Training inputs.
    :param y_train: Training outputs.
    :param clf: Untrained classifier object.
    :return: Trained classifier object.
    """
    clf.fit(x_train, y_train)  # train classifier

    return clf


def run():
    """
    main.
    :return: None
    """
    voice_data = read()  # read data
    x_train, x_test, y_train, y_test = preprocess(voice_data)  # preprocess data

    for clf_name, clf in zip(clf_names, clfs):  # for all classifiers
        clf = train_clf(x_train, y_train, clf)  # train classifier
        print()
        print(clf_name)
        get_accuracy(x_train, x_test, y_train, y_test, clf)  # print results


if __name__ == '__main__':
    voice_data = read()
    x_train, x_test, y_train, y_test = preprocess(voice_data)

    results = []  # Create a list to store the results

    for clf_name, clf in zip(clf_names, clfs):
        clf = train_clf(x_train, y_train, clf)
        color_name = ()
        if clf_name == 'Near. Neigh.':
            color_name = ('#D8A47F')
        elif clf_name == 'SVM':
            color_name = ('#EF8354')
        elif clf_name == 'Decision Tree':
            color_name = ('#EE4B6A')
        elif clf_name == 'Random Forest':
            color_name = ('#DF3B57')
        elif clf_name == 'Neural Net':
            color_name = ('#0F7173')   
            
        print()
        print(clf_name)
        accuracy, precision = get_accuracy(x_train, x_test, y_train, y_test, clf)  # Use the testing data

        # Store the results in a dictionary
        result_entry = {
            "Classifier": clf_name,
            "Accuracy": accuracy,
            "Precision": precision,
            "Color": color_name
        }

        results.append(result_entry)
        

    # Specify the CSV file path
    csv_file = "classifier_results.csv"

    # Write the results to the CSV file
    with open(csv_file, mode="w", newline="") as file:
        fieldnames = ["Classifier", "Accuracy", "Precision", "Color"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    print(f"Results (Accuracy and Precision) have been saved to {csv_file}")
    #run()
