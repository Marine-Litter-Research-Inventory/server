columns = (
    'Research Scope Aim of Research',
    'Period of Study',
    'Period of Study_Year',
    'Location of Work',
    'Relevant Water Body_Detailed',
    'Relevant Water Body_General',
    'Coastal or Offshore',
    'Plastic Sizes Examined',
    'Adopted GESAMP Size',
    'Microplastic Sizes',
    'Contaminants Examined',
    'Fishing Gear Examined',
    'Legal/Regulatory Study',
    'Social/Cultural Study',
    'Economic/Management Study',
    'Policy Study',
    'Research Methodology Methodologies Used',
    'Field Sampling_Conducted',
    'Field Sampling_Compartment',
    'Field Sampling_Frequency',
    'Survey/Interview_Conducted',
    'Other Sampling_Type',
    'Biota_Species',
    'Biota (Phyllum)',
    'Biota_Applied',
    'Common names',
    'Literature Review_Conducted',
    'Literature Review_Volume',
    'Desktop / Deductive analysis',
    'Modelling_Conducted',
    'Modelling_Type',
    'Plankton Net_Mesh Size',
    'Water Sampling_Depth',
    'Shoreline Sediment Sampling_ Depth',
    'Seabed Sediment Sampling_Depth',
    'Mangrove/Mudflat Sediment Sampling_Depth',
    'Controls_Blanks',
    'Research Findings Key Findings',
    'Source of Plastics',
    'Source of Plastics_General',
    'Research Topics',
    'Plastic Characterisation_Conducted',
    'Plastic Characterisation_Colour',
    'Plastic Characterisation_Colours Found',
    'Plastic Characterisation_Shape',
    'Plastic Characterisation_Shapes Found',
    'Plastic Characterisation_Polymer',
    'Plastic Characterisation_Polymers Found',
    'Macro_Uses',
    'Macro_Mean Abundance_Count',
    'Macro_Mean Abundance_Weight',
    'Water_Mean Abundance_Count',
    'Water_Mean Abundance_Weight',
    'Shoreline Sediment_Mean Abundance_Count',
    'Shoreline Sediment_Mean Abundance_Weight',
    'Seabed Sediment_Mean Abundance_Count',
    'Seabed Sediment_Mean Abundance_Weight',
    'Mangrove_Mean Abundance_Count',
    'Mangrove_Mean Abundance_Weight',
    'Biota_Mean Abundance_Count',
    'Biota_Mean Abundance_Weight',
    'Degradation Indicated'
)

def get(pos, pattern):
  result = ''
  for (index, col) in enumerate(columns):
    if index == 0 and pos == 0:
      result += f"WHERE ([{col}] regexp '{pattern}'"
    else:
      if index == 0:
        result += f"AND ([{col}] regexp '{pattern}'"
      else:
        result += f" OR [{col}] regexp '{pattern}'"
  result += ")"
    
  return result
