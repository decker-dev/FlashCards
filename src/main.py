import json
import random
from datetime import datetime, timedelta

def clear_screen():
    print('\n' * 100)


def load_data():
    try:
        with open("flashcards_data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return (data.get('decks', {'General': []}),
                    data.get('users', {}),
                    data.get('card_history', {}),
                    data.get('scores', {}))
    except FileNotFoundError:
        return {'General': []}, {}, {}, {}


def save_data(decks, users, card_history, scores):
    data = {
        'decks': decks,
        'users': users,
        'card_history': card_history,
        'scores': scores
    }
    with open("flashcards_data.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def show_error(message):
    print(f"\n{message}")
    input("Press Enter to continue...")


def select_user(users):
    while True:
        clear_screen()
        print("\n=== User Selection ===")

        if users:
            print("\nExisting users:")
            for i, name in enumerate(users.keys(), 1):
                print(f"{i}. {name}")
            print(f"{len(users) + 1}. Create new user")

            option = input("\nChoose an option: ")
            if option.isdigit():
                option = int(option)
                if 1 <= option <= len(users):
                    return list(users.keys())[option - 1]
                elif option == len(users) + 1:
                    return create_user(users)
        else:
            print("\nNo registered users.")
            return create_user(users)

        show_error("Invalid option.")


def update_score(scores, user, results):
    if user not in scores:
        scores[user] = {
            'points': 0,
            'total_correct': 0,
            'total_attempts': 0,
            'streak': 0,
            'best_streak': 0
        }

    points_per_answer = {
        'Perfect': 10,
        'Good': 7,
        'Bad': 3,
        'Terrible': 1
    }

    session_points = sum(points_per_answer[response] * quantity
                         for response, quantity in results.items())

    scores[user]['points'] += session_points
    scores[user]['total_correct'] += results['Perfect'] + results['Good']
    scores[user]['total_attempts'] += sum(results.values())

    if sum(results.values()) > 0:
        if results['Perfect'] + results['Good'] > results['Bad'] + results['Terrible']:
            scores[user]['streak'] += 1
        else:
            scores[user]['streak'] = 0

    if scores[user]['streak'] > scores[user]['best_streak']:
        scores[user]['best_streak'] = scores[user]['streak']


def create_user(users):
    while True:
        clear_screen()
        print("\n=== Create New User ===")
        name = input("\nEnter your name: ").strip()

        if name and name not in users:
            users[name] = {
                'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return name

        show_error("Invalid or already existing name. Try another one.")


def select_deck(decks, mode="practice"):
    while True:
        clear_screen()
        print(f"\n=== Select Deck for {mode} ===")

        print("\nAvailable decks:")
        for i, name in enumerate(decks.keys(), 1):
            count = len(decks[name])
            print(f"{i}. {name} ({count} cards)")

        if mode == "create":
            print(f"{len(decks) + 1}. Create new deck")

        option = input("\nChoose an option: ")
        if option.isdigit():
            option = int(option)
            if 1 <= option <= len(decks):
                return list(decks.keys())[option - 1]
            elif mode == "create" and option == len(decks) + 1:
                return create_deck(decks)

        show_error("Invalid option.")


def create_deck(decks):
    while True:
        clear_screen()
        print("\n=== Create New Deck ===")
        name = input("\nEnter the name of the deck: ").strip()

        if name and name not in decks:
            decks[name] = []
            return name

        show_error("Invalid or already existing name. Try another one.")


def add_card(decks):
    deck_name = select_deck(decks, "create")
    clear_screen()
    print(f"\n=== Add New Card to Deck '{deck_name}' ===")
    question = input("\nEnter the question: ")
    answer = input("Enter the answer: ")

    new_card = {
        "id": f"{deck_name}_{len(decks[deck_name]) + 1}",
        "question": question,
        "answer": answer,
        "deck": deck_name
    }
    decks[deck_name].append(new_card)
    print("\nCard added successfully!")
    input("Press Enter to continue...")
    return decks


def get_rating():
    while True:
        print("\nHow did you do with this card?")
        print("1. Perfect - Immediate and correct response")
        print("2. Good - Hesitated but remembered")
        print("3. Bad - Struggled to remember")
        print("4. Terrible - Didn't remember at all")

        result = input("\nChoose an option (1-4): ")
        if result in ['1', '2', '3', '4']:
            intervals = {
                '1': ('Perfect', timedelta(days=7).total_seconds()),
                '2': ('Good', timedelta(days=1).total_seconds()),
                '3': ('Bad', timedelta(minutes=10).total_seconds()),
                '4': ('Terrible', 0.0)
            }
            return intervals[result]
        print("Please enter a number from 1 to 4")


def calculate_available_cards(cards, card_history, user):
    now = datetime.now()
    available_cards = []

    for card in cards:
        card_id = card['id']
        history_key = f"{user}_{card_id}"

        if history_key not in card_history:
            available_cards.append(card)
        else:
            last_review = datetime.strptime(
                card_history[history_key]['last_review'],
                "%Y-%m-%d %H:%M:%S"
            )
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval

            if now >= next_review:
                available_cards.append(card)

    return available_cards


def show_ranking(scores):
    clear_screen()
    print("\n=== 🏆 User Ranking ===\n")

    if not scores:
        print("No scores registered yet.")
        input("\nPress Enter to continue...")
        return

    sorted_users = sorted(scores.items(),
                          key=lambda x: x[1]['points'],
                          reverse=True)

    max_points = max(data[1]['points'] for data in sorted_users)
    max_name_length = max(len(user) for user, _ in sorted_users)
    graph_width = 30

    print(f"{'User':<{max_name_length}} | {'Points':>7} | {'Accuracy':>8} | Graph")
    print("-" * (max_name_length + graph_width + 22))

    for pos, (user, data) in enumerate(sorted_users, 1):
        points = data['points']
        total_correct = data['total_correct']
        total_attempts = data['total_attempts']
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0

        bar_length = int((points / max_points) * graph_width) if max_points > 0 else 0
        bar = '█' * bar_length

        medal = ''
        if pos == 1:
            medal = '🥇 '
        elif pos == 2:
            medal = '🥈 '
        elif pos == 3:
            medal = '🥉 '

        print(f"{medal}{user:<{max_name_length}} | {points:>7} | {accuracy:>7.1f}% | {bar}")

    print("\nLegend:")
    print("• Points: Perfect = 10pts, Good = 7pts, Bad = 3pts, Terrible = 1pt")
    print("• Accuracy: Percentage of correct answers (Perfect + Good)")
    input("\nPress Enter to continue...")


def show_user_stats(scores, user):
    clear_screen()
    if user not in scores:
        print(f"\nNo statistics available for {user}")
        input("\nPress Enter to continue...")
        return

    data = scores[user]
    print(f"\n=== 📊 Statistics of {user} ===\n")

    accuracy = (data['total_correct'] / data['total_attempts'] * 100) if data['total_attempts'] > 0 else 0

    print(f"🏆 Total points: {data['points']}")
    print(f"📈 Global accuracy: {accuracy:.1f}%")
    print(f"🎯 Total correct: {data['total_correct']}")
    print(f"🔄 Total attempts: {data['total_attempts']}")
    print(f"🔥 Current streak: {data['streak']}")
    print(f"⭐ Best streak: {data['best_streak']}")

    if data['total_attempts'] > 0:
        print("\nProgress:")
        level = "Beginner"
        if data['points'] >= 1000:
            level = "Master"
        elif data['points'] >= 500:
            level = "Expert"
        elif data['points'] >= 200:
            level = "Advanced"
        elif data['points'] >= 100:
            level = "Intermediate"

        print(f"📚 Current level: {level}")

        if level != "Master":
            next_level = {
                "Beginner": ("Intermediate", 100),
                "Intermediate": ("Advanced", 200),
                "Advanced": ("Expert", 500),
                "Expert": ("Master", 1000)
            }
            next_level_name, points_needed = next_level[level]
            points_remaining = max(0, points_needed - data['points'])
            print(f"🎯 Points for {next_level_name}: {points_remaining}")

    input("\nPress Enter to continue...")


def practice(decks, user, card_history, scores):
    deck_name = select_deck(decks)
    cards = decks[deck_name]

    if not cards:
        show_error(f"There are no cards in the deck '{deck_name}'. Add some first.")
        return

    available_cards = calculate_available_cards(cards, card_history, user)

    if not available_cards:
        show_error(f"No cards available for review in the deck '{deck_name}'.\n" +
                   "Come back later when the review intervals are up.")
        return

    random.shuffle(available_cards)
    results = {'Perfect': 0, 'Good': 0, 'Bad': 0, 'Terrible': 0}

    for i, card in enumerate(available_cards, 1):
        clear_screen()
        print(f"\n=== Deck: {deck_name} - Question {i}/{len(available_cards)} ===")
        print(f"\nQuestion: {card['question']}")
        input("\nPress Enter to see the answer...")
        print(f"\nAnswer: {card['answer']}")

        rating, interval = get_rating()
        results[rating] += 1

        history_key = f"{user}_{card['id']}"
        card_history[history_key] = {
            'last_review': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'rating': rating,
            'interval': interval
        }

    update_score(scores, user, results)
    show_results(results, len(available_cards))


def show_results(results, total_cards):
    clear_screen()
    print("\n=== Session Results ===")
    print("\nBreakdown by rating:")
    for rating, count in results.items():
        percentage = (count / total_cards) * 100 if total_cards > 0 else 0
        print(f"{rating}: {count} cards ({percentage:.1f}%)")

        if rating == 'Perfect':
            print("  → Next review in 1 week")
        elif rating == 'Good':
            print("  → Next review in 1 day")
        elif rating == 'Bad':
            print("  → Next review in 10 minutes")
        else:
            print("  → Will appear in the next session")

    input("\nPress Enter to continue...")


def view_cards(decks, user, card_history):
    deck_name = select_deck(decks)
    cards = decks[deck_name]

    clear_screen()
    if not cards:
        show_error(f"There are no cards in the deck '{deck_name}'.")
    else:
        print(f"\n=== Cards of Deck '{deck_name}' ===\n")
        for i, card in enumerate(cards, 1):
            print(f"Card {i}:")
            print(f"Question: {card['question']}")
            print(f"Answer: {card['answer']}")

            history_key = f"{user}_{card['id']}"
            if history_key in card_history:
                last_review = datetime.strptime(
                    card_history[history_key]['last_review'],
                    "%Y-%m-%d %H:%M:%S"
                )
                interval = timedelta(seconds=card_history[history_key]['interval'])
                next_review = last_review + interval
                now = datetime.now()

                if now < next_review:
                    remaining_time = next_review - now
                    print(f"Status: Locked - Available in {format_time(remaining_time)}")
                else:
                    print("Status: Available for review")
            else:
                print("Status: New - Not studied yet")
            print()
    input("\nPress Enter to continue...")


def format_time(td):
    days = td.days
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60

    if days > 0:
        return f"{days} days, {hours} hours"
    elif hours > 0:
        return f"{hours} hours, {minutes} minutes"
    else:
        return f"{minutes} minutes"


def edit_card(decks):
    deck_name = select_deck(decks)
    cards = decks[deck_name]
    if not cards:
        show_error(f"There are no cards in the deck '{deck_name}'.")
        return

    while True:
        clear_screen()
        print(f"\n=== Edit Card in Deck '{deck_name}' ===")
        for i, card in enumerate(cards, 1):
            print(f"{i}. {card['question']}")

        option = input("\nChoose a card to edit (0 to cancel): ")
        if option == '0':
            return
        if option.isdigit() and 1 <= int(option) <= len(cards):
            card = cards[int(option) - 1]
            card['question'] = input(
                f"Current question: {card['question']} \nNew question (leave blank to keep): ") or card['question']
            card['answer'] = input(
                f"Current answer: {card['answer']} \nNew answer (leave blank to keep): ") or card['answer']
            print("\nCard successfully edited!")
            input("Press Enter to continue...")
            return
        show_error("Invalid option.")


def delete_card(decks):
    deck_name = select_deck(decks)
    cards = decks[deck_name]
    if not cards:
        show_error(f"There are no cards in the deck '{deck_name}'.")
        return

    while True:
        clear_screen()
        print(f"\n=== Delete Card in Deck '{deck_name}' ===")
        for i, card in enumerate(cards, 1):
            print(f"{i}. {card['question']}")

        option = input("\nChoose a card to delete (0 to cancel): ")
        if option == '0':
            return
        if option.isdigit() and 1 <= int(option) <= len(cards):
            cards.pop(int(option) - 1)
            print("\nCard successfully deleted!")
            input("Press Enter to continue...")
            return
        show_error("Invalid option.")


def edit_deck(decks):
    deck_name = select_deck(decks, mode="edit")
    new_name = input(f"\nEnter the new name for the deck '{deck_name}' (Enter to cancel): ").strip()
    if not new_name:
        return
    if new_name and new_name not in decks:
        decks[new_name] = decks.pop(deck_name)
        print("\nDeck successfully renamed!")
        input("Press Enter to continue...")
    else:
        show_error("Invalid or already existing name.")


def delete_deck(decks):
    deck_name = select_deck(decks)
    confirmation = input(f"\nAre you sure you want to delete the deck '{deck_name}' and all its cards? (y/n): ").lower()
    if confirmation == 'y':
        del decks[deck_name]
        print("\nDeck successfully deleted!")
    else:
        show_error("Deletion canceled.")


def main_menu():
    decks, users, card_history, scores = load_data()
    current_user = select_user(users)
    exit_program = True
    while exit_program:
        clear_screen()
        print(f"\n=== 🎮 Flashcard Game - User: {current_user} ===")
        print("\n1. 📝 Add card")
        print("2. 🎯 Practice")
        print("3. 📊 View cards and statuses")
        print("4. 📚 Create new deck")
        print("5. 👤 Change user")
        print("6. ✏️ Edit card")
        print("7. 🗑️ Delete card")
        print("8. 📋 Edit deck")
        print("9. ❌ Delete deck")
        print("10. 🏆 View global ranking")
        print("11. 📈 View my stats")
        print("12. 🚪 Exit")

        option = input("\nChoose an option (1-12): ")

        if option == '1':
            decks = add_card(decks)
        elif option == '2':
            practice(decks, current_user, card_history, scores)
        elif option == '3':
            view_cards(decks, current_user, card_history)
        elif option == '4':
            create_deck(decks)
        elif option == '5':
            current_user = select_user(users)
        elif option == '6':
            edit_card(decks)
        elif option == '7':
            delete_card(decks)
        elif option == '8':
            edit_deck(decks)
        elif option == '9':
            delete_deck(decks)
        elif option == '10':
            show_ranking(scores)
        elif option == '11':
            show_user_stats(scores, current_user)
        elif option == '12':
            print("\nGoodbye! 👋")
            exit_program = False
        else:
            show_error("Invalid option. Please choose an option from 1 to 12.")

        save_data(decks, users, card_history, scores)

if __name__ == "__main__":
    main_menu()