## Sytuacja:
Pewnie każdy z nas posiada taki folder w swoim komputerze do którego wrzuca wszystko, czego aktualnie nie potrzebuje (ale może się przydać). Zazwyczaj kończymy wtedy z folderem zawierającym ponad 100 przeróżnych plików.

## Rozwiązanie:
Napisz skrypt który pokataloguje pliki po zadanym KLUCZU. Pokataloguje np. po rozszerzeniu, znaczy, że skrypt utworzy folder o nazwie "Adobe Photoshop" i przeniesie do niego wszystkie pliki z rozszerzeniem ".psd".

## Oczekiwane Efekty:
tree przed/
```
przed
├── Bardzo ważne rzeczy.docx
├── Egnyte Payrolls.xlsx
├── Zrzut ekranu 2014-12-09 o 15.03.36.png
├── conflicts.png
├── file_including.lol
├── newlogo.indd
└── special_characters.zip

0 directories, 7 files
```
tree po/
```
po
├── Adobe InDesign
│   └── newlogo.indd
├── Microsoft Excel
│   └── Egnyte Payrolls.xlsx
├── Microsoft Word
│   └── Bardzo ważne rzeczy.docx
├── Others
│   ├── file_including.lol
│   └── special_characters.zip
└── PNG images
    ├── Zrzut ekranu 2014-12-09 o 15.03.36.png
        └── conflicts.png

5 directories, 7 files
```
## Wymagania:
Skrypt musi przyjmować parametry pozycyjne: 
```
./tidyup.py /Users/ja/folder/do_posprzatania/ /Users/ja/folder/lad_i_porzadek KLUCZ
```
* pierwszym parametrem pozycyjnym jest folder zawiarający nieład
* drugim parametrem pozycyjnym jest folder do którego mają zostać przeniesione pokatologowane pliki (nie musi istnieć)
* trzecim parametrem pozycyjnym jest KLUCZ. Może to być np. EXTENSTION, CDATE (data utworzenia), MDATA (data
  modyfikacji)

**Skrypt który jest do wykonania na zajęciach, ma układać pliki tylko wg rozszerzeń. JEDNAK powinien być łatwo
rozszerzalny - to znaczy, że jeżeli w pewnym momencie życia chcielibyśmy dodać jakiś nowy sposób katologowania np. po
rozmiarze, rozszerzenie skryptu o nowy KLUCZ nie powinno stanowić większego problemu. Najlepiej, jeżeli była by to
kwestia dodania jedej instrukcji, funkcji itp.**

W pliku snippets.py przydatne fragmenty kodu.
