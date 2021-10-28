# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pickle

# df = pd.read_csv("books_with_blurbs.csv")

# df.drop(columns=["Year"], inplace=True)

# df.drop_duplicates(subset=["Title"],inplace=True, keep="first")
# df.reset_index(drop=True,inplace=True)

# df['wordsBag'] = df['Author'].apply(lambda x:str(x).replace(" ",""))
# df.drop(columns=["Author"], inplace=True)
# df['wordsBag'] = df['wordsBag'] + " " + df['Publisher'].apply(lambda x:str(x).replace(" ",""))
# df.drop(columns=["Publisher"], inplace=True)
# df['wordsBag'] = df['wordsBag'] + " " + df['Title']
# df['wordsBag'] = df['wordsBag'] + " " + df['Blurb']
# df.drop(columns=["Blurb"], inplace=True)

# df = df.iloc[:10000,:]

# cv = CountVectorizer(max_features=5000,stop_words='english')
# vector = cv.fit_transform(df['wordsBag']).toarray()

# similarity = cosine_similarity(vector)

# def recommend(book_name):
#     index_pos = df[df["Title"] == book_name].index[0]
#     book_list = sorted(enumerate(similarity[index_pos]), key=lambda x:x[1] ,reverse=True)[1:6]
#     return [df.iloc[book[0]]["ISBN"] for book in book_list]

# df['Recommended_Books'] = df['Title'].apply(recommend)
# print(df.head(1))

# pickle.dump(df,open('books.pkl','wb'))




import requests

response = requests.get("https://openlibrary.org/isbn/0394525493.json").json()
print(response["publishers"][0])
print(response["title"])
print(response["genres"])