# Riproducibilita

## Ambiente

Installare le dipendenze Python:

```bash
pip install -r requirements.txt
```

## Validazione fact-sheet

```bash
python scripts/validate_factsheets.py data/factsheets/original
python scripts/validate_factsheets.py data/pre_2022/factsheets
```

## Registro delle run

Per ogni sessione di estrazione o generazione registrare:

- identificativo della run;
- data e ora;
- modello;
- versione del prompt;
- parametri;
- input;
- output;
- operatore o procedura;
- note su errori o interventi manuali.

## Versionamento

- Aggiornare i prompt solo con nuova versione esplicita.
- Non sovrascrivere output sperimentali gia analizzati senza registrare la modifica.
- Conservare risultati aggregati in `results/` con nomi file datati o versionati.
