#Name: Kaeden Tony Nelson
#Date Started: October 2020
#Description: A game inspired by Choose Your Class!
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import random
import time
import turtle
import os
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
player_one = turtle.Turtle()
player_one.speed(15)
player_one.shape("circle")
player_one.pensize(3)
color = "cyan"
player_two = turtle.Turtle()
player_two.speed(15)
player_two.shape("circle")
player_two.pensize(3)
color2 = "lime"
enemy_1 = turtle.Turtle()
enemy_1.speed(15)
enemy_1.shape("triangle")
enemy_1.pensize(3)
player1_position = (-70,150)
player2_position = (-70,100)
enemy1_position = (-70,-150)
color_enemy = "red"
atk = 0
atk2 = .0000000000001
def_ = 0
def2_ = 0
spd = 0
spd2 = 0
mana = 0
mana2 = 0
class_w = 0
class2_w2 = 0
clase = 0
clase2 = 0
en_1_class = " "
en_1_class2 = 0
en1_1_class_w = 0
spd2_2 = 0
atk2_2 = 0
def2_2 = 0
spd_2 = 0
atk_2 = 0
def_2 = 0
e1_atk = 0
e1_def = 0
e1_spd = 0
atk3 = .0000000000001
spd3 = 0
def3_ = 0
mana3 = 0
x2 = 0
y2 = 0
z2 = 0
m_Burst3_type = 0
m_Burstx_type = 0
w2 = 0
mana2_to = 0
m_Burst2_type = 0
m_Burst_type = 0
clase_str = " "
clase_str2 = " "
BOSS_name = " "
player_3 = turtle.Turtle()
player3_position = (-70,0)
player_3.pensize(3)
color3 = "DeepPink"
player_3.shape("circle")
player_3.speed(15)
mana3_to = 0
m_Burst3_type = 0
player = 0
Name3 = "?"
clase3_str = " "
clase3 = 0
clase3_w = 0
wins = 0
Continue = 0
attack_who = 0
cards = 3
card_selection = 0
taps = 10
crit_d = 0
crit_d2 = 0
crit_d3 = 0
deaths2 = 0
deaths3 = 0
wh = turtle.Screen()
wh.bgcolor("Black")
won = "n"
mana2_2 = 0
mana3_2 = 0
mana_2 = 0
e1_mana = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#cyc_mod_BOSS_theme = "/Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/cyc_mod_BOSS.wav"
#wave.open(cyc_mod_BOSS_theme,mode=None)
def DrawZamu():
    acirema = turtle.Screen()
    acirema.bgcolor("red")
    Zamu = enemy_1
    Zamu.penup()
    Zamu.goto(enemy1_position)
    Zamu.pendown()
    Zamu.speed(15)
    Zamu.fillcolor("khaki")
    Zamu.pensize(4)
    Zamu.begin_fill()
    Zamu.forward(40)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(40)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(40)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-90)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.right(45)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(40)
    Zamu.end_fill()
    Zamu.fillcolor("purple")
    Zamu.begin_fill()
    Zamu.forward(20)
    Zamu.right(-46)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(60)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(60)
    Zamu.right(45)
    Zamu.forward(20)
    Zamu.right(45)
    Zamu.forward(40)
    Zamu.right(135)
    Zamu.end_fill()
    Zamu.fillcolor("chocolate4")
    Zamu.begin_fill()
    Zamu.right(45)
    Zamu.forward(100)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(45)
    Zamu.forward(100)
    Zamu.back(60)
    Zamu.right(-45)
    Zamu.forward(60)
    Zamu.right(135)
    Zamu.forward(40)
    Zamu.back(20)
    Zamu.right(-135)
    Zamu.forward(40)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(60)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(40)
    Zamu.right(-90)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(40)
    Zamu.right(-135)
    Zamu.forward(40)
    Zamu.right(135)
    Zamu.forward(40)
    Zamu.right(45)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.back(40)
    Zamu.right(-45)
    Zamu.forward(40)
    Zamu.right(45)
    Zamu.forward(20)
    Zamu.back(40)
    Zamu.right(-45)
    Zamu.forward(60)
    Zamu.right(-45)
    Zamu.forward(60)
    Zamu.back(100)
    Zamu.forward(100)
    Zamu.right(45)
    Zamu.forward(27)
    Zamu.right(135)
    Zamu.forward(145)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(40)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-90)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.right(45)
    Zamu.forward(20)
    Zamu.right(135)
    Zamu.forward(20)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.end_fill()
    Zamu.right(-45)
    Zamu.forward(15)
    Zamu.right(270)
    Zamu.penup()
    Zamu.goto(enemy1_position)
    Zamu.right(-90)
    Zamu.forward(80)
    Zamu.right(90)
    Zamu.forward(40)
    Zamu.fillcolor("chocolate2")
    Zamu.begin_fill()
    Zamu.pendown()
    Zamu.forward(40)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.right(-45)
    Zamu.forward(40)
    Zamu.right(-135)
    Zamu.forward(20)
    Zamu.end_fill()
    Zamu.penup()
    Zamu.right(-180)
    Zamu.forward(20)
    Zamu.right(-90)
    Zamu.forward(60)
    Zamu.right(90)
    Zamu.begin_fill()
    Zamu.pendown()
    Zamu.forward(40)
    Zamu.right(90)
    Zamu.forward(20)
    Zamu.right(90)
    Zamu.forward(40)
    Zamu.right(90)
    Zamu.forward(20)
    Zamu.right(45)
    Zamu.forward(60)
    Zamu.end_fill()
    Zamu.up()
    Zamu.hideturtle()
    Zamu.right(-90)
    Zamu.right(180)
    Zamu.forward(160)
    Zamu.goto(enemy1_position)
    Zamu.right(-270)
    acirema.bgcolor("black")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
