import time

class Subject:
	
	def __init__(self, name, begin, end):
		self.name = name
		self.begin = begin
		self.end = end
	
	def __str__(self):
		return str(self.name) + " " + str(self.begin) + " " + str(self.end)
	
	def get_name(self):
		return self.name
		
	def get_begin(self):
		return self.begin
		
	def get_end(self):
		return self.end


def find_first_ends(subjects_list):
	first_ends = None
	
	for s in subjects_list:
		if first_ends == None:
			first_ends = s
		else:
			if s.get_end() < first_ends.get_end():
				first_ends = s
	
	return first_ends


def timetable(subjects_list, result = []):
	if subjects_list == []:
		return None
	
	first_ends = find_first_ends(subjects_list)
	result.append(first_ends)
	starts_after_first_ends = [s for s in subjects_list if s.get_begin() >= first_ends.get_end()]
	timetable(starts_after_first_ends, result)	
	
	return result


if __name__ == '__main__':
	art = Subject('art', 9.0, 10.0)
	english = Subject('english', 9.3, 10.3)
	math = Subject('math', 10.0, 11.0)
	cs = Subject('cs', 10.3, 11.3)
	music = Subject('music', 11.0, 12.0)
	physics = Subject('physics', 8.30, 9.30)

	subjects_list = [art, english, math, cs, music, physics]

	result_table = timetable(subjects_list)
	
	for subject in result_table:
		print(subject)
