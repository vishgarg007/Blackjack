# Blackjack
import random
import time
def main():
    print("\nWelcome to Blackjack!")
    print(50 * "_")
    while True:
        input_a = input("\nDo you wish to start a new game? (y/n): ")
        while True:
            if input_a in ["Y", "y"]:
                p_card1 = int(random.randint(1, 10))
                p_card2 = int(random.randint(1, 10))
                player = p_card1 + p_card2
                print(f"\nYou draw a {p_card1} and a {p_card2}. Your total is {player}.")
                d_card1 = int(random.randint(1, 10))
                d_card2 = int(random.randint(1, 10))
                dealer = d_card1 + d_card2
                print(f'\nDealer draws a', d_card1, 'and a hidden card.')
                while True:
                    input_b = input("\nHit or Stand? (h/s): ")
                    if input_b not in ["H", "h", "S", "s"]:
                        print ("Incorrect entry. Please try again")
                    if input_b in ["H", "h"]:
                        p_card3 = int(random.randint(1, 10))
                        player = player + p_card3
                        print(f"\nHit! You draw a {p_card3} and your total is {player}.")
                        if player > 21:
                                print("\nSorry you busts and Dealer wins!")
                                break
                        continue
                    if player == 21 or input_b in ["S", "s"]:
                        print("\nYou Stand!")
                        time.sleep(2)
                        print(f"\nDealer reveals hidden card of {d_card2} and has a total of {dealer}.")
                        time.sleep(2)
                        while True:
                            if dealer <= 16:
                                print("\nThe Dealer hits!")
                                time.sleep(2)
                                d_card3 = int(random.randint(1, 10))
                                dealer = dealer + d_card3
                                print(f"\nThe dealer is dealt a {d_card3}. The dealer's total is {dealer}.")
                                time.sleep(2)
                            elif dealer >= 17 or dealer <= 21:
                                print("\nDealer Stand!")
                                time.sleep(2)
                                print(f"\nYou have a total of {player} and dealer has a total of {dealer}.")
                                if dealer >= player and dealer <= 21:
                                    time.sleep(2)
                                    print("\nDealer Wins")
                                    break
                                elif dealer > 21:
                                    print("\nDealer busts and You Win!")
                                    break
                                else:
                                    time.sleep(2)
                                    print("\nYou Win!")
                                    break
                            continue
                    break
                break
            elif input_a in ["N", "n"]:
                print("\nThank you for visiting Python Casino.\nWe hope to see you again!\nGood Bye!\n")
                exit()
            else:
                print("Incorrect entry. Please try again\n")
                break
            break
        print(50 * "_", "\n")
        continue
if __name__ == '__main__':
    main()
