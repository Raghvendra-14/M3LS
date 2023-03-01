import os

# Define the list of available languages
languages = ["english", "japanese", "hindi", "tamil", "sinhala", "french", "bangla", "chinese", "nepali", "russian", "indonesia", "marathi", "telugu", "ua", "urdu", "punjabi", "brasil", "spanish", "gujarati", "pashto"]

print("Available languages are: ", languages)

# Prompt the user to input the language names
language_names = input("Enter one or more language names separated by spaces: ").split()

# Filter the language names to include only those that are available
language_names = [language_name for language_name in language_names if language_name in languages]

# Loop through the selected language names
for language_name in language_names:
    # Construct the path to the spider file
    lang_path = os.path.join("scrapy-code", language_name)
    for root, dirs, files in os.walk(lang_path):
        for dir in dirs:
            # check for folder with bbc as prefix
            if dir.startswith("bbc"):
                spiders_path = os.path.join(root, dir, "spiders")
                # "spiders" folder inside folder with prefix "bbc" contains the spider file
                if os.path.exists(spiders_path):
                    os.chdir(spiders_path)
                    os.system(f"scrapy runspider bbcspider.py")
