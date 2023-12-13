import matplotlib.pyplot as plt
import pandas as pd

# Read data from the CSV file
file_path = 'qPCR results.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Create a color map for unique sample names
colors = {'Heterozygous alleles': 'b', 'FAM alleles': 'g', 'HEX alleles': 'r', 'NTC': 'c'}

# Create a scatter plot with different colors for each sample
for sample, group in df.groupby('Sample'):
    plt.scatter(group['X'], group['Y'], label=sample, color=colors[sample])

# Add labels and legend
plt.xlabel('FAM', fontsize=14)
plt.ylabel('HEX',fontsize=14)
plt.legend(fontsize=14, bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
# plt.title('Scatter plot of KASP assays for 16 introgressed B. napus (S), \n 3 B. napus (Bn), 3 radish (Rs) and negative control (NC).',fontsize=14)
plt.title ('Schematic illustration of kompetitive allele specific PCR (KASP)')
plt.savefig('KASP.png')
plt.show()
