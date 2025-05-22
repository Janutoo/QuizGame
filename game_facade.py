from file_reader import File_Reader

class Game_Facade:
    def __init__(self, questions_file="Questions.txt", report_file="results.txt"):
        self.questions_file = questions_file
        self.report_file = report_file
        self.engine = None
    
    def read_files(self):
        print("bbb")

    def start_quiz(self):
        file_reader = File_Reader(self.questions_file)
        questions = file_reader.loading_file()
        
        

    def show_statistics(self):
        print("cccc")
    
    def save_report(self):
        print("dddd")


