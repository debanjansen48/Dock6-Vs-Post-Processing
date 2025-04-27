import csv

# Input and Output file names
input_file = "viout.out"  # Change this to your actual filename
output_file = "molecule_grid_scores.csv"

# Lists to store the extracted data
molecules = []
scores = []

# Reading the file
with open(input_file, 'r') as file:
    lines = file.readlines()
    current_molecule = None

    for line in lines:
        line = line.strip()
        if line.startswith("Molecule:"):
            current_molecule = line.split("Molecule:")[1].strip()
        elif line.startswith("Grid_Score:") and current_molecule is not None:
            score = float(line.split("Grid_Score:")[1].strip())
            molecules.append(current_molecule)
            scores.append(score)
            current_molecule = None  # Reset for the next molecule

# Writing to CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Molecule", "Grid_Score"])  # Header
    for mol, score in zip(molecules, scores):
        writer.writerow([mol, score])

print(f"Data has been written to {output_file}")

