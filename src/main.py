import JobLL

from skills import skill
from skills import experience

def fill_information():
    pass


def main():

    print("Program that takes users skills and experience as input and outputs a\nregex string")


    
    loop = True
    while loop:

        # skills and experiences will be made as a class
        # skills: skill name, proficientcy, additional comments
        # experience: experience type, time started, time ended, additional comments
        
        print("options: 1. add skills\n 2. add experience\n 3. end\n")

        user_skills = []
        user_experience = []
        action = str(input("Action: "))

        if action == '1':
            name = input("Enter skill name: ")
            proficiency = input("Enter skill proficiency")
            comments = input("Enter any additional comments: ")

            current_skill = skill(name, proficiency, comments)
            
            user_skills.append(current_skill)
            print("you have entered: ")
            print(current_skill) # gonna need a str def 

        elif action == '2':
            experience_type = input("Enter title of job/experience: ")
            start_t = input("Enter start date in yyyy/mm/dd: ")
            end_t = input("Enter end date in same format, if to present, enter present: ")
            comments = input("Enter any additional comments: ")

            user_experience.append( experience(experience_type, start_t, end_t, comments) )

            print("you've entered: \n", user_skills[-1])

        elif action == '3':
            loop = False
       

    # now to summarize everything the user inputed

    print("Summary: \n\n skills: \n")
    for i in range( len(user_skills)):
        print(user_skills[i])
    
    for i in range( len (user_experience) ):
        print(user_experience[i])


    return


if __name__ == '__main__':
    main()

