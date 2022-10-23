dog_age_in_human_years = int(input("POdaj wiek psa w latach ludzkich"))



i = 1

dog_age_in_dog_years = 0


while i <= dog_age_in_human_years:
    if i<=2:
        dog_age_in_dog_years += 10.5
    else:
        dog_age_in_dog_years += 4
    i +=1

print(dog_age_in_dog_years)