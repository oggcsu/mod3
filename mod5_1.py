valid_year = False 
while not valid_year:
    try:    
        num_years = int(input("Enter the Number of Years:: "))
        if num_years < 0:
            assert ValueError("Must be a positive integer")
        else:
            valid_year = True
    except:
        pass
        
months = ['January', 'February', 'March', 'April','May','June','July','August','September','October','November','December']

tracker = []
for year in range(num_years):
    for month in months:
        valid_number = False 
        while not valid_number: 
            try:
                temp_num = int(input(f"Enter the total for Year {year+1}/{month}: "))
                if temp_num < 0:
                    assert ValueError("Must be a positive integer")
                else:
                    valid_number = True
                    tracker.append(temp_num)
            except:
                pass 
            

print(f"\n\nTotal Months: {len(tracker)}")
print(f"Total Rainfall Inches Across Period: {sum(tracker)}")
print(f"Average Rainfall Inches Across Period: {sum(tracker)/len(tracker):.1f}\n")
        