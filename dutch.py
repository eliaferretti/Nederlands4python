# Full path to VLC executable
vlc_path = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"

from gtts import gTTS
import subprocess
import random 
import time
import re
import os  

def clear_screen():
    # Clear screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def remove_symbold(word):
    word = word.replace('-', '').strip()
    word = word.replace('+', '').strip()
    word = word.replace('_', '').strip()
    word = word.replace('>', '').strip()
    word = word.replace('<', '').strip()
    word = word.replace('?', '').strip()
    word = word.replace('!', '').strip()
    word = word.replace(':', '').strip()
    word = word.replace('(', '').strip()
    word = word.replace(')', '').strip()
    word = word.replace("'", '').strip()
    word = word.replace('"', '').strip()
    word = word.replace('.', '').strip()
    word = word.replace(',', '').strip().lower()
    word = word.replace(',', '').strip().lower()
    return word

def highlight_text(original_text, user_input, correct_words, total_words):
    # ANSI escape codes for highlighting
    RED   = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    originaloriginal = original_text

    original_text = remove_symbold(original_text)
    user_input = remove_symbold(user_input)
    
    highlighted = ''
    original_words = original_text.split()
    user_words = user_input.split()

    max_len = max(len(original_words), len(user_words))
    
    for i in range(max_len):
        original_word = original_words[i] if i < len(original_words) else ''
        user_word = user_words[i] if i < len(user_words) else ''
        
        if original_word == user_word:
            highlighted += GREEN + user_word + RESET + ' '
            correct_words += 1
            total_words   += 1
        else:
            highlighted += RED + original_word + RESET + ' '
            total_words   += 1
    
    return originaloriginal,highlighted,correct_words,total_words

def read_text_aloud(paragraph, les_nummer, vlc_path, lang="nl"):
        
    # Split the paragraph into lines
    lines = paragraph.split('\n')

    correct_words=0
    total_words=0
    
    for i, line in enumerate(lines):
        
        line = line.replace('>', '').strip()
        line = line.replace('<', '').strip()
        line = re.sub(r'\(.*?\)', '', line)
        # Convert the line to speech

        if not(line==''):
            # tts = gTTS(text=line, lang=lang, slow=False)
            tts = gTTS(text=". " + line,tld="com", lang=lang, slow=False)

            # Save the audio to a file
            audio_file = f"audio/audio{les_nummer}_{i+1}.mp3"
            tts.save(audio_file)

            clear_screen()
            if total_words>0: print(f"Score: {correct_words/total_words*100:.1f}%")

            vlc_command = [vlc_path, '--qt-start-minimized', '--play-and-exit', audio_file]
            subprocess.run(vlc_command)

            user_input = input("Please enter the text you hear\n\n")

            orig,highlighted_text,correct_words,total_words = highlight_text(line, user_input,correct_words,total_words)
            
            clear_screen()
            print(f"Score: {correct_words/total_words*100:.1f}%")
            print("--------------------------------------------------------------")
            print(orig)
            print("----")
            print(user_input)
            print(highlighted_text)
            print("--------------------------------------------------------------")
            
            time.sleep(5)
    if correct_words/total_words > 0.8:
        print("\nCongrats, you passed!")
    else:
        print("\nYou failed, you stupid donkey")

clear_screen()

if not os.path.exists("audio"):
    os.makedirs("audio")

user_input = input("Please enter de les: ")

# Specify the path to the text file
file_path = "les/les"+user_input+".txt"

# Open the file and read its contents into a variable
with open(file_path, 'r') as file:
    file_contents = file.read()
paragraphs = file_contents.split('\n\n')

type_of_par = input("select paragraph of niet [n]/y?")

if type_of_par=="y":
    par = 10000
    while int(par) > len(paragraphs):
        par = input(f"Please enter valid paragraph number (<{len(paragraphs)+1}): ")
    par = int(par)-1
    read_text_aloud(paragraphs[par],user_input,vlc_path)
else:
    read_text_aloud(random.choice(paragraphs),user_input,vlc_path)
