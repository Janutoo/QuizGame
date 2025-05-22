from game_facade import Game_Facade
class Menu:
    def __init__(self):
        self.game_facade = Game_Facade()
        
    def display_menu(self):
        
        print("\n===MENU===")           
        print("1. Start the Quiz ")
        print("2. Export Report to File")
        print("3. Show Statstics")
        print("4. Exit")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Twój wybór: ")
            if choice == '1':
                self.game_facade.start_quiz()
            elif choice == '2':
                self.game_facade.save_report()
            elif choice == '3':
                self.game_facade.show_statistics()
            elif choice == '4':
                break
            else:
                print("Nieprawidłowy wybór.")


def main():
    menu = Menu()
    menu.run()

if __name__ == "__main__":
    main()

