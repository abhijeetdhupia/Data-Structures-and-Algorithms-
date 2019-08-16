#Code to find out the age of a person in days given the date of birth and the current date.  

def leap_year(year):
  return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))
  
  # inputs: two dates 
  # second date(Current date) must not be before the first date(DOB)
  # we are going to use Gergorian calender which started from 15 Oct,1582, so to be on safer side we should use dates after this. 
