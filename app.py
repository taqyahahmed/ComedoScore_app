from flask import Flask, render_template, request

app = Flask(__name__)

comedogenicity_dict = {
    #user inout converts to lowercase, so dict needs to be lowercase
    "ascorbyl palmitate": 2,
    "abyssinian (crambe) oil": 1,
    "acai berry oil": 2,
    "acetylated lanolin": 4,
    "acetylated lanolin alcohol": 4,
    "almond oil, sweet": 2,
    "algae extract": 5,
    "algin": 4,
    "almond oil": 2,
    "amla (gooseberry) oil": 1,
    "andiroba seed oil": 2,
    "apricot kernel oil": 2,
    "argan oil": 1,
    "avocado oil": 3,
    "babassu oil": 2,
    "bacuri butter": 4,
    "baobab seed oil": 2,
    "benzoic acid": 2,
    "beta carotene": 1,
    "beeswax": 2,
    "butyl stearate": 3,
    "butyl oleate": 3,
    "butylene glycol": 1,
    "black cumin (nigella) oil": 2,
    "black currant seed oil": 1,
    "blackberry seed oil": 1,
    "blueberry seed oil": 1,
    "borage oil": 2,
    "borage co2": 2,
    "brazil nut oil": 2,
    "broccoli seed oil": 1,
    "buriti oil": 3,
    "butyl myristate": 3,
    "cacay oil": 2,
    "calendula": 1,
    "camphor": 2,
    "candelilla wax": 1,
    "capric acid": 2,
    "caprylic acid": 3,
    "carbomer": 1,
    "carnuba wax": 1,
    "carrageenan": 5,
    "cetearyl alcohol": 2,
    "ceteareth-20": 4,
    "ceteareth-6": 2,
    "ceteareth-3": 2,
    "cetyl alcohol": 2,
    "cetyl palmitate": 4,
    "cetearyl isononanoate": 2,
    "cocoa butter": 4,
    "coconut butter": 4,
    "colloidal sulfur": 4,
    "camellia (oleifera) seed oil": 2,
    "camellia (oleifera) seed oil - high oleic acid": 3,
    "carrot seed oil": 4,
    "caprylic capric triglyceride": 1,
    "castor oil": 2,
    "cherry kernel oil": 2,
    "chia seed oil": 1.5,
    "chia seed co2": 2,
    "cloudberry seed oil": 1,
    "coconut oil": 4,
    "coconut oil, fractionated": 3,
    "cottonseed oil": 3,
    "cranberry seed oil": 2,
    "cucumber seed oil": 1,
    "cupuacu butter": 4,
    "corn oil": 3,
    "decyl oleate": 3,
    "d&c red #17": 3,
    "d&c red #19": 2,
    "d&c red #21": 3,
    "d&c red #3": 3,
    "d&c red #4": 1,
    "d&c red #6": 1,
    "d&c red #7": 1,
    "d&c red #9": 1,
    "dimethicone": 1,
    "diisopropyl adipate": 3,
    "dioctyl succinate": 3,
    "emu oil": 0,
    "ethylparaben": 0,
    "ethylhexyl palmitate": 4,
    "ethylhexyl stearate": 3,
    "echium seed oil": 2,
    "elderberry seed oil": 2,
    "evening primrose oil": 2,
    "flax seed oil (linseed)": 4,
    "goji berry seed oil": 1,
    "grapeseed oil": 1,
    "guava seed oil": 1,
    "glyceryl stearate nse": 1,
    "glyceryl stearate se": 3,
    "glyceryl oleate": 3,
    "glyceryl dilaurate": 3,
    "glycol stearate": 3,
    "hazelnut oil": 1,
    "hemp seed oil": 0.5,
    "hexyl laurate": 4,
    "isoamyl laurate": 2,
    "isocetyl stearate": 5,
    "isopropyl alcohol": 4,
    "isopropyl isostearate": 5,
    "isopropyl myristate": 5,
    "isopropyl palmitate": 4,
    "isopropyl stearate": 2,
    "isostearyl neopentanoate": 3,
    "isopropyl lanolate": 4,
    "isopropyl linoleate": 5,
    "jojoba oil": 2,
    "kigelia africana seed oil": 2,
    "kiwi seed oil": 1,
    "kukui nut oil": 2,
    "lanolin alcohol": 2,
    "lanolin oil": 1,
    "lanolin wax": 1,
    "laureth 23": 3,
    "laureth 4": 5,
    "lauric acid": 4,
    "lithiumm stearate": 1,
    "magneseium aluminum silicate": 0,
    "magnesium stearate": 1,
    "myristic acid": 3,
    "macadamia nut oil": 2.5,
    "mango butter": 2,
    "mango seed oil": 2,
    "marula oil": 4,
    "meadowfoam seed oil": 1,
    "myristyl myristate": 5,
    "moringa oil": 3,
    "murumuru butter": 3,
    "myristyl lactate": 4,
    "myristyl alcohol": 2,
    "neem oil": 2,
    "oat oil": 2,
    "octyl cocoate": 2,
    "olive oil": 2,
    "octyl palmitate": 4,
    "octyl stearate": 5,
    "oleth-3": 5,
    "oleth-10": 2,
    "oleic acid": 2,
    "palm oil (pulp)": 4,
    "palm kernel oil": 3,
    "pentaerythrityl tetraoctanoate": 2,
    "papain": 3,
    "papaya seed oil": 3,
    "passionfruit (maracuja) seed oil": 2,
    "palmitic acid": 2,
    "polyethylene glycol (peg 400)": 1,
    "propylene glycol monostearate": 4,
    "peach kernel oil": 2,
    "peanut oil": 2,
    "peg 75 lanolin": 3,
    "peg 100 stearate": 1,
    "peg-40 sorbitan peroleate": 3,
    "peg 16 lanolin": 4,
    "peg 8 stearate": 3, 
    "peg-200 dilaurate": 4,
    "pequi oil": 3,
    "perilla oil": 2,
    "plum kernel oil": 2,
    "propylene glycol dicaprylate": 2,
    "pomegranate seed oil": 1,
    "poppyseed oil": 1,
    "ppg-3 myristyl ether": 5,
    "prickly pear seed oil": 2,
    "red algea": 5,
    "pumpkin seed oil": 2,
    "raspberry seed oil": 2,
    "red raspberry seed oil": 1,
    "rice bran oil": 2,
    "rosehip oil (seed)": 1,
    "rosehip co2 (seed)": 1,
    "rosehip oil (pulp)": 2,
    "rosehip co2 (pulp)": 2,
    "sacha inci": 1,
    "sea buckthorn oil (pulp)": 2,
    "sea buckthorn co2 (pulp)": 2,
    "sea buckthorn oil (seed)": 1,
    "sesame seed oil": 3,
    "shea butter": 1,
    "soybean oil": 5,
    "safflower oil": 2,
    "simethicone": 1,
    "sodium chloride": 5,
    "sodium laureth sulfate": 3,
    "sodium lauryl sulfate": 5,
    "sorbitan oleate": 3,
    "squalene": 1,
    "stearic acid": 2,
    "stearyl alcohol": 2,
    "sulfated castor oil": 3,
    "sulfated jojoba oil": 3,
    "squalane": 1,
    "strawberry seed oil": 1,
    "sunflower seed oil": 2,
    "sunflower oil": 1,
    "syearyl heptanoate": 4,
    "talc": 1,
    "tacuma butter": 3,
    "tamanu oil": 2,
    "tomato seed oil": 2,
    "tocopheryl acetate": 2,
    "ucuuba butter": 4,
    "vitamin e (tocopherol)": 2,
    "vitamin a palmitate": 2,
    "walnut seed oil": 2,
    "watermelon seed oil": 1,
    "wheat germ oil": 5,
    "zinc oxide": 1
}

