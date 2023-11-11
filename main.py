# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    from nba_api.stats.endpoints import playercareerstats

    # Nikola Jokić
    career = playercareerstats.PlayerCareerStats(player_id='203999')

    # pandas data fraes (optional: pip install pandas)
    career.get_data_frames()[0]

    # jsoneval "$(ssh-agent -s)"
    # ssh-add ~/.ssh/id_r
    career.get_json()

    # dictionary
    career.get_dict()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
