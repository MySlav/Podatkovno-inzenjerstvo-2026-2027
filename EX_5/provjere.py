"""Provjere zadataka za Vježbu 5.

Bilježnica poziva funkcije iz ove datoteke u ćelijama "✅ Provjera".
Očekivani rezultati spremljeni su kao sažeci (hash), a ne kao brojevi – rješenje morate izračunati sami.
Ako nakon `git pull` dobijete novu verziju ove datoteke, ponovno pokrenite ćelije cjeline 0.
"""
import hashlib
import sqlite3

import numpy as np
import pandas as pd

_OCEKIVANO = {'z10_kat': 'b73be535cc1bf5a1',
 'z10_redaka': 'cf22d5a7596393a0',
 'z1_mjere': '8c4c22fcbc2386c8',
 'z2_kupaca': 'b47825c26fb4e368',
 'z4': '0c7c37d18e2d629c',
 'z5': '7b717fe6b7101e40',
 'z6': '4fae6c7d0dce2934',
 'z7_redaka': 'd833e06acdb74b8a',
 'z8_iznos': '64e67eb35c696e94',
 'z8_k3': 'edd4049cc1c266b3'}


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
    return hashlib.sha256(("ex5m|" + _norm(x)).encode("utf-8")).hexdigest()[:16]


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


def _izvrsi_upit(sql, upit):
    _nije_rijeseno(upit)
    if "___" in upit:
        raise AssertionError("❌ Zadatak još nije riješen – popuni sva mjesta označena s ___ i ponovno pokreni ćeliju zadatka.")
    try:
        return sql(upit)
    except Exception as greska:
        raise AssertionError(f"❌ Upit se ne može izvršiti: {str(greska).splitlines()[0][:150]}")


def zadatak_1(prodaja, stupci_granulacije, mjere):
    _nije_rijeseno(stupci_granulacije, mjere)
    stupci = list(stupci_granulacije)
    _provjeri(_sigurno(lambda: prodaja.duplicated(subset=stupci).sum() == 0),
              "a) Ti stupci ne određuju redak jednoznačno – neke se kombinacije ponavljaju.")
    _provjeri(len(stupci) <= 2, "a) Dovoljna su dva stupca: koji račun i koja stavka na njemu?")
    _provjeri(_tocno("z1_mjere", sorted(mjere)),
              "b) Mjere se zbrajaju i svaka stavka ima svoju vrijednost. Što se događa s popust_racuna na računu s više stavki?")


def zadatak_2(dim_kupac_df):
    _nije_rijeseno(dim_kupac_df)
    _provjeri(isinstance(dim_kupac_df, pd.DataFrame), "dim_kupac_df treba biti DataFrame.")
    _provjeri(list(dim_kupac_df.columns) == ["kupac_key", "sifra_kupca", "kupac", "grad"],
              "Stupci trebaju biti redom: kupac_key, sifra_kupca, kupac, grad. Ako nedostaje kupac_key, dovrši drugi TODO.")
    _provjeri(_tocno("z2_kupaca", len(dim_kupac_df)), "Krivi broj redaka – svaki kupac smije se pojaviti samo jednom (drop_duplicates).")
    _provjeri(dim_kupac_df["kupac_key"].is_unique and dim_kupac_df["kupac_key"].min() == 1,
              "kupac_key mora biti jedinstven i počinjati od 1.",
              "✅ Točno! Dimenzija kupca je gotova.")


def zadatak_3(f, prodaja):
    _nije_rijeseno(f)
    _provjeri(isinstance(f, pd.DataFrame) and {"proizvod_key", "kupac_key"} <= set(f.columns),
              "Tablica treba imati stupce proizvod_key i kupac_key – dovrši oba merge.")
    _provjeri(len(f) == len(prodaja), "Broj redaka se promijenio: merge ne smije izgubiti ni udvostručiti retke. Provjeri dimenziju.")
    _provjeri(f[["proizvod_key", "kupac_key", "trgovina_key"]].notna().all().all(), "Neki ključevi su prazni.")
    _provjeri(np.isclose(f["iznos"].sum(), prodaja["iznos"].sum()), "Ukupan iznos se promijenio.",
              "✅ Točno! Poslovni ključevi zamijenjeni su surogatnim, a broj redaka i ukupan iznos su isti.")


def zadatak_4(sql, upit):
    r = _izvrsi_upit(sql, upit)
    _provjeri(list(r.columns) == ["naziv_mjeseca", "grad", "prihod"], "Rezultat treba imati stupce naziv_mjeseca, grad, prihod.")
    _provjeri(_tocno("z4", sorted(round(float(v), 2) for v in r["prihod"])),
              "Brojevi nisu dobri. Zbrajamo iznos, a trgovinu spajamo po trgovina_key.",
              "✅ Točno! Upit ima uvijek isti oblik: fact + JOIN dimenzija + GROUP BY.")
    return r


def zadatak_5(sql, upit):
    r = _izvrsi_upit(sql, upit)
    _provjeri(_tocno("z5", sorted(round(float(v), 2) for v in r["prihod"])),
              "Brojevi nisu dobri. Pod-dimenzija je dim_grad, a spaja se po grad_key.",
              "✅ Točno! Rezultat je isti kao u star shemi, ali uz jedno spajanje više.")
    return r


