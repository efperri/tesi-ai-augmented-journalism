# Licenze e provenienza dei dati

Questa pagina documenta la provenienza, i diritti e i vincoli di riuso dei materiali usati nella ricerca.

## Principi

- Separare sempre codice, documentazione, dati originali, dati derivati e output generati.
- Non pubblicare articoli integrali quando copyright, termini editoriali o accordi di accesso non lo consentono.
- Preferire metadati, identificativi persistenti, URL, hash crittografici e istruzioni di recupero quando il testo completo non e redistribuibile.
- Segnalare chiaramente i testi generati artificialmente.
- Conservare una traccia delle trasformazioni applicate a ogni documento.

## Registro minimo per ogni fonte

Per ogni articolo o fonte, compilare `metadata/source_register_template.csv` con identificativo interno, titolo, testata, autore se disponibile, data di pubblicazione, URL o riferimento, data di accesso, licenza o termini d'uso, stato di redistribuzione e note su restrizioni.

## Tipi di materiale

| Tipo | Percorso | Licenza prevista | Redistribuzione |
| --- | --- | --- | --- |
| Articoli originali | `data/original_articles/` | Da verificare fonte per fonte | Solo se consentita |
| Fact-sheet JSON | `data/factsheets/original/` | Derivata dai vincoli delle fonti | Da valutare |
| Articoli generati | `data/generated_articles/original_factsheets/` | Da definire | Consentita solo con chiara etichettatura |
| Corpus pre-2022 | `data/pre_2022/original_articles/` | Da verificare fonte per fonte | Solo se consentita |
| Risultati aggregati | `results/` | Preferibilmente aperta | Di norma pubblicabile se non ricostruisce testi protetti |
