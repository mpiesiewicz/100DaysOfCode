from Config import Config
import random


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_already_answered = []
        self.question_list = question_list

    def draw_question(self):
        random_question_number = random.randint(0, len(self.question_list)-1)
        while random_question_number in self.questions_already_answered:
            random_question_number = random.randint(0, len(self.question_list))
        else:
            return random_question_number

    def next_question(self):
        current_question = self.question_list[self.draw_question()]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Right!')
            self.score += 1
        else:
            print('Wrong...')
        print(f'The correct answer was {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')

    def still_has_questions(self):
        return self.question_number < len(self.question_list) and self.question_number < Config.NUMBER_OF_QUESTIONS

