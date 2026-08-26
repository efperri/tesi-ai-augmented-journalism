# Tesi di dottorato: IA, augmented journalism e linguistica computazionale

Repository di lavoro per una tesi di dottorato su intelligenza artificiale e augmented journalism, con analisi di linguistica computazionale, generazione controllata di articoli tramite fact-sheet e valutazioni etiche.

## Obiettivi

Questa repository organizza materiali, procedure e risultati relativi a:

- corpus di articoli giornalistici originali;
- fact-sheet JSON estratti dagli articoli;
- articoli generati con ChatGPT a partire dai fact-sheet;
- corpus di articoli pre-2022 per analisi comparative su testi prodotti prima della diffusione mainstream dell'IA generativa;
- fact-sheet JSON e articoli generati a partire dal corpus pre-2022;
- prompt, setup del progetto ChatGPT e parametri di generazione;
- risultati completi in XLS, CSV e altri formati;
- documentazione metodologica, riproducibilita, provenienza dati, licenze e note etiche.

## Struttura della repository

```text
.
├── chatgpt_project/
├── data/
│   ├── original_articles/
│   ├── factsheets/original/
│   ├── generated_articles/original_factsheets/
│   └── pre_2022/
├── docs/
├── metadata/
├── notebooks/
├── prompts/
├── results/
└── scripts/
```

## Dati previsti

- `data/original_articles/`: articoli giornalistici usati come base di partenza.
- `data/factsheets/original/`: JSON estratti dagli articoli originali.
- `data/generated_articles/original_factsheets/`: articoli generati via ChatGPT dai fact-sheet originali.
- `data/pre_2022/original_articles/`: corpus storico pre-2022.
- `data/pre_2022/factsheets/`: fact-sheet JSON estratti dal corpus pre-2022.
- `data/pre_2022/generated_articles/`: articoli generati dai fact-sheet pre-2022.

Prima di caricare articoli integrali, verificare copyright, termini di riuso, consenso e possibilita di redistribuzione. Quando la redistribuzione non e consentita, conservare nella repository solo metadati, hash, URL, estratti minimi consentiti o istruzioni di recupero.

## Workflow sintetico

1. Registrare ogni fonte in `metadata/source_register_template.csv`.
2. Inserire o indicizzare gli articoli nei percorsi appropriati sotto `data/`.
3. Estrarre i fact-sheet con il prompt in `prompts/extraction_prompt.md`.
4. Validare i JSON con `scripts/validate_factsheets.py`.
5. Generare articoli sintetici con il prompt in `prompts/generation_prompt.md`.
6. Salvare risultati, metriche e tabelle in `results/`.
7. Documentare modifiche metodologiche in `docs/methodology.md` e `docs/reproducibility.md`.

## Riproducibilita

Le istruzioni di riproducibilita sono in `docs/reproducibility.md`. Ogni run sperimentale dovrebbe indicare data, modello, versione del prompt, parametri di generazione, input, output e note su interventi manuali.

## Etica e responsabilita

Le note etiche sono in `docs/ethics.md`. La repository distingue tra testi giornalistici originali, strutture informative estratte e testi generati artificialmente. Ogni output sintetico deve restare identificabile come generato o derivato da generazione assistita.

## Licenze

Il codice e la documentazione sono rilasciati secondo `LICENSE`, salvo diversa indicazione. I dati possono avere licenze e vincoli separati: vedere `LICENSES_AND_DATA_PROVENANCE.md`.
