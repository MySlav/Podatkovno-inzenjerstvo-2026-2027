"""Provjere zadataka za Vježbu 6.

Bilježnica poziva funkcije iz ove datoteke u ćelijama "✅ Provjera".
Očekivani rezultati spremljeni su kao sažeci (hash), a ne kao brojevi – rješenje morate izračunati sami.
Ako nakon `git pull` dobijete novu verziju ove datoteke, ponovno pokrenite ćelije cjeline 0.
"""
import hashlib

import numpy as np
import pandas as pd

_OCEKIVANO = {'z1_broj': 'c3f66ebb96dde64a',
 'z1_godina': 'cdca8820438008a7',
 'z2_cabin': 'a24754f2eb361895',
 'z2_embarked': '8efc3331500e01fc',
 'z2d': '2e59135480d67aba',
 'z3_postotak': '0f9f891e77d3852a',
 'z3_redaka': 'cb413b3dfc8283cd',
 'z3_svi': '2746a8bf7a522080',
 'z4_indikator': 'ce7997bc350e7fa6',
 'z4_medijani': '35fcd3ac558fed5f',
 'z4_redak5': '23204079de0215d0',
 'z5b_preostalo': '97329ec779c0cf2d',
 'z6_granice': 'd24c3d43590ebc78',
 'z6_z': '96ce644edada39f0',
 'z7_2000': 'cb6a5ceebed97625',
 'z7_elektricni': 'aec04af1827d5336',
 'z7_ford': '0e8323ade9a18a4b',
 'z9_cilindri': '76d3b2b1c1c3c67b',
 'z9_hp': 'cfe619377063b232',
 'z9_max': 'db1f5740bb87acd9',
 'z9_msrp': '99eab6f9b8f8efc8',
 'z9_redaka': '37f1cdc7a7bc31a7'}


# ---------------------------------------------------------------- pomoćne funkcije

def _norm(x):
    if isinstance(x, (list, tuple, np.ndarray, pd.Series)):
        return "(" + ",".join(_norm(v) for v in list(x)) + ")"
    if isinstance(x, (bool, np.bool_)):
        return str(bool(x))
    if isinstance(x, (int, float, np.integer, np.floating)):
        v = float(x)
        if v != v:
            return "nan"
        return f"{round(v, 3) + 0.0:.3f}"
    return str(x)


def _sazetak(x):
    return hashlib.sha256(("ex5|" + _norm(x)).encode("utf-8")).hexdigest()[:16]


def _tocno(kljuc, vrijednost):
    try:
        return _sazetak(vrijednost) == _OCEKIVANO[kljuc]
    except Exception:
        return False


def _nije_rijeseno(*vrijednosti):
    if any(v is ... for v in vrijednosti):
        raise AssertionError("❌ Zadatak još nije riješen – zamijeni `...` svojim kodom i ponovno pokreni ćeliju zadatka.")


def _provjeri(uvjet, poruka_greske, poruka_ok="✅ Točno!"):
    if not uvjet:
        raise AssertionError("❌ " + poruka_greske)
    print(poruka_ok)


def _sigurno(test):
    try:
        return bool(test())
    except Exception:
        return False


# ---------------------------------------------------------------- 1. kvaliteta podataka

def zadatak_1(broj_cijena_2000, najnovija_godina_2000):
    _nije_rijeseno(broj_cijena_2000, najnovija_godina_2000)
    _provjeri(_tocno("z1_broj", broj_cijena_2000),
              "a) Broj nije dobar – usporedi stupac MSRP s 2000 i zbroji True vrijednosti.")
    _provjeri(_tocno("z1_godina", najnovija_godina_2000),
              "b) Godina nije dobra – filtriraj retke s MSRP == 2000 i uzmi max stupca Year.",
              "✅ Točno! Nijedan automobil noviji od te godine nema cijenu 2000 – to nije cijena, nego oznaka 'cijena nepoznata'.")


# ---------------------------------------------------------------- 3. MCAR / MAR / MNAR