def DrawKimbley():
    acirema = turtle.Screen()
    acirema.bgcolor("red")
    Kimbley = enemy_1
    Kimbley.penup()
    Kimbley.goto(enemy1_position)
    Kimbley.pendown()
    Kimbley.speed(15)
    Kimbley.fillcolor("tan")
    Kimbley.pensize(4)
    Kimbley.begin_fill()
    Kimbley.forward(40)
    Kimbley.right(-90)
    Kimbley.forward(20)
    Kimbley.right(45)
    Kimbley.forward(60)
    Kimbley.right(-45)
    Kimbley.forward(80)
    Kimbley.right(-45)
    Kimbley.forward(20)
    Kimbley.right(45)
    Kimbley.forward(20)
    Kimbley.right(-45)
    Kimbley.forward(40)
    Kimbley.back(20)
    Kimbley.right(-45)
    Kimbley.forward(40)
    Kimbley.right(-45)
    Kimbley.forward(60)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd):
                mana2_to = random.randint(1,4)
                if mana2_to == 1:
                    if clase2 == 1:
                        m_Burst2_to = random.randint(1,3)
                        if m_Burst2_to == 1:
                            print(Name2,"did a mana burst on the enemy's attack.")
                            e1_atk = (e1_atk - mana2)
                            print("Enemy attack is",e1_atk,".")
                            time.sleep(.5)
                            print(" ")
                        elif m_Burst2_to == 2:
                            print(Name2,"did a mana burst on the enemy's defense.")
                            e1_def = (e1_def - mana2)
                            print("Enemy defense is",e1_def,".")
                            time.sleep(.5)
                            print(" ")
                        else:
                            print(Name2,"did a mana burst on the enemy's speed.")
                            e1_spd = (e1_spd - mana2)
                            time.sleep(.5)
                            print(" ")
                            print("Enemy speed is",e1_spd,".")
                            time.sleep(.5)
                            print(" ")
                        m_Burst2_type = 1
                    elif clase2 == 2:
                        mana2_to = random.randint(2,4)
                        m_Burst2_type = 2
                    elif clase2 == 4:
                        print(Name2,"did a gunner mana burst!")
                        time.sleep(.5)
                        print(" ")
                        print(Name2," has +8 attack!")
                        atk2 = (atk2 + 8)
                        m_Burst2_type = 4
                    elif clase2 == 3:
                        print(Name2,"did a giant mana burst.")
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_to = random.randint(1,3)
                        if m_Burst2_to == 1:
                            print(Name2,"did a mana burst on the enemy's attack.")
                            e1_atk = (e1_atk - mana2)
                            print("Enemy attack is",e1_atk,".")
                            time.sleep(.5)
                            print(" ")
                        elif m_Burst2_to == 2:
                            print(Name2,"did a mana burst on the enemy's defense.")
                            e1_def = (e1_def - mana2)
                            print("Enemy defense is",e1_def,".")
                            time.sleep(.5)
                            print(" ")
                        else:
                            print(Name2,"did a mana burst on the enemy's speed.")
                            e1_spd = (e1_spd - mana2)
                            time.sleep(.5)
                            print(" ")
                            print("Enemy speed is",e1_spd,".")
                            time.sleep(.5)
                            print(" ")
                        print(Name2,"now has regeneration!")
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_type = 3
                    elif clase2 == 5:
                        print(Name2,"did a techster mana burst.")
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_to = random.randint(1,3)
                        if m_Burst2_to == 1:
                            print(Name2,"did a mana burst on the enemy's attack.")
                            e1_atk = (e1_atk - mana2)
                            print("Enemy attack is",e1_atk,".")
                            time.sleep(.5)
                            print(" ")
                        elif m_Burst2_to == 2:
                            print(Name2,"did a mana burst on the enemy's defense.")
                            e1_def = (e1_def - mana2)
                            print("Enemy defense is",e1_def,".")
                            time.sleep(.5)
                            print(" ")
                        else:
                            print(Name2,"did a mana burst on the enemy's speed.")
                            e1_spd = (e1_spd - mana2)
                            time.sleep(.5)
                            print(" ")
                            print("Enemy speed is",e1_spd,".")
                            time.sleep(.5)
                            print(" ")
                        print(Name2,"also attacked the enemy.")
                        time.sleep(.5)
                        print(" ")
                        e1_spd = (e1_spd - (atk2 / 10))
                        print("Enemy speed is now",e1_spd,".")
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_type = 5
                    elif clase2 == 6:
                        print(Name2,"did a healer mana burst!")
                        time.sleep(.5)
                        print(" ")
                        print("Your speed and",Name2,"'s speed just got increased!")
                        spd = (spd + 5)
                        spd2 = (spd2 + 10)
                        time.sleep(.5)
                        print(" ")
                        print("Your speed is now",spd,".")
                        time.sleep(.5)
                        print(" ")
                        print(Name2,"'s speed is now",spd2,".")
                        m_Burst2_type = 6
                    elif clase2 == 7:
                        print(Name2,"did an assassin mana burst!")
                        time.sleep(.5)
                        print(" ")
                        e1_spd = (e1_spd / 2)
                        print("Enemy speed is now",e1_spd,".")
                        m_Burst2_type = 7
                    elif clase2 == 8:
                        print(Name2,"did a beast mana burst!")
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_to = random.randint(1,3)
                        if m_Burst2_to == 1:
                            print(Name2,"did a mana burst on the enemy's attack.")
                            e1_atk = (e1_atk - mana2)
                            print("Enemy attack is",e1_atk,".")
                            time.sleep(.5)
                            print(" ")
                        elif m_Burst2_to == 2:
                            print(Name2,"did a mana burst on the enemy's defense.")
                            e1_def = (e1_def - mana2)
                            print("Enemy defense is",e1_def,".")
                            time.sleep(.5)
                            print(" ")
                        else:
                            print(Name2,"did a mana burst on the enemy's speed.")
                            e1_spd = (e1_spd - mana2)
                            time.sleep(.5)
                            print(" ")
                            print("Enemy speed is",e1_spd,".")
                            time.sleep(.5)
                            print(" ")
                        m_Burst2_type = 8
                    elif clase2 == 9:
                        print(Name2,"did a merfolk mana burst!!")
                        time.sleep(.25)
                        print(" ")
                        print("Each turn the enemy loses .5 speed!")
                        m_Burst2_type = 9
                    elif clase2 == 10:
                        print(Name2,"did a shador mana burst!")
                        time.sleep(.5)
                        print(" ")
                        time.sleep(.5)
                        print(" ")
                        print("Effects of enemy mana are reversed!")
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_to = random.randint(1,3)
                        if m_Burst2_to == 1:
                            print(Name2,"did a mana burst on the enemy's attack.")
                            e1_atk = (e1_atk - mana2)
                            print("Enemy attack is",e1_atk,".")
                            time.sleep(.5)
                            print(" ")
                        elif m_Burst2_to == 2:
                            print(Name2,"did a mana burst on the enemy's defense.")
                            e1_def = (e1_def - mana2)
                            print("Enemy defense is",e1_def,".")
                            time.sleep(.5)
                            print(" ")
                        else:
                            print(Name2,"did a mana burst on the enemy's speed.")
                            e1_spd = (e1_spd - mana2)
                            time.sleep(.5)
                            print(" ")
                            print("Enemy speed is",e1_spd,".")
                            time.sleep(.5)
                            print(" ")
                        m_Burst2_type = 10
                    elif clase2 == 11:
                        print(Name2,"did a demon mana burst!")
                        time.sleep(.5)
                        print(" ")
                        print(Name2,"'s attack has been doubled!")
                        atk2 = (atk2 * 2)
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_type = 11
                    elif clase2 == 12:
                        print(Name2,"did an angel mana burst!")
                        time.sleep(.5)
                        print(" ")
                        print(Name2,"'s defense has been doubled!")
                        def2_ = (def2_ * 2)
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_type = 12
                    else:
                        print(Name2,"did a brawler mana burst!")
                        mana2 = (mana2 * 2.5)
                        time.sleep(.5)
                        print(" ")
                        m_Burst2_to = random.randint(1,3)
                        if m_Burst2_to == 1:
                            print(Name2,"did a mana burst on the enemy's attack.")
                            e1_atk = (e1_atk - mana2)
                            print("Enemy attack is",e1_atk,".")
                            time.sleep(.5)
                            print(" ")
                        elif m_Burst2_to == 2:
                            print(Name2,"did a mana burst on the enemy's defense.")
                            e1_def = (e1_def - mana2)
                            print("Enemy defense is",e1_def,".")
                            time.sleep(.5)
                            print(" ")
                        else:
                            print(Name2,"did a mana burst on the enemy's speed.")
                            e1_spd = (e1_spd - mana2)
                            time.sleep(.5)
                            print(" ")
                            print("Enemy speed is",e1_spd,".")
                            time.sleep(.5)
                            print(" ")
                            m_Burst2_type = 13
                    mana2 = 0
                elif mana2_to == 2:
                    atk2 = (atk2 + mana2)
                    print(Name2,"'s mana went to attack.")
                    time.sleep(.5)
                    print(" ")
                    print(Name2,"'s attack is now",atk2)
                    time.sleep(.5)
                    print(" ")
                elif mana2_to == 3:
                    def2_ = (def2_ + mana2)
                    print(Name2,"'s mana went to defense.")
                    time.sleep(.5)
                    print(" ")
                    print(Name2,"'s defense is now",def2_)
                    time.sleep(.5)
                    print(" ")
                else:
                    spd2 = (spd2 + mana2)
                    print(Name2,"'s mana went to speed.")
                    time.sleep(.5)
                    print(" ")
                    print(Name2,"'s speed is now",spd2) 
                true_turns = true_turns2
                mana2 = 0
                return[mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def rush_mode():
    print(" ")
    time.sleep(.25)
    y_or_n = int(input("Rush mode?! (fewer turns to win battles) 1 = yes 2 = no:"))
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    return(y_or_n)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def gameplay_ver():
    response1 = rush_mode()
    if response1 == 1:
        print(" ")
        time.sleep(.25)
        response2 = int(input("How many turns per battle?:"))
        os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    if response1 == 2:
        print(" ")
        time.sleep(.25)
        response2 = 99999
    return(response2)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def numb_of_turns():
    turns = gameplay_ver()
    return(turns)
def WaWrites_MyName(player,Name,color):
    wa = player
    wa.right(90)
    wa.forward(20)
    wa.left(90)
    wa.fillcolor(color)
    wa.forward(15)
    wa.write(Name)
    wa.back(15)
def WaErase_stats(player,position):
    wa = player
    wa.penup()
    wa.goto(position)
    wa.pendown()
    wa.color("black")
    wa.pensize(12)
    wa.forward(1000)
    wa.back(1000)
    wa.up()
    wa.goto(position)
def WaWrites_MyStats(player,color,atk,def_,spd,mana,position):
    wa = player
    WaErase_stats(player,position)
    wa.penup()
    wa.goto(position)
    wa.forward(10)
    wa.color(color)
    if atk > 0:
        wa.write("Attack:")
        wa.forward(30)
        wa.write(atk)
        wa.forward(60)
    if def_ > 0:
        wa.write("Defense:")
        wa.forward(60)
        wa.write(def_)
        wa.forward(30)
    if mana > 0:
        wa.write("Mana:")
        wa.forward(30)
        wa.write(mana)
        wa.forward(60)
    wa.goto(position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def get_class(crit_d,clase,atk,def_,spd,class_w,spd_2,atk_2,def_2,clase_str):
    print("These are the 13 choices, Knight(type1), Mage(type2) Giant(type3), Gunner(type4), Techster(type5), Healer(type6), Assassin(type7), Beast(type8), Merfolk(type9), Shador(type10), Demon(type11), Angel(type12), Brawler(type13)")
    print(" ")
    time.sleep(.25)
    clase = int(input("Choose a class:"))
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    if clase == 1:
        clase = 0
        print("So, a knight, got it!")
        print(" ")
        time.sleep(.25)
        atk = ((random.randint(1, 5)) + 5) / 2
        def_ = ((random.randint(3, 7)) + 7) / 2
        spd = ((random.randint(1, 5)) + 1) / 2
        en1_1_class_w = random.randint(11,12)
        crit_d = 1.5
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        clase_str = "knight"
    if clase == 2:
        class_w = float(10)
        print("So, a mage, got it!")
        print(" ")
        time.sleep(.25)
        atk = 4
        def_ = 3
        spd = 4
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        clase_str = "mage"
        crit_d = 1.5
    if clase == 3:
        print("So, a giant, got it!")
        clase_str = "giant"
        print(" ")
        time.sleep(.25)
        atk = ((random.randint(1, 5)) + 3) / 2
        def_ = ((random.randint(0, 5)) + 3) / 2
        spd = ((random.randint(2, 5)) + 6) / 2
        class_w = float(2)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 3
    if clase == 4:
        print("So, a gunner, got it!")
        clase_str = "gunner"
        print(" ")
        time.sleep(.25)
        atk = ((random.randint(1, 5)) + 5) / 2
        def_ = ((random.randint(1, 5)) + 2.5) / 2
        spd = ((random.randint(1, 5)) + 3) / 2
        class_w = float(3)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 2.6
    if clase == 5:
        print("So, a techster, got it!")
        print(" ")
        clase_str = "techster"
        time.sleep(.25)
        atk = ((random.randint(3, 5)) + 2) / 2
        def_ = ((random.randint(1, 5)) + 2) / 2
        spd = ((random.randint(0, 7)) + 7) / 2
        class_w = float(9)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 1.7
    if clase == 6:
        print("So, a healer, got it!")
        print(" ")
        clase_str = "healer"
        time.sleep(.25)
        atk = ((random.randint(2, 6)) + 0) / 2
        def_ = ((random.randint(1, 6)) + 6.5) / 2
        spd = ((random.randint(1, 5)) + 5) / 2
        class_w = float(5)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 4
    if clase == 7:
        print("So, an assassin, got it!")
        print(" ")
        clase_str = "assassin"
        time.sleep(.25)
        atk = ((random.randint(1, 6)) + 6) / 2
        def_ = ((random.randint(1, 4)) + 0) / 2
        spd = ((random.randint(1, 5)) + 5) / 2
        class_w = float(1)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 3
    if clase == 8:
        print("So, a beast, got it!")
        print(" ")
        clase_str = "beast"
        time.sleep(.25)
        atk = ((random.randint(1, 6)) + 5) / 2
        def_ = ((random.randint(1, 5)) + 2) / 2
        spd = ((random.randint(1, 4)) + 4) / 2
        class_w = float(4)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 2.5
    if clase == 9:
        class_w = float(8)
        print("So, a mefolk, got it!")
        clase_str = "merfolk"
        print(" ")
        time.sleep(.25)
        atk = ((random.randint(1, 5)) + 4) / 2
        def_ = ((random.randint(1, 5)) + 1) / 2
        spd = ((random.randint(1, 6)) + 6) / 2   
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 2
    if clase == 10:
        print("So, a shador, got it!")
        clase_str = "shador"
        print(" ")
        time.sleep(.25)
        atk = ((random.randint(2, 6)) + 6) / 2
        def_ = ((random.randint(1, 5)) + 2) / 2
        spd = ((random.randint(0, 5)) + 3) / 2
        class_w = float(7)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 2
    if clase == 11:
        print("So, a demon, got it!")
        print(" ")
        clase_str = "demon"
        time.sleep(.25)
        atk = ((random.randint(4, 9)) + 6) / 2
        def_ = ((random.randint(1, 5)) + 0) / 2
        spd = ((random.randint(2, 12)) + 0) / 2
        class_w = float(13)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 3
    if clase == 13:
        print("So, a brawler, cool!")
        print(" ")
        clase_str = "brawler"
        time.sleep(.25)
        atk = ((random.randint(0, 7)) + 7) / 2
        def_ = ((random.randint(1, 5)) + 5) / 2
        spd = ((random.randint(1, 5)) + 0) / 2
        class_w = float(6)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 2
    if clase == 12: 
        print("So, an angel, got it!")
        print(" ")
        clase_str = "angel"
        atk = ((random.randint(0, 7)) + 0) / 2
        def_ = ((random.randint(5, 10)) + 8) / 2
        spd = ((random.randint(1, 5)) + 4) / 2
        class_w = float(13)
        clase = float(12)
        print("And the stats are:", atk, "attack", def_, "defense", "and", spd, "speed")
        print(" ")
        time.sleep(.25)
        crit_d = 4
    spd_2 = spd
    atk_2 = atk
    def_2 = def_
    return[crit_d,clase,atk,def_,spd,class_w,spd_2,atk_2,def_2,clase_str]    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def get_enemy_class(en_1_class,en_1_class2,en1_1_class_w):
    en_1_class = random.randint(1, 13)
    if en_1_class == 1:
        en_1_class = ("knight")
        en_1_class2 = 1
        en1_1_class_w = random.randint(11,12)
    if en_1_class == 2:
        en_1_class = ("mage")
        en_1_class2 = 2
        en1_1_class_w = float(10)
    if en_1_class == 3:
        en_1_class = ("giant")
        en_1_class2 = 3
        en1_1_class_w = float(2)
    if en_1_class == 4:
        en_1_class = ("gunner")
        en_1_class2 = 4
        en1_1_class_w = float(3)
    if en_1_class == 5:
        en_1_class = ("techster")
        en_1_class2 = 5
        en1_1_class_w = float(9)
    if en_1_class == 6:
        en_1_class = ("healer")
        en_1_class2 = 6
        en1_1_class_w = float(5)
    if en_1_class == 7:
        en_1_class = ("assassin")
        en_1_class2 = 7
        en1_1_class_w = float(1)
    if en_1_class == 8:
        en_1_class = ("beast")
        en_1_class2 = 8
        en1_1_class_w = float(4)
    if en_1_class == 9:
        en_1_class = ("merfolk")
        en_1_class2 = 9
        en1_1_class_w = float(8)
    if en_1_class == 10:
        en_1_class = ("shador")
        en_1_class2 = 10
        en1_1_class_w = float(7)
    if en_1_class == 11:
        en_1_class = ("demon")
        en_1_class2 = 11
        en1_1_class_w = float(13)
    if en_1_class == 12:
        en_1_class = ("angel")
        en_1_class2 = 12
        en1_1_class_w = float(13)
    if en_1_class == 13:
        en_1_class = ("brawler")
        en_1_class2 = 13
        en1_1_class_w = float(6)
    return[en_1_class,en_1_class2,en1_1_class_w]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def get_enemy_stats(e1_atk,e1_def,e1_spd):
    e1_atk = random.randint(1,5)
    e1_def = random.randint(1,3)
    e1_spd = float(random.randint(1,5))
    return[e1_atk,e1_def,e1_spd]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Dance(wa):
    wa.penup()
    for all in range(4):
        wa.forward(30)
        time.sleep(.1)
        wa.backward(30)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Attack_sequence1(won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd):
    if e1_spd <= 0:
            won = "y"
    if won != "y":
        true_turns = (true_turns - 1)
        if e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
                if spd < 1 and def_ > e1_atk:
                    print("Your defense is too strong to break.")
                    print(" ")
                    time.sleep(.25)
                print("Opponent Turn.")
                print(" ")
                time.sleep(.25)
                spd = (spd - e1_atk/10)
                print("They attacked" " Your speed is now", spd, ".")
                print(" ")
                time.sleep(.25)
                print("You can attack now though")
                print(" ")
                time.sleep(.25)
                move = int(input("You or your partner(1 or 2):"))
                os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
                print(" ")
                time.sleep(.25)
                luck2 = random.randint(1,2)
                if move == 1:
                    if luck2 == 2:
                        print("The next attack is a critical hit!")
                        print(" ")
                        time.sleep(.25)
                        atk = (atk * crit_d)
                    e1_spd = (e1_spd - (atk/10))
                    print("Opponent speed is now", e1_spd, ".")
                    print(" ")
                    time.sleep(.25)
                    if luck2 == 2:
                            atk = (atk / crit_d)
                if move == 2:
                    if luck2 == 2:
                        print("The next attack is a critical hit!")
                        print(" ")
                        time.sleep(.25)
                        atk2 = (atk2 * crit_d2)
                    e1_spd = (e1_spd - (atk2/10))
                    print("Opponent speed is now", e1_spd, ".")
                    print(" ")
                    time.sleep(.25)
                    if luck2 == 2:
                        atk2 = (atk2 / crit_d2)
        return[won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd]
    else:
        return[won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
def Player_attack(crit_d3,crit_d2,crit_d,atk,atk2,atk3,e1_spd):
    print(" ")
    move = int(input("Who's attacking; you or your partner(1, 2 or 3):"))
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    print(" ")
    time.sleep(.25)
    luck2 = random.randint(1,2)
    if move == 1:
        if luck2 == 2:
            print("The next attack is a critical hit!")
            print(" ")
            time.sleep(.25)
            atk = (atk * crit_d)
        e1_spd = (e1_spd - (atk/10))
        print("Opponent speed is now", e1_spd, ".")
        print(" ")
        time.sleep(.25)
        if luck2 == 2:
                atk = (atk / crit_d)
    if move == 2:
        if luck2 == 2:
            print("The next attack is a critical hit!")
            print(" ")
            time.sleep(.25)
            atk2 = (atk2 * crit_d2)
        e1_spd = (e1_spd - (atk2/10))
        print("Opponent speed is now", e1_spd, ".")
        print(" ")
        time.sleep(.25)
        if luck2 == 2:
            atk2 = (atk2 / crit_d2)
    if move == 3:
        if luck2 == 2:
            print("The next attack is a critical hit!")
            print(" ")
            time.sleep(.25)
            atk3 = (atk3 * crit_d3)
        e1_spd = (e1_spd - (atk3/10))
        print("Opponent speed is now", e1_spd, ".")
        print(" ")
        time.sleep(.25)
        if luck2 == 2:
            atk3 = (atk3 / crit_d3)
    elif move > 3:
        time.sleep(.5)
        print("You missed...bruh.")
        print(" ")
    return[crit_d3,crit_d2,crit_d,atk,atk2,atk3,e1_spd]    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Draw_healthbars(position,wa,spd,color):
    if spd < 0:
        spd = 0
    wa.begin_fill()
    for all in range(2):
        wa.forward(spd * 30)
        wa.right(90)
        wa.forward(10)
        wa.right(90)
    wa.end_fill()
    wa.fillcolor(color)
    return(spd)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def WaErase(spd,player1_position,player_one):
    wa = player_one
    wa.penup()
    wa.goto(player1_position)
    wa.color("black")
    wa.down()
    wa.pensize(30)
    wa.forward(1000)
    wa.back(1000)
    return[spd,player1_position,player_one]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Draw_healthbars2(position,wa,spd,color):
    if spd < 0:
        spd = 0
    wa.penup()
    wa.goto(position)
    wa.fillcolor("maroon")
    Draw_healthbars(position,wa,spd,color)
    wa.penup()
    return(spd)
def True_healthbars(position,wa,spd,color,spd_3):
    if spd != spd_3:
        Draw_healthbars2(position,wa,spd,color)
        Draw_healthbars(position,wa,spd,color)
    return[position,wa,spd,color,spd_3]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def attack_who(spd,spd2,def2_,Name2,spd3,def3_,Name3,e1_atk):
    attack_who = random.randint(1,3)
    if attack_who == 1:
        spd = (spd - ( e1_atk/ 10))
        print("They attack you.")
        print(" ")
        time.sleep(.5)
        print("Your speed is now",spd,".")
    if attack_who == 2:
        if spd2 > 0 or def2_ > e1_atk:
            spd2 = (spd2 - (e1_atk / 10))
            print("They attack",Name2,".")
            print(" ")
            time.sleep(.5)
            print("Their speed is now",spd2,".")
        else:
            spd = (spd - (e1_atk / 10))
            print("They attack you.")
            print(" ")
            time.sleep(.5)
            print("Your speed is now",spd,".")
    elif attack_who == 3:
        if spd3 > 0 or def3_ > e1_atk:
            spd3 = (spd3 - (e1_atk / 10))
            print("They attack",Name3,".")
            print(" ")
            time.sleep(.5)
            print(Name3,"' speed is now",spd3,".")
        else:
            spd = (spd - (e1_atk / 10))
            print("They attack you.")
            print(" ")
            time.sleep(.5)
            print("Your speed is now",spd,".")
    return[spd,spd2,def2_,Name2,spd3,def3_,Name3,e1_atk]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Boss_weakness(atk,atk2,atk3,en1_1_class_w,BOSS_name,clase,clase2,clase3,Name2,Name3):
    if en1_1_class_w == clase:
        atk = (atk * 2)
        print(BOSS_name,"is a", en_1_class, ".")
        print(" ")
        time.sleep(.25)
        print("You deal double damage to",BOSS_name,"!")
        print(" ")
        time.sleep(.25)
    if en1_1_class_w == clase2:
        atk2 = (atk2 * 2)
        print(BOSS_name,"is a", en_1_class, ".")
        print(" ")
        time.sleep(.25)
        print(Name2, "deals double damage to",BOSS_name,"!")
        print(" ")
        time.sleep(.25)

    if en1_1_class_w == clase3:
        atk3 = (atk3 * 2)
        print(BOSS_name,"is a", en_1_class, ".")
        print(" ")
        time.sleep(.25)
        print(Name3, "deals double damage to",BOSS_name,"!")
        print(" ")
        time.sleep(.25)
    else:
        print(BOSS_name,"is a", en_1_class, ".")
        print(" ")
        time.sleep(.25)
    return[atk,atk2,atk3,en1_1_class_w,BOSS_name,clase,clase2,clase3,Name2,Name3]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3):
    if en1_1_class_w == clase:
        atk = (atk * 2)
        print(" ")
        time.sleep(.25)
        print("You deal double damage!")
        print(" ")
        time.sleep(.25)
    elif en1_1_class_w == clase2:
        atk2 = (atk2 * 2)
        print(" ")
        time.sleep(.25)
        print(Name2, "deals double damage!")
        print(" ")
        time.sleep(.25)
    elif en1_1_class_w == clase3:
        atk3 = (atk3 * 2)
        print(" ")
        time.sleep(.25)
        print(Name3, "deals double damage!")
        print(" ")
        time.sleep(.25)
    else:
        print(" ")
        time.sleep(.25)
    return[en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3):
    if en_1_class2 == class_w or en_1_class2 == class2_w2 or en_1_class2 == clase3_w:
        e1_atk = (e1_atk * 2)
        print("The enemy deals double damage")
        print(" ")
        time.sleep(.5)
        if en_1_class2 == class_w:
            print("The enemy is strong to you.")
            print(" ")
            time.sleep(.5)
        elif en_1_class2 == class2_w2:
            print("The enemy is strong to",Name2,".")
            print(" ")
            time.sleep(.5)
        else:
            print("The enemy is strong to",Name3,".")
            print(" ")
            time.sleep(.5)
    else:
        print("No one is weak to the enemy.")
        print(" ")
        time.sleep(.5)
    return[en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3]
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3):
    if e1_spd <= 0:
            won = "y"
    if won != "y":
        print("Enemy stats are:",e1_atk,"attack,",e1_def,"defense, and",e1_spd,"speed.")
        true_turns = true_turns - 1
        if e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
                if m_Burst_type == 9 or m_Burst2_type == 9 or m_Burst3_type == 9:
                    e1_spd = (e1_spd - .5)
                    print("Enemy lost .5 speed to merfolk mana burst.")
                    time.sleep(.5)
                    print(" ")
                    print("Enemy speed is now",e1_spd,".")
                if m_Burst_type == 3 or m_Burst2_type == 3 or m_Burst3_type == 3:
                    if m_Burst_type == 3:
                        spd = (spd + .5)
                        print("Your speed is now",spd,".")
                        time.sleep(.5)
                        print(" ")
                    if m_Burst2_type == 3:
                        spd2 = (spd2 + .5)
                        print(Name2,"'s speed is now",spd2,".")
                        time.sleep(.5)
                        print(" ")
                    if m_Burst3_type == 3:
                        spd3 = (spd3 + .5)
                        print(Name3,"'s speed is now",spd3,".")
                        time.sleep(.5)
                        print(" ")
                if m_Burst_type == 10 or m_Burst2_type == 10 or m_Burst3_type == 10:
                    e1_spd_beta = e1_spd_2 - e1_spd
                    if (e1_spd + e1_spd_beta) == (e1_spd_2 + e1_mana):
                        e1_spd = (e1_spd - e1_mana)
                        time.sleep(.5)
                        print(" ")
                        print("Enemy speed has been lowered and is now",e1_spd)
                        time.sleep(.5)
                        print(" ")
                        print("Enemy stats were returned due to shador mana burst.")
                    elif e1_atk == (e1_atk_2 + e1_mana):
                        e1_atk = (e1_atk - e1_mana)
                        time.sleep(.5)
                        print(" ")
                        print("Enemy attack has been lowered and is now",e1_atk)
                        time.sleep(.5)
                        print(" ")
                        print("Enemy stats were returned due to shador mana burst.")
                    elif e1_def == (e1_def_2 + e1_mana):
                        e1_def = (e1_def - e1_mana)
                        time.sleep(.5)
                        print(" ")
                        print("Enemy defense has been lowered and is now",e1_def)
                        time.sleep(.5)
                        print(" ")
                        print("Enemy stats were returned due to shador mana burst.")
                    else:
                        time.sleep(.5)
                        print(" ")
                        print("There was nothing to return.")
                if spd < 1 and def_ > e1_atk:
                    print("Your defense is too strong to break.")
                    print(" ")
                    time.sleep(.5)
                print("Enemy turn.")
                print(" ")
                time.sleep(.5)
                [spd,spd2,def2_,Name2,spd3,def3_,Name3,e1_atk] = attack_who(spd,spd2,def2_,Name2,spd3,def3_,Name3,e1_atk)    
                print("It's your turn now.")
                print(" ")
                time.sleep(.5)
                print("Will you attack, use mana, or use an effect?")
                print(" ")
                time.sleep(.5)
                choiceA = int(input("(1 = attack 2 = use mana 3 = use effect):"))
                os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
                if choiceA == 1:
                    print(" ")
                    time.sleep(.5)
                    print("1 = you. 2 =",Name2,"3 =",Name3)
                    move = int(input("You or your partner(1 2, or 3):"))
                    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
                    print(" ")
                    time.sleep(.5)
                    luck2 = random.randint(1,2)
                    if move == 1:
                        if luck2 == 2:
                            print("The next attack is a critical hit!")
                            print(" ")
                            time.sleep(.5)
                            atk = (atk * crit_d)
                        e1_spd = (e1_spd - (atk/10))
                        print("Opponent speed is now", e1_spd, ".")
                        print(" ")
                        time.sleep(.5)
                        if luck2 == 2:
                                atk = (atk / crit_d)
                    elif move == 2:
                        if luck2 == 2:
                            print("The next attack is a critical hit!")
                            print(" ")
                            time.sleep(.5)
                            atk2 = (atk2 * crit_d2)
                        e1_spd = (e1_spd - (atk2/10))
                        print("Opponent speed is now", e1_spd, ".")
                        print(" ")
                        time.sleep(.5)
                        if luck2 == 2:
                            atk2 = (atk2 / crit_d2)
                    elif move == 3:
                        if luck2 == 2:
                            print("The next attack is a critical hit!")
                            print(" ")
                            time.sleep(.5)
                            atk3 = (atk3 * crit_d3)
                        e1_spd = (e1_spd - (atk3/10))
                        print("Opponent speed is now",e1_spd,".")
                        print(" ")
                        time.sleep(.5)
                        if luck2 == 2:
                            atk3 = (atk3 / crit_d3)
                    elif move > 3:
                        print("You missed...bruh")
                elif choiceA == 2:
                    print(" ")
                    time.sleep(.5)
                    manaSet = int(input("Mana Burst(1), Equip mana to speed(2), Equip Mana to attack(3), Equip mana to defense(4):"))
                    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
                    if mana > 0:
                        if manaSet == 1:
                            if spd < 2:
                                mana = (mana * 2)
                            print(" ")
                            time.sleep(.5)
                            if clase == 2:
                                if mana > 0:
                                    print("Mages can't do mana bursts silly.")
                                    time.sleep(.5)
                                    print(" ")
                                else:
                                    print("You're out of mana.")
                            elif clase == 4:
                                if mana > 0:
                                    atk = (atk + 8)
                                    print("Gunner mana burst: attack is now +8. New attack value: ",atk)
                                    time.sleep(.5)
                                    print(" ")
                                    mana = 0
                                else:
                                    print("You're out of mana.")
                            elif clase == 6:
                                if mana > 0:
                                    print("Healer mana burst.")
                                    time.sleep(.5)
                                    print(" ")
                                    print("Your team's speed just got increased!")
                                    spd = (spd + 10)
                                    spd2 = (spd2 + 5)
                                    time.sleep(.5)
                                    print(" ")
                                    print(Name2,"'s speed is now",spd2,".")
                                    spd3 = (spd3 + 5)
                                    time.sleep(.5)
                                    print(" ")
                                    print(Name3,"'s speed is now",spd3,".")
                                    time.sleep(.5)
                                    print(" ")
                                    print("Your speed is now",spd,".")
                                    mana = 0
                                else:
                                    print("You're out of mana.")
                            elif clase == 7:
                                if mana > 0:
                                    e1_spd = (e1_spd / 2)
                                    print("Assassin mana burst. Enemy speed is now",e1_spd,".")
                                    time.sleep(.5)
                                    print(" ")
                                else:
                                    print("You're out of mana.")
                            elif clase == 9:
                                if mana > 0:
                                    print("Merfolk mana burst.")
                                    time.sleep(.5)
                                    print(" ")
                                    print("Each turn the enemy loses .5 speed")
                                    time.sleep(.5)
                                    print(" ")
                                    m_Burst_type = 9
                                else:
                                    print("You're out of mana.")
                            elif clase == 11:
                                if mana > 0:
                                    print("Demon mana burst; attack is doubled.")
                                    time.sleep(.5)
                                    print(" ")
                                    atk = (atk * 2)
                                    print("Attack is: ",atk)
                                    time.sleep(.5)
                                    print(" ")
                                    m_Burst_type = 11
                                else:
                                    print("You're out of mana.")
                            elif clase == 12:
                                if mana > 0:
                                    print("Angel mana burst; defense is doubled.")
                                    time.sleep(.5)
                                    print(" ")
                                    def_ = (def_ * 2)
                                    print("Defense is: ",def_)
                                    time.sleep(.5)
                                    print(" ")
                                    m_Burst_type = 12
                                else:
                                    print("You're out of mana.")
                                
                                    
                            else:
                                M_Burst = int(input("Mana Burst on what? (Enemy Attack = 1 Enemy Defense = 2 Enemy Speed = 3):"))
                                os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
                                if M_Burst == 1:
                                    if mana < 1:
                                        print("You're out of mana.")
                                    e1_atk = (e1_atk - mana)
                                    time.sleep(.5)
                                    print(" ")
                                    print("Enemy attack is now",e1_atk,".")
                                elif M_Burst == 2:
                                    if mana < 1:
                                        print("You're out of mana.")
                                    e1_def = (e1_def - mana)
                                    time.sleep(.5)
                                    print(" ")
                                    print("Enemy defense is now",e1_def,".")
                                elif M_Burst == 3:
                                    if mana < 1:
                                        print("You're out of mana.")
                                    e1_spd = (e1_spd - mana)
                                    time.sleep(.5)
                                    print(" ")
                                    print("Enemy speed is now",e1_spd,".")
                                if clase == 10:
                                    if mana > 0:
                                        print("Effects of enemy mana have been reversed!")
                                        time.sleep(.5)
                                        print(" ")
                                        mana = 0
                                        m_Burst_type = 10
                                    else:
                                        print("You're out of mana.")
                                if clase == 5:
                                    if mana > 0:
                                        if e1_spd > 0:
                                            print("You took the chance, and you attacked!")
                                            time.sleep(.5)
                                            print(" ")
                                            e1_spd = (e1_spd - (atk/10))
                                        time.sleep(.5)
                                        print(" ")
                                        print("Enemy speed is now",e1_spd,".")
                                        time.sleep(.5)
                                        print(" ")
                                        mana = 0
                                    else:
                                        print("You're out of mana.")
                                        
                                if clase == 3:
                                    if mana > 0:
                                        print("You now have regen!")
                                        time.sleep(.5)
                                        print(" ")
                                        mana = 0
                                    else:
                                        print("You're out of mana.")
                        elif manaSet == 2:
                            spd = (spd + mana)
                            print(" ")
                            time.sleep(.5)
                            print("Your speed is now",spd,".")
                            mana = 0
                        elif manaSet == 3:
                            atk = (atk + mana)
                            print(" ")
                            time.sleep(.5)
                            print("Your attack is now",atk,".")
                            mana = 0
                        elif manaSet == 4:
                            def_ = (def_ + mana)
                            print(" ")
                            time.sleep(.5)
                            print("Your defense is now",def_,".")
                        mana = 0
                    else:
                        print("You're out of mana.")
                elif choiceA == 3:
                    if cards > 0:
                        card_selection = random.randint(1,3)
                        if card_selection == 1:
                            time.sleep(.5)
                            print("You drank mana water!")
                            print(" ")
                            mana = mana_2
                            print("Mana is now",mana,".")
                        elif card_selection == 2:
                            taps = (taps + 1)
                            time.sleep(.5)
                            print("Double-tap:")
                            print(" ")
                            time.sleep(.5)
                            print("You can attack twice per turn now!")
                            print(" ")
                        elif card_selection == 3:
                            time.sleep(.5)
                            print("You got nothing...")
                            print(" ")
                        cards = (cards - 1)
                    else:
                        time.sleep(.5)
                        print("You're out of cards.")
                        print(" ")
                else:
                    time.sleep(.5)
                    print("You skipped your turn.")
                    print(" ")
        if card_selection == 2:
            if taps >= 3:
                    taps = 3
            for all in range(taps):
                [crit_d3,crit_d2,crit_d,atk,atk2,atk3,e1_spd] = Player_attack(crit_d3,crit_d2,crit_d,atk,atk2,atk3,e1_spd)
        return[won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3]
    else:
        return[won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3]            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#               
def Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk):
    deaths2 = 1
    time.sleep(.5)
    print(" ")
    if spd2 <= 0 and def2_ < e1_atk:
        time.sleep(.5)
        print(" ")
        atk2 = 0
        def2_ = 0
        print(Name2,"isn't alive, but they can be revived.")
        time.sleep(.5)
        print(" ")
        print(Name2,"'s stats are now",atk2,"attack,",def2_,"defense, and",spd2,"speed.")
    elif spd2 < 0 and def2_ > e1_atk:
        deaths2 = 3
        print(Name2,"is alive.")
        print(Name2,"'s stats are now",atk2,"attack,",def2_,"defense, and",spd2,"speed.")
    elif spd2 > 0 and def2_ != 0:
        deaths2 = 3
        print(Name2,"is alive.")
        print(Name2,"'s stats are now",atk2,"attack,",def2_,"defense, and",spd2,"speed.")
    elif spd2 > 0 and deaths2 == 1:
        time.sleep(.5)
        print(" ")
        atk2 = atk2_2
        def2_ = def2_2
        print(Name2,"has been revived!")
        print(Name2,"'s stats are now",atk2,"attack,",def2_,"defense, and",spd2,"speed.")
       
    return[deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk]
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def WINNER(wins,Continue,true_turns):
    wins2 = wins
    if e1_spd <= 0:
        if atk >= e1_def or atk2 >= e1_def or atk3 >= e1_def:
            print("You won!!")
            wins += 1
            time.sleep(.5)
    if e1_spd > 0:
        print("You lost.")
        if true_turns == 0:
            time.sleep(.75)
            print(" ")
            print("You ran out of turns.")
            print(" ")
    if e1_def > atk and e1_def > atk2 and e1_def > atk3:
        print("Attack =",atk)
        print(" ")
        time.sleep(.5)
        print("Ally attack =",atk2)
        print(" ")
        time.sleep(.5)
        if atk > 0:
            print("Other ally attack =",atk3)
            print(" ")
            time.sleep(.5)
        print("Enemy defense =",e1_def)
        print(" ")
        time.sleep(.5)
        print("You lost; their defense is too high to break.")
        if true_turns == 0:
            time.sleep(.75)
            print(" ")
            print("You ran out of turns.")
            print(" ")
    if wins > wins2:
        time.sleep(.7)
        print(" ")
        Continue = int(input("Continue? 1 = yes 2 = no: "))
        os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    else:
        print(" ")
        time.sleep(.5)
        print("GAME OVER.")
        time.sleep(999999999)#<---Error Boi is back again!
        while 3 > 1:
            print("ERROR")
    return[wins,Continue,true_turns]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#           