def zadatak_6(stvarni_popust):
    _nije_rijeseno(stvarni_popust)
    _provjeri(_tocno("z6", stvarni_popust), "Nije dobro: svaki račun mora se brojati jednom – drop_duplicates(subset='broj_racuna').",
              f"✅ Točno! Stvarni popust je {float(stvarni_popust):.2f} €.")


def zadatak_7(conn, primijeni_scd2, promjene):
    kopija = sqlite3.connect(":memory:")
    conn.backup(kopija)
    try:
        for _, p in promjene.iterrows():
            primijeni_scd2(kopija, p["sifra_kupca"], p["novi_grad"], p["datum_promjene"])
    except sqlite3.Error as greska:
        tekst = str(greska)
        if "___" in tekst or "near" in tekst or "no such column" in tekst:
            raise AssertionError("❌ Zadatak još nije riješen – popuni sva mjesta označena s ___ u funkciji primijeni_scd2.")
        raise AssertionError("❌ Greška u SQL-u: " + tekst[:150])
    d = pd.read_sql_query("SELECT * FROM dim_kupac ORDER BY kupac_key", kopija)
    k1 = d[d["sifra_kupca"] == "K001"].sort_values("valid_from")
    _provjeri(_tocno("z7_redaka", len(d)), "Krivi broj redaka: svaka promjena mora dodati točno jedan redak.")
    _provjeri(d["kupac_key"].is_unique, "kupac_key se ponavlja.")
    _provjeri(_sigurno(lambda: k1["is_current"].tolist() == [0, 1] and k1["valid_to"].iloc[1] == "9999-12-31"),
              "Stari redak treba imati is_current = 0, a novi is_current = 1 i valid_to = 9999-12-31.")
    _provjeri(_sigurno(lambda: k1["valid_to"].iloc[0] == "2026-05-31" and k1["valid_from"].iloc[1] == "2026-06-01"),
              "Razdoblja se ne smiju preklapati: stari redak završava dan prije nego što novi počinje.")
    _provjeri(d.groupby("sifra_kupca")["is_current"].sum().eq(1).all(), "Svaki kupac mora imati točno jedan trenutni redak.",
              "✅ Točno! Kupac ima dvije verzije, a povijest je sačuvana.")
    print(k1[["kupac_key", "sifra_kupca", "grad", "valid_from", "valid_to", "is_current"]].to_string(index=False))


def zadatak_8(nova_prodaja, nova_s_kljucem):
    _nije_rijeseno(nova_s_kljucem)
    _provjeri(len(nova_s_kljucem) == len(nova_prodaja),
              "Svaka stavka mora imati točno jednu verziju kupca. Uvjet: datum >= valid_from I datum <= valid_to.")
    k1 = nova_s_kljucem[nova_s_kljucem["sifra_kupca"] == "K003"]
    _provjeri(_tocno("z8_k3", sorted(int(v) for v in k1["kupac_key"].unique())),
              "Kupac K003 selio se u srpnju, pa mora imati dvije verzije ključa.")
    _provjeri(_tocno("z8_iznos", round(float(nova_s_kljucem.groupby("kupac_key")["iznos"].sum().max()), 2)),
              "Ključevi nisu dobro dodijeljeni. Provjeri granice uvjeta (uključivo).",
              "✅ Točno! Svaka stavka dobila je verziju kupca koja je vrijedila na datum prodaje.")


def zadatak_10(sql, nova_prodaja, nova_s_proizvodom):
    def korak(opis, test):
        uspjeh = _sigurno(test)
        print(("✅ " if uspjeh else "❌ ") + opis)
        return uspjeh

    d = sql("SELECT * FROM dim_proizvod")
    p = d[d["sifra_proizvoda"] == "P003"].sort_values("valid_from")
    rezultati = [
        korak("1) P003 ima dvije verzije", lambda: len(p) == 2 and p["proizvod_key"].is_unique),
        korak("2) stari redak je zatvoren dan prije promjene", lambda: p["valid_to"].iloc[0] == "2026-05-31" and p["is_current"].iloc[0] == 0),
        korak("3) novi redak je trenutni i ima novu kategoriju", lambda: _tocno("z10_kat", p["kategorija"].iloc[1])
              and p["is_current"].iloc[1] == 1 and p["valid_to"].iloc[1] == "9999-12-31"),
        korak("4) ostali proizvodi su netaknuti", lambda: _tocno("z10_redaka", len(d))),
        korak("5) nova prodaja ima po jedan redak za svaku stavku", lambda: nova_s_proizvodom is not ... and len(nova_s_proizvodom) == len(nova_prodaja)),
        korak("6) sva nova prodaja soka ima ključ nove verzije",
              lambda: set(nova_s_proizvodom.loc[nova_s_proizvodom["sifra_proizvoda"] == "P003", "proizvod_key"]) == {int(p["proizvod_key"].iloc[1])}),
    ]
    print(f"\n{sum(rezultati)}/{len(rezultati)} koraka točno")
