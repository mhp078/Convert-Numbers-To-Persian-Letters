import sys

def PersianTyper(value):
    splitv = value.split(" ")
    i = 0
    while i < len(splitv):
        if splitv[i] == "":
            splitv[i] = ""
            splitv.remove("")
        elif splitv[i] == " " :
            splitv[i] = " "
            splitv.remove(" ")
        elif " " in splitv[i] :
            splitv[i] = " "
            splitv[i] = "#$#$#$#$#|"
            splitv.remove("#$#$#$#$#|")
        i = i + 1

    b = 0
    while b < len(splitv):
        q = 0
        word = ""
        lastw = ""
        splitv[b] = splitv[b]
        for txt in splitv[b]:
            q = q + 1
            if lastw == "":
                if q == 1:
                    txt = checkerFunction(txt,"start")
                elif q == len(splitv[b]):
                    txt = checkerFunction(txt,"end")
                elif q > len(splitv[b]):
                    txt = checkerFunction(txt,"end")
                else:
                    txt = checkerFunction(txt,"center")
                
            else :
                if q == 1:
                    txt = checkerFunction(txt,"start")
                elif q == len(splitv[b]):
                    if "ا" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "آ" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "د" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ذ" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ر" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ز" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ژ" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "و" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    else:
                        txt = checkerFunction(txt,"end")
                elif q > len(splitv[b]):
                    if "ا" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "آ" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "د" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ذ" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ر" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ز" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "ژ" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    elif "و" in lastw:
                        txt = checkerFunction(txt,"endPlus")
                    else:
                        txt = checkerFunction(txt,"end")
                else:
                    if "ا" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "آ" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "د" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "ذ" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "ر" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "ز" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "ژ" in lastw:
                        txt = checkerFunction(txt,"start")
                    elif "و" in lastw:
                        txt = checkerFunction(txt,"start")
                    else:
                        txt = checkerFunction(txt,"center")
            lastw = txt
            word = word + txt
        word = word[::-1]
        splitv[b] = word
        b = b+1
    #
    l = len(splitv)
    all_txt = ""
    while 0 < l:
        m = l - 1
        all_txt = all_txt + splitv[m] + " "
        l = l - 1
    editor = all_txt
    editor = editor[::-1]
    editor = editor.replace(" ","",1)
    editor = editor[::-1]
    all_txt = editor
    return all_txt
