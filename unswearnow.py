from pynput import keyboard
k = keyboard

keylog = ''
file = open('filter.txt', 'r', encoding="utf-8").readlines()

for i in range(len(file)):      # convert the txt file into a list of list
    if file[i][0:1:] != '#':
        cache = []
        fx = file[i]
        fx = fx.rstrip('\n')

        for j in range(len(fx)):
            if fx[j:j+1:] == '=':
                cache.append(fx[:j:])
                cache.append(fx[j+1::])
                file[i] = cache

def down(key):     # main function
    global keylog

    if len(str(key)) == 3:      # key management
        keylog += str(key)[1:2:]
    if str(key) == 'Key.space':
        keylog += ' '
    if str(key) == 'Key.backspace':
        keylog = keylog[:-1:]
    if str(key) == 'Key.enter':
        keylog = ''
    
    for i in range(len(file)):       # word changer
        if file[i][0] in keylog:
            for _ in range(len(file[i][0])):
                k.Controller().press(keyboard.Key.backspace)
                k.Controller().release(keyboard.Key.backspace)
            k.Controller().type(file[i][1])

    # print(keylog)

with k.Listener(on_press=down) as listener:     # keylogger
    listener.join()
