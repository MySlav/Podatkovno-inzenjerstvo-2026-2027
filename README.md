# Podatkovno inženjerstvo (2026./2027.)

Materijali za laboratorijske vježbe kolegija **Podatkovno inženjerstvo** na Sveučilištu Algebra Bernays, ak. god. 2026./2027.
Za svaku vježbu postoji zasebna mapa s materijalima: Jupyter bilježnice, SQL skripte, Python i drugi kod, podaci i pomoćne datoteke.
Što je u kojoj mapi i kako s tim raditi, piše u README-u te mape.

## Vježbe

| Mapa | Tema | Okruženje |
|---|---|---|
| [`EX_5/`](EX_5/) | Nedostajuće vrijednosti i ekstremne vrijednosti (outlieri) | Jupyter pod |

Nove vježbe dodavat će se tijekom semestra u nove mape (`EX_6/`, `EX_7/` …), pa prije svake vježbe povucite najnoviju verziju (vidi dolje).

## Struktura repozitorija

```
Podatkovno-inzenjerstvo-2026-2027/
├─ README.md            ← ova datoteka
├─ okruzenje/           ← YAML datoteke za Podman podove (Jupyter, kasnije i SQL)
└─ EX_n/                ← jedna mapa po vježbi
   ├─ README.md         ← upute za tu vježbu
   ├─ *.ipynb, *.sql, *.py …  ← bilježnice, SQL skripte i drugi kod (ovisno o vježbi)
   ├─ podaci/           ← skupovi podataka (ako ih vježba koristi)
   └─ slike/            ← slike za bilježnice (ako ih ima)
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
4. U pregledniku datoteka pojavit će se mapa `Podatkovno-inzenjerstvo-2026-2027`. Otvorite mapu vježbe i pratite njezin README.

Za vježbe sa SQL-om skripte otvarate u alatu koji ta vježba navodi (npr. pgAdmin). Kako ih prenijeti, piše u README-u te vježbe.

## Prije svake vježbe: povlačenje novosti

U Jupyter terminalu:
```bash
cd Podatkovno-inzenjerstvo-2026-2027
git pull
```
U Jupyter bilježnicama isto možete napraviti i iz bilježnice – prva ćelija je `!git pull`.

## Radite u svojoj kopiji

Prije nego što počnete rješavati zadatke, spremite kopiju datoteke sa zadacima i dodajte nazivu `_moj_rad`:
* bilježnica: **File → Save Notebook As…** → npr. `EX_5_moj_rad.ipynb`,
* SQL skripta ili drugi kod: npr. `EX_6_zadaci_moj_rad.sql`.

Ako mijenjate originalnu datoteku, a nastavnik u međuvremenu objavi ispravak iste datoteke, `git pull` će javiti grešku
(*Your local changes … would be overwritten by merge*). Datoteke s `_moj_rad` u nazivu git ne prati, pa ih `git pull` nikad ne dira.

Ako vam se to ipak dogodi:
```bash
git status          # pokazuje koje ste originalne datoteke promijenili
git stash           # privremeno sklanja vaše izmjene
git pull            # povlači novu verziju
git stash pop       # vraća vaše izmjene (ako javi sukob, spremite svoj rad kao kopiju i ponovite)
```

## Ako `git clone` ne radi

Na GitHubu kliknite **Code → Download ZIP** i raspakirajte arhivu na računalu.
Za Jupyter vježbe mapu vježbe prenesite u Jupyter gumbom **Upload** (datoteke unutar mapa `podaci/` i `slike/` prenesite u iste podmape).
Novosti tada nećete moći povući s `git pull`, nego ponovno preuzimate ZIP.

## Rješenja

Rješenja zadataka nisu u repozitoriju prije vježbe. Ako budu objavljena, nalazit će se u podmapi `rjesenja/` mape te vježbe.

## Izvori podataka

Skupovi podataka preuzeti su s javnih izvora i koriste se isključivo u nastavne svrhe. Izvor je naveden u README-u svake vježbe.
