def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    return base_fare + (distance_fare * distance)


def calculate_total_fare(trips):
    total_fare = 0
    for i, trip in enumerate(trips, start=1):
        fare = calculate_fare(trip)
        print("Trip " + str(i) + ": $" + str(fare))
        total_fare += fare
    return total_fare


trips = [5, 10, 3]
total_fare = calculate_total_fare(trips)
print("Total Fare: $" + str(total_fare))
