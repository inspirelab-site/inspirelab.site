import re
import string
from datetime import datetime
from collections import defaultdict

def roman_numeral(n):
    roman_numerals = {
        1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v',
        6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x'
    }
    return roman_numerals.get(n, str(n))

def convert_format_with_strict_info_v17(text):
    entries = text.split('\n\n')  # Split based on double newline separating entries
    formatted_entries = []
    publisher_keys = []  # To store the publisher keys
    authors_set = set()  # To store unique authors
    entry_list = []
    id_value_count = defaultdict(int)  # To count occurrences of each id_value

    for entry in entries:
        # Using regex to capture the necessary fields
        title_match = re.search(r'TI\s+-\s+(.+)', entry)
        # Adjust the regex to correctly capture authors
        authors_matches = re.findall(r'AU\s+-\s([^,]+),([^,]+),(?:([^,\n]))?', entry)
        
        publisher_match = re.search(r'CT\s+-\s+(.+)', entry)
        date_match = re.search(r'CY\s+-\s+([\d\s]+)', entry)

        if title_match and authors_matches and publisher_match and date_match:
            title = title_match.group(1).strip()
            # Format author names correctly
            authors = []
            for last, first, middle in authors_matches:
                if middle:
                    author = f"{first.strip()} {middle.strip()}. {last.strip()}"
                else:
                    author = f"{first.strip()} {last.strip()}"
                authors.append(author)
                authors_set.add(author)
                
            publisher = publisher_match.group(1).strip()
            date = date_match.group(1).strip().replace(' ', '-')
            year_for_id = date.split('-')[0]  # Extracting year for ID
            
            # Creating the publisher key for the ID, skipping numbers and punctuation, and converting specific words
            publisher_words = re.split(r'\s+', publisher)
            base_publisher_key = ''.join([
                word[0].lower() if word.lower() != 'neuroradiology' else 'nr' 
                for word in publisher_words 
                if word.lower() not in ['for', 'and', 'the', 'annual', 'meeting', 'of', 'ieee', 'international', 'conference', 'in'] 
                and not any(char.isdigit() for char in word) 
                and all(char not in string.punctuation for char in word)
            ])
            id_value = f"{base_publisher_key}{year_for_id}"
            id_value_f = f"{base_publisher_key}{year_for_id}"
            
            # Ensure unique id_value
            count = id_value_count[id_value]
            id_value_f += roman_numeral(count+1)             
            id_value_count[id_value] += 1
            
            # Storing the publisher key
            publisher_keys.append(f"{id_value}: {publisher}")
            
            formatted_entry = (
                f"- title: \"{title}\"\n"
                f"  authors:\n" + ''.join([f"    - {author}\n" for author in authors]) +
                f"  publisher: {publisher}\n"
                f"  date: '{date}'\n"
                f"  type: conference\n"
                f"  tags:\n"
                f"    - conference\n"
            )
            entry_list.append((formatted_entry, datetime.strptime(date, '%Y-%m-%d')))
    
    # Sort entries by date from newest to oldest
    entry_list.sort(key=lambda x: x[1], reverse=True)
    formatted_entries = [entry[0] for entry in entry_list]
    
    return '\n'.join(formatted_entries), '\n'.join(publisher_keys), '\n'.join(sorted(authors_set))

# Reading the content of the uploaded file
with open('abstracts.txt', 'r') as file:
    content_v17 = file.read()

# Converting the content to the desired format with full author names and strict info from the .txt file
strict_formatted_content_v17, publisher_keys_content_v17, authors_content_v17 = convert_format_with_strict_info_v17(content_v17)

# Writing the formatted content to a new file
with open('formatted_abstracts_noid.yaml', 'w') as output_file:
    output_file.write(strict_formatted_content_v17)

# Writing the publisher keys to a separate file
with open('publisher_keys.txt', 'w') as output_keys_file:
    output_keys_file.write(publisher_keys_content_v17)

# Writing the authors to a separate file
with open('authors.txt', 'w') as output_authors_file:
    output_authors_file.write(authors_content_v17)

print("Conversion completed. Check the formatted_abstracts.yaml, publisher_keys.txt, and authors.txt files for the output.")
