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
            proficientcy = input("Enter skill proficientcy")
            comments = input("Enter any additional comments: ")

            current_skill = skill(name, proficientcy, comments)
            
            user_skills.append(current_skill)

        elif action == '2':
            experience_type = input("Enter title of job/experience: ")
            start_t = input("Enter start date in yyyy/mm/dd: ")
            end_t = input("Enter end date in same format, if to present, enter present: ")
            comments = input("Enter any additional comments: ")

            user_skills.append( experience(experience_type, start_t, end_t, comments) )

        if action == 'q':
            loop = False


    

    return


if __name__ == '__main__':
    main()

