from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))


    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.IMAGE:
        handle_media(file, folder / 'image')
    for file in parser.VIDEO:
        handle_media(file, folder / 'video')
    for file in parser.DOCS:
        handle_media(file, folder / 'docs')
    for file in parser.AUDIO:
        handle_media(file, folder / 'audio')

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'other')
    for file in parser.ARCHIVE:
        handle_archive(file, folder / 'archives')


    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

def start():
    if __name__ == '__main__':
        try:
            folder = sys.argv[1]
        except IndexError:
            print('Enter path to folder')

    else:
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(fprint(f'Start in folder {folder_for_scan.resolve()}'))






