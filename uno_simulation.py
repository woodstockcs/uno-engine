import time

player_names = []

def main():
    #TODO: get basic game info from user
    
    print("hello")
    result = playGame()
    print("winner:", result)
    print("goodbye")

def playGame():
    print("playing the game...")
    time.sleep(1)
    print("finished the game!")
    winner = "someone"
    return winner

if __name__ == '__main__':
    main()
