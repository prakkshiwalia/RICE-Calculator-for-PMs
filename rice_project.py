#Feature priortisation using RICE scoring 

#Step 1 - Defining an empty list to store the features
features = []

#Step 2 - Function to get valid integer input:
def get_valid_int(prompt, min_value, max_value):
	while True: 
		value = input(prompt) #storing the input of prompt as value variable
		if value.isdigit(): #checks if input is a number
			value = int(value)
			if min_value <= value <= max_value:
				return value
			else:
				print(f"Please enter a number between {min_value} and {max_value}.")
		else:
			print("Invalid input! Please enter a number.")

#Step 3 Function to get valid float input
def get_valid_float(prompt):
	while True:
		value = input(prompt)
		if value.replace(".", "",1).isdigit(): #allows decimals and is converted to whole number 
			return float(value)
		else:
			print("Invalid input! Please enter a valid number.") 

#Step 4 Function to add a new feature 
def add_feature():
	name = input("Enter feature name: ")

	reach = get_valid_int("Reach (1-100): ",1,100)
	impact = get_valid_int("Impact(1-5): ",1,5)
	confidence = get_valid_int("Confidence(1-100): ",1, 100)
	effort = get_valid_float("Effort in person-weeks(example, 2.5): ")

    # Calculating RICE score
	rice_score = (reach * impact * (confidence/100)) / effort

    # Store the feature details
	features.append((name, rice_score))

	print(f"feature '{name}' added with RICE score: {rice_score:.2f}")

#Step 5 Function to display ranked features
def display_features():
	if not features:
		print("No features added yet.")
		return

	#Sort and store features in rice_scores by DESC order
	sorted_features = sorted(features, key=lambda x: x[1], reverse=True)

	print("\nFeature Priortization List (Ranked by RICE Score):")
	for i, (name, score) in enumerate(sorted_features, start=1):
		print(f"{i}.{name} | RICE Score: {score:.2f}")

#Step 6: Menu for user interaction
while(True):
	print("\n1. Add Feature")
	print("2. View Priortized Features")
	print("3. Exit")
	choice = str(input("Choose an option (1/2/3): "))
	print(f"User entered: {choice}")
	if choice == "1":
		print("Calling add_feature()...")
		add_feature()
	elif choice == "2":
		display_features()
	elif choice == "3":
		print("Exiting program. Goodbye!")
		exit()
	else:
		print("Invalid choice! Please enter 1,2 or 3.")