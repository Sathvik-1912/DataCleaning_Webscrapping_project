import pandas as pd
import re

import chardet

with open("C:/Users/vanap/sath_project/sahithya_akademi/sahithya_akademi/output.csv", 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large

charenc = result['encoding']
print(charenc)

df = pd.read_csv("C:/Users/vanap/sath_project/sahithya_akademi/sahithya_akademi/output.csv", encoding=charenc)

# Extract category from book title
def extract_category(book):
    match = re.search(r'\((.*)\)', book)
    if match:
        return match.group(1).strip(), re.sub(r'\s*\((.*)\)', '', book)
    else:
        return 'Unknown', book

df[['category', 'book']] = df['book'].apply(extract_category).apply(pd.Series)

# Add notes based on special characters in author name
def add_notes(author):
    if '*' in author:
        return 'Awarded Posthumously'
    else:
        return ''

df['notes'] = df['author'].apply(add_notes)

# Remove special characters from author names
def remove_special_chars(author):
    return re.sub(r'[^a-zA-Z\s]', '', author)

if 'author' in df.columns:
    df['author'] = df['author'].apply(remove_special_chars)

# Rename columns
df.columns = ['year', 'book', 'author', 'language', 'category', 'notes']

# Reorder columns
df = df[['year', 'category', 'book', 'author', 'language', 'notes']]

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_sahitya_akademi_awards.csv', index=False)