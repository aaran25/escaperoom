#Needed game code
import pygame

In_Main_Room = True
In_RichBedroom = False
In_Room2 = False

pygame.init()
#Variables
Screen_Dimensions = pygame.display.set_mode((1920, 1880))
Red = (265, 0, 0)
NextRoomButton = pygame.image.load("other_room_button.png")
Escape_View = pygame.image.load("EscapeView.webp")
Scaled_NextRoomButton = pygame.transform.scale(NextRoomButton, (170, 232))
RichBedroom = pygame.image.load("RichBedroom.jpeg")
key = pygame.image.load("Key.png")
Room2 = pygame.image.load("Room2.png")
InsideLock = pygame.image.load("InsideLock.png")
Lock = pygame.image.load("Lock.png")
Black_Rectangle = pygame.image.load("Black_Rectangle.png")
Scaled_Black_Rectangle = pygame.transform.scale(Black_Rectangle, (115, 190)).convert_alpha()
Scaled_Black_Rectangle2 = pygame.transform.scale(Black_Rectangle, (115, 190))
Scaled_Black_Rectangle3 = pygame.transform.scale(Black_Rectangle, (115, 190))
Scaled_Black_Rectangle4 = pygame.transform.scale(Black_Rectangle, (115, 190))
Won_Game = False
Clicked_Key = False
Scaled_Lock = pygame.transform.scale (Lock, (75, 75))
Rotated_And_Scaled_NextRoomButton = pygame.transform.rotate(Scaled_NextRoomButton, 40)
Scaled_RichBedroom = pygame.transform.scale(RichBedroom, (1920, 999.99))
white = (255, 255, 255)
Looking_At_Lock = False
#Slot lists
Slot_1_List = [1, 2, 3, 4]

NextRoomButton2 = pygame.image.load("other_room_button.png")
Scaled_NextRoomButton = pygame.transform.scale(NextRoomButton, (170, 232))
Rotated_And_Scaled_NextRoomButton2 = pygame. transform. rotate(Scaled_NextRoomButton, 320)
Hitbox_Of_Rotated_And_Scaled_NextRoomButton = Rotated_And_Scaled_NextRoomButton.get_rect()
Scaled_Key = pygame.transform.scale(key, (30,23.5))
Scaled_Key2 = pygame.transform.scale(key, (60,50))
Hitbox_Of_Scaled_Key = Scaled_Key.get_rect()
Hitbox_Of_Scaled_Key.center = (580,310)
Hitbox_Of_Rotated_And_Scaled_NextRoomButton.center = (1778, 853)
Hitbox_Of_Rotated_And_Scaled_NextRoomButton2 = Rotated_And_Scaled_NextRoomButton2.get_rect()
Scaled_Room2 = pygame.transform.scale(Room2, (1940, 1068))
Main_Room = pygame.image.load("backgroundhouse.jpg")
Scaled_Main_Room = pygame.transform.scale(Main_Room, (1950, 1000))
Current_Room = ("main")


Room_Dictionary = {Main_Room: 1, Scaled_RichBedroom: 2, Scaled_Room2: 3}


#Custom_Font= pygame.font('timesnewroman', 32)
Custom_Font = pygame.font.SysFont("timesnewroman", 40, 30, 20)
Custom_Font2 = pygame.font.SysFont("comicsansms", 20, 10, 0)
Comic_Font3 = pygame.font.SysFont(("timesnewroman"), 130, 30, 20)
Text_Render = Comic_Font3.render, ("Hi", True, (255, 255, 255))
message = Custom_Font.render("INVENTORY", True, (0, 0, 0))
message2 = Custom_Font.render("dude ur stuck get out", True, (0, 0, 0))
CANT_LEAVE = Custom_Font.render("Cant go there", True, (0, 0, 0))
Number2 = Comic_Font3.render(str(Slot_1_List[1]), True, (white))


