# Find who wins the tournament

# Input array is of the form:[ [homeTeam,awayTeam] ]

# results=[0,0,1] where 0 means home team lost and vice versa

# Print who wins that tournament


def tournamentWinner(competitions, results):
    # Write your code here.
	winner = ""

	tourny_score = {winner: 0}

	for i, arr in enumerate(competitions):

		if results[i] == 0:
			winner = arr[1]
			if winner in tourny_score:
				tourny_score[winner] += 3
			else:
				tourny_score[winner] = 3
		else:
			winner = arr[0]
			if winner in tourny_score:
				tourny_score[winner] += 3
			else:
				tourny_score[winner] = 3



    return max(tourny_score,key=tourny_score.get)
