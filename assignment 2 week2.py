# Theatre Booking System

TOTAL_SEATS = 350
remaining_seats = TOTAL_SEATS

total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while True:
    print(f"\nRemaining Seats: {remaining_seats}")
    
    tickets = int(input("Enter number of tickets (0 to exit): "))
    
    # Exit condition
    if tickets == 0:
        break
    
    # Validate ticket count
    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED - Invalid ticket count (1-15 allowed)")
        rejected_bookings += 1
        continue
    
    # Check seat availability
    if tickets > remaining_seats:
        print("BOOKING REJECTED - Not enough seats available")
        rejected_bookings += 1
        continue
    
    valid_booking = True
    
    # Check ages
    for i in range(tickets):
        age = int(input(f"Enter age of person {i+1}: "))
        
        if age < 12:
            valid_booking = False
            # Continue to take remaining ages but mark invalid
            continue
    
    # Final decision
    if valid_booking:
        print(f"BOOKING CONFIRMED - {tickets} tickets")
        remaining_seats -= tickets
        tickets_sold += tickets
        total_bookings += 1
    else:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1
    
    # Stop if theatre is full
    if remaining_seats == 0:
        print("Theatre is fully booked!")
        break

# Final Report
print("\n--- FINAL REPORT ---")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {remaining_seats}")