def Story_time2(Name,Name2,Name3,BOSS_name,spd2,def2_,player3_position,player_3,color3,spd3,def3_,e1_atk):
    print("Press \"Enter\" to advance diolouge.")
    print(" ")
    input(" ")
    if spd3 > 0 or def3_ > e1_atk:
        print(Name3,": We won!!")
        Dance(player_3)
        print(" ")
        input(" ")
    if spd2 > 0 or def2_ > e1_atk:
        print(Name2,": Yeah, guess we did that!")
        print(" ")
        input(" ")
    print(Name,": Yeah, we won. We beat you Kimbley, fairly.")
    print(" ")
    input(" ")
    print(BOSS_name,": You expect me to agree to that?")
    print(" ")
    input(" ")
    print(BOSS_name,": I was going easy on you punks.")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": Oh, hi Kimbley. What an unpleasant surprise it is to see you...")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,": Oh, h-hey Krystal... It's been a while hasn't it?...")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": Oh, shut up Kimbley! I don't have time listen to your idiocy right now.")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": That's what I thought.")
    print(" ")
    input(" ")
    print(BOSS_name,": Kimbley, what did I tell you about picking on the children?")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    time.sleep(.3)
    print(BOSS_name,": You said don-")
    print(" ")
    time.sleep(.3)
    BOSS_name = "Krystal"
    print(BOSS_name,": Exactly, I said don't.")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": So, tell me Kimbley, why are you hurting these poor little children?")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": What did they do to hurt you Kimbley?")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": That's what I thought.")
    print(" ")
    input(" ")
    print(BOSS_name,": Kimbley, you idiot, look at where your arrogance has gotten you.")
    print(" ")
    input(" ")
    print(BOSS_name,": You lost to these children...")
    print(" ")
    input(" ")
    print(BOSS_name,": ...the children which I told YOU PERSONALLY not to fight...")
    print(" ")
    input(" ")
    print(BOSS_name,": ...and you, being as unintelligent as you are challenged them anyway, and lost.")
    print(" ")
    input(" ")
    print(BOSS_name,": I told you already, DON'T start fights unless you KNOW you'll win.")
    print(" ")
    input(" ")
    print(BOSS_name,": I also told you DO NOT pick fights with CHILDREN.")
    print(" ")
    input(" ")
    print(BOSS_name,": But here you are.")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,": Kimbley at times like these, I wonder why I even bother with you.")
    print(" ")
    input(" ")
    print(BOSS_name,": ...Oh yeah, now I remember...")
    print(" ")
    input(" ")
    print(BOSS_name,": It was back in high school...")
    print(" ")
    input(" ")
    print(BOSS_name,": ...")
    print(" ")
    input(" ")
    print(BOSS_name,": *laughs*...when you asked me for help with your Science homework...")
    print(" ")
    input(" ")
    print(BOSS_name,": ...and, those muscles of yours took me by surprise.")
    print(" ") 
    input(" ")
    print(BOSS_name,": Not much has changed since then.")
    print(" ")
    input(" ")
    print(BOSS_name,": Anyway, sorry for that, kids. I can promise you Kimbley will never hurt you guys from this moment forward.")
    print(" ")
    input(" ")
    print(BOSS_name,": *agressively tugs on Kimbley's ear* Isn't that right Kimbley.")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,": Ow, yeah sure. Just, let go of my ear; that hurts.")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": My name is Krystal: The Fine, primary boss of the Zuza clan.")
    print(" ")
    input(" ")
    print(BOSS_name,": If you kids ever need help, you can just give me a call...")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,": Just know I'll be mad if a certain someone's is why you're calling...")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    BOSS_name = "Krystal"
    print(BOSS_name,": *pierces Kimbley's skin with her eyballs* Oh, you've gone so silent, Kimbley.")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,": We'll be on our way now. Come on dear.")
    print(" ")
    input(" ")
    BOSS_name = "Kimbley"
    print(BOSS_name,": I'm coming...")
    print(" ")
    input(" ")
    print("*Kimbley and Krystal vanish...*")
    print(" ")
    input(" ")
    return[Name,Name2,Name3,BOSS_name,spd2,def2_,player3_position,player_3,color3,spd3,def3_,e1_spd]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Story_time3(Name,Name2,Name3,BOSS_name,spd,def3_,player1_position,player_one,color,spd3,def_,e1_spd,spd2,def2_):
    BOSS_name = "Zane"
    print("Press \"Enter\" to advance diolouge.")
    print(" ")
    input(" ")
    print(Name,": Alright", BOSS_name,", why did you attack us?")
    print(" ")
    input(" ")
    print(BOSS_name,": I had to to protect the Zuza Clan.")
    print(" ")
    input(" ")
    if spd3 > 0 or def3_ > .7:
        print(Name3,": You attacked us to protect the Zuza Clan, but why?")
        print(" ")
        input(" ")
    print(BOSS_name,": Here's why:")
    print(" ")
    input(" ")
    print(BOSS_name,":")
    print(" ")
    input(" ")
    print(BOSS_name,":")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,": What, you thought I was actually going to say why?")
    print(" ")
    input(" ")
    print(Name,": You owe us that much for losing to us; by law you're now my war prisoner.")
    print(" ")
    input(" ")
    print(BOSS_name,":... WAIT... You can't be serious!?!")
    print(" ")
    input(" ")
    print(Name2,": Don't act like you don't know the law of Acirema...")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print(BOSS_name,":...")
    print(" ")
    input(" ")
    print("*Zane starts running away*")
    print(" ")
    input(" ")
    if spd3 > 0 or def3_ > .7:
        print(Name3,": Hey, wait, we weren't going to hurt you.")
        print(" ")
        input(" ")
        print(Name3,": *Looks at you*")
        print(" ")
        input(" ")
        print(Name3,": Right",Name,"?")
        print(" ")
        input(" ")
        print(Name,": Of course not...")
        print(" ")
        input(" ")
    print(Name,":... but now we have to catch h-.")
    print(" ")
    input(" ")
    BOSS_name = "Sal"
    print(BOSS_name,":-Oh, no you don't!")
    print(" ")
    input(" ")
    capsName = Name.upper()
    print(BOSS_name,":",capsName,"!! I'm not done with YOU yet!")
    print(" ")
    input(" ")
    if spd2 > 0 or def2_ > .7:
        cutName = Name[:5]
        print(Name2,": What did",cutName,"-")
        print(" ")
        input(" ")
    print(BOSS_name,"attacked you!")
    Draw_healthbars2(player1_position,player_one,spd,color)
    Draw_healthbars(player1_position,player_one,spd2,color)
    WaWrites_MyName(player_one,Name,color)
    WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
    spd -= .7
    Draw_healthbars2(player1_position,player_one,spd,color)
    Draw_healthbars(player1_position,player_one,spd,color)
    WaWrites_MyName(player_one,Name,color)
    WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
    print(" ")
    input(" ")
    print("Your speed is now:",spd,".")
    print(" ")
    input(" ")
    print(BOSS_name,":-EVERYTHING!")
    print(" ")
    input(" ")
    print(BOSS_name,":",capsName,"is the one threat of the Zuza Clan...")
    print(" ")
    input(" ")
    print(BOSS_name,": ...and if killing",capsName,"is the only thing that keeps the Zuza Clan from safety....")
    print(" ")
    input(" ")
    print(BOSS_name,": ...")
    print(" ")
    input(" ")
    print(BOSS_name,": *attempts to attack you, but you dodge*")
    print(" ")
    input(" ")
    print(BOSS_name,": THEN, I CHALLENGE YOU",capsName,"!")
    print(" ")
    input(" ")
    print(BOSS_name,": Good luck!")
    print(" ")
    input(" ")
    return[Name,Name2,Name3,BOSS_name,spd,def3_,player1_position,player_one,color,spd3,def_,e1_spd,spd2,def2_]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
