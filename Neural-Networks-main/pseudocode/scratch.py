#Copyright Fortior Blockchain, LLLP 2021

class neural_network():
    def input_layer():
        for row in data: 
            i0 = RELU('close')
            i1 = RELU('openprice')
            i2 = RELU('volume')
            i3 = RELU('high')
    def first_hidden_layer():
        input_layer(i0,i1,i2,i3)
        w0 = 0.01
        w1 = 0.01
        w2 = 0.01
        i4 = i0*i1*w0
        i5 = i1 *i2*w1
        i6 = i2 *i3*w2
    def second_hidden_layer():
        first_hidden_layer(i4,i5,i6)
        w3 = 0.01
        w4 = 0.01
        i7 = i4*i5*w3
        i8 = i5 *i6*w4
    def output_layer():
        second_hidden_layer(i7, i8)
        w5 = 0.01
        i9 = i7*i8*w5
    def activation_function():
        output_layer(i9)
        error = i9 - real_value
        if error > 0:
            update_weights =+ 0.1
        else:
            iterate

        





