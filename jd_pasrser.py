import os

#Loading job description as a txt file

def load_jd_text(source):
     final_text = ""
     with open(source, "r", encoding="utf-8") as file: #Handles special characters (e.g., in foreign JDs)
          text = file.read() #Reads the entire file as one string
          clean_text = text.strip() #Removes extra line breaks and spacing
          final_text += clean_text
          return clean_text