while True:
    if Won_Game == True:
        Screen_Dimensions.blit(Escape_View, (0, 0))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            Hitbox_Of_Scaled_Lock = Scaled_Lock.get_rect()
            Hitbox_Of_Scaled_Lock.center = (223, 400)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Hitbox_Of_Rotated_And_Scaled_NextRoomButton == Rotated_And_Scaled_NextRoomButton.get_rect():
                    Hitbox_Of_Rotated_And_Scaled_NextRoomButton.center = (1778, 853)
                #Right Arrow
                if Hitbox_Of_Rotated_And_Scaled_NextRoomButton.collidepoint(event.pos):
                    print(event.pos)
                    if Current_Room == ("main"):
                        In_Richbedroom = True
                        In_Room2 = False
                        In_Main_Room = False
                        print(In_Richbedroom)
                        print(In_Room2)
                        print(In_Main_Room)
                        Current_Room = ("richbedroom")
                    elif Current_Room == ("Room2"):
                        In_Main_Room = True
                        In_Room2 = False
                        In_Richbedroom = False
                        Current_Room = ("main")
                    elif Current_Room == ("richbedroom"):
                        In_RichBedroom = True
                        In_Main_Room = False
                        In_Room2 = False

                if Hitbox_Of_Rotated_And_Scaled_NextRoomButton2 == Rotated_And_Scaled_NextRoomButton2.get_rect():
                    Hitbox_Of_Rotated_And_Scaled_NextRoomButton2.center = (100, 853)
                # Left Arrow
                if Hitbox_Of_Rotated_And_Scaled_NextRoomButton2.collidepoint(event.pos):
                    if Current_Room == ("main"):
                        In_Room2 = True
                        In_Main_Room = False
                        In_RichBedroom = False
                        Current_Room = ("Room2")
                    elif Current_Room == ("richbedroom"):
                        In_Main_Room = True
                        In_Room2 = False
                        In_RichBedroom = False
                        Current_Room = ("main")
                        Looking_At_Lock = False
                Hitbox_Of_Rotated_And_Scaled_NextRoomButton = Rotated_And_Scaled_NextRoomButton.get_rect()
                Hitbox_Of_Rotated_And_Scaled_NextRoomButton.center = (1778, 853)
                print (Hitbox_Of_Rotated_And_Scaled_NextRoomButton)
                #Lock Hitbox
                Hitbox_Of_Scaled_Lock = Scaled_Lock.get_rect()
                Hitbox_Of_Scaled_Lock.center = (235, 410)
                #Slot 1 hitbox
                Hitbox_Of_Scaled_Lock_Slot1 = Scaled_Black_Rectangle.get_rect()
                Hitbox_Of_Scaled_Lock_Slot1.center = (585, 850)
                mask = pygame.mask.from_surface(Scaled_Black_Rectangle)
                auto_outline = mask.outline()
                auto_outline_image = pygame.Surface(Hitbox_Of_Scaled_Lock_Slot1.size).convert_alpha()
                auto_outline_image.fill((8, 189, 7))
                for point in auto_outline:
                    auto_outline_image.set_at(point, (255, 255, 255))
                #Slot 2 hitbox
                Hitbox_Of_Scaled_Lock_Slot2 = Scaled_Black_Rectangle.get_rect()
                Hitbox_Of_Scaled_Lock_Slot2.center = (700, 850)
                #Slot 3 hitbox
                Hitbox_Of_Scaled_Lock_Slot3 = Scaled_Black_Rectangle.get_rect()
                Hitbox_Of_Scaled_Lock_Slot3.center = (830, 850)
                #Slot 4 hitbox
                Hitbox_Of_Scaled_Lock_Slot4 = Scaled_Black_Rectangle.get_rect()
                Hitbox_Of_Scaled_Lock_Slot4.center = (947,850)
                #Scaled Key hitbox

                if Looking_At_Lock == True:
                #Scaled hitbox
                    if Hitbox_Of_Scaled_Lock_Slot1.collidepoint(event.pos):
                        Slot_1_List[0] += 1
                    if Slot_1_List[0] == 10:
                            Slot_1_List[0] = 0
                    if Hitbox_Of_Scaled_Lock_Slot2.collidepoint(event.pos):
                        Slot_1_List[1] += 1
                        if Slot_1_List[1] == 10:
                            Slot_1_List[1] = 0
                        # Slot 3
                    if Hitbox_Of_Scaled_Lock_Slot3.collidepoint(event.pos):
                        Slot_1_List[2] += 1
                    if Slot_1_List[2] == 10:
                        Slot_1_List[2] = 0
                        # Slot 4
                    if Hitbox_Of_Scaled_Lock_Slot4.collidepoint(event.pos):
                        Slot_1_List[3] += 1
                        if Slot_1_List[3] == 10:
                            Slot_1_List[3] = 0
                if Hitbox_Of_Scaled_Lock.collidepoint(event.pos)and Clicked_Key == True:
                    Looking_At_Lock = True

                Hitbox_Of_Scaled_Key = Scaled_Key.get_rect()
                Hitbox_Of_Scaled_Key.center = (580, 310)
                if Hitbox_Of_Scaled_Key.collidepoint(event.pos):
                    Clicked_Key = True

        if In_Main_Room == True:
            print("hi")
            Screen_Dimensions.blit(Scaled_Main_Room, (0, 0))
            if Clicked_Key == True:
                Screen_Dimensions.blit(Scaled_Key2, (1710, 38))
        elif In_Room2 == True:
            Screen_Dimensions.blit(Scaled_Room2, (0, 0))
            Screen_Dimensions.blit(CANT_LEAVE, (90, 925))
            if Clicked_Key == False:
                    Screen_Dimensions.blit(Scaled_Key, (580, 310))
            if Clicked_Key == True:
                Screen_Dimensions.blit(Scaled_Key2, (1710, 38))
        elif In_RichBedroom == True:
            Screen_Dimensions.blit(Scaled_RichBedroom, (0, 0))
            Screen_Dimensions.blit(Scaled_Lock, (215, 360))
            if Looking_At_Lock == True:
                Screen_Dimensions.blit(InsideLock, (400, 200))
                Screen_Dimensions.blit(Scaled_Black_Rectangle2, (525, 755))
                Screen_Dimensions.blit(Scaled_Black_Rectangle, (885, 755))
                Screen_Dimensions.blit(Scaled_Black_Rectangle3, (645, 755))
                Screen_Dimensions.blit(Scaled_Black_Rectangle4, (765, 755))
                Number = Comic_Font3.render(str(Slot_1_List[0]), True, (white))
                Screen_Dimensions.blit(Number, (550, 755))
                Number2 = Comic_Font3.render(str(Slot_1_List[1]), True, (white))
                Screen_Dimensions.blit(Number2, (660, 755))
                Number3 = Comic_Font3.render(str(Slot_1_List[2]), True, (white))
                Screen_Dimensions.blit(Number3, (775, 755))
                Number4 = Comic_Font3.render(str(Slot_1_List[3]), True, (white))
                Screen_Dimensions.blit(Number4, (900, 755))
                if Slot_1_List[0] == 3 and Slot_1_List[1] == 5 and Slot_1_List[2] == 7 and Slot_1_List[3] == 9:
                    Won_Game = True
            Screen_Dimensions.blit(CANT_LEAVE, (1550, 925))
            if Clicked_Key == True:
                Screen_Dimensions.blit(Scaled_Key2, (1710, 38))
        Screen_Dimensions.blit(Rotated_And_Scaled_NextRoomButton,(1778, 853))
        Screen_Dimensions.blit(Rotated_And_Scaled_NextRoomButton2, (-136, 853))
        Screen_Dimensions.blit(message, (1410, 30))
        Screen_Dimensions.blit(message2, (750, 950))
        pygame.draw.circle(Screen_Dimensions, (195, 94, 36), (1860, 60), 48, 10)
        pygame.draw.circle(Screen_Dimensions, (195, 94, 36), (1860, 180), 48, 10)
        pygame.draw.circle(Screen_Dimensions, (195, 94, 36), (1740, 60), 48, 10)
        if Hitbox_Of_Scaled_Key.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif Hitbox_Of_Scaled_Lock.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif Hitbox_Of_Rotated_And_Scaled_NextRoomButton.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif Hitbox_Of_Rotated_And_Scaled_NextRoomButton2.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.update()