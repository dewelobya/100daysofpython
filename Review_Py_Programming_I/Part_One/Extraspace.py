# Extra space 

#pilkulla lisää välilyönnin plussa ei lisää ja f toiminnot käteviä

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is" + " " + name + ", I am", age, "years old")
print()
print("my skills are")
print(" - " + skill1 , "("+level1+")")
print(" - " + skill2 , "("+level2+")")
print(" - " + skill3 , "("+level3+")")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")