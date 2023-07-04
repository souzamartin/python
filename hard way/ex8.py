# defines variable as string of 4 insertion anchors
formatter = "{} {} {} {}"

# prints string from variable, calls format to insert numbers 1–4
print(formatter.format(1, 2, 3, 4))
# prints string from variable, calls format to insert 4 strings in succession
print(formatter.format("one", "two", "three", "four"))
# prints string from variable, calls format to insert series of true/false values
print(formatter.format(True, False, False, True))
# prints string from variable, calls format to insert variable itself 4 times
print(formatter.format(formatter, formatter, formatter, formatter))
# prints string from variable, calls format to insert 4 strings in succession
# here written on separate lines for convenience, but printed on 1 line
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
