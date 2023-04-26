
# Weekly Meal Planner using ChatGPT

A weekly vegetarian meal plan web app using Python, Flask and Bootstrap powered by ChatGPT. 

The web app takes cuisine choice and number of calories for the total day as input and creates a weekly menu in the form of a table. The menu can also be downloaded as a pdf.

The following ChatGPT prompt is used to generate the weekly menu
`

**`Generate a weekly Vegetarian {cuisine} meal plan with only 1 choice for breakfast, 1 choice for lunch, 1 choice for dinner and 1 choice for snacks. The total calories of the day is {cal}. Exclude eggs.Also print the approximate calorie count for each meal. Format the output as the following : Day \n mealtype \n meal \n calories No other text is required. The mealtype should be in the following format and spelling : Breakfast, Lunch, Dinner ,Snacks.`**

 ---

![alt text](https://github.com/anaghamoosad/meal_plan_app/blob/main/meal_plan.gif "meal planner app")

---

**Features**

 - uses ChatGPT 3.5 to generate weekly menu
 - uses jsPdf library file to download the menu as a pdf
 - takes cuisine and number of calories as input
 - generates only vegetarian meal plan
---

**Additional features to be added**

 - Add user option to remove ingredients when suggesting meal plan
 - Update the UI
 - option to save the meal plan as a csv
 - option to generate two options for each meal eg : two options for breakfast
