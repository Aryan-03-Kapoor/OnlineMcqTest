questions = ["Q1) What is 2 + 3",
             "Q2) Who is the 11th president of India?",
             "Q3) True or False... Indian Cricket Team won the 2011 world cup?",
             "Q4) When did the Indian Cricket Team won the world cup before 2011?",
             "Q5) True or False... The current Prime Minister of India is Pierre Manmohan Singh?"]
answer_choices = ["a)1\nb)5\nc)3\nd)4\n:",
                  "a)Ram Nath Kovind\nb)K. R. Narayanan\nc)Abdul Kalam\nd)Pratibha Patil\n:",
                  ":",
                  "a)1983\nb)1985\nc)1987\nd)1994\n:",
                  ":"]
correct_choices = [{"b", "2"},
                   {"c", "Abdul Kalam"},
                   {"true", "t"},
                   {"a", "1983"},
                   {"false", "f"}]
answers = ["2 + 3 is 5",
           "The 11th president of India is Abdul Kalam",
           "",
           "The last time the Indian Cricket Team won the world cup before 2011 was 1983",
           "The current Prime Minster of India is Narendra Modi"]


def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

if __name__ == "__main__":
    quiz()
