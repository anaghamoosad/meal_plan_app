import os
import openai
from flask import *
from flask import Flask, render_template, url_for, request
app= Flask(__name__)

@app.route('/',methods = ['POST', 'GET']) 
def index():
    if request.method == "POST":
        print("Entered flask Application!!!!")
        ingredients_to_exclude=["mushroom","oats","eggs","eggplant"]
        print("ing_list",ingredients_to_exclude)
        print("Entered flask Application!!!!")
        result= generate_meal_plan(ingredients_to_exclude)
        return render_template('index.html',result = result) 
        
    return render_template('index.html')
    

    
 
def generate_meal_plan(ing):
    # Initialize ChatGPT instance
    openai.api_key = "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"
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
                        f"Generate a weekly vegetarian South Indian meal plan with only 1 choice for breakfast, 1 choice for lunch, 1 choice for dinner and 1 choice for snacks. The total calories of the day is 1200. Exclude eggs.Also print the approximate calorie count for each meal. Do not suggest meals that conatin the following {ingredients_to_exclude} ingredients .Format the output as the following : Day \n mealtype \n meal \n calories",
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

 

if __name__ == '__main__':
   app.run(debug = True)
   
 
   