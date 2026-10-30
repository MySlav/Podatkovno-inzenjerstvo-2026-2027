# Vježba 5 – Dimenzijsko modeliranje u praksi: star shema, snowflake i SCD

Vezano uz predavanje: **1. prezentacija** (podatkovna skladišta, dimenzijsko modeliranje) i **radni list 3 – Star vs. Snowflake** (maloprodajni lanac MarketPlus).
Trajanje: 90 minuta. Okruženje: [Jupyter pod](../okruzenje/README.md). Baza je SQLite, koji dolazi s Pythonom, pa **ne treba dodatni pod**.

## Nakon vježbe znat ćete

* primijeniti korake dimenzijskog modeliranja i odrediti granularnost tablice činjenica,
* izgraditi star shemu: dimenzije sa surogatnim ključevima i tablicu činjenica,
* pisati analitičke upite po obrascu „fact + JOIN dimenzija + GROUP BY” (upiti su pripremljeni, popunjavate označena mjesta),
* usporediti star i snowflake shemu,
* prepoznati vrijednost koja nije na granularnosti tablice i izbjeći krivi zbroj,
* razlikovati SCD 1, 2 i 3 te implementirati SCD 2 i učitati novu prodaju uz verziju dimenzije koja je vrijedila na datum prodaje.

## Sadržaj mape

| Datoteka / mapa | Opis |
|---|---|
| `EX_5_Dimenzijsko_modeliranje_MarketPlus.ipynb` | bilježnica s teorijom, demo kodom i zadacima |
| `provjere.py` | provjere zadataka koje bilježnica poziva u ćelijama ✅ (ne treba je otvarati ni mijenjati) |
| `podaci/prodaja_sirovo.csv` | sirova prodaja od 5. 3. do 31. 5. 2026. |
| `podaci/nova_prodaja.csv` | prodaja za lipanj i srpanj (novo učitavanje) |
| `podaci/promjene_kupaca.csv`, `promjene_proizvoda.csv` | promjene za SCD zadatke |
| `podaci/dim_kupac_scd2.csv` | gotova dimenzija kupca nakon promjena |
| `podaci/marketplus_gotovo.db`, `marketplus_scd2_gotovo.db` | gotove SQLite baze od kojih kreću kasnije cjeline |

Bilježnica u mapi vježbe stvara `marketplus.db` i `marketplus_rad.db`. To su vaše radne baze, git ih ne prati i možete ih slobodno obrisati.

## Kako krenuti

1. Povucite novosti (`git pull`) – vidi [glavni README](../README.md#prije-svake-vježbe-povlačenje-novosti).
2. Otvorite `EX_5_Dimenzijsko_modeliranje_MarketPlus.ipynb` i odmah ga spremite kao **`EX_5_moj_rad.ipynb`** (File → Save Notebook As…).
3. Ćelije pokrećite redom. Upute su u bilježnici:
   * 📖 teorija (s brojem slajda s predavanja),
   * ▶️ demo,
   * 🧩 zadatak – zamijenite `...` ili `___` svojim kodom,
   * ✅ provjera – ispisuje ✅ ili objašnjava što ne valja,
   * ✏️ odgovor u markdown ćeliji,
   * ⭐ dodatni zadatak.

SQL još ne trebate znati: upiti su pripremljeni, a vi popunjavate označena mjesta.

## Cjeline

| # | Cjelina | ≈ min |
|---|---|---|
| 0 | Priprema okruženja | 4 |
| 1 | SQLite u dvije minute i sirovi podaci | 6 |
| 2 | Pet koraka dimenzijskog modeliranja | 10 |
| 3 | Gradnja star sheme | 20 |
| 4 | Analitički upiti nad star shemom | 10 |
| 5 | Snowflake shema | 8 |
| 6 | Zamka granulacije | 7 |
| 7 | Sporo mijenjajuće dimenzije (SCD) | 25 |
| 8 | ⭐ Završni zadatak: SCD 2 za proizvod | doma |
| 9 | Neobavezno: veza sa SQL podom | – |

Završni zadatak (cjelina 8) nije obavezan i ne predaje se. Cjelina 9 je samo za one koji su već pokrenuli SQL pod.

## Podaci

Podaci su **izmišljeni** za potrebe vježbe. Prva četiri retka sirove prodaje iste su prodaje kao u radnom listu 3.
