
import requests
import pandas as pd

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Step 1: Search NCBI Gene for human genes related to DNA repair
search_params = {
    "db": "gene",
    "term": 'DNA repair[All Fields] AND Homo sapiens[Organism]',
    "retmax": 10,
    "retmode": "json"
}

response = requests.get(
    f"{BASE_URL}/esearch.fcgi",
    params=search_params,
    timeout=30
)
response.raise_for_status()

gene_ids = response.json()["esearchresult"]["idlist"]

if not gene_ids:
    print("No genes found. Try adjusting the search.")
    raise SystemExit

print(f"Found {len(gene_ids)} gene IDs.")

# Step 2: Retrieve summaries for those genes
summary_params = {
    "db": "gene",
    "id": ",".join(gene_ids),
    "retmode": "json"
}

response = requests.get(
    f"{BASE_URL}/esummary.fcgi",
    params=summary_params,
    timeout=30
)
response.raise_for_status()

records = response.json()["result"]

# Step 3: Extract useful information
rows = []

for gene_id in gene_ids:
    gene = records.get(gene_id, {})

    rows.append({
        "Gene ID": gene_id,
        "Gene Symbol": gene.get("name", "N/A"),
        "Description": gene.get("description", "N/A")
    })

df = pd.DataFrame(rows)

# Step 4: Display and save the results
print("\nHuman gene records related to DNA repair:\n")
print(df.to_string(index=False))

df.to_csv("dna_repair_genes.csv", index=False)
print("\nResults saved to dna_repair_genes.csv")
