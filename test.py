from difflib import SequenceMatcher

with open('file1.txt') as file1, open('file2.txt') as file2:
    file1_data = file1.read()
    file2_data = file2.read()
    similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
    print(f"The contents are {similarity*100}% common.")