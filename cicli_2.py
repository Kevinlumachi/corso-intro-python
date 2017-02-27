def test_while():
	        i = 0

	        while i < 6:
		        print 'Posizione %s' % i

		        i += 1

	        print "il risultato finale e'", i

from funzioni_2 import divide_string, upper_word

again = True
while again:
    operation = raw_input('Cosa vuoi fare?(1: dividere frase 2: uppercase 0: uscire)')
    
    if operation == '1':
        sentence = raw_input('Frase:')
        print divide_string(sentence)
    elif operation == '2':
        sentence = raw_input('Frase:')
        print upper_word(sentence)
    elif operation == '0':
        again = False
    else:
        print 'Comando %s sconosciuto' % operation

