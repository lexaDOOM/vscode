def main (avscore, drscore, count, mark):
    """Main def of increasing mark"""
    counter = 0 # Counter
    if (avscore > 5 or avscore < 2) or (drscore > 5 or drscore < 2):
        return 'Error: Average score and/or dream score ∉ [2; 5]'
    if avscore >= drscore: # Exception extra actions
        return 0
    else: # Main algorithm
        while avscore <= drscore:
            summ = avscore * count
            summ += mark
            count += 1
            avscore = summ / count
            counter += 1
    return counter


"""Collecting data"""
average_score = float(input('Enter average score >> '))  # Current average score
dream_score = float(input('Enter \"dream\" score >> '))  # "Dream" score
count_marks = int(input('Enter marks count >> '))  #  Current marks count
mark_for_solve = int(input('Enter mark for solving >> '))  # Mark that will be used for solving

"""Exception of infinite cycle"""
if dream_score % 1 == 0:
    round_number = 1 - float(input('Enter minimal decimal part for rounding your mark >> '))
    dream_score -= round_number

# Output of the result using 
print(main(average_score, dream_score, count_marks, mark_for_solve))
