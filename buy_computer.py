current_chocie = "-"
computer_parts = []
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi"
                   ]
#valid_choices = [str(i) for i in range (1, len(available_parts)+1)]
valid_choices = []
for i in range(1, len(available_parts)+1):
    valid_choices.append((str(i)))
print(valid_choices)

while current_chocie != '0':
    if current_chocie in valid_choices:
        print("Adding {}".format(current_chocie))
        if current_chocie == '1':
            computer_parts.append("computer")
        elif current_chocie == '2':
            computer_parts.append("monitor")
        elif current_chocie == '3':
            computer_parts.append("keyboard")
        elif current_chocie == '4':
            computer_parts.append("mouse")
        elif current_chocie == '5':
            computer_parts.append("mouse mat")
        elif current_chocie == '6':
                computer_parts.append("hdmi")
    else:
        print("Please add options from the list below")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number+1,part))
    current_chocie = input()
computer_parts.pop(0)
print(computer_parts)