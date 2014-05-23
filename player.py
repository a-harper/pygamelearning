class Player():
    x_speed = 0
    y_speed = 0
    x_coord = 0
    y_coord = 0
    washing = False
    idle_sprites = ""
    walk_sprites = ""
    wash_sprites = ""
    image = ""
    wash_loop = 0
    frame_loop = 0


def do_updates(player, tick_rate):
    player.x_coord += player.x_speed
    player.y_coord += player.y_speed
    if player.x_coord > 1024:
        player.x_coord = 1024
    if player.x_coord < 0:
        player.x_coord = 0
    if player.y_coord > 768:
        player.y_coord = 768
    if player.y_coord < 0:
        player.y_coord = 0

    if not player.washing:
        if player.frame_loop > tick_rate / 2:
            if player.x_speed == 0 and player.y_speed == 0:
                player.image = player.idle_sprites[1]
            else:
                player.image = player.walk_sprites[1]
        else:
            if player.x_speed == 0 and player.y_speed == 0:
                player.image = player.idle_sprites[0]
            else:
                player.image = player.walk_sprites[0]
        if player.frame_loop > tick_rate:
            player.frame_loop = 0
        player.wash_loop = 0
        player.frame_loop += 1
    else:
        if player.wash_loop < len(player.wash_sprites):
            player.image = player.wash_sprites[player.wash_loop]
            player.wash_loop += 1
        else:
            player.image = player.wash_sprites[len(player.wash_sprites) - 1]
    return player