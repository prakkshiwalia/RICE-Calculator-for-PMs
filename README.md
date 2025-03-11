# RICE-Calculator-for-PMs
This RICE Calculator helps Product Managers focus on the most valuable features first, so time, money, and effort aren't wasted on low-impact ideas.

# Code Breakup

1. We need a place to store feature details, like a list, so we introduce a list.&#x20;
2. We also have to make sure that the PM enters only valid numbers instead of letters for calculating RICE. In addition to this, we also limit numbers within a valid range (example - Impact should be within 1-5). The .isdigit() is needed to make sure the input is a digit (it only works for whole numbers)&#x20;

```
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

```

3. Since, effort is usually measured in fractions (eg - 2.5 weeks), it is important to add a float number since the .isdigit() does not work for decimal numbers. In the the\_value.replace(".", "", 1) breakdown - "."  is used to replace the occurrence of decimal in the string value with an empty string " " and only allows this to happen for one decimal point

```
#Step 3 Function to get valid float input
def get_valid_float(prompt):
	while True:
		value = input(prompt)
		if value.replace(".", "",1).isdigit(): #allows decimals and is converted to whole number 
			return float(value)
		else:
			print("Invalid input! Please enter a valid number.") 
```

4. Functions are added for new feature - This function will be called when we want to add a new feature to the priortisation list. It doesn't take any parameters but interacts with the user to collect feature details. The user is asked to add a name to the feature and is then stored in name variable.&#x20;

The get\_valid\_int() function ensures the user enters valid number between the range provided for the value of Reach(1-100) provided based on the define function above.&#x20;

```
#Step 4 Function to add a new feature 
def add_feature():
	name = input("Enter feature name: ")

	reach = get_valid_int("Reach (1-100): ",1,100)
	impact = get_valid_int("Impact(1-5): ",1,5)
	confidence = get_valid_int("Confidence(1-100): ",1, 100)
	effort = get_valid_float("Effort in person-weeks(example, 2.5): ")
```

5. Now the rice\_score will be calculated and stored in this variable. In addition to this the features list is edited and the name, and rice\_score is added to it. {:.2f} is added to make sure that the score is only displayed till two decimal places.

```
 # Calculating RICE score
	rice_score = (reach * impact * (confidence/100)) / effort

    # Store the feature details
	features.append((name, rice_score))

	print(f"feature '{name}' added with RICE score: {rice_score:.2f}")
```

6. The next step would display the functions from highest to lowest features with function name as display\_features(). If there are no features, it will print "no features added yet" and returns stop execution and exits the function.&#x20;

The sorted() built-in python function will sorts the list from lowest to highest by default. Key=lambda x: x\[1] in which key = tell python how to sort the items and lambda x: x\[1] is a lambda function which means "use the second value (x\[1]) of each tuple to sort, in which the feature would be at index x\[0] and rice\_score would be at x\[1].

In other words,&#x20;

In this case, `lambda x: x[1]` is an **anonymous function** (or **lambda function**) that takes one element `x` from `features` and returns its second element (`x[1]`).

* For example, if `features` is a list of tuples like `[("feature1", 10), ("feature2", 5), ("feature3", 20)]`, `x[1]` refers to the second element of each tuple (the numerical values `10`, `5`, and `20`).
* This means the sorting will be based on the **second element** of each item in the list.

Furthermore, reverse=True is used to sort the list in descending order.&#x20;

<pre><code><strong>#Step 5 Function to display ranked features
</strong>def display_features():
	if not features:
		print("No features added yet.")
		return

	#Sort and store features in rice_scores by DESC order
	sorted_features = sorted(features, key=lambda x: x[1], reverse=True)
</code></pre>

7. enumerate() function adds numbers like 1,2,3.. to each feature starting from 1. Without it, the program wouldn't know the ranking order.&#x20;

'for' starts the loop, 'i' stores the ranking number(1,2,3..). (name, score) extracts the feature name and rice\_score from the sorted list and then assigns the numbers starting from 1 to each feature.&#x20;

```
print("\nFeature Priortization List (Ranked by RICE Score):")
	for i, (name, score) in enumerate(sorted_features, start=1):
		print(f"{i}.{name} | RICE Score: {score:.2f}")
```

8. To make sure the user can add multiple features to rank before the  code runs once (for one feature) and exits, the below code is an important part of the entire script to be successful. This block of code will allow the user to interact with the program.&#x20;

* This program will allow user Interaction and serve as the main control system of the program. Through this feature, the user can add features, view rankings, or exit the program using simple choices.
* Keeps the Program Running Until User Chooses to Exit: The while true creates an infinite loop, meaning the program keeps running until the user decides to exit. If this step was missing, the program would run once and exit immediately.
* Ensures Users Select a Valid Option: It checks user input and ensures they enter a valid choice like 1,2,3..
* Calls the Right Functions Based on User Choice: If the user selects `"1"`, it calls `add_feature()` to allow them to add a feature. If the user selects `"2"`, it calls display\_feature() to call the ranked function. If the user selects `"3"`, it prints a goodbye message and exits the loop.

#### **What Will Happen Without This Step?**

* The program will exit immediately after execution. Without the while true loop, the script will run once and stop, meaning the user won’t get a chance to interact.
* Users won’t be able to add multiple features. If a user adds one feature, the program will stop, forcing them to restart it every time.
* No way to view the feature list. Without this menu, there’s no way to see the prioritized features after adding them.
* The program will be non-interactive. Without a menu, the program won’t wait for user input, making it useless as a tool.

```
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
```

Breakdown of the above program is as follows:

* the while True loop creates an infinite loop, meaning the menu will keep appearing until the user chooses to exit.
  * Why is this needed? If we don’t have this loop, the program would run once and then exit immediately, not allowing the user to add multiple features.
  * How does it stop? When the user selects `"3"` (Exit), the loop stops using `break`.\\
* The  \n at the beginning of the first line ensures a **new line for spacing**, making the menu easier to read. The three print() statements **display options for the user**.
*   input("Choose an option (1/2/3):  ") **asks the user** to enter the number.  The entered value is stored in the variable choice. .

    **Important:** input( ) always returns a string so we need to compare `choice` as a string rather than numbers.
* The if-elif-else conditions are used to determine what to do based on the user's input.

Option 1: If the user enters 1,  the program calls the add\_feature function. This function collects details about a new feature and calculates its RICE score.

Option 2: If the user enters 2, the program calls display\_features( ), which: Sorts all features by RICE score and displays the ranked list.

Option 3:  If the user enters 3, the program prints "Exiting program. Goodbye!", then breaks the `while` loop (break stops the loop) and program execution ends.

However, if the user enters anythign other than 1,2,3, the program gives an error message and asks the user to try again.&#x20;

Final summary -

| **Code Part**         | **Purpose**                                                |
| --------------------- | ---------------------------------------------------------- |
| `while True:`         | Keeps showing the menu until the user chooses to exit.     |
| `print()`             | Displays the options (`1: Add`, `2: View`, `3: Exit`).     |
| `input()`             | Gets user choice as a **string**.                          |
| `if choice == "1":`   | Calls `add_feature()` to add a feature.                    |
| `elif choice == "2":` | Calls `display_features()` to show the ranking.            |
| `elif choice == "3":` | Prints exit message and **stops the loop** using `break`.  |
| `else:`               | Handles **invalid inputs** and asks the user to try again. |
