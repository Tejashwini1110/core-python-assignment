def calculate_fare(distance):
#Calculate the fare for a single trip based on distance.
    base_fare = 50  # Base fare for each trip
    distance_fare = 10  # Fare per kilometer
# Total fare for the trip
    total_fare = base_fare + (distance_fare * distance)

    return total_fare

def calculate_total_fare(trips):
#Calculate the total fare for multiple trips.
    total_fare = 0
    # Loop through each trip, calculate its fare, and add it to the total
    for i, distance in enumerate(trips, start=1):
        trip_fare = calculate_fare(distance)
        print(f"Trip {i}: ${trip_fare}")
        total_fare += trip_fare

    return total_fare
# Input Example
trips = [5, 10, 3]  # Distances in km
# Calculate the total fare for the trips
total_fare = calculate_total_fare(trips)
# Output the total fare for all trips
print(f"Total Fare: ${total_fare}")
