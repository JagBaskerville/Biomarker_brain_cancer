import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from lifelines import KaplanMeierFitter

#Show genes have significant log rank test and Hazard Ratio >= 1.2
filtered_results_brain= pd.read_csv('data/statistics/filtered_results_brain.csv', sep=',', index_col = False)
filtered_results_brain = filtered_results_brain.sort_values('Hazard_Ratio',ascending = False)
# Import data for survival analysis with candidate gene
## Merged gene expression
merged_gene_expression_brain= pd.read_csv('data/statistics/merged_gene_expression_brain.csv', sep=',', index_col = False)
## brain metadata survival
brain_metadata_survival = pd.read_csv('data/statistics/brain_metadata_survival.csv', sep=',', index_col = False)
# brain code
brain_code = pd.read_csv('data/statistics/brain_code.csv', sep=',', index_col = False)

def plot_gene_analysis(data, gene, brain_code, survival_data):
    # Filter the data for the specific gene
    brain_gene = data[data['Gene name'] == gene]
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot boxplot for gene expression
    brain_gene_boxplot = pd.merge(brain_gene, brain_code, how='inner', on='barcode')
    sns.boxplot(data=brain_gene_boxplot, x='shortLetterCode', y='Expression', ax=axes[0])
    axes[0].set_title(f'{gene} expression')
    axes[0].set_ylabel('Normalized gene expression')
    axes[0].set_xlabel('')
    
    # Calculate the median expression level for survival curve
    median_expression = np.median(brain_gene['Expression'])    
    # Create 'strata' column based on median expression
    brain_gene['strata'] = np.where(brain_gene['Expression'] <= median_expression, 'low', 'high')
    # Merge with survival data
    brain_gene_survival = pd.merge(brain_gene, survival_data, how='inner', on='barcode')
    # Drop rows with missing survival data
    brain_gene_survival = brain_gene_survival.dropna(subset=['overall_survival'])
    # Initialize the KaplanMeierFitter
    kmf = KaplanMeierFitter()
    strata = brain_gene_survival['strata'].unique()
    
    # Plot survival curve
    for stratum in strata:
        mask = brain_gene_survival['strata'] == stratum
        kmf.fit(durations=brain_gene_survival['overall_survival'][mask], 
                event_observed=brain_gene_survival['deceased'][mask], 
                label=stratum)
        kmf.plot_survival_function(ax=axes[1])  
    
    # Add survival plot details
    axes[1].set_title(f'Survival Curve for {gene}')
    axes[1].set_xlabel('Time (Days)')
    axes[1].set_ylabel('Survival Probability')
    axes[1].legend(title='Gene Expression')
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the figure
    return fig

gene_list = filtered_results_brain.Gene.tolist()
gene = st.selectbox('Select a gene for survival rate analysis:', gene_list)
fig = plot_gene_analysis(merged_gene_expression_brain, gene , brain_code, brain_metadata_survival)
st.pyplot(fig)