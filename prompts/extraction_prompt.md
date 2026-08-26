# Prompt per estrazione fact-sheet JSON

Versione: `v0.1`

## Scopo

Estrarre da un articolo giornalistico un fact-sheet strutturato in JSON, adatto a generazione controllata e analisi comparativa.

## Prompt

```text
Leggi l'articolo fornito e restituisci esclusivamente un oggetto JSON valido.

Il JSON deve rappresentare un fact-sheet informativo, senza aggiungere fatti non presenti nel testo.

Campi richiesti:
- source_id: identificativo dell'articolo sorgente, se fornito;
- title: titolo dell'articolo;
- publication_date: data di pubblicazione, se disponibile;
- outlet: testata o fonte, se disponibile;
- author: autore, se disponibile;
- topic: tema principale;
- summary: sintesi fattuale in massimo 120 parole;
- key_facts: lista di fatti verificabili;
- actors: persone, istituzioni, aziende o gruppi citati;
- locations: luoghi citati;
- dates: date o riferimenti temporali citati;
- claims: affermazioni rilevanti attribuite a soggetti;
- evidence: dati, documenti, studi o fonti richiamate;
- uncertainties: aspetti non chiari, controversi o non verificabili dal solo testo;
- ethical_notes: possibili implicazioni etiche, sociali o deontologiche;
- generation_constraints: indicazioni utili per generare un articolo derivato senza introdurre informazioni nuove.

Vincoli:
- Non inventare informazioni.
- Usa null per informazioni non disponibili.
- Mantieni distinzione tra fatti, opinioni, attribuzioni e inferenze.
- Non includere commenti fuori dal JSON.
```