def story_time1(Name,Name2,Name3,BOSS_name,spd2,player2_position,player_two,color2,atk2,def2_,e1_spd):
    e1_atk = 10
    print("(Press \"Enter\" to advance diologue)")
    print(" ")
    input(" ")
    print("Congratulations, you got through the tutorial!")
    print(" ")
    input(" ")
    print("Now the story can begin...")
    print(" ")
    input(" ")
    print("Once upon a time, there was a planet named Acirema.")
    print(" ")
    input(" ")
    print("The planet of Acirema was founded the year 2040 after finally gaining independence from Earth, more-so America.")
    print(" ")
    input(" ")
    print("Acirema wins the war, but, sadly, in year 2045, just five years later, another war epupts: The Aciremian Civil War.")
    print(" ")
    input(" ")
    print("The Aciremian Civil War was fought between the Savokist and the Munkist parties.")
    print(" ")
    input(" ")
    print("The Savokist party favored Science and Mathematics in schools, while the Munkist party favored History and English in schools.")
    print(" ")
    input(" ")
    print("The two opposing views, as well as a lack of central government resulted in the Aciremian Civil War")
    print(" ")
    input(" ")
    print("On this planet, Acirema, however, there were 12 mighty dieties called the Zodiac.")
    print(" ")
    input(" ")
    print("These warriors unlocked and harnessed the magical power of the planet Acierema, and saved the planet from the Aciremian Civil War.")
    print(" ")
    input(" ")
    print("Upon unlocking unlimited magic, the mighty Zodiac decided to add learing these god-like powers to the schools of Acirema.")
    print(" ")
    input(" ")
    print("The Zodiac also organized the magical planet of Acirema into city-states and clans to keep from another civil war.")
    print(" ")
    input(" ")
    print("Soon, you come in...")
    print(" ")
    input(" ")
    print("In the year 2090",Name,"the mighty warrior of Acirema begain the journey of their life.")
    print(" ")
    input(" ")
    print(Name2,": *gasps* ",Name,"! It's been a while.")
    print(" ")
    input(" ")
    print(Name,": I know, it's been two years since we last talked.")
    print(" ")
    input(" ")
    print(Name2,": Yeah, since middle school.")
    print(" ")
    input(" ")
    print(Name2,": So, how has life been since then?")
    print(" ")
    text = input("(Type a response to be used later):")
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    input(" ")
    print(Name2,": It is good you let me know life has been",text,".")
    print(" ")
    input(" ")
    print(Name,": How are you?")
    print(" ")
    input(" ")
    print(Name2,": I am good! I just mastered my mana burst!")
    print(" ")
    input(" ")
    print(Name,": What's that???")
    print(" ")
    input(" ")
    print(Name2,":",Name,"what's that, you're kidding?")
    print(" ")
    input(" ")
    print(Name,": No, seriously, what's that?")
    print(" ")
    input(" ")
    print(Name2,": You really don't know, how did you not die by now?")
    print(" ")
    input(" ")
    print(Name2,": A mana burst is when the user takes all of their mana")
    print(" ")
    input(" ")
    print(Name2,": and releases it, usually in the form of GIANT EXPLOSION")
    print(" ")
    input(" ")
    print(Name2,": ,you mean you haven't heard of THAT!?!")
    print(" ")
    text = input("(Type response here): ")
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    input(" ")
    print(" ")
    print(Name2,": ...",text,"?")
    input(" ")
    print(Name2,": *laughs* Classic",Name,".")
    print(" ")
    input(" ")
    print(Name,": Wait, so am I going to learn what a mana burst is or what?")
    print(" ")
    input(" ")
    print(Name2,": It's a bit too late for that now.")
    print(" ")
    input(" ")
    print(Name2,": You should've learned already. Teaching you now would be impossible.")
    print(" ")
    input(" ")
    print(Name,": ...But, you said \"how did you not die by now?\"")
    print(" ")
    input(" ")
    print(Name,": Isn't it safe to assume that learning to do mana bursts is important?")
    print(" ")
    input(" ")
    print(Name,": From what you have told me, using a mana burst can save my life")
    print(" ")
    input(" ")
    print(Name,": So, shouldn't you teach me.")
    print(" ")
    input(" ")
    print(Name2,": I would...")
    print(" ")
    input(" ")
    print(Name2,": ...")
    print(" ")
    input(" ")
    print(Name2,": ... but I can't")
    print(" ")
    input(" ")
    print(Name,": What do you mean?")
    print(" ")
    input(" ")
    print(Name2,": Learning how to do a mana burst, it takes a certain will.")
    print(" ")
    input(" ")
    print(Name2,": I can't tell you all that much about it, but I can say this, it costs a lot,")
    print(" ")
    input(" ")
    print(Name2,": and I'm not just talking about mana, it takes hormones to activate.")
    print(" ")
    input(" ")
    print(Name2,": For example, you need dopamine to even attempt a mana burst, and adrenaline helps get the mana through your veins faster.")
    print(" ")
    input(" ")
    print(Name2,": To do a mana burst, the time has to be right, and you have to \"feel\" the mana burst.")
    print(" ")
    input(" ")
    Dance(player_two)
    print(Name2,": It's a bit of a weird feeling, honestly.")
    print(" ")
    input(" ")
    print(Name,": Okay, but what exactly is a mana burst?")
    print(" ")
    input(" ")
    print(Name2,": It is when you take all of your mana and release it.")
    print(" ")
    input(" ")
    print(Name,": So, is it not like using it normally?")
    print(" ")
    input(" ")
    print(Name2,": No, it's very different; when you do a mana burst, there's more that comes with it that doesn't come from simply 'applying you mana to your abilities'.")
    print(" ")
    input(" ")
    print(Name,": Different how?")
    print(" ")
    input(" ")
    print(Name2,": Seriously",Name,"you were born on this planet right, how do you NOT know this?")
    print(" ")
    input(" ")
    print(Name2,": For example, giants become nearly invincible, and shadors reverse mana effects.")
    print(" ")
    input(" ")
    print(Name2,": You know about those right?")
    print(" ")
    input(" ")
    text =input("(Please type a response here.): ")
    print(" ")
    input(" ")
    print(Name2,": \"",text,"\"")
    print(" ")
    input(" ")
    print(Name2,": You know what,",Name," It doesn't even matter.")
    print(" ")
    input(" ")
    print(Name2,": I'll tell you what I can about mana bursts.")
    print(" ")
    input(" ")
    print(Name2,": Each warrior has an exclusive variant of mana burst, each of wh-")
    print(" ")
    time.sleep(.2)
    print("Unknown Boss: -Well, what do we have here, a couple of runts?...")
    print(" ")
    input(" ")
    print(Name2,": Come on; I was just about to teach",Name,"about what a mana burst is.")
    print(" ")
    input(" ")
    print("Unknown Boss: *mumbled* These guys are a bit more runt than I thought...")
    print(" ")
    input(" ")
    print(Name2,": Hey, are you even listening!?!")
    print(" ")
    input(" ")
    print("SLASH!!")
    print(" ")
    input(" ")
    print(Name2,"lost 1 speed! That was a strong attack!")
    print(" ")
    WaErase(spd2,player2_position,player_two)
    Draw_healthbars2(player2_position,player_two,spd2,color2)
    Draw_healthbars(player2_position,player_two,spd2,color2)
    WaWrites_MyName(player_two,Name2,color2)
    WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
    input(" ")
    spd2 = (spd2 - 1)
    print(Name2,"'s speed is now",spd2)
    print(" ")
    input(" ")
    print("Unknown Boss: See, Kimbley does what he wants, and what runts want doesn't matter much to Kimbley.")
    print(" ")
    input(" ")
    print(Name2,"attempted to attack Kimbley, but",Name2, "missed.")
    print(" ")
    input(" ")
    print(BOSS_name,": DID YOU JUST ATTACK KIMBLEY THE BIG!!??!!")
    print(" ")
    input(" ")
    print(BOSS_name,": Do you know what happens when you attack Kimbley?")
    print(" ")
    input(" ")
    print("...")
    print(" ")
    input(" ")
    print("...")
    print(" ")
    input(" ")
    print("SLASH! SLASH!")
    print(" ")
    input(" ")
    WaErase(spd2,player2_position,player_two)
    Draw_healthbars2(player2_position,player_two,spd2,color2)
    spd2 = (spd2 - 2)
    Draw_healthbars(player2_position,player_two,spd2,color2)
    WaWrites_MyName(player_two,Name2,color2)
    WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
    Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
    time.sleep(.5)
    print(" ")
    print(Name,": Looks like I don't have much of a choice here.")
    print(" ")
    input(" ")
    print("You challenged Zuza Boss Kimbley!")
    print(" ")
    input(" ")
    print(BOSS_name,": I'm in a generous mood today.")
    print(" ")
    input(" ")
    print(BOSS_name,":  *throws a person at you*")
    print(" ")
    input(" ")
    print(BOSS_name,":  You're a couple of runts... or maybe just one runt...")
    print(" ")
    input(" ")
    print(BOSS_name,":  ... I don't think your friend is doing so hot over there...")
    print(" ")
    input(" ")
    print(BOSS_name,": Now, you're a trio of runts. You can say you're the Legion Against Evil or whatever.")
    print(" ")
    input(" ")
    print(BOSS_name,": The person I just gifted you used to be my war prisoner, but I'm setting them free...")
    print(" ")
    input(" ")
    print(BOSS_name,": ...that is of coarse if you can beat ME.")
    print(" ")
    input(" ")
    print(BOSS_name,":  KIMBLEY THE BIG OF THE ZUZA CLAN ACCEPTS YOUR CHALLENGE!!!")
    print(" ")
    name_choice = random.randint(1,13)
    if name_choice == 1:
        Name3 = "Karly"
    elif name_choice == 2:
        Name3 = "James"
    elif name_choice == 3:
        Name3 = "Jessie"
    elif name_choice == 4:
        Name3 = "Mike"
    elif name_choice == 5:
        Name3 = "Tina"
    elif name_choice == 6:
        Name3 = "Sam"
    elif name_choice == 7:
        Name3 = "Alex"
    elif name_choice == 8:
        Name3 = "Christian"
    elif name_choice == 9:
        Name3 = "Jackie"
    elif name_choice == 10:
        Name3 = "Robin"
    elif name_choice == 11:
        Name3 = "Zaye"
    elif name_choice == 12:
        Name3 = "Zoe"
    else:
        Name3 = "Eli"
    input(" ")
    print(BOSS_name,": Really hope it was worth it",Name3,", your freedom and all...")
    print(" ")
    input(" ")
    
    return[Name,Name2,Name3,BOSS_name,spd2,player2_position,player_two,color2,atk2,def2_,e1_spd]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2):
    en_mana_to = random.randint(1,3)
    if en_mana_to == 1:
        e1_atk += (e1_mana)
        print(" ")
        time.sleep(.5)
        print("Enemy mana went to attack.")
        print(" ")
        time.sleep(.5)
        print("Enemy attack is now",e1_atk,".")
    elif en_mana_to == 2:
        e1_def += (e1_mana)
        print(" ")
        time.sleep(.5)
        print("Enemy mana went to defense.")
        print(" ")
        time.sleep(.5)
        print("Enemy defense is now",e1_def,".")
    else:
        e1_spd += (e1_mana)
        print(" ")
        time.sleep(.5)
        print("Enemy mana went to speed.")
        print(" ")
        time.sleep(.5)
        print("Enemy speed is now",e1_spd,".")
    return[e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2]   
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Not_So_Secret_Code(Name2,atk,atk2,def2_,atk2_2):
    FiveNineCounter = 0
    if Name2[-2:] == "59":
        print(" ")
        print("Code activated.")
        print(" ")
        for fiftynines in Name2:
            if fiftynines == "5":
                FiveNineCounter += .5
                Name2 = Name2[:-1]
            if fiftynines == "9":
                FiveNineCounter += .5
                Name2 = Name2[:-1]
        atk2 +=int((FiveNineCounter) + 2)
        atk2_2 += int(FiveNineCounter)
        print("CODE #:",atk,atk2,def2_,atk2_2)
    return[Name2,atk,atk2,def2_,atk2_2]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Battle_Text1(e1_spd,enemy_name):
    Battle_text = random.randint(1,3)
    if enemy_name == "Zane":
        text1 = "You guys are no match for me!"
        text2 = "After I beat you guys, I'll be a boss!"
        text3 = "I'll pound each of you into the ground."
        text4 = "This is more fun than I expected!"
        text5 = "You can't take me down."
        text6 = "I'll still pound each of you into the ground."
        text7 = "Just... die already..."
    elif enemy_name == "Sal":
        text1 = "You're dead."
        text2 = "The Zuza Clan is all I know; I'll defend it with my life!"
        text3 = "You guys are filty rats: nothing but contagious garbage."
        text4 = "Oh, now you're really dead!!"
        text5 = "I won't let you rodents plague the Zuza Clan"
        text6 = "If I let you win here, it's the end for everyone. I WON'T LET THAT HAPPEN!"
        text7 = "No..."
    if e1_spd > 3:
        if Battle_text == 1:
            print(" ")
            print(enemy_name,":",text1)
            time.sleep(.5)
        elif Battle_text == 2:
            print(" ")
            print(enemy_name,":",text2)
            time.sleep(.5)
        else:
            print(" ")
            print(enemy_name,":",text3)
            time.sleep(.5)
    elif e1_spd <= 3 and e1_spd > 1:
         if Battle_text == 1:
            print(" ")
            print(enemy_name,":",text4)
            time.sleep(.5)
         elif Battle_text == 2:
            print(" ")
            print(enemy_name,":",text5)
            time.sleep(.5)
         else:
            print(" ")
            print(enemy_name,":",text6)
            time.sleep(.5)
    else:
        print(" ")
        print(enemy_name,":",text7)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def EXP_points(Name,atk,def_,spd,mana,atk_2,def_2,spd_2,mana_2,Name2,atk2,def2_,spd2,mana2,atk2_2,def2_2,spd2_2,mana2_2,Name3,atk3,def3_,spd3,mana3,atk3_2,def3_2,spd3_2,mana3_2,cards):
    exp_pts = 9
    time.sleep(.5)
    print(" ")
    print(" 1 = add exp to mana.","\n", " 2 = add exp to attack.","\n"," 3 = add exp to speed.","\n", " 4 = add exp to defense.","\n", " 5 = add exp to effect cards (you probably don't want this one).")
    print(" ")
    print(" 6 = add exp to",Name2,",s mana.","\n", " 7 = add exp to",Name2,"'s attack.","\n", " 8 = add exp to",Name2,"'s speed.","\n", " 9 = add exp to",Name2,"'s defense.")
    print(" ")
    print(" 10 = add exp to",Name3,",s mana.","\n", " 11 = add exp to",Name3,"'s attack.","\n", " 12 = add exp to",Name3,"'s speed.","\n", " 13 = add exp to",Name3,"'s defense.")                                           
    exp_to = int(input("Where will you put your experience points?: "))
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
    if exp_to == 1:
        mana = (mana + exp_pts)
        mana_2 = (mana_2 + exp_pts)
    elif exp_to == 2:
        atk = (atk + exp_pts)
        atk_2 = (atk_2 + exp_pts)
    elif exp_to == 3:
        spd = (spd + exp_pts)
        spd_2 = (spd_2 + exp_pts)
    elif exp_to == 4:
        def_ = (def_ + exp_pts)
        def_2 = (def_2 + exp_pts)
    elif exp_to == 5:
        cards = (cards + exp_pts)
    elif exp_to == 6:
        mana2 = (mana2 + exp_pts)
        mana2_2 = (mana2_2 + exp_pts)
    elif exp_to == 7:
        atk2 = (atk2 + exp_pts)
        atk2_2 = (atk2_2 + exp_pts)
    elif exp_to == 8:
        spd2 = (spd2 + exp_pts)
        spd2_2 = (spd2_2 + exp_pts)
    elif exp_to == 9:
        def2_ = (def2_ + exp_pts)
        def2_2 = (def2_2 + exp_pts)
    elif exp_to == 10:
        mana3 = (mana3 + exp_pts)
        mana3_2 = (mana3_2 + exp_pts)
    elif exp_to == 11:
        atk3 = (atk3 + exp_pts)
        atk3_2 = (atk3_2 + exp_pts)
    elif exp_to == 12:
        spd3 = (spd3 + exp_pts)
        spd3_2 = (spd3_2 + exp_pts)
    elif exp_to == 13:
        def3_ = (def3_ + exp_pts)
        def3_2 = (def3_2 + exp_pts)
    else:
        while exp_to < 1 or exp_to > 13:
            time.sleep(.5)
            print(" ")
            print("That number was invalid. Valid numbers include anything from 1 to 13")
            time.sleep(.5)
            print(" ")
            print("Please try again.")
            time.sleep(.5)
            print(" ")
            print("1 = add exp to mana. 2 = add exp to attack.  3 = add exp to speed.  4 = add exp to defense. 5 = add exp to effect cards (you probably don't want this one). 6 = add exp to",Name2,",s mana. 7 = add exp to",Name2,"'s attack. 8 = add exp to",Name2,"'s speed. 9 = add exp to",Name2,"'s defense. 10 = add exp to",Name3,",s mana. 11 = add exp to",Name3,"'s attack. 12 = add exp to",Name3,"'s speed. 13 = add exp to",Name3,"'s defense.")  
            exp_to = int(input("Where will you put your experience points (1-13)?: "))
            os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
            if exp_to == 1:
                mana = (mana + exp_pts)
                mana_2 = (mana_2 + exp_pts)
            elif exp_to == 2:
                atk = (atk + exp_pts)
                atk_2 = (atk_2 + exp_pts)
            elif exp_to == 3:
                spd = (spd + exp_pts)
                spd_2 = (spd_2 + exp_pts)
            elif exp_to == 4:
                def_ = (def_ + exp_pts)
                def_2 = (def_2 + exp_pts)
            elif exp_to == 5:
                cards = (cards + exp_pts)
            elif exp_to == 6:
                mana2 = (mana2 + exp_pts)
                mana2_2 = (mana2_2 + exp_pts)
            elif exp_to == 7:
                atk2 = (atk2 + exp_pts)
                atk2_2 = (atk2_2 + exp_pts)
            elif exp_to == 8:
                spd2 = (spd2 + exp_pts)
                spd2_2 = (spd2_2 + exp_pts)
            elif exp_to == 9:
                def2_ = (def2_ + exp_pts)
                def2_2 = (def2_2 + exp_pts)
            elif exp_to == 10:
                mana3 = (mana3 + exp_pts)
                mana3_2 = (mana3_2 + exp_pts)
            elif exp_to == 11:
                atk3 = (atk3 + exp_pts)
                atk3_2 = (atk3_2 + exp_pts)
            elif exp_to == 12:
                spd3 = (spd3 + exp_pts)
                spd3_2 = (spd3_2 + exp_pts)
            elif exp_to == 13:
                def3_ = (def3_ + exp_pts)
                def3_2 = (def3_2 + exp_pts)
    time.sleep(.5)
    print(" ")
    print("It's been done! See stat increases next battle!")
    return[Name,atk,def_,spd,mana,atk_2,def_2,spd_2,mana_2,Name2,atk2,def2_,spd2,mana2,atk2_2,def2_2,spd2_2,mana2_2,Name3,atk3,def3_,spd3,mana3,atk3_2,def3_2,spd3_2,mana3_2,cards]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#This is where the actual game starts.
