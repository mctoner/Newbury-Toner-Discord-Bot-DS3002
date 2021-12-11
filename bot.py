#Abby Newbury and Maura Toner- Discord "Food" Bot
#mct2kc and amn5ye
import discord
import requests
from discord.ext import commands

# discord token and guild
TOKEN='OTE3NTIwMjQwMTkwMDUwMzU1.Ya55Tw.xLclZkm4iSuMNfHh8cuhIA3y3A4' #token for bot
GUILD= '917520892614017074' #guild id

# set designated bot prefix
bot = commands.Bot(command_prefix='!') #prefix for all commands


# INFORMATION (!docs)
@bot.command(name='docs', help='enter !docs to provide a summary of commands') #instantiate command for docs
async def docs(ctx): #docs takes no args
    # description of bot functions and commands
    answer = "Hi, I am the MandA Bot made by Maura and Abby! I have 7 commands\n\n1. dish (1 parameter)\n2. mealplan (no parameters)\n3. conversion (4 parameters)\n4. docs (no parameters)\n5. help (1 parameter)\n6. image (1 parameter)\n7. funfact (no parameters) \n\nIf you want command specific information please run \"!help command\". \n\nPrefix any commands with a ! (i.e. \"!dish Spaghetti\")" \
             "\n\nYou can find our github repository under the link https://github.com/mctoner/Newbury-Toner-Discord-Bot-DS3002 \n\nSee you later and get cookin'!"
    # embedding Guy Fieri gif
    embed = discord.Embed(title="Guy Fieri", description="Chef Extraordinaire", color=0x00ff00)  # creates embed
    embed.set_image(url="https://media0.giphy.com/media/S6Bb5IEuEeWpp81NaY/giphy.gif")
    # sending response of all docs and the gif to discord when prompted
    await ctx.send(answer, embed=embed)

# FOOD IMAGE (!image)
# build command with name image and help statement
@bot.command(name='image', help='enter !image and a food or dish of your choice and this command will return an image of the food or dish (i.e. \"!image apple_fruit\")\n Make sure to be as specific as possible in the food or dish description. \n If no image appears, try again with a more specific wording!')
async def docs(ctx, food): #image has one arg, the food name
    # replacing underscore with space (so there is only one arg in discord)
    food = food.replace("_"," ")
    # API for image search
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"
    #calling Web Search API for image of specified search term
    querystring = {"q": food, "pageNumber": "1", "pageSize": "1", "autoCorrect": "true"}
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "86c3a427e7msh9f5124431b54772p1fbe72jsn146f648808b4"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status() #raise for status if invalid
    # photo link is json with a certain value for the image url
    photo_link = response.json() #convert API repsonse to json
    # embedding food image
    embed = discord.Embed(title=food, description="Image of "+food, color=0x00ff00)  # creates embed
    embed.set_image(url=photo_link['value'][0]['url']) #parse json for image url and use to embed in discord
    # sending response
    await ctx.send(embed=embed) #send response of image when promted by !image food_name

# DISH NUTRITION INFO
# build command with name dish that takes a dish name and returns nutritional info
@bot.command(name='dish', help='enter !dish and a dish name with white space denoted by underscores (i.e. \"dish Spaghetti_Aglio_et_Olio\") and this command will give you Calories, Fat, Protein, and Carbs information')
async def dish_facts(ctx, dish): #command has one input, the dish name; if multiple words, using underscore since discord takes one arg and space recongizes two+
    # API for dish search
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"
    dish = dish.replace("_"," ") #replace _ with white space to search API
    querystring = {"title": dish} # search term for API call is the dish name with whitespace

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "86c3a427e7msh9f5124431b54772p1fbe72jsn146f648808b4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring) #call API
    response.raise_for_status() #raise for status if empty or invalid
    # json with nutritonal info for a given dish
    nutrition_json = response.json() #convert response to json
    try: #if all went well, print the dish name and it's nutritional info, parsed from the json
        answer = "The dish you searched for is: " + dish + '\nCalories: ' + str(nutrition_json['calories']['value']) + '\nFat (g): ' + str(nutrition_json['fat']['value']) +'\nProtein (g): ' + str(nutrition_json['protein']['value']) + '\nCarbs (g): ' + str(nutrition_json['carbs']['value'])
    # exception to catch KeyError when dish name not recognized
    except:
        answer = "You did not enter a known dish. Please try again."
    # sending response in discord when completed
    await ctx.send(answer)