def zadatak_2(cabin_po_klasi, embarked_nedostaje):
    _nije_rijeseno(cabin_po_klasi, embarked_nedostaje)
    _provjeri(isinstance(cabin_po_klasi, pd.Series) and len(cabin_po_klasi) == 3,
              "a) cabin_po_klasi treba biti Series s po jednom vrijednošću za svaku klasu – grupiraj isna() po titanic['Pclass'].")
    _provjeri(_tocno("z2_cabin", cabin_po_klasi.sort_index()),
              "a) Udjeli nisu dobri – trebaju biti udjeli između 0 i 1 (srednja vrijednost od isna()), kao u demu za Age.")
    _provjeri(isinstance(embarked_nedostaje, pd.DataFrame) and _tocno("z2_embarked", len(embarked_nedostaje)),
              "b) Krivi retci – filtriraj titanic maskom titanic['Embarked'].isna().")


def zadatak_2d(prezivljavanje_po_age):
    _nije_rijeseno(prezivljavanje_po_age)
    _provjeri(_sigurno(lambda: _tocno("z2d", [prezivljavanje_po_age.loc[False], prezivljavanje_po_age.loc[True]])),
              "Grupiraj titanic po titanic['Age'].isna() i uzmi srednju vrijednost stupca 'Survived'.",
              "✅ Točno! Putnici bez upisane dobi preživljavali su rjeđe. Sama činjenica da podatak nedostaje nosi "
              "informaciju – zato ćemo u cjelini 5 dodati indikator nedostajanja (sl. 64–66).")


# ---------------------------------------------------------------- 4. brisanje

def zadatak_3(titanic_bez_age_nan, titanic_bez_cabin, postotak_izgubljenih):
    _nije_rijeseno(titanic_bez_age_nan, titanic_bez_cabin, postotak_izgubljenih)
    print("a)", titanic_bez_age_nan.shape, " b)", titanic_bez_cabin.shape, " c)", round(float(postotak_izgubljenih), 2), "%")
    _provjeri(_tocno("z3_redaka", len(titanic_bez_age_nan)) and titanic_bez_age_nan["Age"].notna().all(),
              "a) Obriši samo retke kojima nedostaje Age – dropna(subset=['Age']).")
    _provjeri("Cabin" not in titanic_bez_cabin.columns and _tocno("z3_svi", len(titanic_bez_cabin)),
              "b) Stupac Cabin mora nestati, a broj redaka ostati isti – drop(columns=['Cabin']).")
    _provjeri(_tocno("z3_postotak", postotak_izgubljenih),
              "c) Usporedi len(titanic) i len(titanic.dropna()) i pretvori razliku u postotak (0–100).",
              "✅ Točno! Gubimo većinu putnika, i to uglavnom zbog stupca Cabin. Slijepi dropna() je loša ideja.")


# ---------------------------------------------------------------- 5. imputacija

def zadatak_4(titanic_imp, medijan_po_klasi):
    _nije_rijeseno(medijan_po_klasi)
    _provjeri(_sigurno(lambda: _tocno("z4_medijani", medijan_po_klasi.sort_index())),
              "Medijani po klasi nisu dobri – groupby('Pclass')['Age'].median().")
    _provjeri(_sigurno(lambda: _tocno("z4_indikator", titanic_imp["Age_nedostaje"].astype(bool).sum())),
              "Age_nedostaje treba biti True točno za putnike bez dobi – je li napravljen PRIJE popunjavanja?")
    _provjeri(_sigurno(lambda: titanic_imp["Age"].isna().sum() == 0), "U stupcu Age još ima NaN vrijednosti.")
    _provjeri(_sigurno(lambda: _tocno("z4_redak5", titanic_imp.loc[5, "Age"])),
              "Putnik u retku 5 je u 3. klasi i nema dob – trebao bi dobiti medijan 3. klase.",
              "✅ Točno! Svaki putnik dobio je medijan svoje klase, a stupac Age_nedostaje čuva informaciju o tome tko je imao prazninu.")


