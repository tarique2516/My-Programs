def KBC_Game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
            "answer": "B"
        },
        {
            "question": "Which cricketer makes ODI highest score in an ODI innings ?",
            "options": ["A) Rohit sharma", "B) Martin Guptil", "C) Chris Gayle", "D) Rickey Ponting"],
            "answer": "A"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C"
        },
        {
            "question": "Which city is known as pink city'?",
            "options": ["A) Mumbai", "B) Jaipur", "C) Bengaluru", "D) Chennai"],
            "answer": "B"
        },
        {
            "question": "Which of these is a prime number?",
            "options": ["A) 4", "B) 6", "C) 9", "D) 11"],
            "answer": "D"
        },
        {
            "question":"In which City Taj Mahal is Located?",
            "options": ["A) New Delhi", "B) Noida", "C) Agra", "D) Kota"],
            "answer": "C"
        },
        {
            "question":"Who is the current Prime Minister of India",
            "options": ["A) Manmohan Singh", "B) Rahul Gandhi", "C) Nitish Kumar", "D) Narendra Modi"],
            "answer": "D"
        },
        {
            "question":"Which of the following Bollywood superstars lives in a Bungalow called Mannat?",
            "options": ["A) Salman Khan", "B) Akshay Kumar", "C) Shah Rukh Khan", "D) Amir Khan"],
            "answer": "C"
        },
        {
            "question":" Who is the author of the famous book “The God of Small Things”?",
            "options": ["A) R.K. Narayan", "B) Salman Rushdie ", "C) Jhumpa Lahiri", "D) Arundhati Roy"],
            "answer": "D"
        },
        {
            "question": "What is the full form of the URL?",
            "options": ["A) User Response Level", "B) Uniform Resource Locator", "C) Universal Random Language", "D) Updated Research Library"],
            "answer": "B"
        },
        {
            "question": "What was the name of Pakistan’s first governor general?",
            "options": ["A) Shahid Afridi", "B) Imran Khan", "C) Muhammad Ali Jinnah", "D) Babar Azam"],
            "answer": "C"
        },
        {
            "question": "Which Pakistani's cricket player make double century in One Day International?",
            "options": ["A) Muhammad Rizwan", "B) Fakahar Zaman", "C) Kamran Akmal", "D) Javed Miandaad"],
            "answer": "B"
        }
    ]
    

    prize = [10000, 20000, 30000, 40000, 50000, 100000, 300000, 600000, 1200000, 10000000, 30000000, 50000000, 70000000]
    total_prize = 0
    question_number = 1

    print("********  Welcome To Kon Banega Crorepati  ********\n")

    for q in questions:
        print(f"Question {question_number}: {q['question']}")
        for option in q["options"]:
            print(option)

        answer = input("Enter the options (A/B/C/D): ").strip().upper()

        if answer not in ["A","B","C","D"]:
            print("Invalid Choice! You Need To choose From A/B/C/D")
            break

        # Check tha answer is correct
        if answer == q["answer"]:
            total_prize += prize[question_number - 1]
            print(f"Correct! You have won prize Rs{prize[question_number - 1]}.\n")
        else:
            print(f"The Correct answer is {q['answer']}. You Have Won Rs{total_prize}\n")
            break

        question_number += 1
    else:
        print(f"Congratulations! you answered all question correctly! Your Total prize Rs{total_prize}.\n ")

    print("Thank You For Playing Kon Banega Crorepati!")
KBC_Game()