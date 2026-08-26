# Prompt per generazione articoli da fact-sheet

Versione: `v0.1`

## Scopo

Generare un articolo giornalistico a partire da un fact-sheet JSON, mantenendo controllo fattuale e tracciabilita.

## Prompt

```text
Usa il fact-sheet JSON fornito per scrivere un articolo giornalistico coerente.

Regole obbligatorie:
- Non introdurre fatti, citazioni, numeri, fonti, luoghi o date non presenti nel fact-sheet.
- Mantieni tono giornalistico informativo.
- Distingui chiaramente fatti accertati, dichiarazioni attribuite e incertezze.
- Non presentare inferenze come fatti.
- Non imitare lo stile di una specifica testata o di un autore reale.
- Non aggiungere link o riferimenti bibliografici inventati.
- Se il fact-sheet contiene lacune informative, scrivi in modo prudente.

Output richiesto:
1. Titolo.
2. Sottotitolo opzionale.
3. Corpo dell'articolo.
4. Breve nota finale per uso di ricerca: "Testo generato artificialmente a partire da fact-sheet strutturato".
```

## Parametri da registrare

- modello;
- data della generazione;
- temperatura o parametro equivalente;
- eventuale seed, se disponibile;
- versione del prompt;
- identificativo del fact-sheet di input.