#DrawKimbley()
os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/CYC_VG_INTRO.wav&")
Name = input("What's your name:")
os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
print(" ")
time.sleep(.25)
print("Your name is,", Name)
print(" ")
time.sleep(.25)
true_turns = numb_of_turns()
true_turns2 = true_turns
print("You have",true_turns, "turns.")
print(" ")
time.sleep(.25)
if true_turns == 99999:
    y_or_n2 = 2
else:
    y_or_n2 = 1
[crit_d,clase,atk,def_,spd,class_w,spd_2,atk_2,def_2,clase_str] = get_class(crit_d,clase,atk,def_,spd,class_w,spd_2,atk_2,def_2,clase_str)
print("You're also going to need a partner.")
print(" ")
time.sleep(.25)
Name2 =str(input("What is their name?:"))
if Name == Name2:
    attempts = 0
    while Name == Name2 and attempts < 4:
        print(" ")
        time.sleep(.5)
        print("Those names are exactly the same and would cause confusion later...")
        print(" ")
        time.sleep(.5)
        Name2 = input("Please type another name for player two (if you add a symbol that's fine): ")
        os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
        attempts = attempts + 1
        print("attempts:",attempts)
        if attempts > 3:
            time.sleep(.5)
            print(" ")
            print("Whatever; I was trying to help...")
            time.sleep(.5)
