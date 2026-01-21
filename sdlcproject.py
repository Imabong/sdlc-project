# Hostel Room Checker System
# Only input: Matric Number

hostel_allocation = {
    "24/14801": "Room A12",
    "24/14802": "Room B05",
    "24/14803": "Room C08"
}

print("HOSTEL ROOM CHECKER")

# Input matric number
matric_number = input("Enter your matric number: ")

# Check room allocation
if matric_number in hostel_allocation:
    print("\nMatric Number:", matric_number)
    print("Hostel Room:", hostel_allocation[matric_number])
else:
    print("\nMatric Number:", matric_number)
    print("Hostel Room: Not Allocated")
