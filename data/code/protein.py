import requests
import time
import py3Dmol
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def get_gene_name(csv_file):
    try:
        df = pd.read_csv(f'{csv_file}', sep=',')
        second_column = df.iloc[:, 0]
        unique_values = second_column.drop_duplicates()
        unique_list = unique_values.tolist()
        unique_list.insert(0,'None')
        return unique_list
    except:
        raise ValueError

def get_uniprot_id(gene_name):
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene_name}&format=json"
    response = requests.get(url)
    data = response.json()

    if 'results' in data and data['results']:
        return data['results'][0]['primaryAccession']
    else:
        raise ValueError(f"No UniProt entry found for gene: {gene_name}")

def submit_mapping_request(from_db, to_db, ids):
    url = "https://rest.uniprot.org/idmapping/run"
    params = {
        'from': from_db,
        'to': to_db,
        'ids': ids
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()["jobId"]
    else:
        raise Exception(f"Error {response.status_code}: Unable to submit mapping request.")

def check_job_status(job_id):
    url = f"https://rest.uniprot.org/idmapping/status/{job_id}"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            job_status = response.json()
            if 'jobStatus' in job_status:
                if job_status["jobStatus"] == "FINISHED":
                    return True
                elif job_status["jobStatus"] == "RUNNING":
                    time.sleep(2)
                else:
                    raise Exception("Job failed or unknown status.")
            elif 'results' in job_status:
                return True
            else:
                raise Exception(f"Unexpected response format: {job_status}")
        else:
            raise Exception(f"Error {response.status_code}: Unable to check job status.")

def retrieve_mapping_results(job_id):
    url = f"https://rest.uniprot.org/idmapping/results/{job_id}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        if 'results' in results:
            return results['results']
        else:
            return []
    else:
        raise Exception(f"Error {response.status_code}: Unable to retrieve results.")

def convert_uniprot_to_pdb(uniprot_id):
    from_db = 'UniProtKB_AC-ID'
    to_db = 'PDB'
    job_id = submit_mapping_request(from_db, to_db, uniprot_id)
    if check_job_status(job_id):
        results = retrieve_mapping_results(job_id)
        if results:
            pdb_ids = [result['to'] for result in results]
            return pdb_ids
        else:
            return ValueError
        
def get_entry_id(uniprot_id):
    try:    
        response = requests.get(f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}?")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data[0]['entryId']
    except requests.exceptions.RequestException:
        return ValueError("Invalid PDB ID or network issue")

def fetch_AF_PDB(uniprot_id):
    try:    
        response = requests.get(f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}?")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        url = data[0]['pdbUrl']
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError("Invalid URL or network issue")
    except requests.exceptions.RequestException:
        return ValueError("Invalid UniProt ID or network issue")

        
def fetch_pdb(pdb_id):
    url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError("Invalid PDB ID or network issue")

def get_protein_name(Id):
    if len(Id) == 4:
        url = f'https://data.rcsb.org/rest/v1/core/entry/{Id}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data['struct']['title']
        else:
            raise ValueError("Invalid PDB ID or network issue")
    else:
        UniProtId = Id.replace('AF-', '').replace('-F1', '')
        url = f'https://alphafold.ebi.ac.uk/api/prediction/{UniProtId}?'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data[0]['uniprotDescription']
        else:
            raise ValueError("Invalid PDB ID or network issue")

def generate_3d_html(Id, Data):
    view = py3Dmol.view(width=1000, height=1000)
    view.addModel(Data, 'pdb')
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    view.addLabel(get_protein_name(Id), {'fontColor':'black','backgroundColor':'white', 'font': 'calibri', 'fontSize': 18, 'useScreen': True, 'position':{'x': 10, 'y': 60, 'z': 0 }})
    view.addLabel(f'{Id}', {'fontColor':'black','backgroundColor':'white', 'font': 'calibri', 'fontSize': 36, 'useScreen': True, 'position':{'x': 10, 'y': 5, 'z': 0 }})
    view.spin(False)
    
    html_content = view._make_html()
    
    return html_content

def main(csv_file):
    st.title("Protein Structure Display")
    try:
        gene_list = get_gene_name(csv_file)
    except ValueError:
        st.warning('Errooooooooor')
    gene_name = st.selectbox("Select the protein coding gene:",gene_list)

    if gene_name == 'None':
        st.warning("Please select a protein coding gene.")
        return

    try:
        uniprot_id = get_uniprot_id(gene_name)
        st.text(f'UniProt ID for {gene_name}: {uniprot_id}.')
    except ValueError:
        st.text('UniProt ID not found.')
        return

    try:
        pdb_ids = convert_uniprot_to_pdb(uniprot_id)
        if isinstance(pdb_ids, list):
            try:
                display_Id = st.selectbox('Please select the PDB ID: ', pdb_ids)
                pdb_data = fetch_pdb(display_Id)
                html_content = generate_3d_html(display_Id, pdb_data)
                components.html(html_content, height=1000, width= 1000)
            except ValueError:
                st.text('PDB ID not found. Now searching in AlphaFold database...')
        else:
            try:
                pdb_data = fetch_pdb(pdb_ids)
                html_content = generate_3d_html(pdb_ids, pdb_data)
                components.html(html_content, height=1000, width= 1000)
            except ValueError:
                st.text('PDB ID not found. Now searching in AlphaFold database...')
    except ValueError:
        st.text('PDB ID not found. Now searching in AlphaFold database...')
        pass

    try:
        AF_data = fetch_AF_PDB(uniprot_id)
        AF_ID = get_entry_id(uniprot_id)
        html_content = generate_3d_html(AF_ID, AF_data)
        components.html(html_content, height=800, width= 800)
    except ValueError:
        st.text('AlphaFold predicted structure also not found.')

if __name__ == "__main__":
    main('filtered_results_brain.csv')