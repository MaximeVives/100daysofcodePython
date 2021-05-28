class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.hasLose = False

    def still_has_questions(self):
        return self.question_number < len(self.question_list) and not self.hasLose

    def next_question(self):
        choice = 0
        while choice != "True" and choice != "False":
            choice = input(f'Q{self.question_number + 1}. {self.question_list[self.question_number].question} "True" or "False"')
        return choice

    def check_answer(self, answer):
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            self.question_number += 1
            return True
        else:
            self.hasLose = True
            return False
