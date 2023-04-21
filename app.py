import os
import openai
from flask import *

app= Flask(__name__)

@app.route('/')
def index():  
    
    return render_template("index.html")


def generate_meal_plan(ing):
    # Initialize ChatGPT instance
    openai.api_key = ""
    model_engine = "gpt-3.5-turbo" 
    ingredients_to_exclude =ing
    
    # Generate a response
    completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        'role': 'system',
                        'content': 'You are a dietician.'
                    }, {
                        "role":
                        "user",
                        "content":
                        f"Generate a weekly vegetarian Indian meal plan with only 1 choice for breakfast, 1 choice for lunch, 1 choice for dinner and 1 choice for snacks. The total calories of the day is 1800. Exclude eggs and include on cheat meal each week on Saturday lunch. Also print the approximate calorie count for each meal. Exclude the following {ingredients_to_exclude} ingredients when suggesting the meals.Format the output as the following : Day \n mealtype \n meal \n calories",
                    }],
                    temperature=0,
                    n=1
                )
 
    text=[]
    response = (completion["choices"][0].get("message").get(
                "content").encode("utf8").decode())
    text = [s for s in response.splitlines() if s]
    final_diet_chart =process_meals(text)
    return final_diet_chart

   


def process_meals(text):
   
    weekdays =["Monday","Tuesday","Wednesday" ,"Thursday","Friday" ,"Saturday","Sunday"]
    meal =["Breakfast","Lunch","Dinner" ,"Snacks"]
    day =""

    diet_chart ={}
    meals=""
    meal_type={} 
    food ={}
    total_meals=[]
    flag =False

    for t in text: 
        if t in weekdays:        
            day =t    
        elif t in meal:
            meals =t         
        elif "calories" in t:     
            food["calories"] =t 
            meal_type[meals]=food 
            food ={}                     
        else:
            food["food"] =t

        if len(meal_type) ==4:      
            diet_chart[day] = meal_type 
            total_meals=[]
            meal_type={} 
            food ={}            
          


    return diet_chart
            






@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == "POST":
        print("Entered flask Application!!!!")
        ingredients_to_exclude=["mushrooms","eggplant"]
        print("ing_list",ingredients_to_exclude)
        print("Entered flask Application!!!!")
        result= generate_meal_plan(ingredients_to_exclude) 
        return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
   
   
   
