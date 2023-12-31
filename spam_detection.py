# -*- coding: utf-8 -*-
"""Spam Detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ioFHj-A1abGkHbW_YVJTW-6i63wlq9Nt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/spam.csv',encoding='latin-1')
df.head()

df.describe()

df.info()

df.columns

label_counts = df['label'].value_counts()
print("\nLabel Distribution:")
print(label_counts)

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x='label', data=df, ax=ax)
plt.title('Label Distribution')
plt.show()

df['message_length'] = df['message'].apply(len)

plt.figure(figsize=(10, 6))
sns.histplot(df['message_length'], bins=50, kde=True)
plt.title('Distribution of Message Lengths')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()

print("\nStatistics on Message Lengths:")
print(df['message_length'].describe())

print("\nExamples of Long Messages:")
print(df[df['message_length'] > 150]['message'].head())

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)
y_pred = classifier.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:{conf_matrix}')
print(f'classification report:{classification_rep}')