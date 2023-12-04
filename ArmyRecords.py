"""
* Name : Final Project - Army Records
* Author: Cole Cooley
* Created : 10/27/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 10
* IDE: PyCharm Community Edition 2022.3.1 - Python 3.9
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : This program was created to assist in gathering Soldier information and outputting it in a clean format.
This program also assists in calculating BMI off of the information provided and will allow you to sort the list by the
Soldiers ETS date or by their last name alphabetically.
* Input: Input Soldier information in all fields of the GUI. Rank, Last Name, First Name, Age, Height, Weight, ETS.
* Output: Outputs all Soldier information as a record as well as the Soldier's calculated BMI.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


import heapq
from datetime import datetime
from CalculateBMI import CalculateBMI

class ArmyRecords:
    def __init__(self):
        # Initializes empty lists to store records and priority queue
        self.records = []
        self.ets_priority_queue = []

    def add_record(self, rank, last_name, first_name, age, height, weight, ets):
        # Calculate BMI using the calculateBMI class
        bmi = CalculateBMI.calculate_bmi(weight, height)

        # Convert ETS date to a datetime object for proper comparison
        ets_date = datetime.strptime(ets, "%Y%m%d")

        # Creates a record dictionary
        record = {
            'Rank': rank,
            'Last Name': last_name,
            'First Name': first_name,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'ETS': ets_date,  # Store the datetime object
            'BMI': bmi
        }

        # Appends the record to records list as well as the priority queue
        self.records.append(record)
        heapq.heappush(self.ets_priority_queue, (ets_date, record))

    # Implements the quick sort algorithm
    def quick_sort(self, array, low, high):
        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quick_sort(array, low, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, high)

    # Partition the array for quick sort
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j]['Last Name'] <= pivot['Last Name']:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]

        return i + 1

    # Function to print records by last name using quick sort
    def print_records_by_last_name(self):
        print("Using Quick Sort to sort by Last Name")
        sorted_records = self.records.copy()
        self.quick_sort(sorted_records, 0, len(sorted_records) - 1)
        self._print_records(sorted_records)

    # Function to extract records from the priority queue
    def print_records_by_ets(self):
        print("Using Priority Queue to print by ETS Date")
        sorted_records = [record for _, record in self.ets_priority_queue]
        self._print_records(sorted_records)

    # Function to print all Soldier information
    def _print_records(self, records):
        for record in records:
            print(f"Rank: {record['Rank']}, Last Name: {record['Last Name']}, "
                  f"First Name: {record['First Name']}, Age: {record['Age']}, "
                  f"Height: {record['Height']}, Weight: {record['Weight']}, "
                  f"ETS: {record['ETS'].strftime('%Y%m%d')}, BMI: {record['BMI']:.2f}")

    def get_records(self):
        return self.records