# MEAL PLAN
# create a command that takes the number of calories desired for the day and returns a randomized meal plan
@bot.command(name='mealplan',
             help='enter !meal-plan and this command will give you a random assortment of drinks and meals, along with how many servings of each, that will provide 2000 calories for the day'
                  '\n(i.e. \"!mealplan\")')
async def mealplan(ctx):
    cals = 2000  # input is number of calories, ensure it's an integer
    # meal plan API
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

    querystring = {"targetCalories": cals, "timeFrame": "day"}  # query for API call with input # calories

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "86c3a427e7msh9f5124431b54772p1fbe72jsn146f648808b4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)  # call API
    response.raise_for_status()  # raise if error
    # response with meal plan
    meals_json = response.json()  # convert response to json
    meals_list = [i['title'] for i in meals_json['meals']]  # pull dish names from meal plan json and store in list
    servings_list = [i['servings'] for i in meals_json['meals']]  # pull servings from meal plan and store in list
    answer_list = []  # to store strings of suggested meals
    # joining list of amounts of certain food items to eat to reach calorie goal
    for i in range(len(meals_list)):  # loop through meal list
        answer_list.extend([str(servings_list[i]), ' servings of ', str(meals_list[i]),
                            '\n'])  # add the string '# servings of X_dish" to running list of meals
        answer = ''.join(answer_list)  # join all meals together in one string
    # sending response in Discord
    await ctx.send(answer)

# CONVERSION
# creates command with the name conversion that converts X units of food/liquid to Y units.
@bot.command(name='conversion',help='enter !conversion with four parameters. ingredient=ingredient you want to convert,starting_unit=unit you start with (ie Liters,L,mL,grams,cups, etc.),amount_to_convert=number of cups,grams,etc. you wish to convert ,final_unit=the measurement you wish to convert to.. ie cups, etc. \n For example, typing "!conversion water mL 1000 Liter" returns "1000 ml water translates to 1 liter."')
async def conversion(ctx, ingredient,starting_unit,amount_to_convert,final_unit): #takes four inputs
    try:
        # conversion API
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/convert"
        # four inputs: ingredient=ingredient using, final_unit=end goal, starting_unit=starting unit ie grams, amount= numeric input of substance ie 2.5
        querystring = {"ingredientName":ingredient,"targetUnit":final_unit,"sourceUnit":starting_unit,"sourceAmount":amount_to_convert}

        headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': "86c3a427e7msh9f5124431b54772p1fbe72jsn146f648808b4"
            }
        #call and store API response
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status() #raise for status
        # json with converted units
        units_json=response.json() #convert response to json
        answer=units_json['answer'] #parse out for conversion, example is '1 liter of water is 1000mL'
    # if faulty arguments given (in wrong order, misspelled unit, etc.)
    except:
         answer = "Something went wrong. Please ensure you have entered four parameters in the correct order. See \"!help conversion\""
    # sending response
    await ctx.send(answer) #send answer in Discord


# FUN FOOD FACT
# command named funfact that sends a random fun fact about food and takes no arguments
@bot.command(name='funfact',
             help='Type !funfact to read a fun, food realated fact. This command take no paramters or inputs!')
async def funfact(ctx): #takes no arguments
    # fun food fact =API
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/trivia/random"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "86c3a427e7msh9f5124431b54772p1fbe72jsn146f648808b4"
    }
    response = requests.request("GET", url, headers=headers) #call API
    response.raise_for_status()
    fact_full = response.json() #store response in json
    # fixing fact formatting
    answer = str(fact_full['text']).replace('\n', '').replace("'","") #fixing formatting of string, as seen in joke command
    # sending response in Discord
    await ctx.send(answer)

# running the bot using the discord Bot token
bot.run(TOKEN)



