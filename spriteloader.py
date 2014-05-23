#!/usr/bin/python

import pygame


def sprite_sheet(size, file, pos=(0, 0), color_key=(0, 0, 0)):

    #Initial Values
    len_sprite_x, len_sprite_y = size  # sprite size
    sprite_rect_x, sprite_rect_y = pos  # where to find first sprite on sheet

    sheet = pygame.image.load(file).convert_alpha()  # Load the sheet
    sheet.set_colorkey(color_key)
    sheet_rect = sheet.get_rect()
    sprites = []
    #print(sheet_rect.width, sheet_rect.height)
    for i in range(0, (sheet_rect.height-len_sprite_y) + 1, size[1]):  # rows
        #print("row")
        for j in range(0, (sheet_rect.width-len_sprite_x) + 1, size[0]):  # columns
            #print("column")
            sheet.set_clip(pygame.Rect(sprite_rect_x, sprite_rect_y, len_sprite_x, len_sprite_y))  # find sprite you want
            sprite = sheet.subsurface(sheet.get_clip())  # grab the sprite you want
            sprites.append(sprite)
            sprite_rect_x += len_sprite_x

        sprite_rect_y += len_sprite_y
        sprite_rect_x = 0
    #print(sprites)
    return sprites