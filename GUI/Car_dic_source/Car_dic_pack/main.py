from Car_dic_pack import Classes
import random
import time
from tkinter import *
from tkinter import messagebox
from random import randint





player1 = Classes.player()
dwarf1 = Classes.dwarf()
elf1 = Classes.elf()
human1 = Classes.human()  
enemy1 = Classes.enemy()
kind_list = [dwarf1,elf1,human1]
actual_damage = 0
actual_damage_to_player = 0
actual_damage_to_enemy = 0
buton_list = []
flaging = True
root = Tk()
root.geometry("400x300")
app = Classes.Window(root)


def Elf_choose():
    player1.add_up(elf1)
    messagebox.showinfo("Info", "You clicked on %s"%player1.kind_name)
    delete_text(buton_list)
    main_menu()
    
def Human_choose():
    player1.add_up(human1)
    messagebox.showinfo("Info", "You clicked on %s"%player1.kind_name)
    delete_text(buton_list)
    main_menu()
    
def Dwarf_choose():
    player1.add_up(dwarf1)
    messagebox.showinfo("Info", "You clicked on %s"%player1.kind_name)
    delete_text(buton_list)
    main_menu()
    
def place_text_Choosekind():
    A = Label(root, text = "Choose your kind : ")
    B = Button(root, text = "Elf : str : 20, int : 80 , agi 80", command = Elf_choose)
    C = Button(root, text = "Human : str : 60, int : 60, agi = 60", command = Human_choose)
    D = Button(root, text = "Dwarf : str : 80, int : 30, agi : 50", command = Dwarf_choose)
    
    A.grid(row = 1, column = 1)
    B.grid(row = 1, column = 2)
    C.grid(row = 2, column = 2)
    D.grid(row = 3, column = 2)
    
    buton_list.append(A)
    buton_list.append(B)
    buton_list.append(C)
    buton_list.append(D)
    
def delete_text(listings):   
    for i in listings:
        i.grid_forget()

def healing():
    player1.health = player1.base_health
    
def main_menu():
    delete_text(buton_list)

    Title = Label(root, text = "What do you want to do ? :")
    Choice_1 = Button(root, text = "Attack", command = attack_text)
    Choice_2 = Button(root, text = "Player Stats", command = player_stats)
    Choice_3 = Button(root, text = "Shop", command = shop)
    Choice_4 = Button(root, text = "Rest(Heal)", command = lambda : healing)
    Choice_5 = Button(root, text = "Quit", command = quit)
    
    Title.grid(row = 1, column = 1)
    Choice_1.grid(row = 2, column = 2)
    Choice_2.grid(row = 3, column = 2)
    Choice_3.grid(row = 4, column = 2)
    Choice_3.grid(row = 5, column = 2)
    Choice_5.grid(row = 6, column = 2)
    
    buton_list.append(Title)
    buton_list.append(Choice_2)
    buton_list.append(Choice_1)
    buton_list.append(Choice_3)
    buton_list.append(Choice_4)
    buton_list.append(Choice_5)
    
def player_stats():# print the player stats
    delete_text(buton_list)
    
    intel = Label(root,text = "Inteligence : %d"%player1.inte)
    agi = Label(root,text ="Agility : %d"%player1.agi)
    stre = Label(root,text ="Strenght : %d"%player1.stre)
    res = Label(root,text ="Resistance : %d"%player1.resistance)
    mag_res = Label(root,text ="Magic Resistance : %d"%player1.magic_resistance)
    lvl = Label(root,text ="Level : %d"%player1.level)
    cash = Label(root,text ="Money : %d"%player1.money)
    back()
    
    intel.grid(row = 1, column = 1)
    agi.grid(row = 2, column = 1)
    stre.grid(row = 3, column = 1)
    res.grid(row = 4, column = 1)
    mag_res.grid(row = 5, column = 1)
    lvl.grid(row = 6, column = 1)
    cash.grid(row = 7, column = 1)

    buton_list.append(intel)
    buton_list.append(agi)
    buton_list.append(stre)
    buton_list.append(res)
    buton_list.append(mag_res)
    buton_list.append(lvl)
    buton_list.append(cash)

def info_attack(): 
    delete_text(buton_list)
    
    xp_gained = random.randint(int(player1.xp_low),int(player1.xp_high))
    money_gained =random.randint(int(player1.money_low),int(player1.money_high))
    enemy_xp_gained = random.randint(int(enemy1.xp_low),int(enemy1.xp_high))
    player1.money_low *= 1.2
    player1.money_high*= 1.2
    player1.xp_low *= 1.2
    player1.xp_high *= 1.2
    player1.exp += xp_gained
    enemy1.exp += enemy_xp_gained
    player1.money += money_gained
    
    info = Label(root,text ="""You killed the %s !
        You gained %d xp
        You now have %d xp
        You gained %d $
        You now have %d $"""%(enemy1.kind_name,xp_gained,player1.exp,money_gained,player1.money))
    info.grid(row = 1, column = 1)
    back()
    global flaging
    flaging = True
    buton_list.append(info)
