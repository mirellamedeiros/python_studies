mimi_str1 = "Run, Forrest! Run!"
mimi_str1 = "Me and Jenny goes together like peas and carrots."
mimi_str3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, saute it. There's shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, shrimp burger, shrimp sandwich. That, that's about it."

# this function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, and assigns that string to the variable 
# spaces_and_letters so that the number of words in it can be found by counting spaces between words.

def word_counter(words):
  spaces_and_letters = ""
  word_count = 1
  for i in words:
    if i.isanum() or i.isspace() or i == "-" or i == "'":
      spaces_and_letters += i
  for j in spaces_and_letters:
    if j == " ":
      word_count += 1
  return word_count
  
