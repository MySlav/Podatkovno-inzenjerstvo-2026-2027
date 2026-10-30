# Vježba 6 – Nedostajuće vrijednosti i ekstremne vrijednosti (outlieri)

Vezano uz predavanje: **2. prezentacija – Rad s nedostajućim podacima** (kvaliteta podataka, nedostajuće vrijednosti, ekstremne vrijednosti).
Trajanje: 90 minuta. Okruženje: [Jupyter pod](../okruzenje/README.md).

## Nakon vježbe znat ćete

* brzo pregledati tablicu (`info`, `describe`, `isna`, `duplicated`, `value_counts`) i prepoznati koja je dimenzija kvalitete podataka narušena,
* iz podataka procijeniti je li nedostajanje MCAR ili MAR (udio nedostajućih vrijednosti po skupinama),
* odabrati između brisanja i imputacije (srednja vrijednost, medijan, mod, konstanta, imputacija po skupini, indikator nedostajanja) i izbjeći curenje podataka,
* popunjavati vremenske nizove (`ffill`, `bfill`, `interpolate`) unutar svake serije,
* otkriti ekstremne vrijednosti (IQR, Z-vrijednost, kutijasti dijagram) i odlučiti je li riječ o pogrešci ili stvarnoj vrijednosti,
* napisati funkciju za čišćenje podataka (korak Bronze → Silver s vježbe 4) s obrazloženjem svake odluke.

## Sadržaj mape

| Datoteka / mapa | Opis |
|---|---|
| `EX_6_Nedostajuce_vrijednosti_i_outlieri.ipynb` | bilježnica s teorijom, demo kodom i zadacima |
| `provjere.py` | provjere zadataka koje bilježnica poziva u ćelijama ✅ (ne treba je otvarati ni mijenjati) |
| `podaci/titanic/train.csv`, `test.csv` | putnici Titanica |
| `podaci/air-quality-data-in-india/city_day.csv` | dnevna kvaliteta zraka u 26 indijskih gradova, 2015.–2020. |
| `podaci/cars.csv` | tehnički podaci i cijene automobila |
| `slike/` | dijagrami metoda obrade nedostajućih vrijednosti |

## Kako krenuti

1. Povucite novosti (`git pull`) – vidi [glavni README](../README.md#prije-svake-vježbe-povlačenje-novosti).
2. Otvorite `EX_6_Nedostajuce_vrijednosti_i_outlieri.ipynb` i odmah ga spremite kao **`EX_6_moj_rad.ipynb`** (File → Save Notebook As…).
3. Pokrenite ćelije cjeline 0 – instaliraju biblioteku `missingno` i učitavaju podatke.
4. Ćelije pokrećite redom. Upute su u bilježnici:
   * 📖 teorija (s brojem slajda s predavanja),
   * ▶️ demo,
   * 🧩 zadatak – zamijenite `...` svojim kodom,
   * ✅ provjera – ispisuje ✅ ili objašnjava što ne valja,
   * ✏️ odgovor u markdown ćeliji,
   * ⭐ dodatni zadatak.

## Cjeline

| # | Cjelina | Podaci | ≈ min |
|---|---|---|---|
| 0 | Priprema okruženja | – | 5 |
| 1 | Kvaliteta podataka – brzi pregled | automobili | 7 |
| 2 | Otkrivanje nedostajućih vrijednosti | Titanic | 5 |
| 3 | Vrste nedostajanja: MCAR, MAR, MNAR | Titanic | 10 |
| 4 | Brisanje nedostajućih vrijednosti | Titanic | 6 |
| 5 | Imputacija nedostajućih vrijednosti | Titanic | 12 |
| 6 | Nedostajuće vrijednosti u vremenskim nizovima | kvaliteta zraka | 10 |
| 7 | Ekstremne vrijednosti – otkrivanje i obrada | niz s predavanja | 10 |
| 8 | Ekstremne vrijednosti na stvarnim podacima | automobili | 13 |
| 9 | ⭐ Završni zadatak: od sirovih do očišćenih podataka | automobili | 12 + doma |

Zadaci označeni s ⭐ nisu obavezni na satu. **Završni zadatak (cjelina 9)** započinjemo na satu, a dovršavate ga samostalno kod kuće.
Ne predaje se – ćelija s provjerom za svaki korak ispisuje je li točan.

## Izvori podataka

* Titanic – [Kaggle: Titanic – Machine Learning from Disaster](https://www.kaggle.com/c/titanic)
* Kvaliteta zraka – [Kaggle: Air Quality Data in India (2015–2020)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india), Vopani (Rohan Rao)
* Automobili – [Kaggle: Car Features and MSRP](https://www.kaggle.com/datasets/CooperUnion/cardataset), CooperUnion
* Slike u mapi `slike/` i dio primjera prilagođeni su iz Kaggle bilježnice *A Guide to Handling Missing values in Python* (Parul Pandey).
