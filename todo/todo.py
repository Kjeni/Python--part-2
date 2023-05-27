import json
from datetime import datetime, timedelta
import os

class Task:
    def __init__(self, task_id, title, description, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def clear_tasks(self):
        self.tasks.clear()
#funkcja dodaj zadanie by id:
    def add_task(self, title, description, due_date):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description, due_date)
        self.tasks.append(task)
        print("Dodano nowe zadanie o ID: ", task_id)
#funkcja usuwajaca zadanie by id:
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Usunięto zadanie o ID:", task_id)
                return
        print("Nie znaleziono zadania o podanym ID.")
#funkcja edytujaca zadanie:
    def update_task(self, task_id, title, description, due_date):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                task.due_date = due_date
                print("Zaktualizowano zadanie o ID:", task_id)
                return
        print("Nie znaleziono zadania o podanym ID.")
#funkcja pobierz zadanie by id:
    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
#funkcja pobierajaca wszystkie zadania:
    def get_all_tasks(self):
        if len(self.tasks) == 0:
            print("Brak zapisanych zadań.")
        else:
            for task in self.tasks:
                print("ID:", task.task_id)
                print("Tytuł:", task.title)
                print("Termin wykonania:", task.due_date.strftime("%Y-%m-%d"))
                print("Opis:", task.description)
#zapis do pliku:
    def save_tasks_to_file(self, file_path):
        tasks_data = []
        for task in self.tasks:
            task_data = {
                "task_id": task.task_id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date.strftime("%Y-%m-%d")
            }
            tasks_data.append(task_data)

        with open(file_path, "w") as file:
            json.dump(tasks_data, file, indent=4)
#funkcja wczytania z pliku z sortowaniem:(json)
    def load_tasks_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                tasks_data = json.load(file)
                task_data = sorted(file, key=lambda x: x['task_id'])
            for task_data in tasks_data:
                task_id = task_data["task_id"]
                title = task_data["title"]
                description = task_data["description"]
                due_date = datetime.strptime(task_data["due_date"], "%Y-%m-%d")
                task = Task(task_id, title, description, due_date)
                self.tasks.append(task)

            print("Załadowano zapisane zadania.")
        except FileNotFoundError:
            print("Nie znaleziono pliku z zapisanymi zadaniami.")
#funkcja z menu:
def display_menu():
    print("======== MENU =======")
    print("1. Dodaj nowe zadanie")
    print("2. Wyświetl zadanie")
    print("2a. Wyświetl zadanie wraz z opisem")
    print("3. Usuń zadanie")
    print("4. Zaktualizuj zadanie")
    print("5. Zapisz zadania do pliku")
    print("6. Wczytaj zadania z pliku")
    print("7. Wyświetl wszystkie zadania")
    print("8. Wyjście")
#walidacja daty:
def validate_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Niepoprawny format daty. Wprowadź datę w formacie RRRR-MM-DD.")
        return None
#program i pętla sterująca dla użytkownika:
def main():
    task_manager = TaskManager()
    file_path = os.path.join(os.path.dirname(__file__), "zapisy", "autozapis" )
    task_manager.load_tasks_from_file(file_path)
    task_manager.get_all_tasks()
    while True:
        display_menu()
        choice = input("Wybierz opcję: ")
        if choice == "1":
            title = input("Podaj tytuł zadania: ")
            description = input("Podaj opis zadania: ")
            due_date_str = input("Podaj termin wykonania (RRRR-MM-DD): ")
            due_date = validate_datetime(due_date_str)
            if due_date is not None:
                task_manager.add_task(title, description, due_date)
        elif choice == "2":
            task_id = int(input("Podaj ID zadania do wyświetlenia: "))
            task = task_manager.get_task(task_id)
            if task:
                print("ID:", task.task_id)
                print("Tytuł:", task.title)
                print("Termin wykonania:", task.due_date)
            else:
                print("Nie znaleziono zadania o podanym ID.")
        elif choice == "2a":
            task_id = int(input("Podaj ID zadania do wyświetlenia: "))
            task = task_manager.get_task(task_id)
            if task:
                print("ID:", task.task_id)
                print("Tytuł:", task.title)
                print("Termin wykonania:", task.due_date)
                print("Opis:", task.description)
            else:
                print("Nie znaleziono zadania o podanym ID.")
        elif choice == "3":
            task_id = int(input("Podaj ID zadania do usunięcia: "))
            task_manager.delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Podaj ID zadania do zaktualizowania: "))
            title = input("Podaj nowy tytuł zadania: ")
            description = input("Podaj nowy opis zadania: ")
            due_date_str = input("Podaj nowy termin wykonania (RRRR-MM-DD): ")
            due_date = validate_datetime(due_date_str)
            if due_date is not None:
                task_manager.update_task(task_id, title, description, due_date)
        elif choice == "5":
            filename = input("Podaj nazwę pliku do zapisu: ")
            file_path = os.path.join(os.path.dirname(__file__), "zapisy", filename )
            task_manager.save_tasks_to_file(file_path)
            print("Zapisano zadania do pliku.")
        elif choice == "6":
            print("UWAGA! Ta operacja wymaga usunięcia dotychczasowych zadań!")
            print("Wpisz: 'tak', aby potwierdzić lub pozostaw pole puste, aby wrócić do menu głównego")
            potwierdzenie = input("Czy potwierdzasz operację usnięcia?: ")
            if potwierdzenie == "tak":
                task_manager.clear_tasks()
                filename = input("Podaj nazwę pliku do wczytania: ")
                file_path = os.path.join(os.path.dirname(__file__), "zapisy", filename )
                task_manager.load_tasks_from_file(file_path)
            else:
                continue
        elif choice == "7":
            task_manager.get_all_tasks()
        elif choice == "8":
            file_path = os.path.join(os.path.dirname(__file__), "zapisy", "autozapis" )
            task_manager.save_tasks_to_file(file_path)   
            print("Program zakończył swoje działanie.")
            break
        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")

if __name__ == "__main__":
    main()

