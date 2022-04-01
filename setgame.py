import itertools as it
import random as rd
import pandas as pd

colors = ['green', 'red', 'purple']
shapes = ['diamond', 'squiggle', 'oval']
numbers = ['1', '2', '3']
shadings = ['outlined', 'striped', 'filled']
user_points = 0


class Card:
    def __init__(self, shape, color, number, shading, is_chosen):
        self.shape = shape
        self.color = color
        self.number = number
        self.shading = shading
        self.is_chosen = is_chosen


def create_card(card_shape, card_color, card_number, card_shading, is_chosen):
    return Card(card_shape, card_color, card_number, card_shading, is_chosen)


def create_deck(combination_list):
    deck_of_cards = []
    for comb in combination_list:
        card_shape = comb[0]
        card_color = comb[1]
        card_number = comb[2]
        card_shading = comb[3]
        card_instance = create_card(
            card_shape, card_color, card_number, card_shading, False)
        deck_of_cards.append(card_instance)
    return deck_of_cards


def initialize_game_setup():
    a = [shapes, colors, numbers, shadings]
    combination_list = list(it.product(*a))

    return create_deck(combination_list)


def create_game_table():
    game_table = []
    while len(game_table) != 12:
        card_selected = rd.randint(0, 80)
        if(card_selected not in game_table):
            game_table.append(card_selected)
        else:
            pass

    return game_table


def check_set_attributes(attribute1, attribute2, attribute3):
    if attribute1 == attribute2 and attribute2 == attribute3:
        return True
    elif (attribute1 != attribute2) and (attribute2 != attribute3) and (attribute3 != attribute1):
        return True
    else:
        return False


def check_set(card1, card2, card3):
    color_check = check_set_attributes(card1.color, card2.color, card3.color)
    shape_check = check_set_attributes(card1.shape, card2.shape, card3.shape)
    num_check = check_set_attributes(card1.number, card2.number, card3.number)
    shade_check = check_set_attributes(
        card1.shading, card2.shading, card3.shading)

    return color_check and shape_check and num_check and shade_check


def print_game_table(game_table, initial_deck):
    display = {}
    for card in game_table:
        display[card] = {
            'shape': initial_deck[card].shape,
            'color': initial_deck[card].color,
            'number': initial_deck[card].number,
            'shading': initial_deck[card].shading,
        }
    return display


def check_set_existence(game_table, initial_deck):
    is_set_exist = False
    for i in game_table:
        for j in game_table:
            for k in game_table:
                card1 = initial_deck[i]
                card2 = initial_deck[j]
                card3 = initial_deck[k]

                if((card1 != card2 and card2 != card3 and card1 != card3) and (card1.is_chosen == False and card2.is_chosen == False and card3.is_chosen == False)):
                    is_a_set = check_set(card1, card2, card3)
                    if(is_a_set == True):
                        is_set_exist = True
                        return is_set_exist
    return is_set_exist


def get_hints(game_table, initial_deck):
    hint_result = []
    for i in game_table:
        for j in game_table:
            for k in game_table:
                card1 = initial_deck[i]
                card2 = initial_deck[j]
                card3 = initial_deck[k]

                if(card1 != card2 and card2 != card3 and card1 != card3):
                    is_a_set = check_set(card1, card2, card3)
                    if(is_a_set == True):
                        hint_result.append(i)
                        hint_result.append(j)
                        hint_result.append(k)
                        return hint_result
    return hint_result


def remove_set_from_deck(card1, card2, card3, initial_deck):
    initial_deck[card1].is_chosen = True
    initial_deck[card2].is_chosen = True
    initial_deck[card3].is_chosen = True

    return initial_deck


def remove_cards_from_remaining_cards(remaining_cards, cards):
    for card in cards:
        remaining_cards.remove(card)

    return remaining_cards


def remove_set_from_game_table(card1, card2, card3, game_table):
    game_table.remove(card1)
    game_table.remove(card2)
    game_table.remove(card3)

    return game_table


def draw_three_cards(initial_deck, game_table, remaining_cards):
    addtl_cards = []

    if(len(remaining_cards) == 0):
        return []

    not_chosen_cards = remaining_cards

    while (len(addtl_cards) != 3):
        card_selected = rd.choice(not_chosen_cards)
        if((card_selected not in game_table) and (initial_deck[card_selected].is_chosen == False) and (card_selected not in addtl_cards)):
            addtl_cards.append(card_selected)

    return addtl_cards


def get_card_choice(game_table):
    while True:
        card = input("Please choose a card from the play table: ")
        if(card.strip().isdigit()):
            if(int(card) in game_table):
                break
    return int(card)


if __name__ == "__main__":
    game_started = False
    user_points = 0
    remaining_cards = list(range(81))
    while True:
        if(game_started == False):
            game_start = input("Start game? y/n: ")

            if game_start.lower() not in ('y', 'n'):
                print("Not an appropriate choice.")

            elif(game_start.lower() == 'y'):
                game_started = True
                initial_deck = initialize_game_setup()
                game_table = create_game_table()
                remaining_cards = remove_cards_from_remaining_cards(
                    remaining_cards, game_table)
            else:
                print("Thank you.")
                print("Your score is {}".format(user_points))
                break

        else:
            print("----------------------------------------------------")
            df = pd.DataFrame(print_game_table(game_table, initial_deck)).T
            print(df)
            print("Remaining cards in the deck: {}".format(
                len(remaining_cards))
            )
            user_answer = input(
                "Is set exists? Y/N (Press 1 for hint, Press 2 for exit game): ")

            if user_answer.lower() == 'y':
                card1 = get_card_choice(game_table)
                card2 = get_card_choice(game_table)
                card3 = get_card_choice(game_table)

                check_result = check_set(
                    initial_deck[card1], initial_deck[card2], initial_deck[card3])
                if(check_result == True):
                    user_points += 1
                    print("Correct! it is a set")

                    initial_deck = remove_set_from_deck(
                        card1, card2, card3, initial_deck)
                    game_table = remove_set_from_game_table(
                        card1, card2, card3, game_table)

                    if(len(game_table) < 12):
                        addtl_cards = draw_three_cards(
                            initial_deck, game_table, remaining_cards)
                        game_table = game_table + addtl_cards
                        remaining_cards = remove_cards_from_remaining_cards(
                            remaining_cards, addtl_cards)
                else:
                    print("Wrong! it is not a set")

            elif user_answer.lower() == 'n':
                if(check_set_existence(game_table, initial_deck) == False):
                    addtl_cards = draw_three_cards(
                        initial_deck, game_table, remaining_cards)
                    game_table = game_table + addtl_cards
                    remaining_cards = remove_cards_from_remaining_cards(
                        remaining_cards, addtl_cards)

                    if(len(remaining_cards) == 0):
                        print("Game over! No remaining sets available")
                        print("Your score is {}".format(user_points))
                        break
                else:
                    print("There exists a set.")
            elif user_answer == '1':
                if(check_set_existence(game_table, initial_deck) == False):
                    print("There's no set available.")
                else:
                    print(get_hints(game_table, initial_deck))
            elif user_answer == '2':
                print("Thank you for playing the game.")
                print("Your score is {}".format(user_points))
                break
            else:
                print("Not an appropriate choice.")
            game_started = True
