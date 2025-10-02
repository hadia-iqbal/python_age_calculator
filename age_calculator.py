import datetime;
def age_calculator(birthdate_str):
    birthdate=datetime.datetime.strptime(birthdate_str,"%Y-%m-%d").date();
    today_date=datetime.date.today();
    age=today_date.year-birthdate.year;
    if(today_date.month,today_date.day)<(birthdate.month,birthdate.day):
        age-=1;
    return age;
dob=input("Enter your birthdate (YY-MM-DD):");
print("Your age is :",age_calculator(dob))