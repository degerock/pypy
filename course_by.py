import random

times = ["Утром","Днем","Вечером","Ночью","После обеда","Перед сном"]
advices = ["ожидайте","предостеригайтесь","будьте открыты для"]
promises = ["гостей из забытого прошлого","встреч со старыми знакомыми","неодиданного праздника","прияных перемен"]

def generated_prophecies(total_num = 3, num_sentences = 4):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
        
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)
            
            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1
        prophecies.append(forecast)
        i = i + 1
    return prophecies

