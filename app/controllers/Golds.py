from system.core.controller import *
import random
import time

class Golds(Controller):
	def __init__(self, action):
		super(Golds, self).__init__(action)

	def index(self):
		try:
			session['goldearned']
			session['message']
		except:
			session['goldearned'] = 0
			session['message'] = []
		return self.load_view('index.html')

	def process_money(self):
		gold = 0;
		curr_time = time.strftime("%m/%d/%y %H:%M:%S")
		if request.form['building'] == 'farm':
			gold=random.randrange(10,21)
			loot=curr_time + ' - Whew, great job in those fields! Walked away with ' + str(gold) + ' gold from the farm!'
			session['message'].insert(0,loot)
			session['goldearned'] += gold
		elif request.form['building'] == 'cave':
			gold=random.randrange(0,51)
			if gold == 0:
				loot = curr_time + ' - Hey waitaminnit... You didn\'t find anything!'
			else:
				loot=curr_time + ' - That was scary... Managed to escape with ' + str(gold) + ' gold from the cave!'
			session['message'].insert(0,loot)
			session['goldearned'] += gold
		elif request.form['building'] == 'house':
			gold=random.randrange(5,16)
			loot=curr_time + ' - Wait a second, why were you looting someone\'s house?! Did you just steal ' + str(gold) + ' gold?!'
			session['message'].insert(0,loot)
			session['goldearned'] += gold
		elif request.form['building'] == 'casino':
			luck = random.randrange(1,100)
			gamble = random.randrange(50,101)
			gold = gamble

		if request.form['building'] == 'casino':
			if int(session['goldearned']) < 0:
				loot = curr_time + ' - You\'re in debt to the casino! You can\'t play! Go earn some money!'
				# loot = curr_time + ' - What are you doing? You owe money, how are you going to play?!'
				session['message'].insert(0,loot)
			elif luck < 70:
				session['goldearned'] -= gamble
				loot = curr_time + ' - Gambling is an addiction... Sorry! You lost ' + str(gold) + ' gold from the casino!'
				session['message'].insert(0,loot)
			elif luck >= 70:
				session['goldearned'] += gamble
				loot = curr_time + ' - Score, you hit a jackpot! Won ' + str(gold) + ' gold from the casino!'
				session['message'].insert(0,loot)

		return redirect('/')

	def reset(self):
		session['goldearned']=0
		session['message']=[]
		return redirect('/')