print(" ")
time.sleep(.25)
print("And,", Name2,"'s class is...:")
print(" ")
time.sleep(.25)
[crit_d2,clase2,atk2,def2_,spd2,class2_w2,spd2_2,atk2_2,def2_2,clase_str2] = get_class(crit_d2,clase2,atk2,def2_,spd2,class2_w2,spd2_2,atk2_2,def2_2,clase_str2)
if clase == 0:
    if clase2 != 0:
        clase = clase2
        print(" ")
        time.sleep(.5)
        print("You are",clase_str2,"enchanted.")
        time.sleep(.5)
        print(" ")
        print("You now have: ",clase_str2,"mana burst,",clase_str2,"strength ,and",clase_str2,"weakness.")
        time.sleep(.5)
        print(" ")
        if clase2 == 2:
            print("You can no longer use a mana burst.")
    else:
        clase = 1
        clase2 = 1
if clase2 == 0:
    if clase != 0:
        clase2 = clase
        print(" ")
        time.sleep(.5)
        print(Name2,"is",clase_str,"enchanted.")
        print(" ")
        time.sleep(.5)
        print(Name2,"now has: ",clase_str,"mana burst,",clase_str,"strength, and",clase_str,"weakness.")
        time.sleep(.5)
        print(" ")
        if clase == 2:
            print(Name2,"can no longer use a mana burst.")
    else:
        clase2 = 1
        clase = 1

[Name,atk2,atk,def_,atk_2] = Not_So_Secret_Code(Name,atk2,atk,def_,atk_2)
[Name2,atk,atk2,def2_,atk2_2] = Not_So_Secret_Code(Name2,atk,atk2,def2_,atk2_2)
[en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)

[en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)

[en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)

[e1_atk,e1_def,e1_spd] = get_enemy_stats(e1_atk,e1_def,e1_spd)#Retrieves the stats of the enemy.

e1_spd_2 = e1_spd
e1_def_2 = e1_def
e1_atk_2 = e1_atk
print("Enemy one, a",en_1_class,"has arrived.")
print(" ")
time.sleep(.5)
print("... with an attack stat of", e1_atk, "a defense stat of" , e1_def, "and a speed stat of" , e1_spd, ".")
print(" ")
time.sleep(.25)
print("They attack ", Name2, "!")
print(" ")
time.sleep(.25)

