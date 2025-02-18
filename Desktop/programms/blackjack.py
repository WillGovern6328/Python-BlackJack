import random, time
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

Game = True

console = Console()

HowManyChips = ("\n[white]How Many Dallars Worth of Chips Would You Like to Buy[/white]")
YourBalence = ("\nYour Bance:")

ChipTotal = int(input(console.print(HowManyChips)))

console.print(YourBalence,"$",ChipTotal)

while Game == True:
    YourCardsTitle = ("[underline][blue]Your Cards[/blue][/underline]")
    DealersCardsTitle = ("[underline][yellow]Dealers Cards[/yellow][/underline]")

    Drawing = True
    YourCards = Table(title=YourCardsTitle)
    DrawCardTotal = 0
    DrawValue = 0
    YourDrawValueTotal = 0
    DealersDrawValueTotal = 0
    AceDraw = False
    HighAce = False
    DrawCount = 0
    DrawAgainPrompt = False
    DealersCards = Table(title=DealersCardsTitle)
    YourTurn = False
    DealersTurn = False
    Stay = False
    Flip = False
    DealersCardsFliped = Table(title=DealersCardsTitle)
    Bust = False
    DealerBust = False
    PlayerHighAce = False
    DealersHighAce = False
    PlayerBlackJack = False
    DealerBlackJack = False
    BlackJackCalus = False

    YouPulled=("\n[blue]You Pulled[/blue]")
    YourCardValue = ("\n[blue]Your Card Value:[/blue]")
    YouBusted = ("\n[blue]You Busted[/blue]")
    WouldYouLikeToHit = ("\n[blue]Would You Like to Hit[/blue]")
    DrawingAgain = ("\n[blue]Drawing Again[/blue]")
    FinishedDrawing = ("\n[blue]Finished Drawing[/blue]")
    InvaledInput = ("\n[blue]invaled input, Please enter Yes or No[/blue]")
    PlayerGotBlackJack = ("\n[blue]You Got BlackJack[/blue]")
    
    PlayAgainInvaledInput = ("\n[white]invaled input, Please enter Yes or No[/white]")
    WouldYouLikeToPlay = ("\n[white]Would You Like to Play Again[/white]")
    BetPrompt = ("\n[white]How Many Dollers Would You LIke to Bet on This Hand[/white]")

    TheDealersCardValue = ("\n[yellow]The Dealers Card Value:[/yellow]")
    DealerBusted = ("\n[yellow]The Dealer Busted[/yellow]")
    DealerMustStay=("\n[yellow]The Dealer Must Stay[/yellow]")
    DealerPulled = ("\n[yellow]The Dealer Pulled[/yellow]")
    DealerGotBlackJack = ("\n[yellow]The Dealer Got BlackJack[/yellow]")

    YouLose = ("\n[red]You Lose[/red]")
    YouWin = ("\n[green]You Win[/green]")
    Push = ("\n[magenta]Push[/magenta]")


    Club = ("[white]:shamrock:[/white]")
    Spade = ("[white]:spades:[/white]")
    Diomond = (":large_orange_diamond:")
    Heart = ("[orange_red1]:hearts:[/orange_red1]") 
    WhiteTwo = ("[bold][white]2[/white][/bold]")
    RedTwo = ("[bold][orange_red1]2[/orange_red1][/bold]")
    WhiteThree = ("[bold][white]3[/white][/bold]")
    RedThree =   ("[bold][orange_red1]3[/orange_red1][/bold]")
    WhiteFour = ("[bold][white]4[/white][/bold]") 
    RedFour  = ("[bold][orange_red1]4[/orange_red1][/bold]")
    WhiteFive = ("[bold][white]5[/white][/bold]") 
    RedFive  = ("[bold][orange_red1]5[/orange_red1][/bold]")
    WhiteSix = ("[bold][white]6[/white][/bold]")
    RedSix  = ("[bold][orange_red1]6[/orange_red1][/bold]")
    WhiteSeven = ("[bold][white]7[/white][/bold]")
    RedSeven   = ("[bold][orange_red1]7[/orange_red1][/bold]")
    WhiteEight = ("[bold][white]8[/white][/bold]")
    RedEight  = ("[bold][orange_red1]8[/orange_red1][/bold]")
    WhiteNine = ("[bold][white]9[/white][/bold]")
    RedNine  = ("[bold][orange_red1]9[/orange_red1][/bold]")
    WhiteTen = ("[bold][white]10[/white][/bold]")
    RedTen  = ("[bold][orange_red1]10[/orange_red1][/bold]")
    WhiteJ = ("[bold][white]J[/white][/bold]")
    RedJ  = ("[bold][orange_red1]J[/orange_red1][/bold]")
    WhiteQ = ("[bold][white]Q[/white][/bold]")
    RedQ  = ("[bold][orange_red1]Q[/orange_red1][/bold]")
    WhiteK = ("[bold][white]K[/white][/bold]")
    RedK = ("[bold][orange_red1]K[/orange_red1][/bold]")
    WhiteA = ("[bold][white]A[/white][/bold]")
    RedA = ("[bold][orange_red1]A[/orange_red1][/bold]")


    TwoOfClubs = WhiteTwo + Club
    TwoOfHearts =RedTwo + Heart
    TwoOfSpades =WhiteTwo + Spade
    TwoOfDimonds =RedTwo + Diomond
    ThreeOfClubs = WhiteThree + Club
    ThreeOfHearts =RedThree + Heart
    ThreeOfSpades =WhiteThree + Spade
    ThreeOfDimonds =RedThree + Diomond
    FourOfClubs = WhiteFour + Club 
    FourOfHearts =RedFour + Heart
    FourOfSpades =WhiteFour + Spade
    FourOfDimonds =RedFour + Diomond
    FiveOfClubs =WhiteFive + Club
    FiveOfHearts =RedFive + Heart
    FiveOfSpades =WhiteFive + Spade
    FiveOfDimonds =RedFive + Diomond
    SixOfClubs =WhiteSix + Club
    SixOfHearts =RedSix + Heart
    SixOfSpades =WhiteSix + Spade
    SixOfDimonds =RedSix + Diomond
    SevenOfClubs =WhiteSeven + Club
    SevenOfHearts =RedSeven + Heart
    SevenOfSpades =WhiteSeven + Spade
    SevenOfDimonds =RedSeven + Diomond
    EightOfClubs =WhiteEight + Club
    EightOfHearts =RedEight + Heart
    EightOfSpades =WhiteEight + Spade
    EightOfDimonds =RedEight + Diomond
    NineOfClubs =WhiteNine+Club
    NineOfHearts =RedNine+Heart
    NineOfSpades =WhiteNine+Spade  
    NineOfDimonds =RedNine+Diomond
    TenOfClubs =WhiteTen+Club
    TenOfHearts = RedTen+Heart
    TenOfSpades =WhiteTen+Spade
    TenOfDimonds =RedTen+Diomond
    JackOfClubs =WhiteJ+Club
    JackOfHearts =RedJ+Heart
    JackOfSpades =WhiteJ+Spade
    JackOfDimonds =RedJ+Diomond
    QueenOfClubs =WhiteQ+Club
    QueenOfHearts =RedQ+Heart
    QueenOfSpades =WhiteQ+Spade
    QueenOfDimonds =RedQ+Diomond
    KingOfClubs =WhiteK+Club
    KingOfHearts =RedK+Heart
    KingOfSpades =WhiteK+Spade
    KingOfDimonds =RedK+Diomond
    AceOfClubs =WhiteA+Club
    AceOfHearts =RedA+Heart
    AceOfSpades =WhiteA+Spade
    AceOfDimonds =RedA+Diomond

    YourBet = int(input(console.print(BetPrompt)))

    def LostBet():
        YourWin = 0 - YourBet
        return YourWin
    
    def WonBet():
        YourWin = YourBet 
        return YourWin
    
    def TieBet():
        YourWin = 0
        return YourWin
    
    def BlackJackBet():
        YourWin = YourBet*1.5
        return YourWin


    Deck=list(range(1,53))


    while Drawing == True:
        DrawCard = random.choice(Deck)
        if DrawCard == 1:
            DrawnCard = TwoOfClubs
            Deck.remove(1)
        if DrawCard == 2:
            DrawnCard = TwoOfDimonds
            Deck.remove(2)
        if DrawCard == 3:
            DrawnCard = TwoOfHearts
            Deck.remove(3)
        if DrawCard == 4:
            DrawnCard = TwoOfSpades
            Deck.remove(4)
        if 1<= DrawCard <=4: 
            DrawValue =2
    
        if DrawCard == 5:
            DrawnCard = ThreeOfClubs
            Deck.remove(5)
        if DrawCard == 6:
            DrawnCard = ThreeOfDimonds
            Deck.remove(6)
        if DrawCard == 7:
            DrawnCard = ThreeOfHearts
            Deck.remove(7)
        if DrawCard == 8:
            DrawnCard = ThreeOfSpades
            Deck.remove(8)
        if 5<= DrawCard <=8: 
            DrawValue =3
        
        if DrawCard == 9:
            DrawnCard = FourOfClubs
            Deck.remove(9)
        if DrawCard == 10:
            DrawnCard = FourOfDimonds
            Deck.remove(10)
        if DrawCard == 11:
            DrawnCard = FourOfHearts
            Deck.remove(11)
        if DrawCard == 12:
            DrawnCard = FourOfSpades
            Deck.remove(12)
        if 9<= DrawCard <=12: 
            DrawValue =4
        
        if DrawCard == 13:
            DrawnCard = FiveOfClubs
            Deck.remove(13)
        if DrawCard == 14:
            DrawnCard = FiveOfDimonds
            Deck.remove(14)
        if DrawCard == 15:
            DrawnCard = FiveOfHearts
            Deck.remove(15)
        if DrawCard == 16:
            DrawnCard = FiveOfSpades
            Deck.remove(16)
        if 13<= DrawCard <=16: 
            DrawValue =5
        
        if DrawCard == 17:
            DrawnCard = SixOfClubs
            Deck.remove(17)
        if DrawCard == 18:
            DrawnCard = SixOfDimonds
            Deck.remove(18)
        if DrawCard == 19:
            DrawnCard = SixOfHearts
            Deck.remove(19)
        if DrawCard == 20:
            DrawnCard = SixOfSpades
            Deck.remove(20)
        if 17<= DrawCard <=20: 
            DrawValue =6
        
        if DrawCard == 21:
            DrawnCard = SevenOfClubs
            Deck.remove(21)
        if DrawCard == 22:
            DrawnCard = SevenOfDimonds
            Deck.remove(22)
        if DrawCard == 23:
            DrawnCard = SevenOfHearts
            Deck.remove(23)
        if DrawCard == 24:
            DrawnCard = SevenOfSpades
            Deck.remove(24)
        if 21<= DrawCard <=24: 
            DrawValue =7
        
        if DrawCard == 25:
            DrawnCard = EightOfClubs
            Deck.remove(25)
        if DrawCard == 26:
            DrawnCard = EightOfDimonds
            Deck.remove(26)
        if DrawCard == 27:
            DrawnCard = EightOfHearts
            Deck.remove(27)
        if DrawCard == 28:
            DrawnCard = EightOfSpades
            Deck.remove(28)
        if 25<= DrawCard <=28: 
            DrawValue =8
        
        if DrawCard == 29:
            DrawnCard = NineOfClubs
            Deck.remove(29)
        if DrawCard == 30:
            DrawnCard = NineOfDimonds
            Deck.remove(30)
        if DrawCard == 31:
            DrawnCard = NineOfHearts
            Deck.remove(31)
        if DrawCard == 32:
            DrawnCard = NineOfSpades
            Deck.remove(32)
        if 29<= DrawCard <=32: 
            DrawValue =9
        
        if DrawCard == 33:
            DrawnCard = TenOfClubs
            Deck.remove(33)
        if DrawCard == 34:
            DrawnCard = TenOfDimonds
            Deck.remove(34)
        if DrawCard == 35:
            DrawnCard = TenOfHearts
            Deck.remove(35)
        if DrawCard == 36:
            DrawnCard = TenOfSpades
            Deck.remove(36)
        
        if DrawCard == 37:
            DrawnCard = JackOfClubs
            Deck.remove(37)
        if DrawCard == 38:
            DrawnCard = JackOfDimonds
            Deck.remove(38)
        if DrawCard == 39:
            DrawnCard = JackOfHearts
            Deck.remove(39)
        if DrawCard == 40:
            DrawnCard = JackOfSpades
            Deck.remove(40)
        
        if DrawCard == 41:
            DrawnCard = QueenOfClubs
            Deck.remove(41)
        if DrawCard == 42:
            DrawnCard = QueenOfDimonds
            Deck.remove(42)
        if DrawCard == 43:
            DrawnCard = QueenOfHearts
            Deck.remove(43)
        if DrawCard == 44:
            DrawnCard = QueenOfSpades
            Deck.remove(44)
        
        if DrawCard == 45:
            DrawnCard = KingOfClubs
            Deck.remove(45)
        if DrawCard == 46:
            DrawnCard = KingOfDimonds
            Deck.remove(46)
        if DrawCard == 47:
            DrawnCard = KingOfHearts
            Deck.remove(47)
        if DrawCard == 48:
            DrawnCard = KingOfSpades
            Deck.remove(48)
            
        if 33<= DrawCard <=48: 
            DrawValue =10
        
        if DrawCard == 49:
            DrawnCard = AceOfClubs
            Deck.remove(49)
        if DrawCard == 50:
            DrawnCard = AceOfDimonds
            Deck.remove(50)
        if DrawCard == 51:
            DrawnCard = AceOfHearts
            Deck.remove(51)
        if DrawCard == 52:
            DrawnCard = AceOfSpades
            Deck.remove(52)
        if 49<= DrawCard <=52:     
            DrawValue =1         
            AceDraw = True
        
        DrawCount = DrawCount + 1

        if DrawCount == 1:
            YourTurn = True
        
        if DrawCount ==2:
            YourTurn = False
            DealersTurn = True
        
        if DrawCount == 3:
            DealersTurn = False
            YourTurn = True
        
        if DrawCount == 4:
            DealersTurn = True
            YourTurn = False

        if YourTurn == True:
            
            YourDrawValueTotal=YourDrawValueTotal+ DrawValue
            console.print(YouPulled, DrawnCard)
            time.sleep(1)
            YourCards.add_column(DrawnCard)
            console.print("\n", YourCards)
            time.sleep(1)
        
            if YourDrawValueTotal <=11 and AceDraw == True:
                YourAceDrawTotal = YourDrawValueTotal +10
                PlayerHighAce = True
                
                if 22 > YourAceDrawTotal:
                    YourDrawValueTotal = YourAceDrawTotal
            
            if YourDrawValueTotal > 21 and PlayerHighAce == True:
                YourDrawValueTotal = YourDrawValueTotal - 10
                PlayerHighAce = False

            AceDraw = False
            
            console.print(YourCardValue,YourDrawValueTotal)
            time.sleep(1) 
            
            if YourDrawValueTotal > 21:
                console.print(YouBusted)
                time.sleep(1)
                Drawing = False
                Bust = True
            
            if YourDrawValueTotal == 21 and DrawCount == 3:
                PlayerBlackJack = True
                console.print(PlayerGotBlackJack)
                time.sleep(1)
            
            if DrawnCard == 3:
                YourTurn = False
        
        if DealersTurn == True:

            if DrawCount > 4 and Flip == False:
                DealersDrawValueTotal = DealersDrawValueTotal + FaceDownCardValue
                console.print("\n",DealersCards, DealersCardsFliped)
                time.sleep(1)
                Flip = True

                if FaceDownCard == AceOfClubs:
                    AceDraw = True

                if FaceDownCard == AceOfDimonds:
                    AceDraw = True

                if FaceDownCard == AceOfHearts:
                    AceDraw = True

                if FaceDownCard == AceOfSpades:
                    AceDraw = True

                if DealersDrawValueTotal <=11 and AceDraw == True:
                    DealersAceDrawTotal = DealersDrawValueTotal +10
                    DealersHighAce = True
                
                    if 22 > DealersAceDrawTotal:
                        DealersDrawValueTotal = DealersAceDrawTotal
            
                if DealersDrawValueTotal > 21 and DealersHighAce == True:
                    DealersDrawValueTotal = DealersDrawValueTotal - 10
                    DealersHighAce = False
                
                AceDraw = False
                

                
                console.print(TheDealersCardValue,DealersDrawValueTotal)
                time.sleep(1)

                if DealersDrawValueTotal == 21:
                    DealerBlackJack = True
                    console.print(DealerGotBlackJack)
                    time.sleep(1)
                    Drawing = False

                if DealersDrawValueTotal > 21:
                    console.print(DealerBusted)
                    time.sleep(1)
                    Drawing = False
                    DealerBust = True
                
                if DealersDrawValueTotal > 16 and Drawing == True:
                    console.print(DealerMustStay)
                    time.sleep(1)
                    Drawing = False
                
            
            if DrawCount == 2:
                FaceDownCardValue = DrawValue
                FaceDownCard = DrawnCard
                console.print(DealerPulled,"?")
                time.sleep(1)
                DealersCards.add_column("?")
                console.print("\n",DealersCards)
                time.sleep(1)
                DealersCardsFliped.add_column(FaceDownCard)
                
                if FaceDownCard == AceOfClubs:
                    AceDraw = False

                if FaceDownCard == AceOfDimonds:
                    AceDraw = False

                if FaceDownCard == AceOfHearts:
                    AceDraw = False

                if FaceDownCard == AceOfSpades:
                    AceDraw = False

            
            else:
                if Drawing == True:
                    DealersDrawValueTotal = DealersDrawValueTotal + DrawValue
                    console.print(DealerPulled, DrawnCard)
                    time.sleep(1)
                    DealersCards.add_column(DrawnCard)
                    DealersCardsFliped.add_column(DrawnCard)

                    if Flip == False:
                        console.print("\n",DealersCards)
                        time.sleep(1)
                    
                    if Flip == True:
                        console.print("\n", DealersCardsFliped)
                        time.sleep(1)
                    
                    if PlayerBlackJack == True:
                        DealersDrawValueTotal = DealersDrawValueTotal + FaceDownCardValue
                        console.print("\n",DealersCards, DealersCardsFliped)
                        time.sleep(1)
                        Flip = True

                        if FaceDownCard == AceOfClubs:
                            AceDraw = True

                        if FaceDownCard == AceOfDimonds:
                            AceDraw = True

                        if FaceDownCard == AceOfHearts:
                            AceDraw = True

                        if FaceDownCard == AceOfSpades:
                            AceDraw = True
                    
                    if DealersDrawValueTotal <=11 and AceDraw == True:
                        DealersAceDrawTotal = DealersDrawValueTotal +10
                        DealersHighAce = True
                    
                        if 22 > DealersAceDrawTotal:
                            DealersDrawValueTotal = DealersAceDrawTotal
                
                    if DealersDrawValueTotal > 21 and DealersHighAce == True:
                        DealersDrawValueTotal = DealersDrawValueTotal - 10
                        DealersHighAce = False
                    
                    AceDraw = False

                    console.print(TheDealersCardValue,DealersDrawValueTotal)
                    time.sleep(1)

                    
                    if DealersDrawValueTotal == 21 and DrawCount == 4:
                        DealerBlackJack = True
                        console.print(DealerGotBlackJack)
                        time.sleep(1)
                        Drawing = False
                    
                    if PlayerBlackJack == True:
                        Drawing = False

                    if DealersDrawValueTotal > 21:
                        console.print(DealerBusted)
                        time.sleep(1)
                        Drawing = False
                        DealerBust = True
                    
                    if DealersDrawValueTotal > 16 and Drawing == True:
                        console.print(DealerMustStay)
                        time.sleep(1)
                        Drawing = False
                


        
        if Drawing ==True and Stay == False and DrawCount > 3:
            DrawAgainPrompt = True
        
        while DrawAgainPrompt == True:
            DrawAgain = input(console.print(WouldYouLikeToHit)).strip().lower()
            time.sleep(1)
            if DrawAgain == "yes":
                console.print(DrawingAgain)
                time.sleep(1)
                DrawAgainPrompt = False
                YourTurn = True
                DealersTurn = False
            elif DrawAgain == "no":
                console.print(FinishedDrawing)
                time.sleep(1)
                YourTurn = False
                DrawAgainPrompt = False
                DealersTurn = True
                Stay = True
            else:
                console.print(InvaledInput)
                time.sleep(1)

    console.print("\n",YourCards)
    console.print(YourCardValue, YourDrawValueTotal)

    if Flip == False:
        console.print("\n",DealersCards)

    if Flip == True:
        console.print("\n",DealersCardsFliped)

    console.print(TheDealersCardValue, DealersDrawValueTotal)

    if PlayerBlackJack == True or DealerBlackJack == True:
        BlackJackCalus = True

    if DealersDrawValueTotal > YourDrawValueTotal and DealerBust == False:
        console.print(YouLose)
        time.sleep(1)
        LostBet()
        YourWin = LostBet() 
    if Bust == True:
        console.print(YouLose)
        time.sleep(1)
        LostBet()
        YourWin = LostBet()
    if DealerBlackJack == True and PlayerBlackJack == False:
        console.print(YouLose)
        time.sleep(1)
        LostBet()
        YourWin = LostBet()
    if DealersDrawValueTotal < YourDrawValueTotal and Bust == False and PlayerBlackJack == False:
        console.print(YouWin)
        time.sleep(1)
        WonBet()
        YourWin = WonBet()
    if DealerBust == True:
        console.print(YouWin)
        time.sleep(1)
        WonBet()
        YourWin = WonBet()
    if PlayerBlackJack == True and DealerBlackJack == False:
        console.print(YouWin)
        time.sleep(1)
        BlackJackBet()
        YourWin = BlackJackBet()
    if DealersDrawValueTotal == YourDrawValueTotal and BlackJackCalus == False:
        console.print(Push)
        time.sleep(1)
        TieBet()
        YourWin = TieBet()
    if DealerBust == True and Bust == True:
        console.print(Push)
        time.sleep(1)
        TieBet()
        YourWin = TieBet()
    if PlayerBlackJack == True and DealerBlackJack == True:
        console.print(Push)
        time.sleep(1)
        TieBet()
        YourWin = TieBet()
    
    console.print("\n$",YourWin)
    time.sleep(1)

    ChipTotal = ChipTotal + YourWin
    console.print(YourBalence,"$",ChipTotal)

    
    PlayAgainPrompt = True
    
    while PlayAgainPrompt == True:

        playagain = input(console.print(WouldYouLikeToPlay)).strip().lower()

        if playagain == "yes":
            Game = True
            time.sleep(1)
            PlayAgainPrompt = False

        elif playagain == "no":
            Game = False
            time.sleep(1)
            PlayAgainPrompt = False

        else:
            console.print(PlayAgainInvaledInput)
            time.sleep(1)


#add assets: complete
# add timeing: complete
# add fonts: complete
# add ace rules to delaer: complete 
# add blackjack: complete
# show to friends: complete
# play again: complete
# gambleing: complete
# add buy in: complete
# rebuy
#add wins and losses
# add win percent
# add card count
# add reshuffle

# git change test 