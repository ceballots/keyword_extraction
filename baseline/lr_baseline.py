import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import f1_score

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = re.sub("\'", "", text)
    text = re.sub("[^a-zA-Z]", " ", text)
    text = ' '.join(text.split())
    text = text.lower()
    return text


def remove_stopwords(text):
    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)


def run_baseline():
    train = pd.read_csv("/app/data/train.csv")
    val = pd.read_csv("/app/data/val.csv")

    train['clean_plot'] = train['plot_synopsis'].apply(lambda x: clean_text(x))
    val['clean_plot'] = val['plot_synopsis'].apply(lambda x: clean_text(x))

    train['clean_plot'] = train['clean_plot'].apply(lambda x: remove_stopwords(x))
    val['clean_plot'] = val['clean_plot'].apply(lambda x: remove_stopwords(x))

    multilabel_binarizer = MultiLabelBinarizer()
    multilabel_binarizer.fit(train['tags'])

    y_train = multilabel_binarizer.transform(train['tags'])
    y_val = multilabel_binarizer.transform(val['tags'])

    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=10000)
    xtrain = train["clean_plot"]
    xval = val["clean_plot"]

    lr = LogisticRegression()
    clf = OneVsRestClassifier(lr)

    xtrain_tfidf = tfidf_vectorizer.fit_transform(xtrain)
    xval_tfidf = tfidf_vectorizer.fit_transform(xval)

    clf.fit(xtrain_tfidf, y_train)
    train_score = f1_score(clf.predict(xtrain_tfidf), y_train, average="micro")
    val_score = f1_score(clf.predict(xval_tfidf), y_val, average="micro")

    print("Train score {}, val score {}".format(train_score, val_score))


if __name__ == '__main__':
    run_baseline()
