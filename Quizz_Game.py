class Questions:
    def __init__(self):
        self.questions = ["What is the capital of France?",
                          "What is the largest planet in our solar system?",
                          "Which country is famous for the Great Wall?",
                          "What is the chemical symbol for water?",
                          "Who wrote 'To Kill a Mockingbird'?"]

        self.options = [
            ('London', 'Berlin', 'Paris', 'Rome'),
            ('Jupiter', 'Saturn', 'Neptune', 'Earth'),
            ('Japan','China', 'India', 'Russia'),
            ('CO2', 'NaCl', 'O2', 'H2O'),
            ('Harper Lee', 'J.K. Rowling', 'Stephen King', 'Charles Dickens')]

        self.answers = [3, 1, 2, 4, 1]
        self.length = len(self.questions)

    def add_questions(self, question, option, answer):
        self.questions.append(question)
        self.options.append(option)
        self.answers.append(answer)
        self.length += 1

    def delete_questions(self, i):
        if i < 0 or i >= self.length:
            print("Question Not Found. Please Check the Question Number Entered!!!")
            return
        if self.length == 0:
            print("No Question To Delete")
            return

        del self.questions[i], self.options[i], self.answers[i]
        self.length = len(self.questions)
        print(f"Question No {i + 1} has Been Deleted")


class Review:
    def __init__(self, user):
        self.user = user
        self.wrong = []

    def show_results(self):
        q1 = Game.q
        score = 0
        for i in range(q1.length):
            if self.user[i] == q1.answers[i]:
                score += 1
            else:
                self.wrong.append(i)
        return f"Your Score Is {score}"

    def display(self):
        q = Game.q
        if q.length == 0:
            print("No Questions to Display ")
        for i in range(q.length):
            print(f"{i + 1}. {Game.q.questions[i]}")
            print(f"1. {q.options[i][0]:<20} 2. {q.options[i][1]}\n"
                  f"3. {q.options[i][2]:<20} 4. {q.options[i][3]}")
            print()
            print(f"Your Answer was {q.options[i][self.user[i] - 1]}")
            if self.user[i] != q.answers[i]:
                print(f"Your Answer is Wrong \n"
                      f"Correct Answer is {q.options[i][q.answers[i] - 1]}\n")
            else:
                print("Your Answer Was Correct \n")


class Game:
    q = Questions()

    def __init__(self):
        self.__password = 'Qwerty1234#'

    def admin_panel(self):
        print("Enter Password :")
        if self.__password == input():
            while True:
                print("\n1. Add Questions \n2. Display Questions \n3. Remove Question \n4. Exit ")
                c1 = input()
                if c1 == '1':
                    ques = []
                    print("Enter Question :")
                    ques.append(input())
                    print("Enter Options in One Line With Space :")
                    ques.append(input())
                    print("Enter Correct Option Number :")
                    ques.append(int(input()))
                    Game.q.add_questions(ques[0], ques[1].split(), ques[2])
                elif c1 == '2':
                    for i in range(Game.q.length):
                        print(f"{i + 1}. {Game.q.questions[i]}")
                        print(f"1. {Game.q.options[i][0]:<20} 2. {Game.q.options[i][1]}\n"
                              f"3. {Game.q.options[i][2]:<20} 4. {Game.q.options[i][3]}\n")
                elif c1 == '3':
                    print("Enter the Question Number to Remove :")
                    num = int(input())
                    Game.q.delete_questions(num - 1)
                elif c1 == '4':
                    print("Logging Out of Admin Panel ")
                    return
                else:
                    print("Please Select Option Between 1 - 4 ")

        else:
            print("Wrong Password!!!!!")

    def quizz(self):
        print("---------------Quizz Game---------------")
        if Game.q.length == 0:
            print("No Question are There in Quiz. Please Contact Admin For More Information")
            return
        user = []
        for i in range(Game.q.length):
            print(f"{i + 1}. {Game.q.questions[i]}")
            print(f"1. {Game.q.options[i][0]:<20} 2. {Game.q.options[i][1]}\n"
                  f"3. {Game.q.options[i][2]:<20} 4. {Game.q.options[i][3]}")
            temp = int(input("Enter Your Option (1-4) : "))
            while temp < 1 or temp > 4:
                print("Please Enter Options Between 1 - 4 : ")
                temp = int(input()) 
            user.append(temp)
            print()
        r = Review(user)
        print(r.show_results())
        print("Wanna Check The Answers (Y/N)")
        check = input()
        if check == 'Y':
            print("\n----------REVIEW----------\n")
            r.display()


if __name__ == '__main__':
    g = Game()
    while True:
        print("----------Quizz Game----------")
        print("1. Admin Panel \n2. Play Quizz \n3. Exit")
        choice = input()
        if choice == '1':
            g.admin_panel()
        elif choice == '2':
            g.quizz()
        elif choice == '3':
            break
        else:
            print("Please Select Options Between 1 - 3 ")
