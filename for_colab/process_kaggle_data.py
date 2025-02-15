import os
import zipfile
import shutil


# japanese
def unzip_japanese():
    zip_file = '/content/japanese-single-speaker-speech-dataset.zip'

    with zipfile.ZipFile(zip_file, 'r') as zip:
        listOfFileNames = zip.namelist()

        for fileName in listOfFileNames:
            if 'ja' in fileName:
                zip.extract(fileName)


def rename_japanese():
    os.rename('/content/ja', '/content/japanese')


def move_japanese():
    shutil.move('/content/japanese', '/content/Multilingual_Text_to_Speech/data/css10')


def process_japanese():
    unzip_japanese()
    rename_japanese()
    move_japanese()


# english
def unzip_english():
    zip_file = '/content/ljspeech.zip'

    with zipfile.ZipFile(zip_file, 'r') as zip:
        listOfFileNames = zip.namelist()

        for fileName in listOfFileNames:
            if 'ljspeech-1.1/LJSpeech-1.1' in fileName or 'LJSpeech-1.1/LJSpeech-1.1' in fileName:
                zip.extract(fileName)


def rename_english():
    os.rename('/content/ljspeech-1.1/LJSpeech-1.1', '/content/ljspeech-1.1/english')


def move_english():
    shutil.move('/content/ljspeech-1.1/english', '/content')
    os.rmdir('/content/ljspeech-1.1')
    shutil.move('/content/english', '/content/Multilingual_Text_to_Speech/data/css10')


def process_english():
    unzip_english()
    rename_english()
    move_english()


process_japanese()
# process_english()