#Python Sets Adventure
#Task 1:Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

similar_routes = our_routes & competitor_routes
print(similar_routes)

exclusive_routes = our_routes.difference(competitor_routes)
print(exclusive_routes)

different_routes = our_routes.symmetric_difference(competitor_routes)
print(different_routes)

#Set Operations in Data Analysis
#Task 1:Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

filtered_custids = set(["C001", "C002", "C003", "C002", "C001", "C004"])
for i in filtered_custids:
    print(f"Customer ID is: {i}")

#Music Festival Playlist Organization
#Task 1:Artist Lineup Compilation

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for i in artist_names:
    unique_artists.add(i)
print(unique_artists)