def checkerFunction(string , value):
    if(value == "start"):
        string = string.replace("ا","ﺍ")
        string = string.replace("آ","ﺁ")
        string = string.replace("ب","ﺑ")
        string = string.replace("پ","ﭘ")
        string = string.replace("ت","ﺗ")
        string = string.replace("ث","ﺛ")
        string = string.replace("ج","ﺟ")
        string = string.replace("چ","ﭼ")
        string = string.replace("ح","ﺣ")
        string = string.replace("خ","ﺧ")
        string = string.replace("د","ﺩ")
        string = string.replace("ذ","ﺫ")
        string = string.replace("ر","ﺭ")
        string = string.replace("ز","ﺯ")
        string = string.replace("ژ","ﮊ")
        string = string.replace("س","ﺳ")
        string = string.replace("ش","ﺷ")
        string = string.replace("ص","ﺻ")
        string = string.replace("ض","ﺿ")
        string = string.replace("ط","ﻃ")
        string = string.replace("ظ","ﻇ")
        string = string.replace("ع","ﻋ")
        string = string.replace("غ","ﻏ")
        string = string.replace("ف","ﻓ")
        string = string.replace("ق","ﻗ")
        string = string.replace("ک","ﮐ")
        string = string.replace("گ","ﮔ")
        string = string.replace("ل","ﻟ")
        string = string.replace("م","ﻣ")
        string = string.replace("ن","ﻧ")
        string = string.replace("و","ﻭ")
        string = string.replace("ه","ﻫ")
        string = string.replace("ی","ﯾ")
    elif(value == "center"):
        string = string.replace("ا","ا")
        string = string.replace("آ","ﺁ")
        string = string.replace("ب","ﺒ")
        string = string.replace("پ","ﭙ")
        string = string.replace("ت","ﺘ")
        string = string.replace("ث","ﺜ")
        string = string.replace("ج","ﺠ")
        string = string.replace("چ","ﭽ")
        string = string.replace("ح","ﺤ")
        string = string.replace("خ","ﺨ")
        string = string.replace("د","ﺪ")
        string = string.replace("ذ","ﺬ")
        string = string.replace("ر","ﺮ")
        string = string.replace("ز","ﺰ")
        string = string.replace("ژ","ﮋ")
        string = string.replace("س","ﺴ")
        string = string.replace("ش","ﺸ")
        string = string.replace("ص","ﺼ")
        string = string.replace("ض","ﻀ")
        string = string.replace("ط","ﻄ")
        string = string.replace("ظ","ﻈ")
        string = string.replace("ع","ﻌ")
        string = string.replace("غ","ﻐ")
        string = string.replace("ف","ﻔ")
        string = string.replace("ق","ﻘ")
        string = string.replace("ک","ﮑ")
        string = string.replace("گ","ﮕ")
        string = string.replace("ل","ﻠ")
        string = string.replace("م","ﻤ")
        string = string.replace("ن","ﻨ")
        string = string.replace("و","ﻮ")
        string = string.replace("ه","ﻬ")
        string = string.replace("ی","ﯿ")
    elif(value == "end"):
        string = string.replace("ا","ﺍ")
        string = string.replace("آ","ﺁ")
        string = string.replace("ب","ﺐ")
        string = string.replace("پ","ﭗ")
        string = string.replace("ت","ﺖ")
        string = string.replace("ث","ﺚ")
        string = string.replace("ج","ﺞ")
        string = string.replace("چ","ﭻ")
        string = string.replace("ح","ﺢ")
        string = string.replace("خ","ﺦ")
        string = string.replace("د","ﺩ")
        string = string.replace("ذ","ﺫ")
        string = string.replace("ر","ﺭ")
        string = string.replace("ز","ﺯ")
        string = string.replace("ژ","ژ")
        string = string.replace("س","ﺲ")
        string = string.replace("ش","ﺶ")
        string = string.replace("ص","ﺺ")
        string = string.replace("ض","ﺾ")
        string = string.replace("ط","ﻂ")
        string = string.replace("ظ","ﻆ")
        string = string.replace("ع","ﻊ")
        string = string.replace("غ","ﻎ")
        string = string.replace("ف","ﻒ")
        string = string.replace("ق","ﻖ")
        string = string.replace("ک","ﮏ")
        string = string.replace("گ","ﮓ")
        string = string.replace("ل","ﻞ")
        string = string.replace("م","م")
        string = string.replace("ن","ﻥ")
        string = string.replace("و","ﻭ")
        string = string.replace("ه","ﻩ")
        string = string.replace("ی","ﯼ")
    elif(value == "endPlus"):
        string = string.replace("ا","ﺍ")
        string = string.replace("آ","ﺁ")
        string = string.replace("ب","ب")
        string = string.replace("پ","پ")
        string = string.replace("ت","ت")
        string = string.replace("ث","ث")
        string = string.replace("ج","ج")
        string = string.replace("چ","چ")
        string = string.replace("ح","ح")
        string = string.replace("خ","خ")
        string = string.replace("د","د")
        string = string.replace("ذ","ذ")
        string = string.replace("ر","ر")
        string = string.replace("ز","ز")
        string = string.replace("ژ","ژ")
        string = string.replace("س","س")
        string = string.replace("ش","ش")
        string = string.replace("ص","ص")
        string = string.replace("ض","ض")
        string = string.replace("ط","ط")
        string = string.replace("ظ","ظ")
        string = string.replace("ع","ع")
        string = string.replace("غ","غ")
        string = string.replace("ف","ف")
        string = string.replace("ق","ق")
        string = string.replace("ک","ک")
        string = string.replace("گ","گ")
        string = string.replace("ل","ل")
        string = string.replace("م","م")
        string = string.replace("ن","ن")
        string = string.replace("و","و")
        string = string.replace("ه","ه")
        string = string.replace("ی","ی")
    return string

