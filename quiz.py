
print("Welcome to this Quiz App\n")
print("There are 5 questions in this Quiz...\nKindly enter\n1 for Option A")
print("2 for Option B\n3 for Option C\n4 for Option D\n...Good Luck")
user_name = input("Please enter your name? ")
no_of_questions = 5
score = 0
questions_dict = {"What is the name of our instructor? ":{ "options": ["Ben","Ade","Ïfe","John"],"answer": "1"},
                  "What does CSS stand for? ": { "options": ["Cascading Style Sheet","Contour Style Sheat","Cascaded Style Sheet","Casser Styles Sharia"],"answer": "1"},
                  "How many colors does Nigerian flag have? ": { "options": ["One","Two","Three","Four"],"answer": "2"},
                  "Who is Nigeria's President?": { "options": ["Buhari","Saraki","Jonathan","Ambode"],"answer": "1"},
                  "What body tackles corruption in Nigeria?": { "options": ["EFCC","INEC","ICPC","NUC"],"answer": "1"}}
for question in questions_dict:
    print(question)
    #print(questions_dict[i])
    for options in questions_dict[question]["options"]:

        print(options)

    user_answer = input("Answer? ")
    if(user_answer == questions_dict[question]["answer"]):
        score += 1

print("Result............\n")
print("Name:",user_name)
print("Your Score is ",score)
percentage_score = (score/no_of_questions) * 100
print("Your Percentage Score is ",percentage_score,"percent")

if(percentage_score >= 70 and percentage_score <= 100):
    print("Excellent... You got an A")

elif(percentage_score >= 60 and percentage_score < 70):
    print("Very Good... You got a B")

elif(percentage_score >= 50 and percentage_score < 60):
    print("Good... You got an C")

elif(percentage_score >= 40 and percentage_score < 50):
    print("Fair... You got an D")

elif(percentage_score < 40):
    print("Poor Attempt... Try again")

else:
    print("Invalid Result")
         
