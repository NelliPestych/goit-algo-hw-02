import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    new_request = f"Request_{random.randint(1, 1000)}"
    request_queue.put(new_request)
    print(f"Generated and added to queue: {new_request}")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: {request}")
    else:
        print("Queue is empty, no requests to process.")

# Головний цикл програми
def main():
    while True:
        user_input = input("Enter 'g' to generate request, 'p' to process request, or 'q' to quit: ").lower()
        if user_input == 'g':
            generate_request()
        elif user_input == 'p':
            process_request()
        elif user_input == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid input, please try again.")
        time.sleep(1)  # Затримка для імітації роботи

if __name__ == "__main__":
    main()
