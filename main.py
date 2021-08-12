def handle_special_charactere(self, inicial_path, final_path):
    file_name = inicial_path

    with open(file_name, 'r', encoding = 'latin_1') as f: # open the excel file using another encoding 'latin_1'
        p = re.compile(r"\\[a-z]{2}[0-9]|\\[a-z][0-9]{2}|\\[a-z]{3}|\\[a-z][0-9][a-z]") # regexr of special characters in the ascii table
        q = re.compile(r"\\[x][c](2|3)") # regexr with the valid characters in the ascii table
        all_chars = [] # vector with the final characters array
        
        for line in f.readlines(): # loop in all file lines
            new_line = []

            for chars in line: # loop with the characters
                if chars in cLib.possibleChars: # checks if the character is within the valid Portuguese characters
                    
                    if chars == ' ': # if it is a blank space, we've got to reset the delimiter
                        last_encoding = "" # resets the delimiter

                    all_chars.append(chars) # concatenate the found character

                else: # if not within the valid characters
                    last_encoding = last_encoding + str(chars.encode(encoding = "latin_1", errors = "backslashreplace")) # pega o codigo asccii
                    m = p.findall(last_encoding) # check if the current character matches the regex

                    if len(m) == 2: # if the regex has a size of 2 (portuguese always come in two pieces)
                        n = q.findall(m[0]) # get the first part of the character

                        if len(n) > 0: # if the first part matches the regex
                            try: # tries to find the character in the lib
                                all_chars.append(cLib.accent_conversion[str(m[0]) + str(m[1])]) # add into the array
                                last_encoding = "" # resets the delimiter
                            except:
                                pass # special characters are ignores

    final_string = "" # resets the final string

    for i in all_chars: # loop in all found characters
        final_string = final_string + i

    file = open(final_path, 'w', encoding = 'utf-8')
    file.write(final_string) # writes the final string in a new file
