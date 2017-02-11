name="Adam Ali"
len_name=len(name)
first_letter=name[0]
second_letter=name[1]
letter_n=name[6]
last_letter=name[-1]
before_last_letter=name[-2]

letter_1_3=name[1:3]
letter_1_end=name[1:]

print name, len(name), first_letter, second_letter, letter_n, last_letter, before_last_letter, letter_1_3, letter_1_end

name_lower=name.lower()
print "name lower case", name_lower
count_a=name_lower.count("a")
print "number of instances of letter a", count_a
