from file_operations import save_cards, load_cards

cards = load_cards()

def create_card():
    question = input("Ingrese la pregunta: ")
    answer = input("Ingrese la respuesta: ")
    card = {"question": question, "answer": answer}
    cards.append(card)
    save_cards(cards)
    print("Tarjeta creada exitosamente.")

def edit_card():
    list_cards()
    index = int(input("Seleccione el número de la tarjeta a editar: "))
    if 0 <= index < len(cards):
        question = input("Ingrese la nueva pregunta: ")
        answer = input("Ingrese la nueva respuesta: ")
        cards[index] = {"question": question, "answer": answer}
        save_cards(cards)
        print("Tarjeta editada exitosamente.")
    else:
        print("Índice no válido.")

def delete_card():
    list_cards()
    index = int(input("Seleccione el número de la tarjeta a eliminar: "))
    if 0 <= index < len(cards):
        cards.pop(index)
        save_cards(cards)
        print("Tarjeta eliminada exitosamente.")
    else:
        print("Índice no válido.")

def list_cards():
    if cards:
        for i, card in enumerate(cards):
            print(f"{i}. Pregunta: {card['question']}, Respuesta: {card['answer']}")
    else:
        print("No hay tarjetas disponibles.")
