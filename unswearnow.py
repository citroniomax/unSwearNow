from pynput import keyboard
k = keyboard

keylog = ' '
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
    insult = ''

    if len(str(key)) == 3:      # key management
        keylog += str(key)[1:2:]
    if str(key) == 'Key.space':
        keylog += ' '
    if str(key) == 'Key.backspace':
        keylog = keylog[:-1:]
    if str(key) == 'Key.enter':
        keylog = ' '
    if keylog == '':
        keylog = ' '
    
    for i in range(len(file)):       # word changer
        fx = file[i][0]
        if fx in keylog:
            if keylog[-len(fx)-1:-len(fx):] == ' ':
                for _ in range(len(file[i][0])):
                    k.Controller().press(keyboard.Key.backspace)
                    k.Controller().release(keyboard.Key.backspace)
                k.Controller().type(file[i][1])
            else:
                for _ in range(len(fx)):        # avoid bug
                    insult += '-'
                keylog = keylog[:-len(fx):] + insult

    # print(keylog)

with k.Listener(on_press=down) as listener:     # keylogger
    listener.join()
