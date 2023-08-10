import os
import shutil
import re
import sys

# Function for transliteration and replacement of invalid characters in file names
def normalize(text):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
        'и': 'i', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z',
        'И': 'I', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Shch', 'Ь': '', 'Ю': 'Yu', 'Я': 'Ya'
    }
    
    normalized_text = ''
    for char in text:
        if char.isalnum():
            normalized_text += char
        elif char in translit_dict:
            normalized_text += translit_dict[char]
        else:
            normalized_text += '_'
    
    return normalized_text

# Function for sorting files in a folder
def sort_folder(path):
    image_extensions = ('JPEG', 'PNG', 'JPG', 'SVG')
    video_extensions = ('AVI', 'MP4', 'MOV', 'MKV')
    document_extensions = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    audio_extensions = ('MP3', 'OGG', 'WAV', 'AMR')
    archive_extensions = ('ZIP', 'GZ', 'TAR')
    
    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            file_extension = file.split('.')[-1].upper()
            normalized_filename = normalize(file.split('.')[0]) + '.' + file_extension
            
            if file_extension in image_extensions:
                new_folder = os.path.join(path, 'images')
            elif file_extension in video_extensions:
                new_folder = os.path.join(path, 'videos')
            elif file_extension in document_extensions:
                new_folder = os.path.join(path, 'documents')
            elif file_extension in audio_extensions:
                new_folder = os.path.join(path, 'audio')
            elif file_extension in archive_extensions:
                new_folder = os.path.join(path, 'archives', normalized_filename)
                os.makedirs(new_folder, exist_ok=True)
                shutil.unpack_archive(full_path, new_folder)
            else:
                new_folder = os.path.join(path, 'unknown')
            
            new_path = os.path.join(new_folder, normalized_filename)
            shutil.move(full_path, new_path)

# Main function for sorting the folder and analyzing the results
def main():
    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
        return
    
    folder_path = sys.argv[1]
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    sort_folder(folder_path)
    print("Folder has been sorted.")

if __name__ == "__main__":
    main()