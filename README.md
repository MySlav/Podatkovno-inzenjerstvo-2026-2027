# Podatkovno inženjerstvo (2026./2027.)

Materijali za laboratorijske vježbe kolegija **Podatkovno inženjerstvo** na Sveučilištu Algebra Bernays, ak. god. 2026./2027.
Bilježnice (Jupyter notebook), podaci i pomoćne datoteke za svaku vježbu nalaze se u zasebnoj mapi.

## Vježbe

| Mapa | Tema | Okruženje |
|---|---|---|
| [`EX_5/`](EX_5/) | Nedostajuće vrijednosti i ekstremne vrijednosti (outlieri) | Jupyter pod |

Nove vježbe dodavat će se tijekom semestra u nove mape (`EX_6/`, `EX_7/` …), pa prije svake vježbe povucite najnoviju verziju (vidi dolje).

## Struktura repozitorija

```
Podatkovno-inzenjerstvo-2026-2027/
├─ README.md            ← ova datoteka
├─ okruzenje/           ← YAML datoteke za Podman podove (Jupyter, kasnije SQL)
└─ EX_5/                ← jedna mapa po vježbi
   ├─ README.md         ← upute za tu vježbu
   ├─ *.ipynb           ← bilježnica
   ├─ podaci/           ← skupovi podataka
   └─ slike/            ← slike koje bilježnica prikazuje
```

## Prvi put: preuzimanje repozitorija

Radimo u **Jupyter podu** (upute za pokretanje: [`okruzenje/README.md`](okruzenje/README.md)).
Pod ima vlastiti disk (volumen), pa se repozitorij klonira **unutar Jupytera**, a ne na Windowsima:

1. Pokrenite Jupyter pod i otvorite Jupyter u pregledniku.
2. U pregledniku datoteka odaberite **New → Terminal**.
3. U terminal upišite:
   ```bash
   git clone https://github.com/MySlav/Podatkovno-inzenjerstvo-2026-2027.git
   ```
4. U pregledniku datoteka pojavit će se mapa `Podatkovno-inzenjerstvo-2026-2027`. Otvorite mapu vježbe i bilježnicu u njoj.

## Prije svake vježbe: povlačenje novosti

U Jupyter terminalu:
```bash
cd Podatkovno-inzenjerstvo-2026-2027
git pull
```
Isto možete napraviti i iz bilježnice – prva ćelija svake bilježnice je `!git pull`.

## Radite u svojoj kopiji bilježnice

Prije nego što počnete rješavati zadatke, spremite kopiju: **File → Save Notebook As…** → npr. `EX_5_moj_rad.ipynb`.

Ako mijenjate originalnu bilježnicu, a nastavnik u međuvremenu objavi ispravak iste datoteke, `git pull` će javiti grešku
(*Your local changes … would be overwritten by merge*). Kopije s nastavkom `_moj_rad.ipynb` git ne prati, pa ih `git pull` nikad ne dira.

Ako vam se to ipak dogodi:
```bash
git status          # pokazuje koje ste originalne datoteke promijenili
git stash           # privremeno sklanja vaše izmjene
git pull            # povlači novu verziju
git stash pop       # vraća vaše izmjene (ako javi sukob, spremite svoj rad kao kopiju i ponovite)
```

## Ako `git clone` ne radi

Na GitHubu kliknite **Code → Download ZIP**, raspakirajte arhivu na računalu i mapu vježbe prenesite u Jupyter gumbom **Upload**
(datoteke unutar mapa `podaci/` i `slike/` prenesite u iste podmape).
Novosti tada nećete moći povući s `git pull`, nego ponovno preuzimate ZIP.

## Rješenja

Rješenja zadataka nisu u repozitoriju prije vježbe. Ako budu objavljena, nalazit će se u podmapi `rjesenja/` mape te vježbe.

## Izvori podataka

Skupovi podataka preuzeti su s javnih izvora i koriste se isključivo u nastavne svrhe. Izvor je naveden u README-u svake vježbe.
