import pygame
from pygame.locals import *
import random
import time
import sys
import os

#DEBUGGER DEVELOPER TOOL
debug = False
if debug == True:
    from threading import *
    from debug import *
    def passthu():
        while True:
            debug.update(globals())
            time.sleep(0.5)
    ptt = Thread(target=passthu)
    ptt.setDaemon(True)
    ptt.start()

suits = ["C","D","H","S"]
nums = ["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
unshuffled_deck = []
if False:
    import pygame._view
class deckmaker:
    for suit in suits:
        for num in nums:
            unshuffled_deck.append(num+suit)
    def deckcreate(decks):
        deck=unshuffled_deck*+int(decks)
        random.shuffle(deck)
        return deck
def rp(relative_path):
    try:
        raise Exception
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)
class inputbox:
    def get_key():
        while 1:
            event = pygame.event.poll()

            if event.type == KEYDOWN:
                return event.key
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                pass
    def display_box(screen, message):
        fontobject = pygame.font.Font(rp('freesans.ttf'), 18)
        pygame.draw.rect(screen, (0, 0, 0),
                         ((screen.get_width() / 2) - 100,
                          (screen.get_height() / 2) - 10,
                          200, 20), 0)
        pygame.draw.rect(screen, (255, 255, 255),
                         ((screen.get_width() / 2) - 102,
                          (screen.get_height() / 2) - 12,
                          204, 24), 1)
        if len(message) != 0:
            screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                        ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
        pygame.display.flip()
    def ask(screen, question, money):
        pygame.font.init()
        current_string = []
        inputbox.display_box(screen, question + ": " + "".join(current_string))
        while 1:
            inkey = inputbox.get_key()
            if inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == K_RETURN:
                  try:
                    amount = int("".join(current_string))
                    if amount < money+1:
                        break
                    else:
                        None
                  except:
                    None
            elif inkey == K_MINUS:
                current_string.append("_")
            elif inkey <= 127:
                current_string.append(chr(inkey))
            inputbox.display_box(screen, question + ": " + "".join(current_string))
        return "".join(current_string)
