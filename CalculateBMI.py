# Class to calculate BMI
class CalculateBMI:
    @staticmethod
    def calculate_bmi(weight, height):
        # BMI formula: weight (lb) / [height (in)]^2 * 703
        bmi = (weight / (height ** 2)) * 703
        return bmi
