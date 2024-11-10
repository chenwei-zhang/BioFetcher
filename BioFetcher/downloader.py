import gzip
import shutil
import requests
import os
import argparse

class BioDownloader:
    def __init__(self, download_path='.', verbose=False):
        """
        Initializes the downloader class.

        Parameters:
            download_path (str): Path to download files to.
            verbose (bool): If True, prints status updates.
        """
        self.download_path = download_path
        self.verbose = verbose


    def unzip_gz_file(self, gz_file_path, output_file_path):
        """
        Unzips a .gz file.

        Parameters:
            gz_file_path (str): The path to the gzipped file.
            output_file_path (str): The output path for the unzipped file.
        """
        with gzip.open(gz_file_path, 'rb') as f_in:
            with open(output_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        if self.verbose:
            print(f"Unzipped {gz_file_path} to {output_file_path}")


    def download_pdb(self, pdb_id):
        """
        Downloads a PDB file from RCSB.

        Parameters:
            pdb_id (str): The PDB ID to download.
        """
        url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
        response = requests.get(url)
        if response.status_code == 200:
            pdb_file_path = os.path.join(self.download_path, f'{pdb_id}.pdb')
            with open(pdb_file_path, 'w') as file:
                file.write(response.text)
            if self.verbose:
                print(f"Downloaded PDB: {pdb_id} to {pdb_file_path}")
        else:
            print(f"Failed to download PDB: {pdb_id}")


    def download_fasta(self, pdb_id):
        """
        Downloads a FASTA file associated with a PDB ID from RCSB.

        Parameters:
            pdb_id (str): The PDB ID to download the FASTA for.
        """
        url = f'https://www.rcsb.org/fasta/entry/{pdb_id}'
        response = requests.get(url)
        if response.status_code == 200:
            fasta_file_path = os.path.join(self.download_path, f'{pdb_id}.fasta')
            with open(fasta_file_path, 'w') as file:
                file.write(response.text)
            if self.verbose:
                print(f"Downloaded FASTA for PDB ID: {pdb_id} to {fasta_file_path}")
        else:
            print(f"Failed to download FASTA for PDB ID: {pdb_id}")


    def download_emdb(self, emdb_id, delete_gz=True):
        """
        Downloads an EMDB map file and unzips it.

        Parameters:
            emdb_id (str): The EMDB ID to download.
            delete_gz (bool): If True, deletes the .gz file after extraction.
        """
        url = f'https://files.rcsb.org/pub/emdb/structures/EMD-{emdb_id}/map/emd_{emdb_id}.map.gz'
        response = requests.get(url)

        gz_file_path = os.path.join(self.download_path, f'emdb_{emdb_id}.map.gz')
        map_file_path = os.path.join(self.download_path, f'emd_{emdb_id}.map')

        if response.status_code == 200:
            with open(gz_file_path, 'wb') as file:
                file.write(response.content)
            if self.verbose:
                print(f"Downloaded EMDB: {emdb_id} to {gz_file_path}")
        else:
            print(f"Failed to download EMDB: {emdb_id}")

        # Unzip the downloaded file
        self.unzip_gz_file(gz_file_path, map_file_path)

        # Optionally delete the .gz file
        if delete_gz:
            os.remove(gz_file_path)
            if self.verbose:
                print(f"Deleted zip file: {gz_file_path}")
    


def extract_res(emdb_id):
    url = f'https://www.ebi.ac.uk/emdb/api/entry/EMD-{emdb_id}'

    response = requests.get(url)
    data = response.json()
    # Extract the resolution value
    resolution_value = data.get('structure_determination_list', {}) \
                        .get('structure_determination', [{}])[0] \
                        .get('image_processing', [{}])[0] \
                        .get('final_reconstruction', {}) \
                        .get('resolution', {}) \
                        .get('valueOf_', None)
    return float(resolution_value)



def is_protein_structure(pdb_file_path):
    # List of standard amino acid codes
    amino_acids = set([
        'ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 
        'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL'
    ])
    
    with open(pdb_file_path, 'r') as pdb_file:
        for line in pdb_file:
            # Look for lines starting with 'ATOM' or 'HETATM'
            if line.startswith(('ATOM', 'HETATM')):
                # Check if the residue (3-letter code) is an amino acid
                residue = line[17:20].strip()
                if residue in amino_acids:
                    return True  # Likely a protein structure
    return False  # Not a protein structure




if __name__ == '__main__':
        
    
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--pdb", type=str, help="PDB ID to download")
    argparser.add_argument("--emd", type=str, help="EMDB ID to download")
    argparser.add_argument("--save_path", default='./', type=str, help="Path to save the downloaded files")
    
    args = argparser.parse_args()
    
    save_path = args.save_path
    pdb = args.pdb
    emd = args.emd
    
    downloader = MapDownloader(download_path=save_path, verbose=False)
    
    
    if pdb is not None:
        downloader.download_pdb(pdb)
        print(f"Downloaded PDB-{pdb}")
        
    if emd is not None:
        downloader.download_emdb(emd)
        print(f"Downloaded EMDB-{emd}")
