## STRING network 
import requests
from time import sleep
import ipywidgets as widgets
from IPython.display import SVG, display



string_api_url = "https://version-11-5.string-db.org/api"
output_format = "svg"
method = "network"
request_url = "/".join([string_api_url, output_format, method])

# Combine all proteins into a single string with newline characters in URL encoding (%0D)
protein_list = brain_string_db_top30.node_name.tolist()
combined_proteins = "%0D".join(protein_list)

# Set parameters
params = {
    "identifiers": combined_proteins,  # combined list of proteins
    "species": 9606,  # species NCBI identifier
    "network_flavor": "confidence",  # show confidence links
    "caller_identity": "Final_project_python_R12B48007",  # your app name
    "required_score": 900,  # optional: to filter for high confidence interactions  
}
# Call STRING
response = requests.post(request_url, data=params)

# Save the network to file
file_name = "combined_network.svg"
print(f"Saving interaction network to {file_name}")
with open(file_name, 'wb') as fh:
    fh.write(response.content)
sleep(1)
def display_svg_in_widget(svg_file):
    output_widget = widgets.Output()
    with output_widget:
        display(SVG(filename=svg_file))
    return output_widget
svg_file = "combined_network.svg"
output_widget = display_svg_in_widget(svg_file)
output_widget