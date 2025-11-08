import json


def load_json(filename: str):
    """ JSON fájl betöltése dict-be """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: {file} not found')
        return {}
    except json.JSONDecodeError:
        print(f"Error: failed to decode {filename}")
        return {}


def save_json(data, filename: str):
    """ Adatok mentése JSON_-be """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Data save to {filename}')
    except IOError as e:
        print(f'Error: cannot save file {filename}, {e}')


def filter_invalid_matches(matches):
    """ Hibás meccsek kiszűrése, ahol hiányzik valamilyen kulcs. Mentés fájlba. """

    valid_matches = []
    invalid_matches = []

    for match in matches:
        try:
            if 'ht' not in match['score']:
                raise KeyError(f'Missing "ht" in match: {match}')
            valid_matches.append(match)
        except KeyError:
            invalid_matches.append(match)

    if invalid_matches:
        save_json({"invalid_matches": invalid_matches}, "hibas.json")
        print("Invalid matches save to hibas.json")

    return valid_matches


def process_matches(matches, condition, error_label):
    results = []
    for match in matches:
        try:
            if condition(match):
                results.append(match)
        except KeyError as e:
            print(f'[{error_label}] - Error processing match: Missing key {e} -> {match}')
            return []

    return results


def home_losing_at_halftime_but_wins(matches):
    return process_matches(
        matches,
        lambda m: (m["score"]["ht"][0] < m["score"]["ht"][1]) and (m["score"]["ft"][0] > m["score"]["ft"][1]),
        "home_losing_at_halftime_but_wins_big_error"
    )


def home_losing_at_halftime_but_draws(matches):
    return process_matches(
        matches,
        lambda m: (m["score"]["ht"][0] < m["score"]["ht"][1]) and (m["score"]["ft"][0] == m["score"]["ft"][1]),
        "home_losing_at_halftime_but_drwas_errorz"
    )


def home_concedes_more_than_three_goals(matches):
    return process_matches(
        matches,
        lambda m: (m["score"]["ft"][1] > 3),
        "home_concedes_more_than_three_goals_err"
    )


def home_score_more_than_three_goals(matches):
    return process_matches(
        matches,
        lambda m: (m["score"]["ft"][0] > 3),
        "home_concedes_more_than_three_goals_err"
    )


def filter_by_matchday(matches, matchday):
    return process_matches(
        matches,
        lambda m: m["round"].lower() == f'matchday {matchday}'.lower(),
        "filter_by_matchday_err"
    )


def filter_by_date(matches, date):
    return process_matches(
        matches,
        lambda m: m["date"] == date,
        "filter_by_date_err"
    )


def print_results(title, matches):
    print(title)

    if matches:
        for match in matches:
            print(f'{match["round"]}: {match["team1"]} vs {match["team2"]}'
                  f'Date: {match["date"]}, HT: {match["score"].get("ht", "N/A")}'
                  f', FT: {match["score"].get("ft", "N/A")}')
            print("-" * 50)


def main():
    filename = "adatok/data.json"
    data = load_json(filename)
    matches = data.get("matches", [])

    matches = filter_invalid_matches(matches)

    while True:
        options = [
            "1. Search by Matchday",
            "2. Search by Date",
            "3. Analyze all matches"
            "end-q-quit"
        ]

        filtered_matches = []

        print(f'Options: {[option for option in options]}')

        choice = input("Choose an option (1/2/3/q): ")

        if choice == "1":
            matchday = input("Enter matchday (1-9): ")
            filtered_matches = filter_by_matchday(matches, matchday)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            filtered_matches = filter_by_date(matches, date)
        elif choice.lower() in ["end", "q", "quit"]:
            break
        else:
            filtered_matches = matches

        halftime_loss_to_win = home_losing_at_halftime_but_wins(filtered_matches)
        halftime_loss_to_draw = home_losing_at_halftime_but_draws(filtered_matches)
        home_concede_3_or_more = home_concedes_more_than_three_goals(filtered_matches)
        home_score_3_or_more = home_score_more_than_three_goals(filtered_matches)

        print_results("1) Hazai félidőben vereségre áll, de fordít", halftime_loss_to_win)
        print_results("2) Hazai félidőben vereségre áll, de X lesz", halftime_loss_to_draw)
        print_results("3) Hazai 3 gólnál többet kap", home_concede_3_or_more)
        print_results("4) Hazai 3 gólnál többet rúg", home_score_3_or_more)


main()