# Show input form:
@app.route("/")
def home():
    return render_template("index.html")

# Handle form submission:
@app.route("/check", methods=["POST"])
def check():
    # Get ingredients from form:
    ingredients = request.form["ingredients"]
    
    # Make lowercase list:
    ingredient_list = [i.strip().lower() for i in ingredients.split(",")]
    
    results = {}
    for ing in ingredient_list: #for each ing entered
        if ing in comedogenicity_dict: #if the ing is comedo
            results[ing] = comedogenicity_dict[ing] #setting the value
            #at the ing in the dict to the one from the comedo list

        else:
            results[ing] = 0

    #code to return flagged ingredients:
    flagged = {}
    for ing in results:
        if results[ing] >=3:
            flagged[ing] = results[ing]
    output = ""
    if flagged:
        output += "Flagged Ingredients:\n"
        for ing, score in flagged.items():
            if score == 3:
                output += f"{ing}: {score} 🟡\n"
            elif score == 4:
                output += f"{ing}: {score} 🟠\n"
            else:
                output += f"{ing}: {score} 🔴\n"



    # code to return overall rating:
    comedo_sum = 0
    num_results = 0
    if results:
        for i in results:
            comedo_sum += results[i]
            num_results += 1
    
        comedo_mean = comedo_sum / num_results #never has division by 0 case

        output += "<br>Overall Comedogenicity Rating:"
        if comedo_mean <= 0.5:
            output += "⭐⭐⭐⭐⭐"
        elif comedo_mean <=1:
            output += "⭐⭐⭐⭐"
        elif comedo_mean <= 2:
            output += "⭐⭐⭐"
        elif comedo_mean <= 3:
            output += "⭐⭐"
        else:
            output += "⭐"
       

    #return:
    return output



if __name__ == "__main__":
    app.run(debug=True)