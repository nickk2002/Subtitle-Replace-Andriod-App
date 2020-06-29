from chardet import detect
import crayons
import os
import regex

modify_text = "MODIFIED#0"

def get_encoding_type(path):
    with open(path,'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

def change_encoding_to_utf8(path):
    code = get_encoding_type(path)

    if code == 'utf-8':
        return
    try:
        text = str()
        with open(path, 'r', encoding=code) as f:
            text = f.read()
        with open(path,'w',encoding='utf-8') as e:
            e.write(text)
    except UnicodeDecodeError:
        print(crayons.red('Decode Error'))
    except UnicodeEncodeError:
        print('Encode Error')
def modify_subtitles_diactritice(path):
    pattern = "0\n00:00:00,000 --> 00:00:00,000\nMODIFIED#0\n"
    text_nou = str()
    text = str()

    with open(path,'r',encoding='utf-8', errors = 'ignore') as file:
        cnt = 0

        for line in file:
            try:
                cnt += 1
                if cnt == 3 :
                    if line.startswith(modify_text):
                        return
                    break
            except:
                print("Continuam")
    change_encoding_to_utf8(path)
    with open(path,'r',encoding='utf-8') as file:
        for line in file:
            line = line.replace('º','ș')
            line = line.replace('þ','ț')
            line = line.replace('ª','Ș')
            text += line
    text_nou = pattern
    text_nou += text

    with open(path, "w",encoding='utf-8') as f:
        f.write(text_nou)
def subtitles_diactritice_all(dir):
    print(crayons.magenta("Running diacritice replace..."))

    cnt = 0
    files_detected = 0
    max_files = 100000
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            files_detected += 1
            path = subdir + os.sep + file
            if files_detected > max_files:
                return
            if file.endswith(".srt"):
                cnt += 1
                print(crayons.cyan(path))
                modify_subtitles_diactritice(path)
    if cnt == 0:
        print(crayons.red("Did not find any subtitles"))



