class Student: 
    def __init__(self, student_name, input_cohort):
        self.name = student_name    
        self.cohort = input_cohort
    
    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return "I love " + favourite_language
    



