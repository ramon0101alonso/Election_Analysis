voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", 
"registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for voting_values  in voting_data:
    print(f"{voting_values['county']}, county has {voting_values['registered_voters']} registered voters")