def main():

    str=input("What time is it? ")

    fl=convert(str)

    if 7.0<=fl<=8.0:

        print("breakfast time")

    elif 12.0<=fl<=13.0:

        print("lunch time")

    elif 18.0<=fl<=19.0:

        print("dinner time")

def convert(time):

    s=time.find(":")

    k=time[s+1:len(time)]

    f= float(time[0:s]) + (float(k)/60)

    return f

if __name__=="__main__":

    main()
    