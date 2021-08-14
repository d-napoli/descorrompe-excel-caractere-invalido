# Uncorrupt Excel Files
Sometimes, when we try to open an **excel file** it has a group of characters that wasn't encoded when the file was created.
#### Such as the error bellow.
![enter image description here](https://raw.githubusercontent.com/d-napoli/uncorrupt-excel-file/main/images/illegal-character.png)

This code opens the xml file of the Excel, using the **specified origin path**. Finds in the entire folder content where's the character that wasn't able to be interpreted by Excel and simply **removes it.**