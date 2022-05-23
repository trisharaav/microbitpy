def blinky_heart():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.pause(500)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
    basic.pause(500)

basic.forever(blinky_heart)