chips = {"currency":"£","amount":1000}
card_value = {"A":11,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
card_value_hard = {"A":1,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
con = ["bust","in","lose","bj","push"]
def card_load(item,x=150,y=200):
    base_path = "./assets/cards/"
    to_load = base_path + item + ".png"
    card_image = pygame.image.load(to_load)
    card =  pygame.transform.scale(card_image,(x,y)).convert_alpha()
    return card
def card_load_unsafe(item):
    base_path = "./assets/cards/"
    to_load = base_path + item + ".png"
    card = pygame.image.load(to_load).convert_alpha()
    return card
def add(give):
    global chips
    chips["amount"] += give
def dubd(bet):
    return 2*bet
def chip_command(command,bet):
    give=0
    if command == "push":
        give = bet
    if command == "win":
        give = 2*bet
    if command == "lose":
        give = 0
    if command == "bj":
        give = 2.5*bet
    add(give)
bet = 0
pygame.init()
size=(900,600)
minsize=(800,550)
if size[0] < minsize[0] or size[1] < minsize[1]:
    size = minsize
fs = True
if fs == True:
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)
pygame.display.set_caption("AA Jack");
back_color = "red"
num_decks = 8
backer = card_load(back_color+"_back")
sides = (size[0] - 300)/2
cardx1 = sides
cardy = size[1]/100*65
deck_start = deckmaker.deckcreate(num_decks)
random.shuffle(deck_start)
deck = deck_start
done = False
screen_width = pygame.display.get_surface().get_size()[0]
screen_height = pygame.display.get_surface().get_size()[1]
swh = pygame.display.get_surface().get_size()
card_width = 150
clock = pygame.time.Clock()
bg = pygame.image.load("assets/table.png")
bg = pygame.transform.scale(bg,swh)
split = False
def check():
    global deck,deck_start
    if len(deck) == 0:
        deck_start = deckmaker.deckcreate(num_decks)
        deck = deck_start
def hit(person):
    global mycards,dealerscards,split,card_side
    if split == False:
        i = "Done"
        if person == "player":
            mycards.append(deck.pop(0))
        elif person == "dealer":
            dealerscards.append(deck.pop(0))
        else:
            i = "Fail"
        return i
    else:
        i = "Done"
        if person == "player":
            mycards[card_side].append(deck.pop(0))
        elif person == "dealer":
            dealerscards.append(deck.pop(0))
        else:
            i = "Fail"
        return i
def reset():
    global mycards,dealerscards, step,split
    mycards = []
    split = False
    card_side = 0
    splitdoubled = [0,0]
    dealerscards = []
    check()
    step = 0
    getbet()
def getbet():
    global bet
    bet = -1
    screen.blit(bg, (0,0))
    titlepic = card_load("title",int(screen_width/1.5),int(screen_height/6))
    w = titlepic.get_rect().size[0]
    whomadeit = card_load("wb",int(screen_width/2.5),int(screen_height/5))
    wm = whomadeit.get_rect().size[0]
    wh = whomadeit.get_rect().size[1]
    screen.blit(titlepic,((screen_width-w)/2,screen_height/8))
    screen.blit(whomadeit,((screen_width-wm)/2,(screen_height-2*wh)))
    dis_money()
    pygame.display.flip()
    bet = int(inputbox.ask(screen,"Bet Amount",chips["amount"]))
    while bet == -1:
        None
    chips["amount"] -= int(bet)
def dis_money():
    text = font.render(("Chips: " + chips["currency"]) + str(chips["amount"]), True, (0, 0, 0), (255, 255, 255))
    screen.blit(text, (0,screen_height/2))
    if bet == -1:
        dim = "None"
    else:
        dim = chips["currency"]+str(bet)
    text = font.render(("Bet: " + str(dim)), True, (0, 0, 0), (255, 255, 255))
    screen.blit(text, (0,screen_height/2+font.size(("Chips: " + chips["currency"]) + str(chips["amount"]))[1]))
def check_amount(cards,who):
    global split
    if split == False or who == "d":
        total = 0
        dsoft = True
        there_is_ace = False
        for card in cards:
            if "A" in card:
                there_is_ace = True
        if (there_is_ace and len(cards) == 2) or ("A" in cards[-1]):
            dsoft = False    
        if dsoft == False:
            for card in cards:
                total += card_value[card[:-1]]
        else:
            for card in cards:
                 total += card_value_hard[card[:-1]]
    else:
        total = []
        for cardlist in cards:
            total_of = 0
            dsoft = True
            there_is_ace = False
            for card in cardlist:
                if "A" in card:
                    there_is_ace = True
            if (there_is_ace and len(cardlist) == 2) or ("A" in cardlist[-1]):
                dsoft = False
            if dsoft == False:
                for card in cardlist:
                    total_of += card_value[card[:-1]]
            else:
                for card in cardlist:
                     total_of += card_value_hard[card[:-1]]
            total.append(total_of)
    return total
def gr(c):
    mess = card_load(c,x=500,y=400)
    w = mess.get_width()
    h = mess.get_height()
    x = screen_width
    y = screen_height
    x = (x-w)/2
    y = (y-h)/2
    screen.blit(mess,[x,y])
    pygame.display.flip()
    time.sleep(3)
def dis_cards(cards,y,r=True):
    row_width = int(card_width * (len(cards))) + int(len(cards) * 30)
    for card in range(len(cards)):
        card_x_pos = (int(screen_width / 2) - int(row_width / 2)) + (card * card_width) + (card * 30)
        screen.blit(card_load(str(cards[card])),[card_x_pos,y])
    if r == False:
        screen.blit(backer,[card_x_pos,y])
def dis_screen(real=False):
    global split
    screen.blit(bg, [0,0])
    if split == True:
        dis_cards_as(mycards,screen_height-210)
    else:
        dis_cards(mycards,screen_height-210)
    dis_cards(dealerscards,5,real)
    if real == True:
        a = dealer_total
    else:
        a = dealer_total-card_value[dealerscards[-1][0]]
    text = font.render(("Dealer: "+str(a)+"| Player: "+str(my_total)), True, (0, 0, 0), (255, 255, 255))
    screen.blit(text, (0,0))
    dis_money()
    cardx1 = (screen_width/2)-180
    screen.blit(card_load("split",x=150,y=50),[cardx1,size[1]/2-55])
    screen.blit(card_load("dd",x=150,y=50),[cardx1,size[1]/2])
    screen.blit(card_load("hit",x=150,y=50),[cardx1+190,size[1]/2-55])
    screen.blit(card_load("stand",x=150,y=50),[cardx1+190,size[1]/2])
def stand():
    global dealer_total,my_total,bet,dealerscards,mycards,split,card_side,splitdoubled
    my_total = check_amount(mycards,"u")
    dealer_total = check_amount(dealerscards,"d")
    dis_screen()
    dis_money()
    if split == False:
        dis_screen(True)
        dis_money()
        pygame.display.flip()
        pygame.display.update()
        time.sleep(2)
        if (dealer_total>my_total) and (dealer_total< 22):
            gr("lose")
            chip_command("lose",bet)
        elif dealer_total == my_total:
            gr("push")
            chip_command("push",bet)
        elif dealer_total >21:
            gr("win")
            chip_command("win",bet)
        elif my_total > 21:
            gr("lose")
            chip_command("lose",bet)
        else:
            while (dealer_total<my_total) and (dealer_total<17):
                hit("dealer")
                dealer_total = check_amount(dealerscards,"d")
                dis_screen(True)
                pygame.display.flip()
                time.sleep(2)
            if dealer_total > 21 or my_total>dealer_total:
                gr("win")
                chip_command("win",bet)
            elif dealer_total == my_total:
                gr("push")
                chip_command("push",bet)
            else:
                if dealer_total > my_total:
                    gr("lose")
                    chip_command("lose",bet)
        reset()
    else:
        dis_screen()
        dis_money()
        if card_side == 0:
            card_side = card_side+1
        else:
            my_totalq = check_amount(mycards,"u")
            c = 0
            base_bet = bet /(splitdoubled[0]+splitdoubled[1]+2)
            amwin = 0
            for my_total in my_totalq:
                bet = base_bet *(splitdoubled[c]+1)
                dis_screen(True)
                pygame.display.flip()
                pygame.display.update()
                time.sleep(2)
                if (dealer_total>my_total) and (dealer_total< 22):
                    chip_command("lose",bet)
                    amwin -= 1
                elif dealer_total == my_total:
                    chip_command("push",bet)
                elif dealer_total >21:
                    chip_command("win",bet)
                    amwin += 1
                elif my_total > 21:
                    chip_command("lose",bet)
                    amwin -=1
                else:
                    while (dealer_total<my_total) and (dealer_total<17):
                        hit("dealer")
                        dealer_total = check_amount(dealerscards,"d")
                        dis_screen(True)
                        pygame.display.flip()
                        time.sleep(2)
                    if dealer_total > 21 or my_total>dealer_total:
                        chip_command("win",bet)
                        amwin += 1
                    elif dealer_total == my_total:
                        chip_command("push",bet)
                    else:
                        if dealer_total > my_total:
                            chip_command("lose",bet)
                            amwin -= 1
                c+1
            if amwin == 0:
                wpl = "push"
            elif amwin < 0:
                wpl = "lose"
            else:
                wpl = "win"
            gr(wpl)
            time.sleep(2)
            reset()
                
def double():
    global chips,bet,card_side,split,splitdoubled
    if split == False:
        if chips["amount"] > bet-1:
            chips["amount"] -= bet
            bet = 2*bet
            time.sleep(2)
            hit("player")
            stand()
        else:
            #print("Cant Double Down, Not enough chips!")
            None
    else:
        if card_side == 0:
            if chips["amount"] > bet/2-1:
                chips["amount"] -= bet/2
                bet += bet/2
                splitdoubled[0] += 1
                time.sleep(2)
                hit("player")
                card_side += 1
            else:
                #print("Cant Double Down, Not enough chips!")
                None
        elif card_side == 1:
            if splitdoubled[0] == 0:
                if chips["amount"] > bet/2-1:
                    chips["amount"] -= bet/2
                    bet += bet/2
                    splitdoubled[1] += 1
                    time.sleep(2)
                    hit("player")
                    stand()
                else:
                    #print("Cant Double Down, Not enough chips!")
                    None
            else:
                if chips["amount"] > bet/3-1:
                    chips["amount"] -= bet/3
                    bet += bet/3
                    splitdoubled[1] += 1
                    time.sleep(2)
                    hit("player")
                    stand()
                else:
                    #print("Cant Double Down, Not enough chips!")
                    None
step = 0
splitdoubled = [0,0]
mycards = []
dealerscards = []
cardx1 = (screen_width/2)-180
split_button = pygame.Rect(cardx1, size[1]/2-55, 150, 50)
dd_button = pygame.Rect(cardx1, size[1]/2, 150, 50)
hit_button = pygame.Rect(cardx1+190, size[1]/2-55, 150, 50)
stand_button = pygame.Rect(cardx1+190, size[1]/2, 150, 50)
dealer_total = 0
my_total = 0
soft_total = False
font = pygame.font.Font(rp('freesans.ttf'), 32)
logo = card_load_unsafe("logo")
pygame.display.set_icon(logo)
def dis_cards_as(allcards,y):
    i = 0
    for cards in allcards:
        row_width = int(card_width * (len(cards))) + int(len(cards) * 30)
        for card in range(len(cards)):
            if i==0:
                card_x_pos = (int(screen_width / 4) - int(row_width / 2)) + (card * card_width) + (card * 30)
            if i==1:
                card_x_pos = (int(screen_width / 4 * 3) - int(row_width / 2)) + (card * card_width) + (card * 30)
            screen.blit(card_load(str(cards[card])),[card_x_pos,y])
        i = i+1
card_side = 0
getbet()
#DAS
#NSAS
while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if split_button.collidepoint(mouse_pos):
                    #print('split_button was pressed at {0}'.format(mouse_pos))
                    if len(mycards) == 2 and split == False and ((chips["amount"] > bet-1)or bet == 0):
                        if card_value[mycards[0][:-1]] == card_value[mycards[1][:-1]]:
                            mycards = [[mycards[0]],[mycards[0]]]
                            split = True
                            card_side = 0
                            chips["amount"] -= bet
                            bet +=bet
                            dis_screen()
                            pygame.display.flip()
                        else:
                            #print("Cant Split. Not same valued cards.")
                            None
                    else:
                        #print("Cant Split. You have already split or not enough chips or not first turn.")
                        None
                if dd_button.collidepoint(mouse_pos):
                    #print('dd_button was pressed at {0}'.format(mouse_pos))
                    double()
                if hit_button.collidepoint(mouse_pos):
                    #print('hit_button was pressed at {0}'.format(mouse_pos))
                    hit("player")
                    check()
                    step = 1
                if stand_button.collidepoint(mouse_pos):
                    #print('stand_button was pressed at {0}'.format(mouse_pos))
                    stand()
    if split == False:
        if my_total > 21 and soft_total == False:
            dis_screen(True)
            gr("bust")
            chip_command("lose",bet)
            reset()
        if my_total == 21 and len(mycards) == 2:
            dis_screen(True)
            if dealer_total == 21:
                gr("push")
                chip_command("push",bet)
            else:
                gr("bj")
                chip_command("bj",bet)
            reset()
        if dealer_total == 21 and len(dealerscards) == 2: 
            dis_screen(True)
            gr("lose")
            chip_command("lose",bet)
            reset()
    if step == 0:
        for i in "12":
            check()
            mycards.append(deck.pop(0))
            check()
            dealerscards.append(deck.pop(0))
        step += 1
    if step == 1:
        dealer_total = 0
        my_total = 0
        soft = False
        dsoft = False
        dealer_total = check_amount(dealerscards,"d")
        my_total = check_amount(mycards,"u")
        #print(dealer_total,my_total)
        step +=1
    dis_screen()
    dis_money()
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
exit()
