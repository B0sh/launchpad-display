import random
import math
import numpy

TRANSITIONS = {
    "hilberts_curve": [
        22,	23,	26,	27,	38,	39,	42,	43,
        21,	24,	25,	28,	37,	40,	41,	44,
        20,	19,	30,	29,	36,	35,	46,	45,
        17,	18,	31,	32,	33,	34,	47,	48,
        16,	13,	12,	11,	54,	53,	52,	49,
        15,	14,	9,	10,	55,	56,	51,	50,
        2,	3,	8,	7,	58,	57,	62,	63,
        1,	4,	5,	6,	59,	60,	61,	64
    ],

    "circle_out": [
        8,	9,	10,	11,	12,	13,	14,	15,
        7,	34,	35,	36,	37,	38,	39,	16,
        6,	33,	52,	53,	54,	55,	40,	17,
        5,	32,	51,	62,	63,	56,	41,	18,
        4,	31,	50,	61,	64,	57,	42,	19,
        3,	30,	49,	60,	59,	58,	43,	20,
        2,	29,	48,	47,	46,	45,	44,	21,
        1,	28,	27,	26,	25,	24,	23,	22
    ],

    "circle_in": [
        57,	56,	55,	54,	53,	52,	51,	50,
        58,	31,	30,	29,	28,	27,	26,	49,
        59,	32,	13,	12,	11,	10,	25,	48,
        60,	33,	14,	3,	2,	9,	24,	47,
        61,	34,	15,	4,	1,	8,	23,	46,
        62,	35,	16,	5,	6,	7,	22,	45,
        63,	36,	17,	18,	19,	20,	21,	44,
        64,	37,	38,	39,	40,	41,	42,	43
    ],

    "diagonal": [
        1,	3,	6,	10,	15,	21,	28,	36,
        2,	5,	9,	14,	20,	27,	35,	43,
        4,	8,	13,	19,	26,	34,	42,	49,
        7,	12,	18,	25,	33,	41,	48,	54,
        11,	17,	24,	32,	40,	47,	53,	58,
        16,	23,	31,	39,	46,	52,	57,	61,
        22,	30,	38,	45,	51,	56,	60,	63,
        29,	37,	44,	50,	55,	59,	62,	64
    ],

    "straight_across": [
        1,	2,	3,	4,	5,	6,	7,	8,
        9,	10,	11,	12,	13,	14,	15,	16,
        17,	18,	19,	20,	21,	22,	23,	24,
        25,	26,	27,	28,	29,	30,	31,	32,
        33,	34,	35,	36,	37,	38,	39,	40,
        41,	42,	43,	44,	45,	46,	47,	48,
        49,	50,	51,	52,	53,	54,	55,	56,
        57,	58,	59,	60,	61,	62,	63,	64
    ],

    "random": "random"
}

def getRandomTransition():
    transition_name = random.choice(list(TRANSITIONS.keys()))

    # randomly generate a transition matrix
    if transition_name == "random":
        matrix = list(range(0, 64))
        random.shuffle(matrix)
        return matrix
    else:
        matrix = TRANSITIONS[transition_name]
        # apply a random rotation
        matrix = rotateTransitionMatrix(matrix, random.randint(0, 3))
        return matrix
        

# based on
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
def rotateTransitionMatrix(matrix, times):
    if times == 0:
        return matrix
    
    # convert to 2d matrix
    matrix = numpy.array(matrix).reshape(8, 8)
    # rotation of the matrix
    for x in range (0, times):
        matrix = numpy.rot90(matrix)
    # convert back to 1d array
    matrix = matrix.flatten()
    # return a normal python array
    return list(matrix)
    
    
