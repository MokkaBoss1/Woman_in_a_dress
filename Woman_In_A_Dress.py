import random

ethnicities = [
    "Random",
    "American",
    "British",
    "English",
    "Scottish",
    "Welsh",
    "French",
    "German",
    "Italian",
    "Spanish",
    "Japanese",
    "Chinese",
    "Russian",
    "Brazilian",
    "Indian",
    "Mexican",
    "Australian",
    "Canadian",
    "Swedish",
    "Dutch",
    "Irish",
    "Korean",
    "Norwegian",
    "Swiss",
    "Danish",
    "Israeli",
    "Greek",
    "Turkish",
    "Portuguese",
    "Belgian",
    "Austrian",
    "Polish",
    "South African",
    "Egyptian",
    "Thai",
    "Argentinian",
    "Chilean",
    "Colombian",
    "Peruvian",
    "Filipino",
    "Vietnamese",
    "Indonesian",
    "Malaysian",
    "Singaporean",
    "New Zealander",
    "Finnish",
    "Czech",
    "Hungarian",
    "Ukrainian",
    "Moroccan",
    "Saudi Arabian",
    "Emirati"
]

haircolours = [
    "Random",
    "Black",
    "Brown",
    "Blonde",
    "Platinum Blonde",
    "Red",
    "Brunette",
    "Auburn",
    "Chestnut",
    "Honey",
    "Dark Brown",
    "Light Brown"
]

hairstyles = [
    "Random",
    "Blunt Bob",
    "Long Bob",
    "Messy Bun",
    "Beach Waves",
    "Sleek Straight",
    "Wavy Lob",
    "Balayage",
    "Ombre",
    "Egyptian Bob",
    "Half-Up Half-Down",
    "Space Buns",
    "Box Braids",
    "Long Layers",
    "High Ponytail",
    "Fishtail Braid",
    "Bubble Ponytail",
    "Slicked Back",
    "Shaggy Layers",
    "Curtain Bangs",
    "Asymmetrical Pixie",
    "Feathered Layers",
    "Layered Shag"
]

dress_styles = [
    "Random",
    "Shift dress",
    "A-line dress",
    "Ball gown",
    "Sheath dress",
    "Wrap dress",
    "Maxi dress",
    "Midi dress",
    "Mini dress",
    "Bodycon dress",
    "Fit and flare dress",
    "Empire waist dress",
    "Peplum dress",
    "Shirt dress",
    "Halter neck dress",
    "Off-the-shoulder dress",
    "One-shoulder dress",
    "Strapless dress",
    "High-low dress",
    "Mermaid dress",
    "Princess dress",
    "Tiered dress",
    "Tunic dress",
    "Chemise dress",
    "Slip dress",
    "Jumper dress",
    "Balloon dress",
    "Cape dress",
    "Kimono dress",
    "Corset dress",
    "Flapper dress",
    "Belted Shirt Dress",
    "Belted V-Neck Midi Dress",
    "Cotton Padded T-Shirt Dress",
    "Embroidered Bell Sleeve Mini Dress",
    "Open Back Chiffon Midi Dress",
    "Printed Belted Shirt Dress",
    "Printed Chiffon Midi Dress",
    "Printed Chiffon Mini Dress",
    "Printed Crêpe Chiffon Mini Dress",
    "Printed Crêpe Midi Dress",
    "Print V-Neck Midi Dress",
    "Ribbed Off-Shoulder Midi Dress",
    "Short-Sleeve Mini Dress",
    "Sleeveless Crêpe Chiffon Mini Dress",
    "Sleeveless Peplum Mini Dress",
    "Sleeveless Punto Mini Dress",
    "Structured Mini Dress",
    "Striped Padded T-Shirt Dress",
    "T-Shirt Midi Dress",
    "Textured Flounced Hem Mini Dress",
    "3/4 Sleeve Crêpe Midi Dress",
    "Lingerie Set",
    "Bodysuit",
    "Corset and Garter Belt Set",
    "Babydoll and Chemise",
    "Roleplay costume"
    
]

