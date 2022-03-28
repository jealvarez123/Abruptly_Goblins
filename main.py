gamers = []


def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers_list.append(gamer)
    else:
        print('Gamer missing critical information')


# Next we want to add our first gamer! Her name is Kimberly Warner, and she's available on Mondays, Tuesdays,
# and Fridays.
kimberly = {
    'name': 'Kimberly Warner',
    'availability': ['Monday', 'Tuesday', 'Friday']
}
# we add kim to the gamers list
add_gamer(kimberly, gamers)
# adding more gamers
add_gamer({'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


# this is checking the availability of the gamers
def build_daily_frequency_table():
    return {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0

    }


count_availability = build_daily_frequency_table()


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        # this is grabbing all the values
        for day in gamer['availability']:
            # this is adding 1 for each day
            available_frequency[day] += 1


calculate_availability(gamers, count_availability)


# this finds the best day with most gamers by going through each day and comparing num of each
def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night


game_night = find_best_night(count_availability)


def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer['availability']]


attending_game_night = available_on_night(gamers, game_night)

form_email = """
Dear {name}

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society

"""


# creating an automated email sent to gamers
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))


send_email(attending_game_night, game_night, "Abruptly Goblins!")


unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")