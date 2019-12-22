import json

from conf import CREDS_JSON_FILE_PATH


# Returns list of credentials from creds.json file located in directory


def read_creds():
    with open(CREDS_JSON_FILE_PATH) as creds_file:
        json_obj = json.load(creds_file)
        return json_obj.get('creds_list')


if __name__ == "__main__":
    print(read_creds())
