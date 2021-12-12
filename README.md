# "Food Bot": A Discord Bot by Maura Toner & Abby Newbury

## Discord Bot Final Project DS 3002

We have created a discord bot using the Discord API and the external Recipe-Food-Nutrition Rapid API (found here: https://rapidapi.com/spoonacular/api/recipe-food-nutrition/ , and images from the Web Search Rapid API: https://rapidapi.com/contextualwebsearch/api/web-search/). The bot takes in various inputs and returns nutritional information for food/dishes, a randomized meal plan to meet caloric needs, or a unit conversion for a various ingredient. Our bot is called 'MandABot and has the following commands:

Note: our special character is !, and all commands must be prefaced by an exclamation point.

1) docs: enter !docs to see a summary of all of the commands and an intro to our bot.
2) help: help shows all of the help messages for all of the commands, in case you get stuck.
3) dish: enter !dish followed by a dish name to see the calories,fat,carbs and sugar in the dish. If the dish has multiple words, whitespace is replaced with an underscore. For example, chicken parmesan should be in the format '!dish Chicken_Parmesan'
4) mealplan: enter mealplan! and this command will generate a random day of eating for you based on a 2000 calorie goal. The output will list every recommended dish and the recommended number of servings for each dish. (These meal plans are ridiculous and we do NOT advise actually eating like this :) )
5) conversion: type '!conversion' with four parameters. ingredient=ingredient you want to convert,starting_unit=unit you start with (ie Liters,L,mL,grams,cups, etc. ),amount_to_convert=number of cups,grams,etc. you wish to convert ,final_unit=the measurement you wish to convert to.. ie cups, etc. For example, typing "!conversion    water mL 1000 Liter" returns "1000 ml water translates to 1 liter."
6) funfact: type !funfact and the bot will return a fun fact about food. No arguments or inputs needed.

There is also added help functionality:
- Type !help command for more info on a command.
- You can also type !help category for more info on a category.

Our bot is hosted in EC2 under the instance id i-0adce608a3110e3cb and the Key Name "MauraandAbbyBot' so that we can interact with our cool bot at all time & it will be running indefinitely!

To join our server and interact with our bot, follow this link:   https://discord.gg/GvP2ye9x


## Screenshots of sample bot usage can be found below.
### Documentation via !docs command

![Screen Shot 2021-12-10 at 9 08 56 PM](https://user-images.githubusercontent.com/57843918/145660348-85464fb6-1691-4bb6-8489-0e5428eddab7.png)

General help command (ehlp for speific functions are shown with each function)
![Screen Shot 2021-12-10 at 9 09 30 PM](https://user-images.githubusercontent.com/57843918/145660368-e40c8946-c8af-4416-a8d3-b90f4e5211d4.png)


### dish function

![Screen Shot 2021-12-10 at 9 10 57 PM](https://user-images.githubusercontent.com/57843918/145660396-cf3314d6-2952-4291-81cd-7f56a9b6a03f.png)

![Screen Shot 2021-12-10 at 9 10 13 PM](https://user-images.githubusercontent.com/57843918/145660384-1cfdc703-f3df-4c11-a6e9-cb309d759e19.png)

### mealplan function
![Screen Shot 2021-12-10 at 9 11 39 PM](https://user-images.githubusercontent.com/57843918/145660408-3377e770-08fd-40ad-845c-a3e2ebdde540.png)

![Screen Shot 2021-12-10 at 9 11 55 PM](https://user-images.githubusercontent.com/57843918/145660418-65c14230-0311-41f3-8000-1bc53d29687d.png)

### Conversion function
![Screen Shot 2021-12-10 at 9 14 28 PM](https://user-images.githubusercontent.com/57843918/145660479-dd9ac811-2698-4f63-bb61-4724ceabaf58.png)

![Screen Shot 2021-12-10 at 9 14 43 PM](https://user-images.githubusercontent.com/57843918/145660484-05ebe136-c266-4cf9-8126-1106f02eaef5.png)

### Fun fact Function
![Screen Shot 2021-12-10 at 9 15 10 PM](https://user-images.githubusercontent.com/57843918/145660497-5f0eb9b2-bbda-49a1-b743-d916609d1342.png)

![Screen Shot 2021-12-10 at 9 15 25 PM](https://user-images.githubusercontent.com/57843918/145660502-2187bf0d-41c8-4885-a97f-bb6d306be170.png)


### Examples of informative errors
![Screen Shot 2021-12-11 at 7 26 45 PM](https://user-images.githubusercontent.com/57843918/145695960-29af4309-e7ab-4db8-b865-b022a24b836b.png)

![Screen Shot 2021-12-11 at 7 28 01 PM](https://user-images.githubusercontent.com/57843918/145695976-b0633949-5398-4887-921d-cc9b945ceb63.png)








