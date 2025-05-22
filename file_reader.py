import re
class File_Reader:
    def __init__(self,fileName):
        self.fileName = fileName

    def loading_file(file_name):
        questions = []

        with open(file_name, 'r', encoding='utf-8') as file:
            linies = file.readlines()
        i = 0 
        while i < len(linies):
            question_line = linies[i]
            match = re.search(r"^(.*?) \[(\d+\.?\d*)\]$", question_line)
            if match:
                question_text = match.group(1)
                score = float(match.group(2))
                answers = []
                correct_index= -1
                for j in range(1, 5):
                    answer = linies[i + j]
                    if answer.startswith("*"):
                        correct_index = j - 1
                        answer = answer[1:].strip()
                    answers.append(answer)

                questions.append({
                    "question": question_text,
                    "score": score,
                    "answers": answers,
                    "correct_index": correct_index
                })            

                