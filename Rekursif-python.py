# Function Fibonacci
def fibonacci(n) :
        if n < 0 :
                print "Tidak ada bilangan yang bernilai negatif"

        if n == 0 or n == 1:
                return n

        else:
                return fibonacci(n-1) + fibonacci(n-2)


# Main Program
nilai = input("Masukkan sebuah bilangan : ")
hasil = fibonacci(nilai)
print "Deret Fibonacci ke-(%d) = %d" % (nilai,hasil)
