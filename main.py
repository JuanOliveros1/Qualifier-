import random


def play_again():
	print()
	response = input('Want to play again(yes or no): ').lower()

	if response == 'yes':
		play_hangman()
	elif response == 'no':
		print('Thanks for playing')
	else:
		play_again()


def play_hangman():
	print('Lets play hangman!!')
	correct_word = random.choice([
	    'car', 'paper', 'rock', 'house', 'painting', 'goat', 'python', 'clown',
	    'elephant'
	]).lower()

	aph = ('abcdefghijklmnopqrstuvwxyz')
	tries = 6
	print(f'Your word contains {len(correct_word)} letters: ')
	letters_tried = []

	print(len(correct_word) * ' _')

	while tries > 0:

		print(f'You have {tries} guesses good luck')
		print()
		guess = input('Try to guess a letter or the world: ').lower()
		if len(guess) == 1:
			if guess not in aph:
				print('Input a letter')
				tries -= 1
			elif guess in letters_tried:
				print('You have already guessed that letter ')
				tries -= 1
			elif guess in correct_word:
				print()
				print('That letter is in the word good try')
				letters_tried.append(guess)

			elif guess not in correct_word:
				tries -= 1
				print()
				print('Wrong guess')
				letters_tried.append(guess)

		elif len(correct_word) == len(guess):
			if guess == correct_word:
				print('You guess the correct word')

				break
			else:
				print('Try again')
				tries -= 1
		else:
			print('Make sure to guess 1 letter or the word. ')
			tries -= 1

		output = ''
		if True:
			for word in correct_word:
				if word in letters_tried:
					output += word
				else:
					output += ' _'
			print(output)

		if output == correct_word:
			print()
			print("congratulations you won")

			break
	play_again()


play_hangman()
