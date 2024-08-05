#  extract the names of the players in file_path and return them as a list
#  will verify name validity when feeding them to Riot's API
def get_players_name(file_path) -> list:
    names = []
    with open(file_path, 'r') as f:
        for line in f:
            names.append(line.strip())
    return names


def main():
    pass


if __name__ == '__main__':
    main()
