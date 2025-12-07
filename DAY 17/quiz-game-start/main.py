from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questionText = question["question"]
    questionAnswer = question["correct_answer"]
    new_question = Question(questionText, questionAnswer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is: {quiz.score}/{len(question_bank)}") 