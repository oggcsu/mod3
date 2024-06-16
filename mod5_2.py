valid_books = False 
while not valid_books:
    try:    
        num_books = int(input("Enter the Number of Books Purchased This Month: "))
        if num_books < 0:
            print("Must be a positive Integer")
        else:
            valid_books = True
    except:
        print("Please input a valid Integer\n")
    
points = 0
    
if num_books < 2:
    points = 0
elif num_books < 4:
    points = 5
elif num_books < 6:
    points =  15
elif num_books < 8:
    points = 30
elif num_books >= 8:
    points = 60

    
print(f"You purchased {num_books} books this month.")
print(f"You have been awarded {points} points!")
