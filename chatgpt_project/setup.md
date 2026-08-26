# Setup del progetto ChatGPT

Questa pagina descrive la configurazione del progetto ChatGPT usato per estrarre fact-sheet e generare articoli.

## Configurazione da registrare

- Nome del progetto ChatGPT.
- Modello usato.
- Data di creazione o modifica del progetto.
- Istruzioni di sistema o istruzioni progetto.
- File caricati nel progetto.
- Prompt di estrazione: `prompts/extraction_prompt.md`.
- Prompt di generazione: `prompts/generation_prompt.md`.
- Parametri di generazione.
- Eventuali regole di esclusione o revisione manuale.

## Template istruzioni progetto

```text
Questo progetto supporta una ricerca di dottorato su IA, augmented journalism e linguistica computazionale.

Quando estrai fact-sheet:
- restituisci solo JSON valido;
- non inventare informazioni;
- distingui fatti, attribuzioni, opinioni e incertezze;
- conserva riferimenti all'articolo sorgente.

Quando generi articoli:
- usa solo informazioni presenti nel fact-sheet;
- non imitare autori o testate reali;
- segnala che il testo e generato artificialmente per uso di ricerca;
- mantieni tono giornalistico neutro.
```