if y_or_n2 == 1:
    e1_atk = (e1_atk + 2)
    enemy_1.showturtle()
    print("The enemy's attack is now", e1_atk, ". Good luck.")
    print(" ")
    time.sleep(.25)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    Draw_healthbars2(player1_position,player_one,spd,color)
    Draw_healthbars2(player2_position,player_two,spd2,color2)
    Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
    WaErase(spd,player1_position,player_one)
    WaErase(spd2,player2_position,player_two)
    WaErase(e1_spd,enemy1_position,enemy_1)
    spd_3 = spd
    spd2_3 = spd2
    e1_spd_3 = e1_spd
    won = "n"
    os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/CYC_Theme_vg.wav&")
    m_Burst_type = 0
    m_Burst2_type = 0
    m_Burst3_type = 0
    while (true_turns) > 0 and won == "n":
        [won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd] = Attack_sequence1(won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd)
        print("You have,",true_turns,"turns left.")
        print(" ")
        time.sleep(.5)
        if spd_3 != spd:
            Draw_healthbars2(player1_position,player_one,spd_3,color)
            Draw_healthbars(player1_position,player_one,spd,color)
            WaWrites_MyName(player_one,Name,color)
            WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
        if spd2_3 != spd2:
            Draw_healthbars2(player2_position,player_two,spd2_3,color2)
            Draw_healthbars(player2_position,player_two,spd2,color2)
            WaWrites_MyName(player_two,Name2,color2)
            WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
        if e1_spd_3 != e1_spd:
            Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
            Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
            WaWrites_MyName(enemy_1,"unknown enemy",color_enemy)
            WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
    WaErase_stats(player_one,player1_position)
    WaErase_stats(player_two,player2_position)
    WaErase_stats(enemy_1,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    if wins == 1:
        true_turns = true_turns2
        m_Burst2_type = 0
        m_Burst_type = 0
        print(" ")
        time.sleep(.75)
        if Continue == 1:
            print(" ")
            time.sleep(.25)
            print("Welcome to level two!!")
            print(" ")
            time.sleep(.25)
            spd = spd_2
            atk = atk_2
            def_ = def_2
            spd2 = spd2_2
            atk2 = atk2_2
            def2_ = def2_2
            e1_atk = random.randint(3,6)
            e1_def = random.randint(2,4)
            e1_spd = random.randint(1,5)
            e1_mana = random.randint(0,4)
            [en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)
            print("The enemy has arrived, and they're a", en_1_class, ".")
            time.sleep(.25)
            print(" ")
            [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
            [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
            mana = random.randint(7,11)
            mana_2 = mana
            print("Your mana is",mana,".")
            time.sleep(.5)
            print(" ")
            mana2 = random.randint(11,20)
            mana2 = (mana2 / 2)
            print(Name2,"'s mana is",mana2)
            print(" ")
            time.sleep(.5)
            print("Opponent's turn.")
            m_Burst2_type = 0
            mana2_to = 0  
            [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
            [e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2] = Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2)
            print(" ")
            time.sleep(.5)
            print("Your stats have been restored. Attack:",atk,"defense:",def_,"speed:",spd,".")
            print(" ")
            time.sleep(.5)
            print(Name2, "'s stats are:",atk2,",",def2_,",",spd2,".")
            time.sleep(.5)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            Draw_healthbars2(player1_position,player_one,spd,color)
            Draw_healthbars2(player2_position,player_two,spd2,color2)
            Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
            WaErase(spd,player1_position,player_one)
            WaErase(spd2,player2_position,player_two)
            WaErase(e1_spd,enemy1_position,enemy_1)
            spd_3 = spd
            spd2_3 = spd2
            e1_spd_3 = e1_spd
            won = "n"
            m_Burst_type = 0
            m_Burst2_type = 0
            m_Burst3_type = 0
            while (true_turns) > 0 and won == "n":
                [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                print("You have,",true_turns,"turns left.")
                print(" ")
                time.sleep(.5)
                if spd_3 != spd:
                    Draw_healthbars2(player1_position,player_one,spd_3,color)
                    Draw_healthbars(player1_position,player_one,spd,color)
                    WaWrites_MyName(player_one,Name,color)
                    WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                if spd2_3 != spd2:
                    Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                    Draw_healthbars(player2_position,player_two,spd2,color2)
                    WaWrites_MyName(player_two,Name2,color2)
                    WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                if e1_spd_3 != e1_spd:
                    Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                    Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                    WaWrites_MyName(enemy_1,"unknown enemy",color_enemy)
                    WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
            WaErase_stats(player_one,player1_position)
            WaErase_stats(player_two,player2_position)
            WaErase_stats(enemy_1,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            if Continue == 1:
                true_turns = true_turns2
                Name3 = " "
                BOSS_name = "Kimbley"
                en_1_class2 = 3
                en_1_class = "knight"
                en1_1_class_w = (2)
                Draw_healthbars2(player1_position,player_one,spd,color)
                Draw_healthbars2(player2_position,player_two,spd2,color2)
                Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                WaErase(spd,player1_position,player_one)
                WaErase(spd2,player2_position,player_two)
                WaErase(e1_spd,enemy1_position,enemy_1)
                [Name,Name2,Name3,BOSS_name,spd2,player2_position,player_two,color2,atk2,def2_,e1_spd] = story_time1(Name,Name2,Name3,BOSS_name,spd2,player2_position,player_two,color2,atk2,def2_,e1_spd)
                WaErase_stats(player_two,player2_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                e1_atk = 10
                e1_def = 0
                e1_spd = 25
                color_enemy = "OrangeRed"
                time.sleep(.5)
                print(" ")
                print("Kimbley's attack is: ",e1_atk,"Kimbley's defense is:",e1_def,"Kimbley's speed is: ",e1_spd)
                Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                [clase3_str,clase3,clase3_w] = get_enemy_class(clase3_str,clase3,clase3_w)
                crit_d3 = random.randint(2,4)
                time.sleep(.5)
                print(" ")
                print(Name3,"is a",clase3_str)
                e1_spd_2 = e1_spd
                e1_def_2 = e1_def
                e1_atk_2 = e1_atk
                if spd2 > 0 or def2_ > e1_atk:
                    spd2 = spd2_2
                    atk2 = atk2_2
                    def2_ = def2_2
                    mana2 = (mana2_2 + 1)
                else:
                    spd2 = 0
                    atk2 = 0
                    def2_ = 0
                    mana2 = 0
                atk = atk_2
                def_ = def_2
                spd = spd_2
                mana = mana_2
                atk3 = random.randint(2,8)
                def3_ = random.randint(1,6)
                spd3 = random.randint(4,7)
                atk3_2 = atk3
                def3_2 = def3_
                spd3_2 = spd3
                mana3 = random.randint(2,10)
                crit_d3 = random.randint(2,4)
                mana3_2 = mana3
                print(" ")
                time.sleep(.5)
                print("Kimbley did a giant mana burst; each turn Kimbley gains 1 speed.")
                print(" ")
                time.sleep(.5)
                print("Your stats have been restored. Attack:",atk,"Defense:",def_,"Speed:",spd,"Mana:",mana)
                print(" ")
                time.sleep(.5)
                print(" ")
                time.sleep(.5)
                cards = cards + 4
                print("You have:",cards,"cards.")
                print(Name2, "'s stats are:",atk2,",",def2_,",",spd2,".")
                time.sleep(.5)
                print(" ")
                print(Name3,"'s stats are: ",atk3,"attack,", def3_,"defense,",mana3,"mana, and",spd3,"speed.")
                Boss_weakness(atk,atk2,atk3,en1_1_class_w,BOSS_name,clase,clase2,clase3,Name2,Name3)
                [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
                if spd2 > 0 or spd2 > e1_atk:
                    [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
                

                [mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd] = player_mana(mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                Draw_healthbars2(player1_position,player_one,spd,color)
                Draw_healthbars2(player2_position,player_two,spd2,color2)
                Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                Draw_healthbars2(player3_position,player_3,spd3,color3)
                WaErase(spd,player1_position,player_one)
                WaErase(spd2,player2_position,player_two)
                won = "n"
                os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/cyc_mod_BOSS.wav&")
                m_Burst_type = 0
                m_Burst2_type = 0
                m_Burst3_type = 0
                while (true_turns) > 0 and won == "n":
                    if true_turns % 6 == 0:
                         os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/cyc_mod_BOSS.wav&") 
                    spd_3 = spd
                    spd2_3 = spd2
                    spd3_3 = spd3
                    e1_spd_3 = e1_spd
                    [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                    print("You have,",true_turns,"turns left.")
                    print(" ")
                    time.sleep(.5)
                    if m_Burst_type == 10 or m_Burst2_type == 10 or m_Burst3_type == 10:
                        print("Kimbley's mana burst was negated due to shador mana burst.")
                    else:
                        e1_spd = (e1_spd + 1)
                        print(" ")
                        time.sleep(.5)
                        print("Kimbley gained 1 speed due to giant mana burst.")
                    if spd_3 != spd:
                        Draw_healthbars2(player1_position,player_one,spd_3,color)
                        Draw_healthbars(player1_position,player_one,spd,color)
                        WaWrites_MyName(player_one,Name,color)
                        WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                    if spd2_3 != spd2:
                        Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                        Draw_healthbars(player2_position,player_two,spd2,color2)
                        WaWrites_MyName(player_two,Name2,color2)
                        WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                        [deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk] = Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
                    if spd3_3 != spd3:
                        Draw_healthbars2(player3_position,player_3,spd3_3,color3)
                        Draw_healthbars(player3_position,player_3,spd3,color3)
                        WaWrites_MyName(player_3,Name3,color3)
                        WaWrites_MyStats(player_3,color3,atk3,def3_,spd3,mana3,player3_position)
                        [deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk] = Dead_player(deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk)
                    if e1_spd_3 != e1_spd:
                        Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                        Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                        WaWrites_MyName(enemy_1,BOSS_name,color_enemy)
                        WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
                WaErase_stats(player_one,player1_position)
                WaErase_stats(player_two,player2_position)
                WaErase_stats(enemy_1,enemy1_position)
                if Continue == 1:
                    [Name,atk,def_,spd,mana,atk_2,def_2,spd_2,mana_2,Name2,atk2,def2_,spd2,mana2,atk2_2,def2_2,spd2_2,mana2_2,Name3,atk3,def3_,spd3,mana3,atk3_2,def3_2,spd3_2,mana3_2,cards] = EXP_points(Name,atk,def_,spd,mana,atk_2,def_2,spd_2,mana_2,Name2,atk2,def2_,spd2,mana2,atk2_2,def2_2,spd2_2,mana2_2,Name3,atk3,def3_,spd3,mana3,atk3_2,def3_2,spd3_2,mana3_2,cards)
                    [Name,Name2,Name3,BOSS_name,spd2,def2_,player3_position,player_3,color3,spd3,def3_,e1_atk] = Story_time2(Name,Name2,Name3,BOSS_name,spd2,def2_,player3_position,player_3,color3,spd3,def3_,e1_atk)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    e1_atk = random.randint(5,7)
                    e1_def = random.randint(5,7)
                    e1_spd = random.randint(10,16)
                    e1_mana = random.randint(7,12)
                    e1_spd_2 = e1_spd
                    e1_def_2 = e1_def
                    e1_atk_2 = e1_atk
                    [en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)
                    time.sleep(.5)
                    print(" ")
                    enemy_name = "Zane"
                    print("You have been challenged by Zane, a",en_1_class,".")
                    print(" ")
                    time.sleep(.5)
                    print("Zane has",e1_atk,"attack,",e1_def,"defense,",e1_spd,"speed, and",e1_mana,"mana.")
                    WaErase(spd,player1_position,player_one)
                    WaErase(spd2,player2_position,player_two)
                    WaErase(spd3,player3_position,player_3)
                    [e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2] = Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2)
                    [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
                    [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
                    if spd2 > 0 or def2_ > e1_atk:
                        spd2 = spd2_2
                        atk2 = atk2_2
                        def2_ = def2_2
                        mana2 = mana2_2
                        [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
                    else:
                        spd2 = 0
                        atk2 = 0
                        def2_ = 0
                        mana2 = 0
                    if spd3 > 0 or spd3 > e1_atk:
                        spd3 = spd3_2
                        atk3 = atk3_2
                        def3_ = def3_2
                        mana3 = mana3_2
                        [mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd] = player_mana(mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd)
                    else:
                        spd3 = 0
                        atk3 = .00000000001
                        def3_ = 0
                        mana3 = 0
                    spd = spd_2
                    atk = atk_2
                    def_ = def_2
                    mana = mana_2
                    color_enemy = "red"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    print(" ")
                    true_turns = true_turns2
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    WaErase(spd,player1_position,player_one)
                    WaErase(spd2,player2_position,player_two)
                    WaErase(e1_spd,enemy1_position,enemy_1)
                    Draw_healthbars2(player1_position,player_one,spd,color)
                    Draw_healthbars2(player2_position,player_two,spd2,color2)
                    Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                    spd_3 = spd
                    spd2_3 = spd2
                    e1_spd_3 = e1_spd
                    won = "n"
                    cards += 1
                    os.system("afplay /CYC_theme_vg.wav&")
                    true_turns = true_turns2
                    m_Burst_type = 0
                    m_Burst2_type = 0
                    m_Burst3_type = 0
                    while (true_turns) > 0 and won == "n":
                        time.sleep(.5)
                        print(" ")
                        Battle_Text1(e1_spd,enemy_name)
                        [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                        print("You have,",true_turns,"turns left.")
                        print(" ")
                        time.sleep(.5)
                        if spd_3 != spd:
                            Draw_healthbars2(player1_position,player_one,spd_3,color)
                            Draw_healthbars(player1_position,player_one,spd,color)
                            WaWrites_MyName(player_one,Name,color)
                            WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                        if spd2_3 != spd2:
                            Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                            Draw_healthbars(player2_position,player_two,spd2,color2)
                            WaWrites_MyName(player_two,Name2,color2)
                            WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                            [deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk] = Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
                        if spd3_3 != spd3:
                            Draw_healthbars2(player3_position,player_3,spd3_3,color3)
                            Draw_healthbars(player3_position,player_3,spd3,color3)
                            WaWrites_MyName(player_3,Name3,color3)
                            WaWrites_MyStats(player_3,color3,atk3,def3_,spd3,mana3,player3_position)
                            [deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk] = Dead_player(deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk) 
                        if e1_spd_3 != e1_spd:
                            Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                            Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                            WaWrites_MyName(enemy_1,enemy_name,color_enemy)
                            WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
                    WaErase_stats(player_one,player1_position)
                    WaErase_stats(player_two,player2_position)
                    WaErase_stats(enemy_1,enemy1_position)
                    if Continue == 1:
                        [Name,Name2,Name3,BOSS_name,spd,def3_,player1_position,player_one,color,spd3,def_,e1_spd,spd2,def2_] = Story_time3(Name,Name2,Name3,BOSS_name,spd,def3_,player1_position,player_one,color,spd3,def_,e1_spd,spd2,def2_)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                        e1_atk = random.randint(5,9)
                        e1_def = random.randint(6,7)
                        e1_spd = random.randint(11,20)
                        e1_mana = random.randint(7,13)
                        e1_spd_2 = e1_spd
                        e1_def_2 = e1_def
                        e1_atk_2 = e1_atk
                        [en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)
                        time.sleep(.5)
                        print(" ")
                        print("You have been challenged by Sal, a",en_1_class,".")
                        print(" ")
                        time.sleep(.5)
                        print("Sal has",e1_atk,"attack,",e1_def,"defense,",e1_spd,"speed, and",e1_mana,"mana.")
                        WaErase(spd,player1_position,player_one)
                        WaErase(spd2,player2_position,player_two)
                        WaErase(spd3,player3_position,player_3)
                        [e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2] = Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2)
                        [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
                        [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
                        if spd2 > 0 or def2_ > e1_atk:
                            spd2 = spd2_2
                            atk2 = atk2_2
                            def2_ = def2_2
                            mana2 = mana2_2
                            [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
                        else:
                            spd2 = 0
                            atk2 = .000000000001
                            def2_ = 0
                            mana2 = 0
                        if spd3 > 0 or spd3 > e1_atk:
                            spd3 = spd3_2
                            atk3 = atk3_2
                            def3_ = def3_2
                            mana3 = mana3_2
                            [mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd] = player_mana(mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd)
                        else:
                            spd3 = 0
                            atk3 = .000000000001
                            def3_ = 0
                            mana3 = 0
                        spd = spd_2
                        atk = atk_2
                        def_ = def_2
                        mana = mana_2
                        color_enemy = "red"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                        print(" ")
                        true_turns = true_turns2
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                        WaErase(spd,player1_position,player_one)
                        WaErase(spd2,player2_position,player_two)
                        WaErase(e1_spd,enemy1_position,enemy_1)
                        Draw_healthbars2(player1_position,player_one,spd,color)
                        Draw_healthbars2(player2_position,player_two,spd2,color2)
                        Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                        spd_3 = spd
                        spd2_3 = spd2
                        spd3_3 = spd3
                        e1_spd_3 = e1_spd
                        won = "n"
                        cards += 2
                        enemy_name = "Sal"
                        os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/CYC_theme_vg.wav&")
                        m_Burst_type = 0
                        m_Burst2_type = 0
                        m_Burst3_type = 0
                        while (true_turns) > 0 and won == "n":
                            Battle_Text1(e1_spd,enemy_name)
                            [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                            if spd_3 != spd:
                                Draw_healthbars2(player1_position,player_one,spd_3,color)
                                Draw_healthbars(player1_position,player_one,spd,color)
                                WaWrites_MyName(player_one,Name,color)
                                WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                            if spd2_3 != spd2:
                                Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                                Draw_healthbars(player2_position,player_two,spd2,color2)
                                WaWrites_MyName(player_two,Name2,color2)
                                WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                                [deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk] = Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
                            if spd3_3 != spd3:
                                Draw_healthbars2(player3_position,player_3,spd3_3,color3)
                                Draw_healthbars(player3_position,player_3,spd3,color3)
                                WaWrites_MyName(player_3,Name3,color3)
                                WaWrites_MyStats(player_3,color3,atk3,def3_,spd3,mana3,player3_position)
                                [deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk] = Dead_player(deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk)    
                            if e1_spd_3 != e1_spd:
                                Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                                Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                                WaWrites_MyName(enemy_1,enemy_name,color_enemy)
                                WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                        [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
                        WaErase_stats(player_one,player1_position)
                        WaErase_stats(player_two,player2_position)
                        WaErase_stats(enemy_1,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                    
else:
    
    if y_or_n2 == 2:
        e1_spd_2 = e1_spd
        e1_def_2 = e1_def
        e1_atk_2 = e1_atk
        os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/CYC_theme_vg.wav&")
        print("Your first enemy has arrived with",e1_atk,"attack",e1_def,"defense, and",e1_spd,"speed.")
        print(" ")
        time.sleep(.5)
        print(Name2,"'s speed is", spd2, "now!")
        print(" ")
        time.sleep(.25)
        print("Now it's your turn")
        print(" ")
        time.sleep(.25)
        print("Who's going to attack, you or", Name2, "?")
        print(" ")
        time.sleep(.25)
        move = int(input("Who are you attacking with?(1= you, 2 = partner):"))
        os.system("afplay /Users/s186986/Desktop/El_juego_cyc_mod/Select_vg.wav&")
        print(" ")
        time.sleep(.25)
        print("ATTACK!")
        print(" ")
        time.sleep(.25)
        luck2 = random.randint(1,2)
        if move == 1:
            if luck2 == 2:
                atk = (atk * crit_d)
            e1_spd = (e1_spd - (atk/10))
            if luck2 == 2:
                atk = (atk / crit_d)
        if move == 2:
            if luck2 == 2:
                atk2 = (atk2 * crit_d2)
            e1_spd = (e1_spd - (atk2/10))
            if luck2 == 2:
                atk2 = (atk2 / crit_d2)
        print("Enemy speed is now", e1_spd, "!")
        print(" ")
        time.sleep(.25)
        print("Your enemy attacks again, but this time you!")
        print(" ")
        time.sleep(.25)
        [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
        [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
        spd = (spd - (e1_atk/10))
        print("Your speed is now", spd, ".")
        luck1 =random.randint(1, 20)
        if luck1 == 5:
            print("WHAT, THEY ATTACKED AGAIN!?!")
            print(" ")
            time.sleep(.25)
            spd = (spd - ((e1_atk/10) * 8))
            print("AND AGAIN!!?!")
            print(" ")
            time.sleep(.25)
            print("AAAAND AGAIN!?!")
            print(" ")
            time.sleep(.25)
            print("...and maybe once more!")
            print(" ")
            time.sleep(.25)
            print("...and each one of those was a critical hit.")
            print(" ")
            time.sleep(.25)
            print("Your speed has dropped to", spd, ".")
        print(" ")
        time.sleep(.25)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
        WaErase(spd,player1_position,player_one)
        WaErase(spd2,player2_position,player_two)
        WaErase(e1_spd,enemy1_position,enemy_1)
        Draw_healthbars2(player1_position,player_one,spd,color)
        Draw_healthbars2(player2_position,player_two,spd2,color2)
        Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
        spd_3 = spd
        spd2_3 = spd2
        e1_spd_3 = e1_spd
        cards = cards + 2
        m_Burst_type = 0
        m_Burst2_type = 0
        m_Burst3_type = 0
        while e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
            [won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd] = Attack_sequence1(won,crit_d2,crit_d,true_turns,atk,def_,spd,atk2,def2_,e1_atk,e1_def,e1_spd)
            if spd_3 != spd:
                Draw_healthbars2(player1_position,player_one,spd_3,color)
                Draw_healthbars(player1_position,player_one,spd,color)
                WaWrites_MyName(player_one,Name,color)
                WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
            if spd2_3 != spd2:
                Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                Draw_healthbars(player2_position,player_two,spd2,color2)
                WaWrites_MyName(player_two,Name2,color2)
                WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
            if e1_spd_3 != e1_spd:
                Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                WaWrites_MyName(enemy_1,"unknown enemy",color_enemy)
                WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#         
        [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
        WaErase_stats(player_one,player1_position)
        WaErase_stats(player_two,player2_position)
        WaErase_stats(enemy_1,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
        if wins == 1:
            mana = random.randint(5,10)
            mana2 = random.randint(1,10)
            while mana2 == mana:
                if mana2 == mana:
                    mana2 = random.randint(1,10)
            print(" ")
            time.sleep(.75)
        if Continue == 1:
            print(" ")
            time.sleep(.25)
            print("Welcome to level two!!")
            print(" ")
            time.sleep(.25)
            spd = spd_2
            atk = atk_2
            def_ = def_2
            spd2 = spd2_2
            atk2 = atk2_2
            def2_ = def2_2
            cards = cards + 2
            e1_atk = random.randint(3,6)
            e1_def = random.randint(2,4)
            e1_spd = random.randint(1,5)
            e1_mana = random.randint(0,4)
            e1_spd_2 = e1_spd
            e1_def_2 = e1_def
            e1_atk_2 = e1_atk
            [en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)
            [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
            [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
            print("The enemy has arrived, and they're a", en_1_class, ".")
            time.sleep(.25)
            print(" ")
            print("Your mana is",mana,".")
            mana_2 = mana
            time.sleep(.5)
            print(" ")
            mana2 = random.randint(1,10)
            mana2_2 = mana2
            print(Name2,"'s mana is",mana2)
            print(" ")
            time.sleep(.5)
            print("Opponent's turn.")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
            [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
            [e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2] = Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2)
            print(" ")
            time.sleep(.5)
            print("Your stats have been restored. Attack:",atk,"defense:",def_,"speed:",spd,".")
            print(" ")
            time.sleep(.5)
            print(Name2, "'s stats are:",atk2,",",def2_,",",spd,".")
            time.sleep(.5)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
            WaErase(spd,player1_position,player_one)
            WaErase(spd2,player2_position,player_two)
            WaErase(e1_spd,enemy1_position,enemy_1)
            Draw_healthbars2(player1_position,player_one,spd,color)
            Draw_healthbars2(player2_position,player_two,spd2,color2)
            Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
            spd_3 = spd
            spd2_3 = spd2
            e1_spd_3 = e1_spd
            won = "n"
            m_Burst_type = 0
            m_Burst2_type = 0
            m_Burst3_type = 0
            while e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
                [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                if spd_3 != spd:
                    Draw_healthbars2(player1_position,player_one,spd_3,color)
                    Draw_healthbars(player1_position,player_one,spd,color)
                    WaWrites_MyName(player_one,Name,color)
                    WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                if spd2_3 != spd2:
                    Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                    Draw_healthbars(player2_position,player_two,spd2,color2)
                    WaWrites_MyName(player_two,Name2,color2)
                    WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                if e1_spd_3 != e1_spd:
                    Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                    Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                    WaWrites_MyName(enemy_1,"unknown enemy",color_enemy)
                    WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#                      
            [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
            WaErase_stats(player_one,player1_position)
            WaErase_stats(player_two,player2_position)
            WaErase_stats(enemy_1,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Semi-skippable cutscene begins before fighting Zuza Boss: Kimbley The Big.
            if Continue == 1:
                Name3 = " "
                BOSS_name = "Kimbley"
                en_1_class2 = 3
                en_1_class = "knight"
                en1_1_class_w = (2)
                Draw_healthbars2(player1_position,player_one,spd,color)
                Draw_healthbars2(player2_position,player_two,spd2,color2)
                Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                cards = cards + 2
                [Name,Name2,Name3,BOSS_name,spd2,player2_position,player_two,color2,atk2,def2_,e1_spd] = story_time1(Name,Name2,Name3,BOSS_name,spd2,player2_position,player_two,color2,atk2,def2_,e1_spd)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                e1_atk = 10
                e1_def = 0
                e1_spd = 15
                color_enemy = "OrangeRed"
                time.sleep(.5)
                print(" ")
                print("Kimbley's attack is: ",e1_atk,"Kimbley's defense is:",e1_def,"Kimbley's speed is: ",e1_spd)
                e1_spd_2 = e1_spd
                e1_def_2 = e1_def
                e1_atk_2 = e1_atk
                Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                [clase3_str,clase3,clase3_w] = get_enemy_class(clase3_str,clase3,clase3_w)
                crit_d3 = random.randint(2,4)
                time.sleep(.5)
                print(" ")
                print(Name3,"is a",clase3_str)
                if spd2 > 0 or def2_ > e1_atk:
                    spd2 = spd2_2
                    atk2 = atk2_2
                    def2_ = def2_2
                    mana2 = (mana2_2 + 1)
                else:
                    spd2 = 0
                    atk2 = .0000000000001
                    def2_ = 0
                    mana2 = 0
                atk = atk_2
                def_ = def_2
                spd = spd_2
                mana = mana_2
                atk3 = random.randint(2,8)
                def3_ = random.randint(1,6)
                spd3 = random.randint(4,7)
                atk3_2 = atk3
                def3_2 = def3_
                spd3_2 = spd3
                mana3 = random.randint(2,10)
                mana3_2 = mana3
                print(" ")
                time.sleep(.5)
                print("Kimbley did a giant mana burst; each turn Kimbley gains 1 speed.")
                print(" ")
                time.sleep(.5)
                print("Your stats have been restored. Attack:",atk,"defense:",def_,"speed:",spd,"mana:",mana,".")
                print(" ")
                time.sleep(.5)
                print(" ")
                time.sleep(.5)
                print("You also have",cards,"cards.")
                print(Name2, "'s stats are:",atk2,",",def2_,",",spd2,".")
                time.sleep(.5)
                print(" ")
                print(Name3,"'s stats are: ",atk3,"attack,", def3_,"defense, and",spd3,"speed.")
                Boss_weakness(atk,atk2,atk3,en1_1_class_w,BOSS_name,clase,clase2,clase3,Name2,Name3)
                [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
                time.sleep(.5)
                if spd2 > 0 or spd2 > e1_atk:
                    spd2 = spd2_2
                    atk2 = atk2_2
                    def2_ = def2_2
                    mana2 = (mana2_2 + 1)
                    [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
                else:
                    spd2 = 0
                    atk2 = .0000000000001
                    def2_ = 0
                    mana2 = 0
                [mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd] = player_mana(mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                WaErase(spd,player1_position,player_one)
                WaErase(spd2,player2_position,player_two)
                WaErase(e1_spd,enemy1_position,enemy_1)
                Draw_healthbars2(player1_position,player_one,spd,color)
                Draw_healthbars2(player2_position,player_two,spd2,color2)
                Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                Draw_healthbars2(player3_position,player_3,spd3,color3)
                won = "n"
                os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/cyc_mod_BOSS.wav&")
                tt = 0
                m_Burst_type = 0
                m_Burst2_type = 0
                m_Burst3_type = 0
                while e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
                    tt += 1
                    if tt % 6 == 0:
                        os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/cyc_mod_BOSS.wav&") 
                    spd_3 = spd
                    spd2_3 = spd2
                    spd3_3 = spd3
                    e1_spd_3 = e1_spd
                    [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                    if m_Burst_type == 10 or m_Burst2_type == 10 or m_Burst3_type == 10:
                        print("Kimbley's mana burst was negated due to shador mana burst.")
                    else:
                        e1_spd = (e1_spd + 1)
                        print(" ")
                        time.sleep(.5)
                        print("Kimbley gained 1 speed due to giant mana burst.")
                    if spd_3 != spd:
                        Draw_healthbars2(player1_position,player_one,spd_3,color)
                        Draw_healthbars(player1_position,player_one,spd,color)
                        WaWrites_MyName(player_one,Name,color)
                        WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                    if spd2_3 != spd2:
                        Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                        Draw_healthbars(player2_position,player_two,spd2,color2)
                        WaWrites_MyName(player_two,Name2,color2)
                        WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                        [deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk] = Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
                    if spd3_3 != spd3:
                        Draw_healthbars2(player3_position,player_3,spd3_3,color3)
                        Draw_healthbars(player3_position,player_3,spd3,color3)
                        WaWrites_MyName(player_3,Name3,color3)
                        WaWrites_MyStats(player_3,color3,atk3,def3_,spd3,mana3,player3_position)
                        [deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk] = Dead_player(deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk)
                    if e1_spd_3 != e1_spd:
                        Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                        Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                        WaWrites_MyName(enemy_1,BOSS_name,color_enemy)
                        WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#                            
                [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
                WaErase_stats(player_one,player1_position)
                WaErase_stats(player_two,player2_position)
                WaErase_stats(enemy_1,enemy1_position)
                if Continue == 1:
                    [Name,atk,def_,spd,mana,atk_2,def_2,spd_2,mana_2,Name2,atk2,def2_,spd2,mana2,atk2_2,def2_2,spd2_2,mana2_2,Name3,atk3,def3_,spd3,mana3,atk3_2,def3_2,spd3_2,mana3_2,cards] = EXP_points(Name,atk,def_,spd,mana,atk_2,def_2,spd_2,mana_2,Name2,atk2,def2_,spd2,mana2,atk2_2,def2_2,spd2_2,mana2_2,Name3,atk3,def3_,spd3,mana3,atk3_2,def3_2,spd3_2,mana3_2,cards)
                    [Name,Name2,Name3,BOSS_name,spd2,def2_,player3_position,player_3,color3,spd3,def3_,e1_atk] = Story_time2(Name,Name2,Name3,BOSS_name,spd2,def2_,player3_position,player_3,color3,spd3,def3_,e1_atk)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    e1_atk = random.randint(4,6)
                    e1_def = random.randint(3,5)
                    e1_spd = random.randint(5,12)
                    e1_mana = random.randint(4,9)
                    e1_spd_2 = e1_spd
                    e1_def_2 = e1_def
                    e1_atk_2 = e1_atk
                    [en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)
                    time.sleep(.5)
                    print(" ")
                    print("You have been challenged by Zane, a",en_1_class,".")
                    print(" ")
                    time.sleep(.5)
                    enemy_name = "Zane"
                    print("Zane has",e1_atk,"attack,",e1_def,"defense,",e1_spd,"speed, and",e1_mana,"mana.")
                    WaErase(spd,player1_position,player_one)
                    WaErase(spd2,player2_position,player_two)
                    WaErase(spd3,player3_position,player_3)
                    [e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2] = Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2)
                    [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
                    [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
                    if spd2 > 0 or def2_ > e1_atk:
                        spd2 = spd2_2
                        atk2 = atk2_2
                        def2_ = def2_2
                        mana2 = mana2_2
                        [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
                    else:
                        spd2 = 0
                        atk2 = .000000000001
                        def2_ = 0
                        mana2 = 0
                    if spd3 > 0 or spd3 > e1_atk:
                        spd3 = spd3_2
                        atk3 = atk3_2
                        def3_ = def3_2
                        mana3 = mana3_2
                        [mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd] = player_mana(mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd)
                    else:
                        spd3 = 0
                        atk3 = .000000000001
                        def3_ = 0
                        mana3 = 0
                    spd = spd_2
                    atk = atk_2
                    def_ = def_2
                    mana = mana_2
                    color_enemy = "red"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    print(" ")
                    true_turns = true_turns2
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    WaErase(spd,player1_position,player_one)
                    WaErase(spd2,player2_position,player_two)
                    WaErase(e1_spd,enemy1_position,enemy_1)
                    Draw_healthbars2(player1_position,player_one,spd,color)
                    Draw_healthbars2(player2_position,player_two,spd2,color2)
                    Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                    spd_3 = spd
                    spd2_3 = spd2
                    spd3_3 = spd3
                    e1_spd_3 = e1_spd
                    won = "n"
                    cards += 3
                    os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/CYC_theme_vg.wav&")
                    m_Burst_type = 0
                    m_Burst2_type = 0
                    m_Burst3_type = 0
                    while e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
                        Battle_Text1(e1_spd,enemy_name)
                        [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                        if spd_3 != spd:
                            Draw_healthbars2(player1_position,player_one,spd_3,color)
                            Draw_healthbars(player1_position,player_one,spd,color)
                            WaWrites_MyName(player_one,Name,color)
                            WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                        if spd2_3 != spd2:
                            Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                            Draw_healthbars(player2_position,player_two,spd2,color2)
                            WaWrites_MyName(player_two,Name2,color2)
                            WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                            [deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk] = Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
                        if spd3_3 != spd3:
                            Draw_healthbars2(player3_position,player_3,spd3_3,color3)
                            Draw_healthbars(player3_position,player_3,spd3,color3)
                            WaWrites_MyName(player_3,Name3,color3)
                            WaWrites_MyStats(player_3,color3,atk3,def3_,spd3,mana3,player3_position)
                            [deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk] = Dead_player(deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk)    
                        if e1_spd_3 != e1_spd:
                            Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                            Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                            WaWrites_MyName(enemy_1,enemy_name,color_enemy)
                            WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                    [wins,Continue,true_turns] = WINNER(wins,Continue,true_turns)
                    WaErase_stats(player_one,player1_position)
                    WaErase_stats(player_two,player2_position)
                    WaErase_stats(enemy_1,enemy1_position)
                    if Continue == 1:
                        [Name,Name2,Name3,BOSS_name,spd,def3_,player1_position,player_one,color,spd3,def_,e1_spd,spd2,def2_] = Story_time3(Name,Name2,Name3,BOSS_name,spd,def3_,player1_position,player_one,color,spd3,def_,e1_spd,spd2,def2_)
                        e1_atk = random.randint(5,7)
                        e1_def = random.randint(4,6)
                        e1_spd = random.randint(9,14)
                        e1_mana = random.randint(5,12)
                        e1_spd_2 = e1_spd
                        e1_def_2 = e1_def
                        e1_atk_2 = e1_atk
                        [en_1_class,en_1_class2,en1_1_class_w] = get_enemy_class(en_1_class,en_1_class2,en1_1_class_w)
                        time.sleep(.5)
                        print(" ")
                        print("You have been challenged by Sal, a",en_1_class,".")
                        print(" ")
                        time.sleep(.5)
                        print("Sal has",e1_atk,"attack,",e1_def,"defense,",e1_spd,"speed, and",e1_mana,"mana.")
                        WaErase(spd,player1_position,player_one)
                        WaErase(spd2,player2_position,player_two)
                        WaErase(spd3,player3_position,player_3)
                        [e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2] = Enemy_mana2(e1_mana,e1_atk,e1_def,e1_spd,e1_atk_2,e1_def_2,e1_spd_2)
                        [en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3] = weakness_enemy(en1_1_class_w,clase,clase2,clase3,atk,atk2,atk3,Name2,Name3)
                        [en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3] = player_weakness(en_1_class2,class_w,class2_w2,clase3_w,e1_atk,Name2,Name3)
                        if spd2 > 0 or def2_ > e1_atk:
                            spd2 = spd2_2
                            atk2 = atk2_2
                            def2_ = def2_2
                            mana2 = mana2_2
                            [mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd] = player_mana(mana2,mana2_to,clase2,m_Burst2_type,Name2,atk2,def2_,spd2,e1_atk,e1_def,e1_spd,spd)
                        else:
                            spd2 = 0
                            atk2 = .000000000001
                            def2_ = 0
                            mana2 = 0
                        if spd3 > 0 or spd3 > e1_atk:
                            spd3 = spd3_2
                            atk3 = atk3_2
                            def3_ = def3_2
                            mana3 = mana3_2
                            [mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd] = player_mana(mana3,mana3_to,clase3,m_Burst3_type,Name3,atk3,def3_,spd3,e1_atk,e1_def,e1_spd,spd)
                        else:
                            spd3 = 0
                            atk3 = .000000000001
                            def3_ = 0
                            mana3 = 0
                        spd = spd_2
                        atk = atk_2
                        def_ = def_2
                        mana = mana_2
                        color_enemy = "red"
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                        print(" ")
                        true_turns = true_turns2
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                        WaErase(spd,player1_position,player_one)
                        WaErase(spd2,player2_position,player_two)
                        WaErase(e1_spd,enemy1_position,enemy_1)
                        Draw_healthbars2(player1_position,player_one,spd,color)
                        Draw_healthbars2(player2_position,player_two,spd2,color2)
                        Draw_healthbars2(enemy1_position,enemy_1,e1_spd,color_enemy)
                        spd_3 = spd
                        spd2_3 = spd2
                        spd3_3 = spd3
                        e1_spd_3 = e1_spd
                        won = "n"
                        cards += 3
                        enemy_name = "Sal"
                        m_Burst_type = 0
                        m_Burst2_type = 0
                        m_Burst3_type = 0
                        os.system("afplay /Users/s186986/Desktop/La_Carpeta_de_las_carpetas/La_musica/CYC_theme_vg.wav&")
                        while e1_spd > int(0) and spd > int(0) or e1_spd > int(0) and def_ > e1_atk:
                            Battle_Text1(e1_spd,enemy_name)
                            [won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3] = Attack_Sequence2(won,e1_spd_2,e1_atk_2,e1_def_2,crit_d,crit_d2,crit_d3,taps,cards,card_selection,mana_2,true_turns,e1_spd,e1_atk,e1_def,e1_mana,spd,atk,def_,mana,spd2,atk2,def2_,mana2,m_Burst_type,m_Burst2_type,m_Burst3_type,atk3,spd3,def3_,mana3,x2,y2,z2,w2,m_Burstx_type,Name2,Name3)
                            if spd_3 != spd:
                                Draw_healthbars2(player1_position,player_one,spd_3,color)
                                Draw_healthbars(player1_position,player_one,spd,color)
                                WaWrites_MyName(player_one,Name,color)
                                WaWrites_MyStats(player_one,color,atk,def_,spd,mana,player1_position)
                            if spd2_3 != spd2:
                                Draw_healthbars2(player2_position,player_two,spd2_3,color2)
                                Draw_healthbars(player2_position,player_two,spd2,color2)
                                WaWrites_MyName(player_two,Name2,color2)
                                WaWrites_MyStats(player_two,color2,atk2,def2_,spd2,mana2,player2_position)
                                [deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk] = Dead_player(deaths2,Name2,spd2,atk2,def2_,spd2_2,def2_2,atk2_2,player2_position,player,player_two,color2,e1_atk)
                            if spd3_3 != spd3:
                                Draw_healthbars2(player3_position,player_3,spd3_3,color3)
                                Draw_healthbars(player3_position,player_3,spd3,color3)
                                WaWrites_MyName(player_3,Name3,color3)
                                WaWrites_MyStats(player_3,color3,atk3,def3_,spd3,mana3,player3_position)
                                [deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk] = Dead_player(deaths3,Name3,spd3,atk3,def3_,spd3_2,def3_2,atk3_2,player3_position,player,player_3,color3,e1_atk)    
                            if e1_spd_3 != e1_spd:
                                Draw_healthbars2(enemy1_position,enemy_1,e1_spd_3,color_enemy)
                                Draw_healthbars(enemy1_position,enemy_1,e1_spd,color_enemy)
                                WaWrites_MyName(enemy_1,enemy_name,color_enemy)
                                WaWrites_MyStats(enemy_1,color_enemy,e1_atk,e1_def,e1_spd,e1_mana,enemy1_position)
