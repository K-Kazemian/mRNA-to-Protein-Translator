# Dictionary for the standard genetic code (codon to amino acid single-letter code)
# Stop codons are marked with '*' but not added to the protein sequence
genetic_code = {
    "AAA": "K", "AAC": "N", "AAG": "K", "AAU": "N",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
    "AGA": "R", "AGC": "S", "AGG": "R", "AGU": "S",
    "AUA": "I", "AUC": "I", "AUG": "M", "AUU": "I",
    "CAA": "Q", "CAC": "H", "CAG": "Q", "CAU": "H",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
    "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
    "GAA": "E", "GAC": "D", "GAG": "E", "GAU": "D",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G",
    "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
    "UAA": "*", "UAC": "Y", "UAG": "*", "UAU": "Y",
    "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
    "UGA": "*", "UGC": "C", "UGG": "W", "UGU": "C",
    "UUA": "L", "UUC": "F", "UUG": "L", "UUU": "F",
}

def translate_mrna(mrna_sequence):
    """
    Translates an mRNA sequence into a protein sequence.
    - Assumes the sequence starts at the beginning (e.g., with a start codon like AUG).
    - Reads in codons (groups of 3 nucleotides).
    - Stops translation at the first stop codon (UAA, UAG, UGA).
    - Uses single-letter amino acid codes.
    - Handles uppercase input; ignores case.
    - If the sequence length is not a multiple of 3, translation stops at the last complete codon.
    - Invalid codons are represented as 'X'.
    """
    mrna_sequence = mrna_sequence.upper()  # Normalize to uppercase
    protein = ""
    i = 0
    while i + 3 <= len(mrna_sequence):
        codon = mrna_sequence[i:i+3]
        if codon in ["UAA", "UAG", "UGA"]:
            break
        aa = genetic_code.get(codon, "X")  # 'X' for unknown/invalid codons
        protein += aa
        i += 3
    return protein

# Example usage: Run the program and input an mRNA sequence
if __name__ == "__main__":
    mrna = input("Enter the mRNA sequence: ").strip()
    protein = translate_mrna(mrna)
    print("Protein sequence:", protein)
