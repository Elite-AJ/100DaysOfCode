class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_num < len(self.question_list)
    
    def next_question(self):
        current_qestion = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_qestion.question} True/False: ")
        self.check_answer(user_answer, current_qestion.correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 
            print("You got it right")
        else:
            print(f"You are wrong,the correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")