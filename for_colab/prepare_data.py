import os
import zipfile
import random
import argparse
from pathlib import Path


MAX_ID_LEN = '000000'
VALID_LEN = 64


def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip() for line in f]

def save_txt(path, txt):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
        

def create_id(idx):
    idx_to_str = str(idx)
    return MAX_ID_LEN[len(idx_to_str):] + idx_to_str


def process_data(args):
    current_dir = os.path.join(os.path.join(args.base_directory, args.language), args.voice_name)
    
    Path(current_dir).mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(args.zip_file, 'r') as zip:
        zip.extractall(args.base_directory)


def modify_speech(value):
    return value.replace(' 。', '。').replace(' 、', '、')


def add_transcript_to_txt(args):
    # train.txt, valid.txt 데이터 형식 
    # 037775|japanese|japanese|japanese/meian/meian_1033.wav|||karera wa min'na jo-ryu- shakai yori yoi ninso- wo shi te iru kara aisatsu wo suru yu-ki no nakat ta tsuda wa、 ichido- wo mimawasu kawari ni、|

    language = args.language
    voice = args.voice_name
    train_path = os.path.join(args.base_directory, 'train.txt')
    val_path = os.path.join(args.base_directory, 'val.txt')

    train_meta = load_txt(train_path)
    val_meta = load_txt(val_path)

    transcript = os.path.join(os.path.join(os.path.join(args.base_directory, args.language), 'transcript.json'))
    data = [f'{create_id(idx)}|{language}|{language}|{key}|||{modify_speech(value)}' for idx, (key, value) in enumerate(transcript.items())]

    train_meta += random.sample(data, len(data))
    val_meta += random.sample(data, VALID_LEN)

    save_txt(train_path, '\n'.join(train_meta))
    save_txt(val_path, '\n'.join(val_meta))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--zip_file', required=True, default='', help='zip file to unzip')
    parser.add_argument('--base_directory', required=True, default='', help='base directory that unzipped data to locate')
    parser.add_argument('--language', required=True, default='japanese', help='current language')
    parser.add_argument('--voice_name', required=True, default='hayaming', help='voice name')
    args = parser.parse_args()
    
    process_data(args)
    add_transcript_to_txt(args)