# Data Management Plan

## Tipi di dati

- Testi giornalistici originali.
- Fact-sheet JSON.
- Testi generati artificialmente.
- Tabelle di risultati.
- Notebook, script e log sperimentali.

## Conservazione

I dati pubblicabili possono essere versionati nella repository. I dati non redistribuibili devono essere conservati separatamente e descritti tramite metadati, hash e istruzioni di recupero.

## Nomenclatura consigliata

```text
<corpus>_<source-id>_<version>.<ext>
```

Esempi:

```text
original_ART0001_v1.json
pre2022_ART1042_v1.txt
generated_ART0001_prompt-v0.1_model-name_v1.md
```

## Controlli

- Verifica licenze.
- Verifica assenza di dati personali non necessari.
- Validazione JSON.
- Controllo duplicati.
- Tracciamento input-output.
