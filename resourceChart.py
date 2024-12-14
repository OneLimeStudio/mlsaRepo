import matplotlib.pyplot as plt
import io
import geopandas as gpd
import json


def generate_chart():
    with open('resources.json', 'r') as file:
        json_data = json.load(file)

    geo_df = gpd.GeoDataFrame.from_features(json_data["features"])
    color_map = {
        True: 'green',
        False: 'red',
        
    }
    
    # Dynamically create a 'color' column based on the property
    if 'camp_exists' in geo_df.columns:
        geo_df['color'] = geo_df['camp_exists'].map(color_map)
    else:
        raise KeyError("The column 'district_type' does not exist in the data.")

    
    # Plot with the dynamically assigned colors
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    geo_df.plot(ax=ax, color=geo_df['color'])
    plt.title("Districts Colored by Property")
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    #plt.show()
    return img