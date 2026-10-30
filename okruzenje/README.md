# Okruženje za vježbe

Sve tehnologije pokrećemo u **Podman** podovima, pa svi rade u istom okruženju kao na nastavi.
Upute za instalaciju (WSL 2, Podman Desktop, Git) dobili ste na početku semestra na platformi kolegija.

| Datoteka | Što pokreće | Za koje vježbe |
|---|---|---|
| [`anaconda_jupyter.yaml`](anaconda_jupyter.yaml) | Jupyter Notebook s Anaconda distribucijom (pandas, numpy, matplotlib, seaborn, scikit-learn …) | EX_5, EX_6 |

## Pokretanje Jupyter poda

1. Preuzmite `anaconda_jupyter.yaml` na računalo (na GitHubu: otvorite datoteku → gumb **Download raw file**).
2. **Podman Desktop → Pods → Play Kubernetes YAML** → odaberite datoteku → **Play**.
   (Ili u terminalu: `podman kube play anaconda_jupyter.yaml`.)
3. Prvo pokretanje preuzima sliku od nekoliko GB – pričekajte da završi.
4. **Containers → jupyter-notebook-anaconda → Logs**: kopirajte adresu oblika `http://127.0.0.1:8888/tree?token=…` i otvorite je u pregledniku.

Datoteke se spremaju u Podman volumen `notebook-storage-pvc` (mapa `/opt/notebooks` u spremniku),
pa ostaju sačuvane i kad zaustavite i ponovno pokrenete pod.

Sljedeći put pod samo pokrenete (**Pods → jupyter-notebook-anaconda → Start**) i ponovno uzmete adresu s tokenom iz Logs.

Kako u pod preuzeti materijale s ovog repozitorija, opisano je u [glavnom README-u](../README.md#prvi-put-preuzimanje-repozitorija).
