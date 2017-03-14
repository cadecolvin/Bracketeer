import core
import json
from collections import namedtuple


def load(path):
    with open(path, 'rt') as f:
        all_games = json.load(f)

    regions = []
    for _region in all_games:
        region = core.Region()
        for _game in _region:
            game = core.Game(core.Team(*_game[0]), core.Team(*_game[1]))
            region.games.append(game)
        regions.append(region)

    return regions

def output_formatted(rounds):
    for round_ in rounds:
        for idx, region in enumerate(round_.regions):
            for game in region.games:
                team1_odds = '{0:.2f}'.format(game.team1.get_odds())
                team2_odds = '{0:.2f}'.format(game.team2.get_odds())
                indent = '  ' * round_.number
                print(f'{indent}{game.team1} {team1_odds}')
                print(f'{indent}{game.team2} {team2_odds}')
                print()

def simulate(round_):
    """Simulates the various games in a round and returns the next round"""
    next_round = core.Round(round_.number + 1)
    for region in round_.regions:
        next_region = core.Region()
        for i in range(0, len(region.games), 2):
            game1_winner = region.games[i].play()
            game2_winner = region.games[i+1].play()
            next_region.games.append(core.Game(game1_winner, game2_winner))
        next_round.regions.append(next_region)
    return next_round


round_1 = core.Round(1)
round_1.regions = load('round1.json')
round_2 = simulate(round_1)
round_3 = simulate(round_2)
round_4 = simulate(round_3)
output_formatted([round_3])

