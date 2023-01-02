#!/usr/bin/python
import struct


#define KEY_RESERVED		0
#define KEY_ESC			1
#define KEY_1			2
#define KEY_2			3
#define KEY_3			4
#define KEY_4			5
#define KEY_5			6
#define KEY_6			7
#define KEY_7			8
#define KEY_8			9
#define KEY_9			10
#define KEY_0			11
#define KEY_MINUS		12
#define KEY_EQUAL		13
#define KEY_BACKSPACE		14
#define KEY_TAB			15
#define KEY_Q			16
#define KEY_W			17
#define KEY_E			18
#define KEY_R			19
#define KEY_T			20
#define KEY_Y			21
#define KEY_U			22
#define KEY_I			23
#define KEY_O			24
#define KEY_P			25
#define KEY_LEFTBRACE		26
#define KEY_RIGHTBRACE		27
#define KEY_ENTER		28
#define KEY_LEFTCTRL		29
#define KEY_A			30
#define KEY_S			31
#define KEY_D			32
#define KEY_F			33
#define KEY_G			34
#define KEY_H			35
#define KEY_J			36
#define KEY_K			37
#define KEY_L			38
#define KEY_SEMICOLON		39
#define KEY_APOSTROPHE		40
#define KEY_GRAVE		41
#define KEY_LEFTSHIFT		42
#define KEY_BACKSLASH		43
#define KEY_Z			44
#define KEY_X			45
#define KEY_C			46
#define KEY_V			47
#define KEY_B			48
#define KEY_N			49
#define KEY_M			50
#define KEY_COMMA		51
#define KEY_DOT			52
#define KEY_SLASH		53
#define KEY_RIGHTSHIFT		54
#define KEY_KPASTERISK		55
#define KEY_LEFTALT		56
#define KEY_SPACE		57
#define KEY_CAPSLOCK		58
#define KEY_F1			59
#define KEY_F2			60
#define KEY_F3			61
#define KEY_F4			62
#define KEY_F5			63
#define KEY_F6			64
#define KEY_F7			65
#define KEY_F8			66
#define KEY_F9			67
#define KEY_F10			68
#define KEY_NUMLOCK		69
#define KEY_SCROLLLOCK		70
#define KEY_KP7			71
#define KEY_KP8			72
#define KEY_KP9			73
#define KEY_KPMINUS		74
#define KEY_KP4			75
#define KEY_KP5			76
#define KEY_KP6			77
#define KEY_KPPLUS		78
#define KEY_KP1			79
#define KEY_KP2			80
#define KEY_KP3			81
#define KEY_KP0			82
#define KEY_KPDOT		83


#define KEY_F13			183
#define KEY_F14			184
#define KEY_F15			185
#define KEY_F16			186
#define KEY_F17			187
#define KEY_F18			188
#define KEY_F19			189
#define KEY_F20			190
#define KEY_F21			191
#define KEY_F22			192
#define KEY_F23			193
#define KEY_F24			194



#define KEY_KP1			79
#define KEY_KP2			80
#define KEY_KP3			81
#define KEY_KP4			75
#define KEY_KP5			76
#define KEY_KP6			77
#define KEY_KPPLUS		78
#define KEY_KP7			71
#define KEY_KP8			72
#define KEY_KP9			73
#define KEY_KP0			82

#https://github.com/kdart/pycopia/blob/1446fabaedf8c6bdd4ab1fc3f0ea731e0ef8da9d/core/pycopia/OS/Linux/event.py#L216

# define file here 
infile_path = ""

thisdict = {
    1: "esc",
    2: "&",3: "é", 4: "\"",5: "'", 6: "(", 7: "-",8: "è", 9: "_", 10: "ç", 11: "à",12: ")", 13: "=", 14: "<-", 15: "\t",
    16: "a", 17: "z", 18: "e", 19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p",26: "^", 27: "$", 28: "\n",29: "Key_CTRL",
    30: "q", 31: "s", 32: "d", 33: "f", 34: "g", 35: "h",36: "j",37: "k", 38: "l",39: "m",40: "ù",
    42: "shift",43: "/",44: "w",45: "x", 46: "c", 47: "v", 48: "b", 49: "n",
    50: ",", 51: ";", 52: ":", 53: "!", 54: "shift", 56: "alt",
    57: " ",
    74: "-",
    78: "+",79:'1',80:'2',81:'3',75:'4',76:'5',77:'6',71:'7',72:'8',73:'9',82:'0',83:'.',86:'<',96: "'enter'",
    100: "alt",
    200: "1",300: "2", 400: "3",500: "4", 600: "5", 700: "6",800: "7", 900: "8", 1000: "9", 1100: "0", 1200: "°", 1300: "+",
    1600: "A", 1700: "Z", 1800: "E", 1900: "R", 2000: "T", 2100: "Y", 2200: "U", 2300: "I", 2400: "O", 2500: "P",
    3000: "Q", 3100: "S", 3200: "D", 3300: "F", 3400: "G", 3500: "H",3600: "J",3700: "K", 3800: "L",3900: "M",4000: "%",
    4400: "W",4500: "X", 4600: "C", 4700: "V", 4800: "B", 4900: "N",
    5000: "?", 5100: ".", 5200: "/", 5300: "§",8600:'>',

    20000: "&",30000: "~", 40000: "#",50000: "{", 60000: "[", 70000: "|",80000: "`", 90000: "\\", 100000: "^", 110000: "@", 120000: "]", 130000: "}",
}


"""
FORMAT represents the format used by linux kernel input event struct
See https://github.com/torvalds/linux/blob/v5.5-rc5/include/uapi/linux/input.h#L28
Stands for: long int, long int, unsigned short, unsigned short, unsigned int
"""
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)
final = ''
lastletter = ''
while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type != 0 or code != 0 or value != 0:
        if value == 1:
            if code in thisdict:
                if lastletter != 'shift':
                    if (code >= 2 and code <= 13) and lastletter == 'alt':
                        final += thisdict[code*10000]
                    elif code != 54 and code != 42 and code != 100 and code != 56 and lastletter != '^':
                        final += thisdict[code]
                else:
                    if (code >= 2 and code <= 13) or (code >= 17 and code <= 25) or (code >= 30 and code <= 40) or (code >= 44 and code <= 49) or (code >= 50 and code <= 53) or (code == 86):
                        final += thisdict[code*100]
                    else:
                        final += thisdict[code]
                if(code == 28):
                    final += str(tv_sec)
                lastletter = thisdict[code]
            else:
                final += '"'+lastletter+'"'+str(code)+'"'
        print("Event type %u, code %u, value %s at %d.%d" % \
             (type, code, value, tv_sec, tv_usec))
        
    else:
        print("===========================================")

    event = in_file.read(EVENT_SIZE)
print(final)
in_file.close()
