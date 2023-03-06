import signal

def handler(signum, frame):
    print("Somatorio final: " + str(sum))
    global cont1
    cont = False

def main():
    print("Systema iniciado no modo (OFF)")
    estate = "OFF"
    global sum
    signal.signal(signal.SIGINT, handler)
    while cont:
        value = input()
        if value.isdigit():
            if estate == "ON":
                sum += int(value) 
        else:
            if value == "=":
                print("Somatorio atual: "+ str(sum))
            else:
                estate = value.upper()

cont = True 
sum = 0
main()