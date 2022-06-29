

# Parent class Job
class Job:
    title = 'Unknown'
    Salary = 'unknown'
    start_date = 'Unknown'
    benefits = True

    def Resume(self):
        name = input("Enter your name: ")
        job_title = input("Enter desired title: ")
        email = input ("Enter your email: ")
        job_experience = input ("Enter job experience: ")
        education = input("Enter education information: ")
        if (job_title == self.title):
            print("{}, thanks for applying for {}!".format(name,self.title))
        else:
            print("Sorry that position has already been filled")

# Child class Restaurant
class Restaurant(Job):
    title = 'Head Chef'
    Salary = 50,000.00
    start_date = '01/02/23'
    benefits = True

    def Resume(self):
        name = input("Enter your name: ")
        chef_title = input("Enter desired title: ")
        email = input ("Enter your email: ")
        cooking_experience = input ("Enter cooking experience: ")
        if (chef_title == self.title):
            print("{}, thanks for applying for {}!".format(name, self.title))
        else:
            print("Sorry that position has already been filled.") 


# Child class Hospital
class Hospital(Job):
    title = 'Nurse'
    Salary = 75,000.00
    start_date = 'ASAP'
    benefits = True

    def Resume(self):
        name = input("Enter your name: ")
        Health_title = input("Enter desired title: ")
        email = input ("Enter your email: ")
        Healthcare_experience = input ("Enter healthcare experience: ")
        education = input("Enter education information: ")
        if (Health_title == self.title):
            print("{}, thanks for applying for {}!".format(name,self.title))
        else:
            print("Sorry that position has already been filled")



job = Job()
job.Resume()

Applicant1 = Restaurant()
Applicant1.Resume()

Applicant2 = Hospital()
Applicant2.Resume()


    



    