def zadatak_4b(titanic_test, titanic_test_imp, medijan_po_klasi):
    _nije_rijeseno(titanic_test_imp["Age"].iloc[0])
    popunjeni = titanic_test["Age"].isna()
    _provjeri(titanic_test_imp["Age"].isna().sum() == 0, "U test skupu još ima NaN vrijednosti u stupcu Age.")
    ocekivano = titanic_test.loc[popunjeni, "Pclass"].map(medijan_po_klasi)
    _provjeri(_sigurno(lambda: np.allclose(titanic_test_imp.loc[popunjeni, "Age"].astype(float), ocekivano)),
              "Popunjene vrijednosti ne odgovaraju medijanima iz TRAIN skupa (medijan_po_klasi). "
              "Medijane test skupa ne smijemo koristiti.",
              "✅ Točno! Test skup popunjen je onim što smo 'naučili' na train skupu – bez curenja podataka.")


# ---------------------------------------------------------------- 6. vremenski nizovi

def zadatak_5(zrak, zrak_ffill, zrak_naivno, stupci):
    _nije_rijeseno(zrak_ffill[stupci[0]].iloc[0])
    nan_prije = zrak[stupci].isna().sum().sum()
    _provjeri(zrak_ffill[stupci].isna().sum().sum() < nan_prije, "Ništa nije popunjeno – jesi li pozvao/la ffill()?")
    prvi_prije = zrak.groupby("City").head(1)[stupci].isna().sum().sum()
    prvi_poslije = zrak_ffill.groupby("City").head(1)[stupci].isna().sum().sum()
    _provjeri(prvi_poslije == prvi_prije,
              "Prvi dan nekog grada dobio je vrijednost iz PRETHODNOG grada – grupiraj po 'City' prije ffill().")
    _provjeri(zrak_ffill.loc[zrak_ffill["City"] == "Aizawl", "Xylene"].isna().all(),
              "Aizawl ne bi smio imati nijednu vrijednost Xylene.",
              "✅ Točno! Vrijednosti se prenose samo unutar istog grada.")
    print("Naivno popunjeno ćelija:", (zrak[stupci].isna() & zrak_naivno[stupci].notna()).sum().sum(),
          "| ispravno popunjeno:", (zrak[stupci].isna() & zrak_ffill[stupci].notna()).sum().sum())


def zadatak_5b(zrak, aqi_interp):
    _nije_rijeseno(aqi_interp)
    nan_prije = zrak["AQI"].isna().sum()
    _provjeri(aqi_interp.isna().sum() < nan_prije, "Ništa nije popunjeno.")
    _provjeri(aqi_interp[zrak["City"] == "Mumbai"].isna().sum() > 1000,
              "Mumbai je popunjen predugo – postavi limit=7 i limit_area='inside'.")
    _provjeri(_tocno("z5b_preostalo", aqi_interp.isna().sum()),
              "Nije dobro – interpoliraj unutar svakog grada (groupby('City')['AQI'].transform(...)), "
              "s limit=7 i limit_area='inside'.",
              f"✅ Točno! Popunjeno {nan_prije - aqi_interp.isna().sum()} od {nan_prije} praznina; "
              "dugačke rupe ostaju NaN, jer bismo ih inače izmislili.")


# ---------------------------------------------------------------- 7. ekstremne vrijednosti

def zadatak_6(iqr_granice, z_vrijednosti, sample):
    _nije_rijeseno(iqr_granice(sample), z_vrijednosti(sample))
    donja, gornja = iqr_granice(sample)
    z = np.asarray(z_vrijednosti(sample), dtype=float)
    print("IQR granice:", donja, gornja)
    print("Z-vrijednosti:", np.round(z, 2))
    _provjeri(_tocno("z6_granice", [donja, gornja]),
              "IQR granice nisu dobre – q1 i q3 su np.percentile(podaci, 25) i (…, 75); granice su q1 − k·IQR i q3 + k·IQR. "
              "Usporedi s ručnim izračunom iz radnog lista 6.1.")
    _provjeri(_tocno("z6_z", z[1]),
              "Z-vrijednost za 101 nije dobra – (x − np.mean) / np.std (np.std računa populacijsku standardnu devijaciju).")
    print("Ekstremne po IQR:", sample[(sample < donja) | (sample > gornja)])
    print("Ekstremne po Z (|z| > 3):", sample[np.abs(z) > 3])


