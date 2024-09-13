import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it

    # Searchs for the value 
    for item in json_data:
        for values in item:
            # print(item[values])
            if item[values] == search_string:
                results.append(item)
        
    return results