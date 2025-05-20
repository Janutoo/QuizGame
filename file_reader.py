
import re

def loading_file(file_name):
    quesrion1 = []
    with open(file_name, 'r', encoding='utf-8') as plik:
        while True:
            question_line = plik.readline().strip()
            if not question_line:
                break  

            match = re.search( )
            

            

            quesrion1.append({
                "pytanie": questions ,
                "odpowiedzi": answers,
                "punkty": points,
                "prawidłowa_odpowiedź": correct_answers
            })
    return quesrion1

file_name = "Questions.txt" 
data = loading_file(file_name)
print(data)