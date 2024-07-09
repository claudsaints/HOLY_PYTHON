class QuizBrain:
	def __init__(self,q_list):
		self.question_number = 0
		self.question_list = q_list
	def stillQuest(self):
		return self.question_number < len(self.question_list)

	def certain(self):
		current_question = self.question_list[self.question_number]
		user_answer = input(f"Q-{self.question_number}: {current_question.text} (True/False)?:")
		self.check(user_answer,current_question.answer)
		self.question_number+=1
	def check(self,resposta,resposta_certa):
		score = 0
		if resposta.lower() == resposta_certa.lower():
			print("Você acertou")
			score += 1
		else:
			print("Você Errou")
			print(f"A Resposta Correta era {resposta_certa}")