baseFarsiLetters = {
	1: "یک",
	2: "دو",
	3: "سه",
	4: "چهار",
	5: "پنج",
	6: "شش",
	7: "هفت",
	8: "هشت",
	9: "نه",
	10: "ده",
	11: "یازده",
	12: "دوازده",
	13: "سیزده",
	14: "چهارده",
	15: "پانزده",
	16: "شانزده",
	17: "هفده",
	18: "هجده",
	19: "نوزده",
	20: "بیست",
	30: "سی",
	40: "چهل",
	50: "پنجاه",
	60: "شصت",
	70: "هفتاد",
	80: "هشتاد",
	90: "نود",
	100: "صد",
	200: "دویست",
	300: "سیصد",
	500: "پانصد",
	600: "ششصد",
	700: "هفتصد",
	800: "هشتصد",
	900: "نهصد",
}
baseFarsiLettersKeys = set(baseFarsiLetters.keys())

baseNumber = ["یک", 
              "هزار", 
              "میلیون"]
basicLetters  = baseNumber + ["بیلیون", 
                              " تریلیون",
                              " کوآدریلیون", 
                              " کوینتیلیون", 
                              " سکستیلیون",
                              " سپتیلیون",
                              " اکتیلیون",
                              " نانیلیون",
                              " دسیلیون",
                              " آندسیلیون",
                              " دیودسیلیون",
                              " تریدسیلیون",
                              " کواتیوردسیلیون",
                              " کویندسیلیون",
                              " سکسدسیلیون", 
                              "سپتدسیلیون",
                              " اُکتودسیلیون",
                              " نومدسیلیون"]


def split(st):
	section = []
	n = len(st)
	d, m = divmod(n, 3)
	for i in range(d):
		section.append(int(st[n - 3 * i - 3:n - 3 * i]))
	if m > 0:
		section.append(int(st[:m]))
	return section


def convertion(text):
	if isinstance(text, int):
		text = str(text)
	elif not isinstance(text, str):
		raise TypeError("تایپ نادرست")
	if len(text) > 3:
		parts = split(text)
		k = len(parts)
		wText = []
		for i in range(k):
			persianFa = ""
			p = parts[i]
			if p == 0:
				continue
			if i == 0:
				partition = convertion(p)
			else:
				if i < len(basicLetters):
					persianFa = basicLetters[i]
				else:
					persianFa = ""
					d, m = divmod(i, 3)
					tb = basicLetters[3]
					for j in range(d):
						if j > 0:
							persianFa += "‌"
						persianFa += tb
					if m != 0:
						if persianFa != "":
							persianFa = "‌" + persianFa
						persianFa = basicLetters[m] + persianFa
				partition = persianFa if i == 1 and p == 1 else convertion(p) + " " + persianFa
			wText.append(partition)
		return " و ".join(reversed(wText))

	n = int(text)
	if n in baseFarsiLettersKeys:
		return baseFarsiLetters[n]
	y = n % 10
	d = int((n % 100) / 10)
	s = int(n / 100)

	dy = 10 * d + y
	temp = ""
	if s != 0:
		if s * 100 in baseFarsiLettersKeys:
			temp += baseFarsiLetters[s * 100]
		else:
			temp += (baseFarsiLetters[s] + baseFarsiLetters[100])
		if d != 0 or y != 0:
			temp += " و "
	if d != 0:
		if dy in baseFarsiLettersKeys:
			temp += baseFarsiLetters[dy]
			return temp
		temp += baseFarsiLetters[d * 10]
		if y != 0:
			temp += " و "
	if y != 0:
		temp += baseFarsiLetters[y]
	return temp


def baseConvertion(n):
	if isinstance(n, int):
		number = n
		st = str(n)
	elif isinstance(n, str):
		number = int(n)
		st = n
	else:
		raise TypeError("تایپ نادرست")
	if number == 1:
		return "اول"
	elif number == 10:
		return "دهم"
	farsi_nurm = convertion(st)
	if not farsi_nurm:
		return ""
	if farsi_nurm.endswith("ی"):
		farsi_nurm += "‌ام"
	elif farsi_nurm.endswith("سه"):
		farsi_nurm = farsi_nurm[:-1] + "وم"
	else:
		farsi_nurm += "م"
	return farsi_nurm

def convert_numbers_to_letters(n):
        if(n < 0):
            return "منفی " + PersianTyper(convertion(n * -1))
        else:
            return PersianTyper(convertion(n))


#Examples
print(convert_numbers_to_letters(-245))
print(convert_numbers_to_letters(1006775))
print(convert_numbers_to_letters(130050))
print(convert_numbers_to_letters(100650))
print(convert_numbers_to_letters(100650))
print(convert_numbers_to_letters(997751076))
print(convert_numbers_to_letters(-100650))