import argparse
from BioFetcher.downloader import BioDownloader, extract_res, is_protein_structure

def main():
    parser = argparse.ArgumentParser(description="Download bioinformatics data")
    parser.add_argument('--pdb', type=str, help="PDB ID to download the PDB file")
    parser.add_argument('--fasta', type=str, help="PDB ID to download the FASTA file")
    parser.add_argument('--emdb', type=str, help="EMDB ID to download the map file")
    parser.add_argument('--download_path', type=str, default='.', help="Path to save downloaded files (default is current directory)")
    args = parser.parse_args()


    if not any([args.pdb, args.fasta, args.emdb]):
            print("No arguments provided. Use --pdb, --fasta, or --emdb to download data.")
            return
        
    downloader = BioDownloader(download_path=args.download_path, verbose=True)

    # Download files based on specified arguments
    if args.pdb:
        downloader.download_pdb(args.pdb)

    if args.fasta:
        downloader.download_fasta(args.fasta)

    if args.emdb:
        downloader.download_emdb(args.emdb)


if __name__ == "__main__":
    main()
