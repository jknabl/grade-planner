#!/usr/bin/python
import datetime
import copy
#title: string w/ title of assignment
#weight = float representing % the assignment is worth of grade
#due = datetime object representing when assignment is due
#description = string
#grade = float
class Assignment:
	def __init__(self, title=None, weight=None, due=None, description=None, grade=None):
		if title==None:
			self.title = "Unnamed Assignment"
		else:
			self.title = title
		if weight==None:
			self.weight = 0
		else:
			self.weight = weight
		if due==None:
			self.due = "no"
		else:
			self.due = due
		if description==None:
			self.description = "A new assignment."
		else:
			self.description = description
		if grade==None:
			self.grade = -1 #we're avoiding NoneType, so make this -1
		else:
			self.grade = grade

class Course:
	def __init__(self, assignments=None, grade=None):
		if assignments==None:
			self.assignments = []
		else:
			self.assignments = assignments
		self.grade = grade
	#Check to see that course grade weights are set up properly.
	#That is, all weights add up to 1 (100%)
	def check_total_weight(self):
		sum = 0
		for x in self.assignments:
			sum += x.weight
		if weight==1:
			return True
		else:
			return False
	#what is the total grade % I've earned for this class
	#so far?
	def calculate_grade(self, assignments=None):
		if assignments==None:
			assignments = self.assignments
		grades, count = 0, 0
		for x in assignments:
			count += 1
			grades += x.grade * x.weight
		return grades
	def hypothetical_grade(self, assignment):
		#what will I have earned if I get X grade on Y assignment, given
		#the grades I've already earned. The input here is a modified 
		#version of an assignment that exists in the list; the modification
		#is a new grade value. 
		new_ass = copy.deepcopy(assignment)
		temp_assignments = []
		for x in self.assignments:
			#check for equality using title, since the grade value is going 
			#to be different.
			if x.title == new_ass.title:
				temp_assignments.append(new_ass)
			else:
				temp_assignments.append(x)
		new_grade = self.calculate_grade(temp_assignments)
		return new_grade
	#get overall grade in the class for each assignment grade
	#that is a multiple of 10. For a SINGLE assignment.
	def possible_grades_results(self, assignment):
		if assignment not in self.assignments:
			print "Error: this assignment doesn't exist for the class."
			return None
		new_ass = copy.deepcopy(assignment)
		temp = []
		count = 0
		while count < 100:
			count += 10
			new_ass.grade = count
			temp.append([count, self.hypothetical_grade(new_ass)])
		print "\n--- POSSIBILITIES FOR %s ---\n" % new_ass.title
		for y in temp:
			print "If you get/got %f for %s, your grade will be: %f\n" % (y[0], new_ass.title, y[1])
		return None
	#what grade do I need on assignment x to obtain y overall grade
	#in the course? All other grades given except for assignment x.
	def what_to_get_x(self, grade, assignment):
		print "\n --- What grade do you need on %s to get %f in this class? ---\n" % (assignment.title, grade)
		if assignment not in self.assignments:
			print "ERROR: assignment doesn't exist for the class."
			return None
		temp_assignments = []
		debug_weight = 0
		for x in self.assignments:
			if not x == assignment:
				debug_weight += x.weight
				temp_assignments.append(x)
		overall_weight = 1 - assignment.weight
		required_grade = (grade - self.calculate_grade(temp_assignments)) / assignment.weight
		if (required_grade > 100):
			print "It is impossible to achieve the grade you want given your constraints :( \n"
		elif (required_grade < 0):
			print "You don't even have to hand this in to obtain your desired grade, given your constraints. \n"
		else:
			print "You need to get %f on %s to obtain a %f in the class.\n" % (required_grade, assignment.title, grade)
		return None

	def print_grades(self):
		print "\n --- GRADES SO FAR --- \n\n"
		for x in self.assignments:
			print "Assignment: %s | Weight: %f | Grade: %f\n" % (x.title, x.weight, x.grade)
		print "TOTAL GRADE is: %f\n" % self.calculate_grade()
		print "------------------------\n"

def main():
	a1 = Assignment("Lab 1", 0.1, "no", "Robots lab 1", 50)
	a2 = Assignment("Lab 2", 0.1, "no", "Robots lab 2", 60)
	a3 = Assignment("Lab 3", 0.1, "no", "Robots lab 3", 0)
	a4 = Assignment("Lab 4", 0.1, "no", "Robots lab 4", 20)
	midterm = Assignment("Midterm", .15, "no", "Robots midterm", 74.3)
	project = Assignment("Project", .20, "no", "Robots project competition", 50)
	exam = Assignment("Final Exam", .25, "no", "Robots final exam", 75)
	assignments = []
	assignments.append(a1)
	assignments.append(a2)
	assignments.append(a3)
	assignments.append(a4)
	assignments.append(midterm)
	assignments.append(project)
	assignments.append(exam)
	comp4807 = Course(assignments)
	comp4807.print_grades()
	comp4807.possible_grades_results(a1)
	comp4807.possible_grades_results(midterm)
	comp4807.possible_grades_results(exam)
	comp4807.possible_grades_results(project)
	comp4807.print_grades()
	comp4807.what_to_get_x(50, exam)
if __name__=="__main__":
	main()



