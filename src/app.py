import random
import os
import openai

def generate_meal_plan():
    # Initialize ChatGPT instance
    openai.api_key = "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"
    model_engine = "gpt-3.5-turbo" 
    ingredients_to_exclude =['mushrooms,eggplant, ']
 

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
                        f"Generate a weekly vegetarian Indian meal plan with two choices for breakfast, two choices for lunch, two choices for dinner, two choices for 2 snacks, each for 1800 calories per day. Exclude eggs and include on cheat meal each week on Saturday lunch. Also print the approximate calorie count for each meal. Exclude the following {ingredients_to_exclude} ingredients when suggesting the meals.",
                    }],
                )
 

    response = (completion["choices"][0].get("message").get(
                "content").encode("utf8").decode())
    print(response)

generate_meal_plan()