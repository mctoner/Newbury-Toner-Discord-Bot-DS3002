# "Food Bot": A Discord Bot by Maura Toner & Abby Newbury

## Discord Bot Final Project DS 3002

We have created a discord bot using the Discord API and the external Recipe-Food-Nutrition Rapid API (found here: https://rapidapi.com/spoonacular/api/recipe-food-nutrition/). The bot takes in various inputs and returns nutritional information for food/dishes, a randomized meal plan to meet caloric needs, or a unit conversion for a various ingredient. Our bot is called 'MandABot and has the following commands:

Note: our special character is !, and all commands must be prefaced by an exclamation point.

1) docs: enter !docs to see a summary of all of the commands and an intro to our bot.
2) help: help shows all of the help messages for all of the commands, in case you get stuck.
3) dish: enter !dish followed by a dish name to see the calories,fat,carbs and sugar in the dish. If the dish has multiple words, whitespace is replaced with an underscore. For example, chicken parmesan should be in the format '!dish Chicken_Parmesan'
4) mealplan: enter mealplan! and a specific number of calories for the day, and this command will generate a random day of eating for you. The output will list every recommended dish and the recommended number of servings for each dish. (These meal plans are ridiculous and we do NOT advise actually eating like this :) )
5) conversion: type '!conversion' with four parameters. ingredient=ingredient you want to convert,starting_unit=unit you start with (ie Liters,L,mL,grams,cups, etc. ),amount_to_convert=number of cups,grams,etc. you wish to convert ,final_unit=the measurement you wish to convert to.. ie cups, etc. For example, typing "!conversion    water mL 1000 Liter" returns "1000 ml water translates to 1 liter."

There is also added help functionality:
- Type !help command for more info on a command.
- You can also type !help category for more info on a category.

Screenshots of sample bot usage can be found below.

To join our server and interact with our bot, follow this link: 
