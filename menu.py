class Menu:
    def __init__(self):
        pass

    def run(self):
        while True:
            print("\nWybierz opcję:")
            print("1. GRAJ")
            print("2. Zapisz zaszyfrowany tekst do pliku")
            print("3. Deszyfruj tekst z pliku")
            print("4. Statystyki")
            print("5. Wyjdź")

            choice = input("Twój wybór: ")
            if choice == '1':
                self.encrypt_text()
            elif choice == '2':
                self.save_to_file()
            elif choice == '3':
                self.decrypt_from_file()
            elif choice == '4':
                self.print_encrypted_texts()
            elif choice == '5':
                break
            else:
                print("Nieprawidłowy wybór.")




