
# BioFetcher

BioFetcher is a Python package that allows you to download bioinformatics data, including PDB, FASTA, and EMDB files. It also includes utilities to extract resolutions for EMDB data and check if a PDB file corresponds to a protein structure.

## Features
- **Download PDB files** from the RCSB Protein Data Bank.
- **Download FASTA files** associated with PDB entries.
- **Download EMDB map files** from the Electron Microscopy Data Bank (EMDB).
- **Extract the resolution** of an EMDB map.
- **Check if a PDB file is a protein structure**.

## Installation
```bash
pip install BioFetcher
```


<details> <summary> Installation - from source codes</summary>

1. Clone this repository:
   ```bash
   git clone https://github.com/chenwei-zhang/BioFetcher.git
   cd BioFetcher
   ```

2. Install the package:
   ```bash
   pip install .
   ```
</details> 

## Python Import

Once you have installed the package, you can import and use the functions in your own Python scripts or projects.

### Importing Functions

Here’s how to import the key functions from the `BioFetcher` package:

```python
from BioFetcher import BioDownloader, extract_res, is_protein_structure
```

### Example Usage in Python

You can use the `BioDownloader` class to download PDB, FASTA, and EMDB files, or use the helper functions to extract EMDB resolution or check if a PDB corresponds to a protein structure.

```python
# Example of using BioDownloader in Python
downloader = BioDownloader(download_path='.', verbose=True)

# Download PDB and FASTA files
downloader.download_pdb('1abc')
downloader.download_fasta('1abc')

# Check if PDB corresponds to a protein structure
is_protein = is_protein_structure('1abc.pdb')
print(f'Is protein structure: {is_protein}')

# Download EMDB file and extract resolution
downloader.download_emdb('1234')
resolution = extract_res('1234')
print(f'Resolution for EMDB 1234: {resolution}')
```

### Functions

#### `extract_res(emdb_id)`
Extracts the resolution value of the EMDB entry with the given ID.

#### `is_protein_structure(pdb_file_path)`
Checks if the downloaded PDB file corresponds to a protein structure.




## Command-Line Usage

You can run `BioFetcher` from the command line to download files based on the PDB and EMDB IDs, and specify the download path.


### Command-Line Arguments

- `--pdb <PDB_ID>`: Download the PDB file associated with the specified PDB ID.
- `--fasta <PDB_ID>`: Download the FASTA file associated with the specified PDB ID.
- `--emdb <EMDB_ID>`: Download the EMDB map file associated with the specified EMDB ID.
- `--download_path <path>`: Specify the directory to save the downloaded files (default is the current directory).

### Example Usage

- To download a PDB file and its associated FASTA file:
  ```bash
  biofetcher --pdb 1abc --fasta 1abc --download_path /path/to/save/files
  ```

- To download an EMDB map
  ```bash
  biofetcher --emdb 1234 --download_path /path/to/save/files
  ```

- To download all files for a specific PDB and EMDB ID:
  ```bash
  biofetcher --pdb 1abc --fasta 1abc --emdb 1234 --download_path /path/to/save/files
  ```



## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.



## Support 
Chenwei Zhang, chwzhan@gmail.com