def randomize():
    global enemy1

    random_choice = random.choice(kind_list)
    enemy1.add_up(random_choice)
def attack_text():
    delete_text(buton_list)
    global flaging
    global enemy1
    if flaging:
        randomize()
        flaging = False

    enemy_text = Label(root,text ="The ennemy is an %s"%enemy1.kind_name)
    enemy_health = Label(root, text = "It has %d hp"%enemy1.health)
    disp_text = Label(root,text ="What do you want to do :")
    magic_button = Button(root, text = "Magic", command = magic_attack)
    melee_button = Button(root, text = "Melee", command = melee_attack)
    dealt_damage = Label(root, text = "It dealt %d damage to you "%actual_damage_to_player)
    
    enemy_text.grid(row = 1, column = 1)
    enemy_health.grid(row = 2, column = 1)
    disp_text.grid(row = 3, column = 1)
    magic_button.grid(row = 4, column = 1)
    melee_button.grid(row = 4, column = 2)
    dealt_damage.grid(row = 5, column = 1)
    
    buton_list.append(enemy_text)
    buton_list.append(enemy_health)
    buton_list.append(magic_button)
    buton_list.append(disp_text)
    buton_list.append(melee_button)
    buton_list.append(dealt_damage)
    
def magic_attack():
    global actual_damage_to_player
    global actual_damage_to_enemy
    
    if player1.kind == 1:
        magic_damage = player1.inte * random.uniform(1,2) 
            
    else :
        magic_damage = player1.inte * random.uniform(0.5,2)
            
    actual_damage_to_player = 0
    actual_damage_to_enemy = 0 #reset previous value
    
    actual_damage_to_player = magic_damage - enemy1.magic_resistance
    actual_damage_to_enemy = magic_damage - player1.magic_resistance
        
    if actual_damage_to_player < 0 or actual_damage_to_enemy < 0: # prevent negative damage point
        actual_damage_to_player = 0
        actual_damage_to_enemy = 0
        
    enemy1.health -= actual_damage_to_enemy
    
    if enemy1.health > 0: #prevent damage to player if enemy already dead
            player1.health -= actual_damage_to_player
            attack_text()
    else :
        info_attack()
        enemy1.health = enemy1.base_health
    
def melee_attack():
    global actual_damage_to_player
    global actual_damage_to_enemy
    if player1.kind ==  3:
        melee_damage = player1.stre * random.uniform(1,2)
        
    else :
        melee_damage = player1.stre * random.uniform(0.5,2)
        
    actual_damage_to_player = 0
    actual_damage_to_enemy = 0 #reset previous value
    actual_damage_to_player = melee_damage - enemy1.resistance
    actual_damage_to_enemy = melee_damage - player1.resistance
    
    if actual_damage_to_player < 0 or actual_damage_to_enemy < 0: # prevent negative damage point
        actual_damage_to_player = 0
        actual_damage_to_enemy = 0
        
    enemy1.health -= actual_damage_to_enemy
    
    if enemy1.health > 0: #prevent damage to player if enemy already dead
        attack_text()
    else :
        info_attack()
        enemy1.health = enemy1.base_health

def back():  
    back = Label(root, text ="Do you want to go back ?")
    back_1 = Button(root,text ="Yes", command = main_menu)
    back_2 = Button(root , text ="No", command = quit)
     
    back.grid(row = 10, column = 1)
    back_1.grid(row = 11, column = 1)
    back_2.grid(row = 11, column = 2)

    buton_list.append(back)
    buton_list.append(back_1)
    buton_list.append(back_2)
    
def shop():#create a shopping area 
    delete_text(buton_list)
    sword = "sword"
    shield = "shield"
    money_label = Label(root, text = "You have %d" %player1.money)
    item_choice = Label(root, text = "This is the available item :")
    item_1 = Button(root, text = "Iron Sword = 50£", command = lambda : buying_items(sword))
    item_2 = Button(root, text = "Iron Shield = 50£", command = lambda : buying_items(shield))
    back()
    
    money_label.grid(row = 1,column = 1)
    item_choice.grid(row = 2,column = 1)
    item_1.grid(row = 3,column = 1)
    item_2.grid(row = 4,column = 1)
    
    buton_list.append(money_label)
    buton_list.append(item_choice)
    buton_list.append(item_1)
    buton_list.append(item_2)
    
def buying_items(item):

    if player1.money>= 50 :
        bought = Label(root, text = "You bought %s !"%item)
        player1.money = player1.money - 500
        
    elif player1.money< 50 :
        bought = Label(root, text = "You need more money")
    bought.grid(row = 5,column = 2)

def main():
    place_text_Choosekind()
    root.mainloop()
    
