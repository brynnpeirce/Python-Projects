

# Parent class Job
class Job:
    title = 'Unknown'
    Salary = 'unknown'
    start_date = 'Unknown'
    benefits = True

    def Resume(self):
        name = input("Enter your name: ")
        email = input ("Enter your email: ")
        job_experience = input ("Enter job experience: ")
        education = input("Enter education information: ")
        if (name == name):
            print("{}, thanks for applying!".format(name))
        else:
            print("You need at least your name entered to apply.")

# Child class Restaurant
class Restaurant(Job):
    title = 'Head Chef'
    Salary = 50,000.00
    start_date = '01/02/23'
    benefits = True

    def Resume(self):
        name = input("Enter your name: ")
        email = input ("Enter your email: ")
        cooking_experience = input ("Enter cooking experience: ")
        if (name == name):
            print("{}, thanks for applying!".format(name))
        else:
            print("You need at least your name entered to apply.") 


# Child class Hospital
class Hospital(Job):
    title = 'Nurse'
    Salary = 75,000.00
    start_date = 'ASAP'
    benefits = True

    def Resume(self):
        name = input("Enter your name: ")
        email = input ("Enter your email: ")
        Healthcare_experience = input ("Enter healthcare experience: ")
        education = input("Enter education information: ")
        if (name == name):
            print("{}, thanks for applying!".format(name))
        else:
            print("You need at least your name entered to apply.")



job = Job()
job.Resume()

Applicant1 = Restaurant()
Applicant1.Resume()

Applicant2 = Hospital()
Applicant2.Resume()


    



    
