vowel=["a","e","i","o","u"]
consonant=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
a=str(input())
if a in vowel:
  print("vowel")
elif a in consonant:
      print("consonant")
else:
        print("Invalid")
