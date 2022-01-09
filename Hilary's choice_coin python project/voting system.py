print('The choice coin voting session has started!!!!!')

print('------------------------------------------------')

print ('should we continue with the proposal method')
nominee_1 = 'yes'
nominee_2 = 'no'

nom_1_votes = 0
nom_2_votes = 0

votes_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter = len(votes_id)

while True:
    voter = int(input('enter your voter id no:'))
    if votes_id ==[]:
        print('voting session over')
        if nom_1_votes >nom_2_votes:
            percent = (nom_1_votes/num_of_voter)*100
            print(nominee_1, 'has won', 'with', percent, '% votes')
            break
        if nom_2_votes > nom_1_votes:
            percent = (nom_2_votes/num_of_voter)*100
            print(nominee_2, 'has won', 'with', percent, '% votes')
            break
    else:
        if voter in votes_id:
            print('you are a voter')
            votes_id.remove(voter)
            vote = int(input('enter your vote 1 for yes, 2 for no: '))
            if vote==1:
                nom_1_votes+=1
                print('thank you for voting')

            elif vote == 2:
                nom_2_votes+=1
                print('thanks for voting')

            else:
                print('you are not a voter here or you have already voted')

        