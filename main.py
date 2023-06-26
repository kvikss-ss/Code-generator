

print (""" 
 ██████  ██████  ██████  ███████      ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
██      ██    ██ ██   ██ ██          ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██      ██    ██ ██   ██ █████       ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██      ██    ██ ██   ██ ██          ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
 ██████  ██████  ██████  ███████      ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                                                                  

 If you use a text that wasn't coded here its wouldn't work.
                                                                              by:Kviks
""")
print()

while True:
    codeOrDecode = input("Wanna code a text or decode? [For decode write d, and for code write c] ")

    if codeOrDecode == "c":
        textcode = input("What text do you want to code? Paste it here: ")
        def howToCode():
            codedText = textcode.replace(" ", "•")
            codedText = codedText.replace("a", "⇠")
            codedText = codedText.replace("A", "⇠")
            codedText = codedText.replace("b", "➛")
            codedText = codedText.replace("B", "➛")
            codedText = codedText.replace("c", "▹")
            codedText = codedText.replace("C", "▹")
            codedText = codedText.replace("d", "◷")
            codedText = codedText.replace("D", "◷")
            codedText = codedText.replace("e", "▇")
            codedText = codedText.replace("E", "▇")
            codedText = codedText.replace("f", "Φ")
            codedText = codedText.replace("F", "Φ")
            codedText = codedText.replace("g", "≣")
            codedText = codedText.replace("G", "≣")
            codedText = codedText.replace("h", "➽")
            codedText = codedText.replace("H", "➽")
            codedText = codedText.replace("i", "◦")
            codedText = codedText.replace("I", "◦")
            codedText = codedText.replace("j", "○")
            codedText = codedText.replace("J", "○")
            codedText = codedText.replace("k", "❃")
            codedText = codedText.replace("K", "❃")
            codedText = codedText.replace("l", "◛")
            codedText = codedText.replace("L", "◛")
            codedText = codedText.replace("m", "▲")
            codedText = codedText.replace("M", "▲")
            codedText = codedText.replace("n", "‡")
            codedText = codedText.replace("N", "‡")
            codedText = codedText.replace("o", "▎")
            codedText = codedText.replace("O", "▎")
            codedText = codedText.replace("p", "◉")
            codedText = codedText.replace("P", "◉")
            codedText = codedText.replace("q", "⚂")
            codedText = codedText.replace("Q", "⚂")
            codedText = codedText.replace("r", "Δ")
            codedText = codedText.replace("R", "Δ")
            codedText = codedText.replace("s", "⋮")
            codedText = codedText.replace("S", "⋮")
            codedText = codedText.replace("t", "⅛")
            codedText = codedText.replace("T", "⅛")
            codedText = codedText.replace("u", "▯")
            codedText = codedText.replace("U", "▯")
            codedText = codedText.replace("v", "▧")
            codedText = codedText.replace("V", "▧")
            codedText = codedText.replace("w", "⠓")
            codedText = codedText.replace("W", "⠓")
            codedText = codedText.replace("x", "↬")
            codedText = codedText.replace("X", "↬")
            codedText = codedText.replace("y", "↜")
            codedText = codedText.replace("Y", "↜")
            codedText = codedText.replace("z", "⠽")
            codedText = codedText.replace("Z", "⠽")
            return codedText

        coded_text = howToCode()
        print(coded_text)


    elif codeOrDecode == "d":
        codedText = input("Type in the coded text: ")

        def howToDecode():
            decodedText = codedText.replace("•", " ")
            decodedText = decodedText.replace("⇠", "a")
            decodedText = decodedText.replace("➛", "b")
            decodedText = decodedText.replace("▹", "c")
            decodedText = decodedText.replace("◷", "d")
            decodedText = decodedText.replace("▇", "e")
            decodedText = decodedText.replace("Φ", "f")
            decodedText = decodedText.replace("≣", "g")
            decodedText = decodedText.replace("➽", "h")
            decodedText = decodedText.replace("◦", "i")
            decodedText = decodedText.replace("○", "j")
            decodedText = decodedText.replace("❃", "k")
            decodedText = decodedText.replace("◛", "l")
            decodedText = decodedText.replace("▲", "m")
            decodedText = decodedText.replace("‡", "n")
            decodedText = decodedText.replace("▎", "o")
            decodedText = decodedText.replace("◉", "p")
            decodedText = decodedText.replace("⚂", "q")
            decodedText = decodedText.replace("Δ", "r")
            decodedText = decodedText.replace("⋮", "s")
            decodedText = decodedText.replace("⅛", "t")
            decodedText = decodedText.replace("▯", "u")
            decodedText = decodedText.replace("▧", "v")
            decodedText = decodedText.replace("⠓", "w")
            decodedText = decodedText.replace("↬", "x")
            decodedText = decodedText.replace("↜", "y")
            decodedText = decodedText.replace("⠽", "z")
            return decodedText

        decodedText = howToDecode()
        print(decodedText)

    else :
        print("I don't understand that sorry big boy.")