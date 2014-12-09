# -*- coding:utf-8 -*-
"""
Pliczek zawierający przydane fragmenty kodu, które mają
inspirować do wykonania zadania.
"""


"""
Wylistowanie jakiegoś katalogu uzywajac os:
"""
import os
lista_plikow_oraz_folderow = os.listdir('.')
# tylko pliki:
pliki = [elem for elem in os.listdir('.') if os.path.isfile(elem)]


"""
Wylistowanie jakiegoś katalogu używając glob:
"""
import glob
pliki_zip = glob.glob('*.zip')


"""
Przyjmowanie parametrów pozycyjnych:

./tidyup.py /Users/ja/folder/do_posprzatania/ /Users/ja/folder/lad_i_porzadek KLUCZ
"""
import sys
try:
    # sys.argv jest listą, której pierwszym elementem zawsze jest nazwa programu
    script_name, source, target, key = sys.argv
except ValueError:
    print u"Musisz podać wszystkie parametry pozycyjne."


"""
Tworzenie folderów:
"""
import os

EXTENSIONS = {
    'psd': "Adobe Photoshop",
    'doc': "Microsoft Word",
    # ...
}

file_ = 'projekt_w_photoshopie.psd'
file_name, file_ext = file_.split('.')

os.mkdir(EXTENSIONS[file_ext])


"""
Przenoszenie plików:
"""

import shutil

shutil.move(source, target)
