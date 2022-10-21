# mainでcsvのファイルを読み込んでいるのでインスタンスを生成するファイルでインポートしてください
import main


class Question:
    def __init__(self, questions_list):
        self.questions_list = questions_list

    def get_questions(self, num):
        return self.questions_list[num][0]

    def get_answer(self, num):
        return self.questions_list[num][1]

    def get_comment(self, num):
        return self.questions_list[num][2]


# テスト用で実際の動きを以下に示します。
questions = Question(main.ans_lists)
print(questions.get_questions(1))
