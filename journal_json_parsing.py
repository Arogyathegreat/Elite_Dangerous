import json
import os


def directory():
    journal_directory = 'C:/Users/arogya.Gurkha/Saved Games/Frontier Developments/Elite Dangerous/'

    list_of_files = [os.path.join(journal_directory, x) for x in os.listdir(journal_directory) if x.endswith(".log")]
    latest_file = max(list_of_files, key=os.path.getctime)

    print(os.path.basename(latest_file))

    json_loading(latest_file)


def json_loading(file):
    journal_entries = []
    current_system = ""
    for line in open(file):
        di = json.loads(line)
        journal_entries.append(di)

    for entry in journal_entries:
        if "FSDJump" in entry.values():
            current_system = entry["StarSystem"]

    print(current_system)

    return current_system


if __name__ == '__main__':
    directory()
