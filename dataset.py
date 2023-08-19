import csv

def convert_csv_to_dictionary(file_path):
    li=[]
    with open(file_path, 'r', encoding='utf8') as file:
        #header=[]
        reader = csv.reader(file)
        #header = next(reader)  # Assuming the first row contains column headers
        
        i=0
       
        for row in reader:
                dataset_dict = {}
              
                #key = row[1]  # Assuming the first column is the key
                #values = row[2:]  # Assuming the remaining columns are values
                dataset_dict['title'] = row[2]
                dataset_dict['lyrics'] = row[6]
                dataset_dict['artist'] = row[1]
                li.append(dataset_dict)
                #print([dict1['title'] for dict1 in li])
        return li

# Example usage
file_path = 'Beyonce.csv'

li1 = convert_csv_to_dictionary(file_path)


file_path = 'BillieEilish.csv'
li2 = convert_csv_to_dictionary(file_path)

file_path = 'BTS.csv'
li3 = convert_csv_to_dictionary(file_path)

file_path = 'CardiB.csv'
li4= convert_csv_to_dictionary(file_path)

file_path = 'ColdPlay.csv'
li5= convert_csv_to_dictionary(file_path)

file_path = 'Drake.csv'
li6= convert_csv_to_dictionary(file_path)

file_path = 'DuaLipa.csv'
li7= convert_csv_to_dictionary(file_path)

file_path = 'EdSheeran.csv'
li8= convert_csv_to_dictionary(file_path)

file_path = 'Drake.csv'
li9= convert_csv_to_dictionary(file_path)

file_path = 'Eminem.csv'
li10= convert_csv_to_dictionary(file_path)

file_path = 'JustinBieber.csv'
li11= convert_csv_to_dictionary(file_path)

file_path = 'Khalid.csv'
li12= convert_csv_to_dictionary(file_path)

file_path = 'LadyGaga.csv'
li13= convert_csv_to_dictionary(file_path)

file_path = 'Maroon5.csv'
li14= convert_csv_to_dictionary(file_path)

file_path = 'NickiMinaj.csv'
li15= convert_csv_to_dictionary(file_path)

file_path = 'PostMalone.csv'
li16= convert_csv_to_dictionary(file_path)

file_path = 'Rihanna.csv'
li17= convert_csv_to_dictionary(file_path)

file_path = 'SelenaGomez.csv'
li18= convert_csv_to_dictionary(file_path)

file_path = 'TaylorSwift.csv'
li19= convert_csv_to_dictionary(file_path)
li = []
li.extend(li1+li2+li3+li4+li5+li6+li7+li8+li9+li10+li11+li18+li19)


#print(li1)

from tkinter import scrolledtext
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from tkinter import *
import tkinter.messagebox as msg
import tkinter.font as font
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string
# Step 1: Gather song data
songs = li


# Step 2: Preprocess song lyrics
def preprocess_lyrics(lyrics):
    lyrics = lyrics.lower()
    
    # Remove punctuation
    lyrics = lyrics.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenize lyrics into words
    words = word_tokenize(lyrics)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    # Perform stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    # Join the preprocessed words back into a string
    preprocessed_lyrics = " ".join(words)
    
    return preprocessed_lyrics

# Step 3: Vectorize song lyrics
def vectorize_lyrics(song_lyrics):
    vectorizer = TfidfVectorizer()
    lyric_vectors = vectorizer.fit_transform(song_lyrics).toarray()
    return lyric_vectors, vectorizer

# Step 4: Calculate lyric similarity and recommend songs
def recommend_songs(user_lyrics):
    user_lyrics = preprocess_lyrics(user_lyrics)
    song_lyrics = [song['lyrics'] for song in songs]
    all_lyrics = [user_lyrics] + song_lyrics

    lyric_vectors, vectorizer = vectorize_lyrics(all_lyrics)

    user_lyric_vector = lyric_vectors[0]
    song_lyric_vectors = lyric_vectors[1:]

    similarity_scores = cosine_similarity([user_lyric_vector], song_lyric_vectors)[0]
    sorted_indices = similarity_scores.argsort()[::-1]  # Sort indices in descending order

    recommended_songs = []
    for index in sorted_indices:
        recommended_songs.append(songs[index])

    return recommended_songs

def recommend_button_click():
    user_lyrics = user_input.get("1.0", END)
    recommended_songs = recommend_songs(user_lyrics)

    result_text.delete("1.0", END)

    if recommended_songs:
        for song in recommended_songs[:10]:
            result_text.insert(END, f"Title: {song['title']}, Artist: {song['artist']}\n")
    else:
        messagebox.showinfo("No Recommendations", "No songs were recommended.")

# Create the main window


root = Tk()
root.wm_attributes('-transparentcolor','#ab23ff')
root.title("Song Recommendation")
root.geometry("640x896")
root.resizable(False,False)
bg = PhotoImage(file="python_project_background_music.png")
canvas1 = Canvas(root, width = 640, height = 896)
canvas1.pack()
canvas1.create_image(0,0, image = bg, anchor = "nw")
# Create the user input text box
user_input_label = Label(root, text="Enter your lyrics:", bg = '#1d3b64',fg='#ffffff')
user_input_canvas = canvas1.create_window(270,150,anchor="nw", window=user_input_label)

user_input = scrolledtext.ScrolledText(root, width = 50, height=4,bg="#1d3b64",fg='#ffffff')
user_input_canvas = canvas1.create_window(120,200,anchor="nw", window=user_input)

# Create the recommend button
recommend_button = Button(root, text="Recommend Songs", command=recommend_button_click,bg="#1d3b64",fg='#ffffff')
recommend_button_canvas = canvas1.create_window(270,300,anchor="nw", window=recommend_button)

# Create the result text box
result_label = Label(root, text="Recommended Songs:",bg="#1d3b64",fg='#ffffff')
result_label_canvas = canvas1.create_window(265,350,anchor="nw", window=result_label)

result_text = scrolledtext.ScrolledText(root,width=50,height=10,bg="#1d3b64",fg='#ffffff')
result_Text = canvas1.create_window(120,400,anchor="nw", window=result_text)

# Start the Tkinter event loop
root.mainloop()
