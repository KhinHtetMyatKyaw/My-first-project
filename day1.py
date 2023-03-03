marks=int(input("Please enter student marks:"))
if  marks <= 0 or marks >= 100:
        print ("Invalid Marks‼️")
elif marks >=80 or marks==99:
        print ("Honorable Marks🥳🎉(grade.🅰️ ✔️)")
elif marks >= 50 or marks == 79:
        print ("exam pass🎊(grade.🅱️ ✔️)")
elif marks >=40 or marks ==50 :
        print ("grade.C ✔️")
elif marks <=39 :
        print ("exam fail ❌")