dress_colours = [
    "Random",
    "Black",
    "Sapphire Blue",
    "Ruby Red",
    "Emerald Green",
    "Amethyst Purple",
    "Coral Pink",
    "Turquoise",
    "Gold",
    "Silver",
    "Ivory",
    "Champagne",
    "Lavender",
    "Magenta",
    "Teal",
    "Burgundy",
    "Lilac",
    "Peach",
    "Mint",
    "Mustard Yellow",
    "Aqua",
    "Indigo",
    "Rose Gold",
    "Copper",
    "Maroon",
    "Periwinkle",
    "Slate Gray",
    "Coral",
    "Navy Blue",
    "Olive Green",
    "Blush",
    "Mauve"
    "Powder Blue",
    "Tangerine",
    "Forest Green",
    "Ruby Pink",
    "Plum",
    "Bronze",
    "Pearl White",
    "Chocolate Brown",
    "Sky Blue",
    "Crimson",
    "Sunset Orange",
    "Charcoal Gray",
    "Moss Green",
    "Turquoise Blue",
    "Coral Reef",
    "Salmon Pink",
    "Lime Green",
    "Electric Blue",
    "Deep Purple",
    "Rosewood"
]

dress_patterns_textures = [
    "Random",
    "Stripes",
    "Polka dots",
    "Floral",
    "Geometric",
    "Plaid",
    "Animal print",
    "Tie-dye",
    "Houndstooth",
    "Checkered",
    "Abstract",
    "Paisley",
    "Embroidery",
    "Lace",
    "Sequins",
    "Velvet",
    "Denim",
    "Paisley",
    "Zebra patterned",
    "Jacquard",
    "Crochet",
    "Mesh",
    "Satin",
    "Gingham",
    "Tartan",
    "Ombre",
    "Brocade",
    "Chiffon",
    "Batik",
    "Tulle",
    "Fringe",
    "Ruffles",
    "Leather",
    "Cotton",
    "Polyester",
    "Chiffon",
    "Silk",
    "Linen",
    "Jersey",
    "Denim",
    "Rayon",
    "Velvet",
    "Tulle"
]

num_ethnicities = len(ethnicities)-1
num_hairstyles = len(hairstyles)-1
num_haircolours = len(haircolours)-1
num_styles = len(dress_styles)-1
num_colours = len(dress_colours)-1
num_patterns = len(dress_patterns_textures)-1






class Woman_in_a_dress:

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text": ("STRING", {"multiline": False, "default": ""}),
                    "ethnicity": ((ethnicities), ),
                    "hair_colour": ((haircolours), ),
                    "hair_style": ((hairstyles), ),
                    "dress_style": ((dress_styles), ),
                    "dress_colour": ((dress_colours), ),
                    "pattern_or_texture": ((dress_patterns_textures), ),
                    }
                }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Positive Prompt",)
    FUNCTION = "test3"
    CATEGORY = "MokkaBoss1"

    def test3(self, text, ethnicity, hair_colour, hair_style, dress_style, dress_colour, pattern_or_texture):

        if ethnicity == "Random":
            random_ethnicity = random.randint(1, num_ethnicities-1)
            ethnicity = ethnicities[random_ethnicity]
            
        if hair_colour == "Random":
            random_haircolour = random.randint(1, num_haircolours-1)
            hair_colour = haircolours[random_haircolour]
        
        if hair_style == "Random":
            random_hairstyle = random.randint(1, num_hairstyles-1)
            hair_style = hairstyles[random_hairstyle]
        
        if dress_style =="Random":
            random_dressstyle = random.randint(1, num_styles-1)
            dress_style = dress_styles[random_dressstyle]
        
        if dress_colour == "Random":
            random_colour = random.randint(1,num_colours-1)
            dress_colour = dress_colours[random_colour]
        
        if pattern_or_texture =="Random":
            random_pattern = random.randint(1,num_patterns-1)
            pattern_or_texture = dress_patterns_textures[random_pattern]
        
    
    
    
    
    
        positive_prompt = f"Pretty 21 year old {ethnicity} woman with {hair_colour} {hair_style}, wearing a {dress_colour} {pattern_or_texture} {dress_style}, {text}"

        print(positive_prompt)

        return [positive_prompt]

NODE_CLASS_MAPPINGS = {"Woman_in_a_dress": Woman_in_a_dress}
NODE_DISPLAY_NAME_MAPPINGS = {"Woman_in_a_dress": "Woman_in_a_dress"}
