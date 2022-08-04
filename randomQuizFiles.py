import random

# Create dictionary of US States as keys 
# and their corresponding capitals as values
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}

# Create 35 copies of quiz forms with shuffled questions.
for quizNum in range(35):
    # Create folder 'quizGame' where a quiz file and answer key file will be written to.
    quizFile = open(f'quizGame/capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'quizGame/capitalsquiz_answers{quizNum + 1}.txt', 'w')

    quizFile.write("Name:\nDate:\n\nPeriod:\n\n")
    quizFile.write(' ' * 20 + f'State Capital Quiz (Form {quizNum + 1})')
    quizFile.write('\n')

    states = list(capitals.keys())
    random.shuffle(states)

    # Create 50 shuffled questions. 
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]     # Correct answer is deleted from the wrongAnswers list.
        wrongAnswers = random.sample(wrongAnswers, 3)           # wrongAnswers list is reduced to 3 samples from the initial list.
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f"\n{questionNum + 1}. What is the capital of "
                       f"{states[questionNum]}?\n")
        # Create multiple choice of 4 choices.
        for i in range(4):
            quizFile.write('\t' + f"{'ABCD'[i]}. {answerOptions[i]}\n")
           
        # Write the correct answers in the answer key within the same loop.
        answerKeyFile.write(f"{questionNum + 1}. "
                            f"{'ABCD'[answerOptions.index(correctAnswer)]}\n")

quizFile.close()
answerKeyFile.close()