def zadatak_7(fordovi_uklonjeno, fordovi_ukupno, elektricni_uklonjeno, elektricni_ukupno, cijena_2000_ostalo):
    _nije_rijeseno(fordovi_uklonjeno, fordovi_ukupno, elektricni_uklonjeno, elektricni_ukupno, cijena_2000_ostalo)
    _provjeri(_tocno("z7_ford", [fordovi_uklonjeno, fordovi_ukupno]),
              "a) Usporedi stupac Make s 'Ford' u tablicama uklonjeni i auti_bd i zbroji.")
    _provjeri(_tocno("z7_elektricni", [elektricni_uklonjeno, elektricni_ukupno]),
              "b) Usporedi stupac 'Engine Fuel Type' s 'electric' u obje tablice.")
    _provjeri(_tocno("z7_2000", cijena_2000_ostalo),
              "c) Broji MSRP == 2000 u tablici auti_slijepo (to su oni koje IQR NIJE uklonio).",
              f"✅ Točno! Uklonjeno je {fordovi_uklonjeno} od {fordovi_ukupno} Fordova i {elektricni_uklonjeno} od "
              f"{elektricni_ukupno} električnih automobila, a {cijena_2000_ostalo} lažnih cijena od 2000 je ostalo.")


# ---------------------------------------------------------------- 9. završni zadatak

def zadatak_9(auti, silver):
    def korak(opis, test):
        uspjeh = _sigurno(test)
        print(("✅ " if uspjeh else "❌ ") + opis)
        return uspjeh

    el = silver["Engine Fuel Type"] == "electric"
    rezultati = [
        korak("0) ulazna tablica auti nije promijenjena",
              lambda: auti.shape == (11914, 16) and _tocno("z1_broj", (auti["MSRP"] == 2000).sum())),
        korak("1) nema potpunih duplikata",
              lambda: _tocno("z9_redaka", len(silver))),
        korak("2) stupac MSRP_nepoznat postoji, nema više cijene 2000",
              lambda: _tocno("z9_msrp", silver["MSRP_nepoznat"].astype(bool).sum())
                      and (silver["MSRP"] == 2000).sum() == 0
                      and silver["MSRP"].isna().sum() == silver["MSRP_nepoznat"].astype(bool).sum()),
        korak("3) nema benzinaca s highway MPG > 60, električni netaknuti",
              lambda: silver.loc[~el, "highway MPG"].max() <= 60 and silver.loc[el, "highway MPG"].min() > 60),
        korak("4) električni automobili imaju 0 cilindara, Mazde RX ostaju NaN",
              lambda: silver.loc[el, "Engine Cylinders"].eq(0).all()
                      and silver.loc[silver["Engine Cylinders"].isna(), "Model"].isin(["RX-7", "RX-8"]).all()
                      and _tocno("z9_cilindri", silver["Engine Cylinders"].isna().sum())),
        korak("5) Engine HP bez NaN, indikator Engine_HP_nedostaje postoji",
              lambda: silver["Engine HP"].isna().sum() == 0
                      and _tocno("z9_hp", silver["Engine_HP_nedostaje"].astype(bool).sum())),
        korak("6) najskuplji automobili su i dalje u tablici, log_MSRP postoji",
              lambda: _tocno("z9_max", silver["MSRP"].max())
                      and np.isclose(silver["log_MSRP"].max(), np.log10(silver["MSRP"].max()))),
    ]
    print(f"\n{sum(rezultati)}/{len(rezultati)} koraka točno")
