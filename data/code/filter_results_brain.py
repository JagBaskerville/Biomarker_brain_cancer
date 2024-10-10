import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test

def gene_to_p_value_and_hr(data, gene, survival_data):
    # Filter the data for the specific gene
    brain_gene = data[data['Gene name'] == gene]
    
    # Calculate the median expression level
    median_expression = np.median(brain_gene['Expression'])
    
    # Create 'strata' column based on median expression
    brain_gene = brain_gene.copy()
    brain_gene.loc[:, 'strata'] = np.where(brain_gene['Expression'] <= median_expression, 'low', 'high')
    
    # Merge with survival data
    brain_gene = pd.merge(brain_gene, survival_data, how='inner', on='barcode')
    
    # Drop rows with missing survival data
    brain_gene = brain_gene.dropna(subset=['overall_survival'])
    
    # Perform the log-rank test
    logrank_results = logrank_test(
        brain_gene['overall_survival'][brain_gene['strata'] == 'low'],
        brain_gene['overall_survival'][brain_gene['strata'] == 'high'],
        event_observed_A=brain_gene['deceased'][brain_gene['strata'] == 'low'],
        event_observed_B=brain_gene['deceased'][brain_gene['strata'] == 'high']
    )
    
    # Get the p-value from the log-rank test
    p_value = logrank_results.p_value
    
    # Prepare data for Cox proportional hazards model
    brain_gene['high_expression'] = brain_gene['strata'].map({'low': 0, 'high': 1})
    
    # Fit the Cox proportional hazards model
    cph = CoxPHFitter()
    cph.fit(brain_gene[['overall_survival', 'deceased', 'high_expression']], duration_col='overall_survival', event_col='deceased')
    
    # Get the hazard ratio
    hazard_ratio = cph.hazard_ratios_['high_expression']
    
    return gene, p_value, hazard_ratio
# Create a empty list
results = []
# Append result into list for each gene in hub_gene_list
for gene in hub_genes_list:
    result = gene_to_p_value_and_hr(merged_gene_expression, gene , brain_metadata_survival)
    results.append(result)

# Convert results into a DataFrame
results_df = pd.DataFrame(results, columns=['Gene', 'P_Value', 'Hazard_Ratio'])
filtered_results_brain = results_df[results_df.Hazard_Ratio >= 1.2]