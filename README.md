# DNA Repair Gene Explorer

## Overview
This project uses the NCBI E-utilities API to retrieve human gene records related to DNA repair from the NCBI Gene database.

## Research Question
Which human gene records are associated with a search for DNA repair, and what gene symbols and descriptions does NCBI provide?

## API
The project uses NCBI E-utilities:
- **ESearch** retrieves gene record IDs matching the search query.
- **ESummary** retrieves summaries for those gene records.

Documentation: https://www.ncbi.nlm.nih.gov/books/NBK25501/

## Implementation
The Python script uses `requests` to make API requests and `pandas` to organize the returned information into a table. It prints selected fields and saves the results to a CSV file.

## Requirements
- Python 3
- requests
- pandas

Install dependencies with:

`pip install requests pandas`

## How to Run
Run the following command from the project directory:

`python dna_repair_explorer.py`

The script displays selected gene information and creates `dna_repair_genes.csv`.

## Limitations
The search uses a broad text query. Returned records should be interpreted as matches to the search, rather than as a definitive list of experimentally confirmed DNA-repair genes.

