import json

from conf import CREDS_JSON_FILE_PATH


# Returns list of credentials from creds.json file located in directory
def choose_creds(creds_list):
    for idx, creds_pair in enumerate(creds_list):
        login = creds_pair['login']
        if creds_pair['password']:
            print(f'{idx+1}: {login}')
    
    print('type in index of intended account you want to use: ', end='')
    idx = input()
    idx = int(idx)
    while True:
      if idx >= 1 and idx <= len(creds_list):
        break
      else:
        print('Wroing choice, try again!')
        print('type in an index of intended account you want to use: ', end='')
        idx = input()
        idx = int(idx)

    idx = int(idx)-1
    return creds_list[idx]


def read_creds():
    with open(CREDS_JSON_FILE_PATH) as creds_file:
        json_obj = json.load(creds_file)
        return json_obj.get('creds_list')


if __name__ == "__main__":
    print(read_creds())
    print(choose_creds(read_creds()))
