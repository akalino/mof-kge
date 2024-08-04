import json
import pandas as pd



def generate_keys():
    identifier_path = "mapping_files/identifiers.json"
    with open(identifier_path, 'r') as file:
        identifiers = json.load(file)

    print("Loaded all identifiers")
    # count = 0
    # for key, value in identifiers.items():
    #     count+=1
    #     print(key, value)
    #     if count > 5:
    #         break

    # Read the CSV file into a DataFrame
    prediction_file = "predictions/topology_small.csv"
    predictions = pd.read_csv(prediction_file)

    def get_mof_key(id):
        return identifiers[str(id)].get("mofkey", None)

    def get_name(id):
        return identifiers[str(id)].get("name", None)


    predictions["subject_mof_key"] = predictions['s'].apply(get_mof_key)
    predictions["name"] = predictions['o'].apply(get_name)
    predictions["valid"] = None

    
    # for index, row in predictions.iterrows():
    #     print(identifiers[str(row['o'])])

    predictions.to_csv("predictions/top_small.csv", index=False)