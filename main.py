from collections import defaultdict
from todoist_api_python.api import TodoistAPI
from dictcc import Dict

API_TOKEN = "<INSERT-YOUR-TOKEN>"  # TODO: Add you REST API token.
VOCABULARY_PROJECT_ID = 123  # TODO: Add your project ID.
SOURCE_LANGUAGE = "en"
DESTINATION_LANGUAGE = "de"


def get_vocabulary_from_todoist():
    api = TodoistAPI(API_TOKEN)
    tasks = api.get_tasks(project_id=VOCABULARY_PROJECT_ID)
    return [task.to_dict()["content"].lower() for task in tasks]


def get_translations_from_dict(vocab):
    translator = Dict()
    translations = [
        translator.translate(v, from_language=SOURCE_LANGUAGE, to_language=DESTINATION_LANGUAGE).translation_tuples[:3]
        for v in vocab]
    result = []
    for entry in translations:
        result_entry = defaultdict(str)
        for pair in entry:
            source_entry = clean_entry(pair[0])
            destination_entry = clean_entry(pair[1])
            if result_entry[source_entry]:
                result_entry[source_entry] += f", {destination_entry}"
            else:
                result_entry[source_entry] += destination_entry
        if result_entry:
            for k, v in result_entry.items():
                k = clean_entry(k)
                v = clean_entry(v)
                result.append((k, v))
    return result


def clean_entry(e):
    e = e.replace(";", ",")
    e = remove_brackets(e, "{", "}")
    e = remove_brackets(e, "[", "]")
    return e.strip()


def remove_brackets(e, start_bracket, stop_bracket):
    num_of_brackets = e.count(start_bracket) if start_bracket in e else 0
    if num_of_brackets == 0:
        return e
    while num_of_brackets > 0:
        try:
            start_pos = e.index(start_bracket)
            stop_pos = e.index(stop_bracket)
            e = e[:start_pos] + e[stop_pos+1:]
            num_of_brackets -= 1
        except ValueError:
            num_of_brackets = 0
    return e


def export_to_csv(fn, entries):
    with open(fn, mode="w", encoding="utf-8") as export_file:
        for entry in entries:
            export_file.write(f"{entry[0]}; {entry[1]}\n")
    return True


def main():
    vocabulary = get_vocabulary_from_todoist()
    translations = get_translations_from_dict(vocabulary)
    export_to_csv("new_entries.csv", translations)


if __name__ == "__main__":
    main()
