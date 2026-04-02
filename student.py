class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):

        if self.score >= 90:
            return "A"
        elif self.score >= 75:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "F - failed"

    def introduce(self):
        return f"I am {self.name}, my score is {self.score}, I have {self.get_grade()}"

    def set_score(self ,new_score):
        if not isinstance(new_score, (int, float)):
            raise ValueError("Score must be a number!")
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be a number!")
        self.score = new_score

    def to_csv_line(self):
        return f"{self.name},{self.score}"
    
    def __str__(self):
        return self.introduce()
    

