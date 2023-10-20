import os
import json

def path_exists(path, create=True, quit_on_false=False):
    if os.path.exists(path):
        return True
    
    elif create:
        os.mkdir(path)
        return

    elif quit_on_false:
        print(f"Error:  {path} not found.")
        quit()
    else:
        return False

def read_json(file):
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to open file {file}.\n",e)
        quit()
    return data

def write_json(content, file, append=None):
    # append = "insert": new data at top;  True: new data at bottom;  False: overwrite old data    

    if file[-5:] != ".json": file += ".json"

    if type(content) in [str, bytes, bytearray]:
        try:
            content = json.loads(content)            

        except json.decoder.JSONDecodeError as e:
            if "Expecting property name enclosed in double quotes" in str(e):
                content = json.loads(content.replace('\'', '\"'))

        except Exception as e:
            print(f"Error: Couldn't convert to json format.\n{e}\n")
            print(f"Type: {type(content)}\n{content}")
            quit()

    if append:
        old_data = read_json('json.json')
        content = content|old_data if append == "insert" else old_data|content

    with open("json.json", "w") as out:
        out.write(json.dumps(content, indent=1))