from re import match
from PIL import Image


special = ["?", "!", "'", ".", ","]
special_dict = {"?":"q_mark.png",
                "!":"e_mark.png",
                "'":"apos.png",
                ".":"per.png",
                ",":",.png"}

special_height = {"?":0,
                "!":0,
                "'":0,
                ".":7,
                ",":7}

def get_name(s):
    name_punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”…’–'
    for p in name_punctuation:
        s = s.replace(p, "")
    return s[:10]

def strip_punc(s):
    punctuation = '"#$%&\()*+-/:;<=>@[\\]^_`{|}~“”–'
    for p in punctuation:
        s = s.replace(p, "")
    s = s.replace("…", "...")
    s = s.replace("’", "'")
    return s

def max_dim(s):
    return (50 + len(s) * 7, 11) # widest chr is 7 px, hopefully my sentences have less than 50 words

def get_chr_name(c):
    if c in special:
        return "./default/" + special_dict[c]
    if c.islower():
        return "./default/{}-001.png".format(c)
    return "./default/{}.png".format(c)

def get_y(c, image):
    if c in special:
        return special_height[c]
    if c.isupper():
        return 0
    else:
        y = 8 - image.size[1]
        if c in "gjpqy":
            y += 3
        return y
            
    

def make_pic(s, counter):
    s_punc = strip_punc(s)
    try:
        i = 0
        im = Image.new("RGBA", (max_dim(s_punc)))
        for char in s_punc:
            if char != " ":
                if char == "'":
                    i -= 1
                elif char == "j":
                    i -= 1
                c_image = Image.open(get_chr_name(char))
                y = get_y(char, c_image)
                im.paste(c_image, (i, y))
                i += 1 + c_image.size[0]
                if char == "'":
                    i -= 1
            else:
                i+=4
        im.save("./output/" + str(counter) + " " + get_name(s_punc) + ".png", "PNG")
    except Exception as e:
        raise e
        print(e)
        print("Failed:{}=>{}".format(s, s_punc))

text = "Insert string here."

counter = 0

text = [sent for sent in text.split("\n") if sent != ""]
for sent in text:
    make_pic(sent, counter)
    counter +=1
